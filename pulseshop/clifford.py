"""
The single-qutrit Clifford group C3 and randomized benchmarking sequences.

C3 is generated from the qutrit Hadamard (discrete Fourier transform) H and
the phase gate S = diag(1, 1, omega), omega = e^{2 pi i/3}: enumerate all
words in H, S up to length 12 (8190 words), drop exact duplicates (937 left),
drop duplicates up to a global phase -> 216 elements (`rb/clifford_gen.ipynb`).

Each element is decomposed into three pulses with `su3.get_parameter`; when
pulses from different Cliffords are concatenated the virtual-Z bookkeeping of
`create_pulse_sequence` tracks the accumulated frame phases (phase_01,
phase_12) including the frame kicks alpha, beta, gamma measured by the
phase-tracking experiments.
"""

import numpy as np
from .su3 import is_global_phase, decompose_all

pi = np.pi
omega = np.exp(2 * pi * 1j / 3)

#: qutrit Hadamard (DFT) and phase gate
H3 = np.array([[1, 1, 1], [1, omega, omega ** 2], [1, omega ** 2, omega]], dtype=complex) / np.sqrt(3)
S3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, omega]], dtype=complex)


def _sum_index(i):
    return 2 ** (i + 1) - 2


def words(max_length=12):
    """All words in {H, S} of length 1..max_length, in generation order."""
    A = []
    for i in range(max_length):
        if i == 0:
            A.append("H"); A.append("S")
        else:
            for j in range(_sum_index(i - 1), _sum_index(i)):
                A.append(A[j] + "H"); A.append(A[j] + "S")
    return A


def word_to_matrix(word):
    m = np.eye(3, dtype=complex)
    for ch in word:
        m = m @ (H3 if ch == "H" else S3)
    return m


def generate_clifford3(max_length=12, return_words=False):
    """
    The 216 single-qutrit Cliffords (list of 3x3 arrays, rounded to 1e-10),
    unique up to global phase.  With return_words=True also returns the
    generating word of each element.
    """
    ws = words(max_length)
    mats = [np.round(word_to_matrix(w), 10) for w in ws]
    # exact duplicates
    uniq, uniq_w = [], []
    for m, w in zip(mats, ws):
        if not any((np.round(m - u, 10) == 0).all() for u in uniq):
            uniq.append(m); uniq_w.append(w)
    # duplicates up to global phase
    keep, keep_w = [], []
    for m, w in zip(uniq, uniq_w):
        if not any(is_global_phase(m, u) for u in keep):
            keep.append(m); keep_w.append(w)
    return (keep, keep_w) if return_words else keep


def find_index(mat, cliffords):
    """Index of `mat` in the group (up to global phase), or -1."""
    for i, c in enumerate(cliffords):
        if is_global_phase(mat, c, decimals=6):
            return i
    return -1


def inverse_table(cliffords):
    """inv[i] = index j such that C_j C_i = identity up to a phase."""
    inv = np.full(len(cliffords), -1, dtype=int)
    I = np.eye(3, dtype=complex)
    for i, ci in enumerate(cliffords):
        for j, cj in enumerate(cliffords):
            if is_global_phase(ci @ cj, I, decimals=6):
                inv[i] = j
                break
    return inv


def multi(indices, cliffords):
    """Product C[indices[0]] C[indices[1]] ... (left to right)."""
    m = np.eye(3, dtype=complex)
    for i in indices:
        m = m @ cliffords[i]
    return m


def rb_sequence(length, cliffords, inv, rng=None):
    """
    Random sequence of `length` Cliffords followed by the Clifford that
    inverts their product (so that the ideal final state is |0>).
    """
    rng = np.random.default_rng() if rng is None else rng
    seq = rng.integers(0, len(cliffords), length)
    total = multi(np.flip(seq), cliffords)
    inv_index = inv[find_index(total, cliffords)]
    return np.concatenate((seq, [inv_index]))


def interleaved_rb_sequence(index, length, cliffords, inv, rng=None):
    """RB sequence with the Clifford `index` interleaved after every random Clifford."""
    rng = np.random.default_rng() if rng is None else rng
    seq = rng.integers(0, len(cliffords), length)
    inter = np.empty(2 * length, dtype=int)
    inter[0::2] = seq; inter[1::2] = index
    total = multi(np.flip(inter), cliffords)
    inv_index = inv[find_index(total, cliffords)]
    return np.concatenate((inter, [inv_index]))


def check_is_inverse(sequence, cliffords):
    """True if applying `sequence` (first element first) to |0> returns |0>."""
    m = multi(np.flip(sequence), cliffords)
    psi = m @ np.array([[1], [0], [0]], dtype=complex)
    return bool(np.round(np.abs(psi[0, 0])) == 1)


def clifford_parameters(cliffords):
    """(216, 9) table of pulse angles, one row per Clifford (su3.get_parameter)."""
    return decompose_all(cliffords)


def pulse_sequence_phases(params_sequence, alpha, beta, gamma):
    """
    Pure-python mirror of `create_pulse_sequence`: for a list of nine-angle
    rows, return the list of (subspace, theta, phi_with_frame) pulses to play
    and the running frame phases.  alpha: 1-2 frame kick caused by a 0-1
    pulse; beta/gamma: 0-1 / 1-2 frame kicks caused by a 1-2 pulse.
    """
    phase_01, phase_12 = 0.0, 0.0
    pulses = []
    for params in params_sequence:
        t1, t2, t3, p1, p2, p3, p4, p5, p6 = params
        pulses.append(("01", t1, p1 + phase_01)); phase_12 += alpha
        pulses.append(("12", t2, p2 + phase_12)); phase_01 += beta; phase_12 += gamma
        pulses.append(("01", t3, p3 + phase_01)); phase_12 += alpha
        # U_d(phi6, phi5, phi4) is absorbed into the frames
        phase_01 += p6 - p5
        phase_12 += p5 - p4
    return pulses, (phase_01, phase_12)


def ideal_sequence_populations(sequence, cliffords):
    """Populations of |0>,|1>,|2> after an ideal RB sequence from |0>."""
    psi = multi(np.flip(sequence), cliffords) @ np.array([[1], [0], [0]], dtype=complex)
    return np.abs(psi.ravel()) ** 2
