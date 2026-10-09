"""
Curve fitting helpers and the model functions that recur across the project.

The core `fit_function` wrapper appeared, copy-pasted, in ~25 notebooks; the
model functions (cosine for Rabi, Lorentzian for spectroscopy, sinusoid for
DRAG sweeps, A p^m + B for randomized benchmarking, the repeated-pi
over-rotation model) are collected here with their original conventions.
"""

import math
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import periodogram


# ------------------------------------------------------------- wrapper ----
def fit_function(x_values, y_values, function, init_params, maxfev=50000, dense=None):
    """
    Thin wrapper around scipy.optimize.curve_fit.

    Returns (params, y_fit, pcov).  If `dense` is an int, `y_fit` is evaluated
    on a dense grid of that many points spanning x_values (used for smooth
    plotting of a fit through sparse data).
    """
    x_values = np.asarray(x_values, dtype=float)
    y_values = np.asarray(y_values, dtype=float)
    params, pcov = curve_fit(function, x_values, y_values, init_params, maxfev=maxfev)
    if dense:
        x_dense = np.linspace(x_values.min(), x_values.max(), dense)
        y_fit = function(x_dense, *params)
    else:
        y_fit = function(x_values, *params)
    return params, y_fit, pcov


def baseline_remove(values):
    """Subtract the mean (used on averaged IQ traces before fitting)."""
    return np.array(values) - np.mean(values)


def r_squared(y, y_fit):
    y = np.asarray(y); y_fit = np.asarray(y_fit)
    ss_res = np.sum((y - y_fit) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    return 1 - ss_res / ss_tot


# ------------------------------------------------------ model functions ----
def cosine(x, A, B, period, phi):
    """Rabi-oscillation ansatz  A cos(2 pi x / period - phi) + B."""
    return A * np.cos(2 * np.pi * x / period - phi) + B


# the DRAG-sweep notebooks called the same thing `sinusoid`
sinusoid = cosine


def damped_cosine(x, A, B, period, phi, tau):
    """Ramsey fringe:  A e^{-x/tau} cos(2 pi x / period - phi) + B."""
    return A * np.exp(-x / tau) * np.cos(2 * np.pi * x / period - phi) + B


def two_cosines(x, A1, f1, phi1, A2, f2, phi2, B):
    """Two-frequency Ramsey (used when the 1-2 fringe showed two components)."""
    return A1 * np.cos(2 * np.pi * f1 * x + phi1) + A2 * np.cos(2 * np.pi * f2 * x + phi2) + B


def lorentzian(x, A, q_freq, B, C):
    """Spectroscopy line shape  (A/pi) B / ((x - q_freq)^2 + B^2) + C."""
    return (A / np.pi) * (B / ((x - q_freq) ** 2 + B ** 2)) + C


def exp_decay(t, A, T1, B):
    """T1 / energy relaxation  A e^{-t/T1} + B."""
    return A * np.exp(-t / T1) + B


def stretched_exp(t, A, T2, alpha, B):
    """Stretched-exponential envelope  A exp(-(t/T2)^alpha) + B (Ramsey T2*)."""
    return A * np.exp(-((t / T2) ** alpha)) + B


def rb_decay(m, A, B, p):
    """Randomized-benchmarking survival  A p^m + B."""
    return A * p ** m + B


def rb_error_per_clifford(p, d=3):
    """Average error per Clifford  r = (1 - p)(d - 1)/d  (d = 3 for a qutrit)."""
    return (1 - p) * (d - 1) / d


def population_theory(n, eps):
    """
    Ground population after n repeated pi pulses with over-rotation eps:
    1/2 cos(n(pi + eps)) + 1/2.   (gaussian_calibration_01, Nov 2022)
    """
    return 0.5 * np.cos(n * (np.pi + eps)) + 0.5


def population_theory_ab(n, A, B, eps):
    """Same as `population_theory` with free amplitude and offset."""
    return A * np.cos(n * (np.pi + eps)) + B


def sx_theory(n, eps):
    """Population after n repeated pi/2 pulses with over-rotation eps: cos^2(n(pi/2+eps)/2)."""
    n = np.asarray(n)
    return np.cos(n * (np.pi / 2 + eps) / 2) ** 2


def sx_odd_theory(n, A, B, eps):
    """Odd-repetition SX model  A + B cos((2n+1)(eps + pi/2))."""
    n = np.asarray(n)
    return A + B * np.cos((2 * n + 1) * (eps + np.pi / 2))


def parabola(x, a, x0, c):
    """a (x - x0)^2 + c  (APE+DRAG beta sweeps: the minimum of p2 vs beta)."""
    return a * (x - x0) ** 2 + c


def line(x, m, c):
    return m * x + c


# ------------------------------------------------------- small helpers ----
def pi_amplitude_from_cosine_fit(amps, signal, guess_period=None):
    """
    Fit a cosine to a Rabi trace and return (pi_amplitude, params, y_fit).
    The pi amplitude is half the fitted period (a convention used throughout).
    """
    amps = np.asarray(amps, dtype=float)
    signal = np.asarray(signal, dtype=float)
    if guess_period is None:
        # dominant Fourier component of the centred trace
        n = len(amps)
        spec = np.abs(np.fft.rfft(signal - signal.mean()))
        freqs = np.fft.rfftfreq(n, d=(amps[-1] - amps[0]) / (n - 1))
        k = np.argmax(spec[1:]) + 1
        guess_period = 1.0 / freqs[k]
    A0 = (signal.max() - signal.min()) / 2
    B0 = signal.mean()
    best = None
    for phi0 in (0.0, np.pi / 2, np.pi, -np.pi / 2):
        try:
            params, y_fit, pcov = fit_function(amps, signal, cosine, [A0, B0, guess_period, phi0])
        except RuntimeError:
            continue
        err = np.sum((y_fit - signal) ** 2)
        if best is None or err < best[0]:
            best = (err, params, y_fit)
    if best is None:
        raise RuntimeError("cosine fit did not converge")
    _, params, y_fit = best
    period = abs(params[2])
    return period / 2, params, y_fit


def dominant_frequency(t, signal):
    """Dominant frequency of a (Ramsey) time trace via a periodogram."""
    t = np.asarray(t, dtype=float)
    fs = 1.0 / np.mean(np.diff(t))
    f, pxx = periodogram(np.asarray(signal) - np.mean(signal), fs=fs)
    return f[np.argmax(pxx[1:]) + 1], f, pxx


def closest_index(arr, v):
    """Index of the element of `arr` closest to `v` (utility.closest_index)."""
    arr = np.asarray(arr)
    return int(np.argmin(np.abs(arr - v)))


def distance(a, b):
    """Euclidean distance between two points of the IQ plane given as complex numbers."""
    return math.sqrt((np.real(a) - np.real(b)) ** 2 + (np.imag(a) - np.imag(b)) ** 2)


def ejec(f01_hz, f12_hz):
    """E_J/E_C from f01, f12 (alias of constants.ej_over_ec, kept under its historical name)."""
    from .constants import ej_over_ec
    return ej_over_ec(f01_hz, f12_hz)
