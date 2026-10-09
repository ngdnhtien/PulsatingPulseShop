"""
Frame-phase ("phase advance") experiments and their models.

When a transmon is driven as a qutrit, a pulse on one transition is not
transparent to the other: the 0-1 and 1-2 drive frames precess at different
rates, so after an X12 pulse the 0-1 frame has moved by beta, after an X01
pulse the 1-2 frame has moved by alpha (and gamma on 1-2 itself).  Three
protocols were used over the years to measure these phases:

1. Ramsey-like (2022, Oslo/Manila; 2023 Lagos):  Y01(pi/2) [X12(pi/2)]^{8n}
   Y01(-pi/2 + 8 n phi): the 0-1 Ramsey fringe shifts linearly with n.
   -> `model_zero_population`, `ramsey_like_sim`.
2. Randomised phase circuits, RPC (2022 find_phase, 2023 lagos, 2024
   brisbane): random strings of R01/R12 rotations with random (theta, phi);
   fit (alpha, beta, gamma) by least squares on the populations.
   -> `population_model_rpc`, `population_model_halfpi`, `fit_phases`.
3. Phase advance with pseudo-identities (2024-25, paper): a 0-1 (or 1-2)
   Ramsey whose idle time is filled with reps x (SX12 SX12^dagger) [or
   (SX12)^4] pseudo-identities; the fringe shift per repetition is 2 beta
   (resp. 2 alpha).  -> `phase_advance_sim`.
"""

import numpy as np
from scipy.optimize import minimize

from .qutrit import (ket0, populations, Z01, Z12, X01, X12, Y01, R01, R12,
                     S01, S12, G01, G12, Lx01, Lx12)
from scipy.linalg import expm

pi = np.pi


# ----------------------------------------------- 1. Ramsey-like protocol ----
def model_zero_population(alpha, n):
    """
    P(|0>) of  Y01(pi/2) . [Z01(alpha) X12(pi/2)]^{8n} . Y01(-pi/2) |0>:
    each X12(pi/2) kicks the 0-1 frame by alpha (ramsey_exp_result, 2022).
    """
    psi = Y01(pi / 2) @ ket0
    for _ in range(8 * n):
        psi = Z01(alpha) @ X12(pi / 2) @ psi
    psi = Y01(-pi / 2) @ psi
    return populations(psi)[0]


def ramsey_like_sim(N, xi, alpha, beta, gamma):
    """
    P(|1>) of the 2023 Lagos Ramsey-like protocol
    S01(pi,0) S12(pi/2,-pi/2) [S01(2pi,0)]^{2N} S12(-pi/2, xi - pi/2).
    """
    psi = S01(pi, 0, alpha) @ ket0
    psi = S12(pi / 2, -pi / 2, beta, gamma) @ psi
    for _ in range(2 * N):
        psi = S01(2 * pi, 0, alpha) @ psi
    psi = S12(-pi / 2, xi - pi / 2, beta, gamma) @ psi
    return populations(psi)[1]


def noisy_ramsey_like(n_max, epsilon, phi, reps_per_step=8):
    """
    2022 Painter.ipynb toy: Y01(pi/2) then 8(i+1) over-rotated X12(pi/2)
    pulses with frame phase phi; returns (n_max, 3) populations.
    """
    def RZ01(p): return np.diag([np.exp(1j * p), 1, 1]).astype(complex)
    def RZ12(p): return np.diag([1, 1, np.exp(1j * p)]).astype(complex)
    def RX12_noisy(theta): return RZ12(phi) @ X12(epsilon) @ X12(theta)
    def RY01_noisy(theta): return RZ01(pi / 2) @ X01(epsilon) @ X01(theta) @ RZ01(-pi / 2) @ RZ01(phi)
    out = []
    for i in range(n_max):
        U = RY01_noisy(pi / 2)
        for _ in range(reps_per_step * (i + 1)):
            U = RX12_noisy(pi / 2) @ U
        out.append(populations(U @ ket0))
    return np.array(out)


# ----------------------------------------- 2. randomised phase circuits ----
def population_model_rpc(thetas, phis, alpha, beta, gamma, order):
    """
    Three-parameter model of the 2023 RPC protocol: state prepared by
    R01(pi/2) R12(pi/2), then for each character of `order` ('1' -> 0-1,
    '2' -> 1-2) a rotation R(theta_i, phi_i) carrying its frame kicks.
    """
    psi = S12(pi / 2, 0, beta, gamma) @ S01(pi / 2, 0, alpha) @ ket0
    for i, level in enumerate(order):
        if level == "1":
            psi = S01(thetas[i], phis[i], alpha) @ psi
        else:
            psi = S12(thetas[i], phis[i], beta, gamma) @ psi
    return populations(psi)


def population_model_halfpi(phi_arr, alpha, beta, order, eps01=0.0, eps12=0.0, xi=0.0):
    """
    RPC v2 (2024): only phase-sandwiched pi/2 gates G01(phi)/G12(phi), no
    state preparation.  Optional phase errors eps01, eps12 and 1-2
    amplitude error xi reproduce the three model variants of
    rpc_data_processing.ipynb.
    """
    psi = ket0.copy()
    for j, level in enumerate(order):
        if level == "1":
            psi = G01(phi_arr[j], alpha, eps01) @ psi
        else:
            psi = G12(phi_arr[j], beta, eps12, xi) @ psi
    return populations(psi)


def rmse(p_model, p_exp):
    p_model = np.asarray(p_model); p_exp = np.asarray(p_exp)
    return float(np.sqrt(np.mean((p_model - p_exp) ** 2)))


def fit_phases(model, params_list, p_exp, order, n_params, n_seeds=20, x0_sampler=None, rng=None):
    """
    Least-squares fit of the frame phases.  `model(params_i, *x, order)`
    must return the three populations for circuit i.  Returns the best
    (x_opt mod 2pi, loss, r2 per level).
    """
    rng = np.random.default_rng() if rng is None else rng
    p_exp = np.asarray(p_exp)

    def loss(x):
        pm = np.array([model(params_list[i], *x, order) for i in range(len(params_list))])
        return rmse(pm, p_exp)

    best = (None, np.inf)
    for _ in range(n_seeds):
        x0 = x0_sampler(rng) if x0_sampler else rng.uniform(-pi / 4, pi / 4, n_params)
        res = minimize(loss, x0=x0)
        if res.fun < best[1]:
            best = (res.x % (2 * pi), res.fun)
    x_opt, l = best
    pm = np.array([model(params_list[i], *x_opt, order) for i in range(len(params_list))])
    r2 = [1 - np.sum((p_exp[:, k] - pm[:, k]) ** 2) / np.sum((p_exp[:, k] - p_exp[:, k].mean()) ** 2) for k in range(3)]
    return x_opt, l, r2, pm


def normalized(arr):
    """Map phases in [0, 2pi) to (-1, 1] in units of pi (for plotting)."""
    out = []
    for phi in arr:
        x = phi / pi
        out.append(x - 2 if x > 1 else x)
    return out


def create_order(length, rng=None):
    """Random string of '1'/'2' of given length (which subspace each rotation acts on)."""
    rng = np.random.default_rng() if rng is None else rng
    return "".join(rng.choice(["1", "2"], length))


# ------------------------------------------ 3. phase advance (2024-25) ----
U_sx01 = expm(-1j * (pi / 2) / 2 * Lx01)
U_sxp12 = expm(-1j * (pi / 2) / 2 * Lx12)
U_sxm12 = expm(-1j * (-pi / 2) / 2 * Lx12)
U_sxp01 = U_sx01
U_sxm01 = expm(-1j * (-pi / 2) / 2 * Lx01)


def phase_advance_sim(measurement, phases, reps_list, beta=None, alpha=None, berry=False):
    """
    Ideal populations of the phase-advance experiment (phase_advance_plot.ipynb).

    measurement 'beta': |0> -> SX01 -> reps x [SX12 (-SX12) with frame kick
    Z01(2 beta)] -> R01(-pi/2, -phase).  With berry=True the pseudo-identity
    is four SX12 (a full 2pi on 1-2, kick Z01(4 beta)).
    measurement 'alpha': |0> -> X01 (two SX01) -> SX12 -> reps x [SX01 (-SX01)
    with Z12(2 alpha)] -> R12(-pi/2, -phase); berry: four SX01, Z12(4 alpha).

    Returns array (len(reps_list), len(phases), 3).
    """
    out = []
    for reps in reps_list:
        row = []
        for phase in phases:
            if measurement == "beta":
                psi = Z12(0) @ U_sx01 @ ket0
                for _ in range(reps):
                    if berry:
                        psi = Z01(4 * beta) @ U_sxp12 @ U_sxp12 @ U_sxp12 @ U_sxp12 @ psi
                    else:
                        psi = Z01(2 * beta) @ U_sxm12 @ U_sxp12 @ psi
                psi = Z12(0) @ R01(-pi / 2, -phase) @ psi
            else:
                psi = Z01(0) @ U_sxp12 @ Z12(2 * alpha) @ U_sx01 @ U_sx01 @ ket0
                for _ in range(reps):
                    if berry:
                        psi = Z12(4 * alpha) @ U_sxp01 @ U_sxp01 @ U_sxp01 @ U_sxp01 @ psi
                    else:
                        psi = Z12(2 * alpha) @ U_sxm01 @ U_sxp01 @ psi
                psi = Z01(0) @ R12(-pi / 2, -phase) @ psi
            row.append(populations(psi))
        out.append(row)
    return np.array(out)


def berry_phase_sim(phi, varphi_list):
    """
    Spin-1 emulation (Neeley 2009) sketch from berry/decomposer_numpy.ipynb:
    R01(pi/2) -> R12(pi) -> R12(pi, axis phi) -> R01(-pi/2, axis varphi).
    """
    out = []
    for varphi in varphi_list:
        psi = R01(pi / 2, 0) @ ket0
        psi = R12(pi, 0) @ psi
        psi = R12(pi, phi) @ psi
        psi = R01(-pi / 2, varphi) @ psi
        out.append(populations(psi))
    return np.array(out)


def fringe_phase_shift(phases, pop, reference_pop=None):
    """
    Phase of the fundamental Fourier component of a fringe pop(phase); the
    difference between two repetitions gives the frame phase accumulated.
    """
    phases = np.asarray(phases); pop = np.asarray(pop)
    c = np.sum(pop * np.exp(-1j * phases)) / len(phases)
    return float(np.angle(c))
