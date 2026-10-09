"""
pulseshop -- the PPS quantum mechanic shop toolbox.

Modular code distilled from three generations of notebooks (PulsatingPulseLab
2022-23, PulsatingPulseShop 2023-24, PulsatingPulseShop_pending 2024-25) on the
pulse-level control of IBM transmon qutrits.

Modules
-------
constants       units, timing granularity, and the calibrated pulse parameters
                of every device/qubit we touched (a history, not a config).
fitting         curve_fit wrapper, model functions (cosine, Lorentzian, sinusoid,
                exponential, RB decay, over-rotation), small numeric helpers.
readout         IQ-plane state discrimination (LDA, nearest centre, radius) and
                readout-error mitigation (SLSQP / cvxopt), plus the historical
                DataAnalysis class.
qutrit          3x3 matrices: kets, Gell-Mann generators, subspace rotations,
                virtual-Z, coherent-error models, APE / rotation-error models.
su3             decomposition of any SU(3) matrix into U_d R01 R12 R01.
clifford        the 216-element single-qutrit Clifford group, inverses, RB and
                interleaved-RB sequences with virtual-Z phase bookkeeping.
phase_tracking  population models and fits for the Ramsey-like, randomised
                (RPC) and phase-advance (alpha/beta) frame-phase experiments.
simulation      QuTiP models: Cooper-pair box, d-level transmon with pulse
                trains, T1 decay, driven two-level toy.
schedules       Qiskit-Pulse schedule builders (needs qiskit<2 with pulse).
io              loading the saved experiments under data/.
"""

__version__ = "1.0.0"
__author__ = "Tien D. Nguyen"

from . import constants, fitting, readout, qutrit, su3, clifford, phase_tracking, simulation, io  # noqa: F401
