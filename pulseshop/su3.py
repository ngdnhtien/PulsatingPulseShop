"""
Decomposition of a qutrit unitary into pulses we can play.

Any U in SU(3) (up to global phase) can be written as

    U = U_d(phi_6, phi_5, phi_4) . R01(theta_3, phi_3) . R12(theta_2, phi_2) . R01(theta_1, phi_1)

i.e. three physical pulses (0-1, 1-2, 0-1) and a diagonal phase gate that is
absorbed in the drive frames (virtual Z).  `get_parameter` is the analytic
nine-angle extraction worked out in `su3_decomposition.ipynb` (sympy) and
`Clifford/probe.ipynb` (numeric, Aug 2022); the general formula fails when
|u33| = 0 (theta_2 = pi) and the special cases are handled explicitly.
`reconstruct` rebuilds the matrix so that the decomposition can be checked.
"""

import numpy as np
from .qutrit import R01, R12, U_d

pi = np.pi


def is_global_phase(mat_1, mat_2, decimals=10):
    """True if mat_1 and mat_2 differ only by a global phase."""
    for i in range(3):
        if mat_1[0][i] != 0:
            arg_1 = np.angle(mat_1[0][i]); arg_2 = np.angle(mat_2[0][i])
            break
    diff = mat_1 * np.exp(1j * arg_2) - mat_2 * np.exp(1j * arg_1)
    return bool((np.round(diff, decimals=decimals) == 0).all())


def reconstruct(theta_1, theta_2, theta_3, phi_1, phi_2, phi_3, phi_4, phi_5, phi_6):
    return U_d(phi_6, phi_5, phi_4) @ R01(theta_3, phi_3) @ R12(theta_2, phi_2) @ R01(theta_1, phi_1)


def _general(U):
    phi_4 = np.angle(U[2, 2])
    theta_2 = 2 * np.arccos(np.round(np.absolute(U[2, 2]), 6))
    phi_2 = np.angle(U[2, 1]) - phi_4 + pi / 2
    phi_1 = np.angle(-U[2, 0]) - phi_2 - phi_4
    theta_1 = 2 * np.arccos(np.round(np.absolute(U[2, 1]) / np.sin(theta_2 / 2), 6))
    theta_3 = 2 * np.arccos(np.round(np.absolute(U[1, 2]) / np.sin(theta_2 / 2), 6))
    phi_5 = np.angle(U[1, 2]) + phi_2 + pi / 2
    phi_3 = np.angle(np.cos(theta_1 / 2) * np.cos(theta_2 / 2) * np.cos(theta_3 / 2) - U[1, 1] * np.exp(-1j * phi_5)) + phi_1
    phi_6 = np.angle(-U[0, 2]) + phi_3 + phi_2
    return theta_1, theta_2, theta_3, phi_1, phi_2, phi_3, phi_4, phi_5, phi_6


def get_parameter(U):
    """
    Nine angles (theta_1, theta_2, theta_3, phi_1, ..., phi_6) such that
    reconstruct(*angles) == U up to numerical precision.  Raises ValueError
    if no branch reproduces U (which never happens for the Clifford group).
    """
    U = np.asarray(U, dtype=complex)
    candidates = []
    u22 = np.round(np.absolute(U[2, 2]), 6)
    if u22 == 1:
        # block-diagonal: a single 0-1 rotation and phases
        if np.round(np.absolute(U[0, 0]), 6) != 0:
            theta_1 = phi_1 = theta_2 = phi_2 = 0
            phi_4 = np.angle(U[2, 2]); phi_5 = np.angle(U[1, 1]); phi_6 = np.angle(U[0, 0])
            phi_3 = np.angle(U[1, 0]) - phi_5 + pi / 2
            theta_3 = 2 * np.arccos(np.round(np.absolute(U[1, 1]), 6))
            candidates.append((theta_1, theta_2, theta_3, phi_1, phi_2, phi_3, phi_4, phi_5, phi_6))
        else:
            theta_1 = phi_1 = theta_2 = phi_2 = phi_3 = 0
            theta_3 = 2 * np.arccos(np.round(np.absolute(U[1, 1]), 6))
            phi_4 = np.angle(U[2, 2])
            phi_6 = np.angle(U[0, 1]) + phi_3 + pi / 2
            phi_5 = np.angle(U[1, 0]) - phi_3 + pi / 2
            candidates.append((theta_1, theta_2, theta_3, phi_1, phi_2, phi_3, phi_4, phi_5, phi_6))
    elif u22 == 0:
        # theta_2 = pi: permutation-like matrices, several sub-cases
        theta_1 = 2 * np.arccos(np.round(np.absolute(U[2, 1]), 6))
        theta_2 = pi
        theta_3 = 2 * np.arccos(np.round(np.absolute(U[1, 2]), 6))
        phi_1 = phi_2 = phi_3 = 0
        if np.round(np.absolute(U[2, 0]), 6) != 0:
            phi_4 = np.angle(-U[2, 0])
            if np.round(np.absolute(U[0, 2]), 6) != 0:
                phi_5 = np.angle(-U[1, 1]); phi_6 = np.angle(-U[0, 2])
            else:
                phi_5 = np.angle(U[1, 2]) + pi / 2; phi_6 = np.angle(U[0, 1]) + pi / 2
            candidates.append((theta_1, theta_2, theta_3, phi_1, phi_2, phi_3, phi_4, phi_5, phi_6))
        if np.round(np.absolute(U[1, 0]), 6) != 0:
            phi_4 = np.angle(U[2, 1]) + pi / 2; phi_5 = np.angle(U[1, 0]) + pi / 2; phi_6 = np.angle(-U[0, 2])
            candidates.append((theta_1, theta_2, theta_3, phi_1, phi_2, phi_3, phi_4, phi_5, phi_6))
        if np.round(np.absolute(U[0, 0]), 6) != 0:
            phi_4 = np.angle(U[2, 1]) + pi / 2; phi_5 = np.angle(U[1, 2]) + pi / 2; phi_6 = np.angle(U[1, 1])
            candidates.append((theta_1, theta_2, theta_3, phi_1, phi_2, phi_3, phi_4, phi_5, phi_6))
        # the probe.ipynb special forms
        th = (0, pi, pi, 0, np.angle(U[2, 1]) + pi / 2, np.angle(U[1, 0]) + pi / 2, 0, 0,
              np.angle(U[1, 0]) + np.angle(U[2, 1]) + np.angle(U[0, 2]))
        candidates.append(th)
        th = (pi, pi, 0, -np.angle(U[0, 1]) - pi / 2, -np.angle(U[1, 2]) - pi / 2, 0,
              np.angle(U[0, 1]) + np.angle(U[1, 2]) + np.angle(U[2, 0]), 0, 0)
        candidates.append(th)
        th = (0, pi, 0, 0, 0, 0, 0, 0, 0)
        candidates.append((0, pi, 0, 0, 0, 0, -0 + np.angle(U[2, 1]) + pi / 2, np.angle(U[1, 2]) + pi / 2, np.angle(U[0, 0])))
    else:
        candidates.append(_general(U))
        # probe.ipynb: theta_2 ~ pi but u33 != 0 numerically
        g = _general(U)
        if abs(g[1] - pi) < 1e-6:
            candidates.append((0, pi, 0, 0, 0, 0, np.angle(U[2, 1]) + pi / 2, np.angle(U[1, 2]) + pi / 2, np.angle(U[0, 0])))
    for cand in candidates:
        if np.allclose(reconstruct(*cand), U, atol=1e-5):
            return tuple(float(x) for x in cand)
    # last resort: also accept equality up to a global phase
    for cand in candidates:
        if is_global_phase(reconstruct(*cand), U, decimals=5):
            return tuple(float(x) for x in cand)
    raise ValueError("no decomposition branch reproduces this unitary")


def decompose_all(unitaries):
    """Decompose a list of unitaries; returns an (n, 9) array."""
    return np.array([get_parameter(U) for U in unitaries])


def find_bug(unitaries, params=None):
    """Indices whose decomposition does not reconstruct the unitary (should be [])."""
    params = decompose_all(unitaries) if params is None else params
    bad = []
    for i, (U, p) in enumerate(zip(unitaries, params)):
        if not np.allclose(reconstruct(*p), U, atol=1e-5):
            bad.append(i)
    return bad
