"""
QuTiP / numpy models of the hardware.

* `cpb_hamiltonian`, `charge_coefficients`, `phase_wavefunction`: the
  Cooper-pair-box / transmon in the charge basis (paper figure 0).
* `transmon_frame_hamiltonian`: the d-level standard nonlinear oscillator in
  the frame rotating at the drive, with couplings lambda_j between adjacent
  levels (notes in `simulation/full_transmon.ipynb`).
* Gaussian pulses and pulse trains (`add_pulse`, `Omega`, `OG`, `deriv_Omega`)
  for time-dependent `sesolve`/`mesolve` runs.
* `collapse_operators`, `simulate_t1`, `simulate_pulse_train`.
* `driven_two_level`: the lab-frame vs rotating-frame toy of `frame.ipynb`.
"""

import math
import numpy as np
from scipy import special

try:
    import qutip as qt
except ImportError:  # pragma: no cover
    qt = None


# ------------------------------------------------------- Cooper-pair box ----
def cpb_hamiltonian(Ec, Ej, N, ng=0.0):
    """Charge-basis Hamiltonian 4Ec(n - ng)^2 - Ej/2 (|n><n+1| + h.c.), n = -N..N."""
    m = np.diag(4 * Ec * (np.arange(-N, N + 1) - ng) ** 2) - 0.5 * Ej * (
        np.diag(np.ones(2 * N), 1) + np.diag(np.ones(2 * N), -1))
    return m


def charge_coefficients(Ec, Ej, N, ng=0.0, n_states=4):
    """Eigenvalues and real charge-basis coefficients of the lowest `n_states` eigenstates."""
    evals, evecs = np.linalg.eigh(cpb_hamiltonian(Ec, Ej, N, ng))
    coefs = [np.real(evecs[:, k]) for k in range(n_states)]
    return evals[:n_states], np.array(coefs)


def phase_wavefunction(coef, phi_grid, N):
    """psi(phi) = (2 pi)^{-1/2} sum_n c_n e^{i n phi} on a phi grid."""
    n = np.arange(-N, N + 1)
    return np.array([np.sum(coef * np.exp(1j * phi * n)) / math.sqrt(2 * np.pi) for phi in phi_grid])


def josephson_potential(phi):
    return -np.cos(phi)


# ----------------------------------------------- d-level transmon model ----
def transmon_frame_hamiltonian(dim, f_qubit_ghz, f_anhar_ghz, lambdas, delta=0.0):
    """
    Rotating-frame SNO Hamiltonian (rad/ns, hbar = 1) as a pair (H0, H1):
    H0 = sum_j [j delta + Delta_j] |j><j| with Delta_j = Delta_2 j(j-1)/2,
    H1 = sum_j lambda_{j-1}/2 (|j-1><j| + h.c.) to be multiplied by Omega(t).
    `delta` is the drive detuning omega_01 - omega_d.
    """
    Delta_2 = 2 * np.pi * f_anhar_ghz
    H0 = np.zeros((dim, dim)); H1 = np.zeros((dim, dim))
    for j in range(1, dim):
        H0[j, j] = j * delta + Delta_2 * j * (j - 1) / 2
        H1[j - 1, j] = H1[j, j - 1] = lambdas[j - 1] / 2
    return H0, H1


def level_projectors(dim):
    """Hd_j = j |j><j| (the operators multiplying a time-dependent detuning)."""
    out = []
    for j in range(1, dim):
        m = np.zeros((dim, dim)); m[j, j] = j
        out.append(m)
    return out


# -------------------------------------------------------- pulse shapes ----
def gaussian_envelope(t_local, tg, sigma, A):
    """Truncated Gaussian normalised to peak A (Qiskit `Gaussian` convention)."""
    return A * (np.exp(-(t_local - tg / 2) ** 2 / (2 * sigma ** 2)) - np.exp(-tg ** 2 / (8 * sigma ** 2))) \
        / (1 - np.exp(-tg ** 2 / (8 * sigma ** 2)))


def gambetta_envelope(t_local, tg, sigma, A):
    """Truncated Gaussian normalised to unit area (Gambetta et al. PRA 83, 012308)."""
    return A * (np.exp(-(t_local - tg / 2) ** 2 / (2 * sigma ** 2)) - np.exp(-tg ** 2 / (8 * sigma ** 2))) \
        / (np.sqrt(2 * np.pi * sigma ** 2) * special.erf(tg / (np.sqrt(8) * sigma)) - tg * np.exp(-tg ** 2 / (8 * sigma ** 2)))


def add_pulse(pulse_train, pulse_name, start, tg, sigma, A):
    """Append a Gaussian pulse to a pulse-train dict and advance its clock."""
    pulse_train[pulse_name] = {"start": start, "tg": tg, "sigma": sigma, "A": A}
    pulse_train["clock"] = pulse_train["clock"] + tg


def new_pulse_train():
    return {"clock": 0}


def Omega(t, args):
    """Envelope of a pulse train at time t (peak-normalised Gaussians)."""
    for item, p in args.items():
        if item == "clock":
            continue
        if t <= p["start"] or t >= p["start"] + p["tg"]:
            continue
        return gaussian_envelope(t - p["start"], p["tg"], p["sigma"], p["A"])
    return 0.0


def OG(t, args):
    """Envelope of a pulse train at time t (area-normalised Gaussians)."""
    for item, p in args.items():
        if item == "clock":
            continue
        if t <= p["start"] or t >= p["start"] + p["tg"]:
            continue
        return gambetta_envelope(t - p["start"], p["tg"], p["sigma"], p["A"])
    return 0.0


def deriv_Omega(t, args):
    """d/dt of `Omega` (the DRAG quadrature)."""
    for item, p in args.items():
        if item == "clock":
            continue
        if t <= p["start"] or t >= p["start"] + p["tg"]:
            continue
        tl = t - p["start"]
        return (p["A"] / (1 - np.exp(-p["tg"] ** 2 / (8 * p["sigma"] ** 2)))) * (p["tg"] / 2 - tl) \
            * np.exp(-(tl - p["tg"] / 2) ** 2 / (2 * p["sigma"] ** 2)) / p["sigma"] ** 2
    return 0.0


def pulse_area(args, t_max=None):
    from scipy.integrate import quad
    t_max = args["clock"] if t_max is None else t_max
    return quad(lambda t: Omega(t, args), 0, t_max, limit=500)[0]


# ------------------------------------------------------------- solvers ----
def _need_qutip():
    if qt is None:
        raise ImportError("qutip is required for this function")


def collapse_operators(dim, gamma_21=0.0, gamma_10=0.0, gamma_20=0.0, gamma_1=0.0, gamma_2=0.0, gamma_3=0.0):
    """Relaxation (|2>->|1>, |1>->|0>, |2>->|0>) and dephasing (0-1, 1-2, 0-2) jump operators."""
    _need_qutip()
    b = lambda i: qt.basis(dim, i)
    return [np.sqrt(gamma_21) * b(1) * b(2).dag(),
            np.sqrt(gamma_10) * b(0) * b(1).dag(),
            np.sqrt(gamma_20) * b(0) * b(2).dag(),
            np.sqrt(gamma_1) * (b(0) * b(0).dag() - b(1) * b(1).dag()),
            np.sqrt(gamma_2) * (b(1) * b(1).dag() - b(2) * b(2).dag()),
            np.sqrt(gamma_3) * (b(0) * b(0).dag() - b(2) * b(2).dag())]


def simulate_t1(dim, H0, delays_ns, c_ops, initial_level=2):
    """Populations after free evolution for each delay (ns) starting in |initial_level>."""
    _need_qutip()
    expect_ops = [qt.basis(dim, i) * qt.basis(dim, i).dag() for i in range(dim)]
    psi0 = qt.basis(dim, initial_level)
    out = []
    for tau in delays_ns:
        times = np.linspace(0, tau, max(2, int(tau)))
        res = qt.mesolve(qt.Qobj(H0), psi0, times, c_ops, e_ops=expect_ops)
        out.append([res.expect[i][-1] for i in range(dim)])
    return np.array(out)


def simulate_pulse_train(dim, H0, H1, pulse_train, t_end=None, steps=2000, c_ops=None, psi0=None,
                         envelope=Omega, store_states=False):
    """
    Solve the d-level transmon driven by `pulse_train` (dict from `add_pulse`).
    Returns (times, populations (steps, dim), result).
    """
    _need_qutip()
    c_ops = c_ops or []
    expect_ops = [qt.basis(dim, i) * qt.basis(dim, i).dag() for i in range(dim)]
    psi0 = qt.basis(dim, 0) if psi0 is None else psi0
    t_end = pulse_train["clock"] if t_end is None else t_end
    times = np.linspace(0, t_end, steps)
    H = [qt.Qobj(H0), [qt.Qobj(H1), lambda t, args: envelope(t, args)]]
    opts = {"store_states": store_states}
    res = qt.mesolve(H, psi0, times, c_ops, e_ops=expect_ops, args=pulse_train, options=opts)
    pops = np.array([res.expect[i] for i in range(dim)]).T
    return times, pops, res


def rabi_vs_amplitude(dim, H0, H1, amplitudes, tg, sigma, c_ops=None):
    """Final populations of a single Gaussian pulse of duration tg as a function of its peak amplitude."""
    out = []
    for A in amplitudes:
        pt = new_pulse_train(); add_pulse(pt, "pulse_1", 0, tg, sigma, A)
        _, pops, _ = simulate_pulse_train(dim, H0, H1, pt, c_ops=c_ops, steps=400)
        out.append(pops[-1])
    return np.array(out)


# ------------------------------------------------------------ 2-level toy ----
def driven_two_level(omega_q=10.0, Omega_0=1.0, omega_d=None, phi=0.0, t_end=5.0, dt=0.001, rotating_frame=False, detuning=0.0):
    """
    frame.ipynb: a qubit driven by Omega_0 cos(omega_d t + phi) in the lab
    frame, or by the RWA Hamiltonian (detuning/2) sigma_z + (Omega_0/2) sigma_x
    in the rotating frame.  Returns (times, <X>, <Y>, <Z>).
    """
    _need_qutip()
    omega_d = omega_q if omega_d is None else omega_d
    k0, k1 = qt.basis(2, 0), qt.basis(2, 1)
    X, Y, Z = qt.sigmax(), qt.sigmay(), qt.sigmaz()
    times = np.arange(0, t_end, dt)
    if rotating_frame:
        H = (detuning / 2) * Z + (Omega_0 / 2) * X
    else:
        H0 = (omega_q / 2) * (k0 * k0.dag() - k1 * k1.dag())
        H = [H0, [k1 * k0.dag() + k0 * k1.dag(), lambda t, args: Omega_0 * np.cos(omega_d * t + phi)]]
    res = qt.sesolve(H, k0, times, e_ops=[X, Y, Z])
    return times, res.expect[0], res.expect[1], res.expect[2]


# ------------------------------------------------------ rate equations ----
def three_level_decay(t, gamma_21, gamma_10, gamma_20=0.0, p2_0=1.0, p1_0=0.0):
    """
    Closed-form populations (P0, P1, P2)(t) of the three-level relaxation
    chain |2> -> |1> (gamma_21), |2> -> |0> (gamma_20), |1> -> |0> (gamma_10)
    starting from (1 - p1_0 - p2_0, p1_0, p2_0).  Rates in 1/time units of t.
    """
    t = np.asarray(t, dtype=float)
    G2 = gamma_21 + gamma_20
    p2 = p2_0 * np.exp(-G2 * t)
    if abs(G2 - gamma_10) < 1e-12:
        feed = p2_0 * gamma_21 * t * np.exp(-gamma_10 * t)
    else:
        feed = p2_0 * gamma_21 / (G2 - gamma_10) * (np.exp(-gamma_10 * t) - np.exp(-G2 * t))
    p1 = p1_0 * np.exp(-gamma_10 * t) + feed
    p0 = 1 - p1 - p2
    return np.vstack([p0, p1, p2]).T
