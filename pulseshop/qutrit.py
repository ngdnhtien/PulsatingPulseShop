"""
3x3 matrices for a transmon qutrit: computational kets, generators of the
0-1 and 1-2 subspaces, subspace rotations with virtual-Z phases, and the
small coherent-error models used to fit the amplified-error sequences.

Conventions (the ones of the 2023-25 notebooks; the 2022 notebooks used
Z01(phi) = diag(e^{+i phi}, 1, 1) which is simply Z01(-phi) here):

    Z01(phi) = diag(e^{-i phi}, 1, 1)         Z12(phi) = diag(1, 1, e^{+i phi})
    X01(theta) = exp(-i theta/2 Lx01)          X12(theta) = exp(-i theta/2 Lx12)
    R01(theta, phi) = Z01(phi) X01(theta) Z01(-phi)
                    = [[c, -i e^{-i phi} s], [-i e^{+i phi} s, c]] on levels 0,1
    R12(theta, phi) = Z12(phi) X12(theta) Z12(-phi)

A physical pulse of area theta on the 0-1 transition, played with a phase
offset phi on the drive channel, realises R01(theta, phi) *and* kicks the
1-2 subspace by a frame phase; this is what the phase-tracking experiments
measure (see `phase_tracking`).
"""

import numpy as np
from scipy.linalg import expm

# ------------------------------------------------------------- kets ----
ket0 = np.array([[1.0], [0.0], [0.0]], dtype=complex)
ket1 = np.array([[0.0], [1.0], [0.0]], dtype=complex)
ket2 = np.array([[0.0], [0.0], [1.0]], dtype=complex)
KETS = (ket0, ket1, ket2)
I3 = np.eye(3, dtype=complex)


def ket(i):
    return KETS[i]


def populations(psi):
    """|<k|psi>|^2 for k = 0, 1, 2 of a column vector psi."""
    psi = np.asarray(psi).reshape(3)
    return np.abs(psi) ** 2


def dagger(m):
    return np.conjugate(np.transpose(m))


# ------------------------------------------------- subspace generators ----
Lx01 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
Ly01 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
Lz01 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
Lx12 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
Ly12 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
Lz12 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, -1]], dtype=complex)

# Gell-Mann matrices lambda_1 ... lambda_8
GELL_MANN = {
    1: Lx01, 2: Ly01, 3: Lz01,
    4: np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
    5: np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
    6: Lx12, 7: Ly12,
    8: np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3),
}


# -------------------------------------------------------- elementary ----
def Z01(phi):
    return np.array([[np.exp(-1j * phi), 0, 0], [0, 1, 0], [0, 0, 1]], dtype=complex)


def Z12(phi):
    return np.array([[1, 0, 0], [0, 1, 0], [0, 0, np.exp(1j * phi)]], dtype=complex)


def X01(theta):
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -1j * s, 0], [-1j * s, c, 0], [0, 0, 1]], dtype=complex)


def X12(theta):
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[1, 0, 0], [0, c, -1j * s], [0, -1j * s, c]], dtype=complex)


def Y01(theta):
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]], dtype=complex)


def Y12(theta):
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]], dtype=complex)


def R01(theta, phi=0.0):
    """Rotation by theta about the axis at angle phi in the 0-1 equatorial plane."""
    return Z01(phi) @ X01(theta) @ Z01(-phi)


def R12(theta, phi=0.0):
    return Z12(phi) @ X12(theta) @ Z12(-phi)


def U_d(phi_1, phi_2, phi_3):
    """Diagonal phase gate diag(e^{i phi_1}, e^{i phi_2}, e^{i phi_3})."""
    return np.diag(np.exp(1j * np.array([phi_1, phi_2, phi_3])))


# ------------------------------------------- rotations with frame phases ----
def S01(theta, phi, alpha):
    """R01 followed by the frame phase alpha it induces on the 1-2 subspace."""
    return Z12(alpha) @ R01(theta, phi)


def S12(theta, phi, beta, gamma=0.0):
    """R12 followed by the frame phases it induces on 0-1 (beta) and 1-2 (gamma)."""
    return Z12(gamma) @ Z01(beta) @ R12(theta, phi)


def G01(phi, alpha, eps01=0.0):
    """Phase-sandwiched pi/2 gate of the RPC v2 protocol (half-pi gates only)."""
    return Z12(alpha) @ Z01(-phi + eps01) @ X01(np.pi / 2) @ Z01(phi + eps01)


def G12(phi, beta, eps12=0.0, xi=0.0):
    return Z01(beta) @ Z12(-phi + eps12) @ X12(np.pi / 2 + xi) @ Z12(phi + eps12)


# ------------------------------------------------- coherent-error models ----
def RX01_overrotated(theta, epsilon):
    """X01(theta) followed by an unwanted extra rotation epsilon (Misrotation 2022)."""
    return X01(theta) @ X01(epsilon)


def RGM01(theta, epsilon, delta):
    """Gell-Mann error model: exp(-i[(theta+eps)/2 lambda_1 - delta lambda_3])."""
    return expm(-1j * (((theta + epsilon) / 2) * Lx01 - delta * Lz01))


def RGM12(theta, epsilon, delta):
    return expm(-1j * (((theta + epsilon) / 2) * Lx12 - delta * Lz12))


def rot_x12(a, p):
    """
    Heuristic model of a faulty SX12: rotation by pi/2 + a about x with a
    simultaneous z-rotation p,  exp(-i[(pi/2 + a)/2 Lx12 + (p/2) Lz12]).
    (paper/plot.ipynb convention; rotation_script used p instead of p/2.)
    """
    return expm(-1j * (((np.pi / 2 + a) / 2) * Lx12 + (p / 2) * Lz12))


def rot_x12_minus(a, p):
    """The -SX12 pulse with the same errors: exp(-i[(-pi/2 - a)/2 Lx12 + (p/2) Lz12])."""
    return expm(-1j * (((-np.pi / 2 - a) / 2) * Lx12 + (p / 2) * Lz12))


def rotation_error_sequence(a, p, N_list, mode="pairs"):
    """
    Population of |1>, |2> after the rotation-error amplifying sequence
    |1> -> SX12 -> (SX12 SX12)^N  (mode 'pairs', Sheldon 2016 / 2024-25 paper)
    or |1> -> SX12 -> SX12^N (mode 'single').  Returns array (len(N_list), 2).
    """
    out = []
    g = rot_x12(a, p)
    for N in N_list:
        psi = g @ ket1
        if mode == "pairs":
            for _ in range(N):
                psi = g @ g @ psi
        else:
            for _ in range(N):
                psi = g @ psi
        pops = populations(psi)
        out.append([pops[1], pops[2]])
    return np.array(out)


def ape_sequence(a, p, angles, rep):
    """
    Amplified phase error sequence on 1-2 (Lucero 2010 adapted):
    |1> -> SX12 -> (-SX12 SX12)^rep -> R12(-pi/2 - a, angle); returns P(|1>)
    for every final-pulse phase in `angles`.
    """
    out = []
    plus, minus = rot_x12(a, p), rot_x12_minus(-a, p)
    for angle in angles:
        psi = plus @ ket1
        for _ in range(rep):
            psi = minus @ plus @ psi
        psi = R12(-np.pi / 2 - a, angle) @ psi
        out.append(populations(psi)[1])
    return np.array(out)


def oas90(n, epsilon, delta):
    """
    Over-rotation amplifying sequence of the 2024 ape_drag fits: P(|2>) after
    X01 then (n+1) x RGM12(pi/2, eps, delta).
    """
    psi = RGM12(np.pi / 2, epsilon, delta) @ RGM01(np.pi, 0, 0) @ ket0
    for _ in range(n):
        psi = RGM12(np.pi / 2, epsilon, delta) @ psi
    return populations(psi)[2]


def repeated_halfpi_populations(theta, epsilon, n_max, subspace="01"):
    """Populations after 1..n_max repeated (over-rotated) pi/2 pulses from |0>."""
    g = RX01_overrotated(theta, epsilon) if subspace == "01" else X12(theta) @ X12(epsilon)
    out, psi = [], ket0.copy()
    for _ in range(n_max):
        psi = g @ psi
        out.append(populations(psi))
    return np.array(out)


# ---------------------------------------------------- QuTiP conversions ----
def to_qobj(m):
    """Return a qutip.Qobj of a 3x3 numpy matrix (QuTiP optional)."""
    import qutip as qt
    return qt.Qobj(np.asarray(m))
