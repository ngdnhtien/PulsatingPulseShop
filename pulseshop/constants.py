"""
Units, timing constraints and the calibrated pulse parameters of the devices
we used, 2022-2025.  The parameter sets are a *history*: each entry records
what was in use at a given date (as written in the original notebooks /
`xp01.py`, `xp12.py`, `pulse.py`, `sx12_params.json`, `x12_params.json`).
"""

# ---------------------------------------------------------------- units ----
kHz = 1.0e3
MHz = 1.0e6
GHz = 1.0e9
us = 1.0e-6
ns = 1.0e-9
ps = 1.0e-12
fs = 1.0e-15

# ------------------------------------------------------- IBM timing rules ----
#: sample time of the IBM Eagle/Falcon pulse hardware (s)
dt = 0.5 * ns
#: every pulse duration must be a multiple of these many samples
acquire_alignment = 16
granularity = 16
pulse_alignment = 16
lcm = 16

#: factor the raw kerneled IQ values are multiplied with before plotting
scale_factor = 1.0e-7

h = 6.62607015e-34


def get_closest_multiple_of(value, base=granularity):
    """Round `value` to the closest multiple of `base` (the hardware granularity)."""
    return int(value + base / 2) - (int(value + base / 2) % base)


def get_closest_multiple_of_16(num):
    """Legacy helper: closest multiple of 16 samples."""
    return int(num + 8) - (int(num + 8) % 16)


def get_dt_from(sec):
    """Convert a duration in seconds to a hardware-legal number of samples."""
    return get_closest_multiple_of(sec / dt, lcm)


# ------------------------------------------- calibrated pulse parameters ----
# Gaussian / DRAG pulses: duration and sigma in samples (dt), amplitude in
# units of the maximum drive, frequency in Hz, beta the DRAG coefficient.
PARAMS = {
    # ---- 2022, PulsatingPulseLab era -------------------------------------
    "manila_q0_2022-05": dict(device="ibmq_manila", qubit=0,
        note="first pulse-gate Rabi, ibmq_manila default x = Drag(160, amp 0.1956, sigma 40, beta -0.55)",
        f01=4.96227e9),
    "manila_q0_2022-09": dict(device="ibmq_manila", qubit=0, note="MANILA-A, used by Misrotation and Ramseyy_ver2",
        f01=4962317255.07658, f12=4618781329.919704,
        x01=dict(shape="gaussian", duration=544, sigma=67, amp=0.09281388317671437),
        x01_fast=dict(shape="gaussian", duration=160, sigma=40, amp=0.2127889627295832, f01=4962131445.5726),
        x12=dict(shape="gaussian", duration=160, sigma=40, amp=0.17306617215735373)),
    "manila_q0_2022-10": dict(device="ibmq_manila", qubit=0, note="MANILA-B, DRAG sweeps",
        x01=dict(shape="gaussian", duration=320, sigma=80, amp=0.10218341976411754),
        x12=dict(shape="gaussian", duration=320, sigma=80, amp=0.08218459717115828)),
    "oslo_q0_2022-08": dict(device="ibm_oslo", qubit=0, note="OSLO-A, Hadamard / Ramsey-like / find-phase experiments",
        f01=4925170000.0, f12=4581552617.648945,
        x01=dict(shape="gaussian", duration=544, sigma=67, amp=0.07999888439750123),
        x12=dict(shape="gaussian", duration=544, sigma=40, amp=0.10879003883868105)),
    "oslo_q0_2022-10": dict(device="ibm_oslo", qubit=0, note="OSLO-C, DRAG N-site sweeps",
        x01=dict(shape="gaussian", duration=320, sigma=80, amp=0.07513041041956571),
        x12=dict(shape="gaussian", duration=320, sigma=80, amp=0.07077182615095635)),
    "oslo_q0_2022-11": dict(device="ibm_oslo", qubit=0, note="OSLO-B, full Gaussian + DRAG calibration",
        f01=4924993522.1397295, f12=4580649319.495695,
        x01=dict(shape="drag", duration=320, sigma=80, amp=0.08766575883814695, amp_corrected=0.08622, beta=-0.170),
        x12=dict(shape="drag", duration=320, sigma=80, amp=0.06870562817072146, beta=0.50),
        confusion_matrix=[[0.9778, 0.0089, 0.0133], [0.0108, 0.9784, 0.0109], [0.0079, 0.0323, 0.9599]]),
    "lagos_q0_2023-08": dict(device="ibm_lagos", qubit=0, note="phase tracking + RB / interleaved RB",
        f12=4895197000.149713,
        x01=dict(shape="drag", duration=160, sigma=40, amp=0.4150600327660328, beta=-1.10),
        x12=dict(shape="gaussian", duration=144, sigma=36, amp=0.3290598588545396),
        frame_phases=dict(alpha=0.61004155, beta=0.72967769, gamma=6.24307464)),
    # ---- 2023-24, PulsatingPulseShop era (ibm_brisbane) ------------------
    "brisbane_q0_2023-12": dict(device="ibm_brisbane", qubit=0, note="pulse.py, 10 Dec 2023",
        meas=dict(amp=0.6, freq_shift=-1 * MHz),
        x12=dict(shape="drag", duration=160, sigma=40, amp=0.24029996372238208, beta=2.0)),
    "brisbane_q109_2023-12": dict(device="ibm_brisbane", qubit=109, note="pulse.py, 10 Dec 2023",
        f01=4.985e9, f12=4.6778e9, anharmonicity=-0.3071e9,
        x12=dict(shape="drag", duration=96, sigma=24, amp=0.2234824425369455, amp_with_drag=0.2230049547984586,
                 beta=-0.5, detuning=-0.072 * MHz)),
    "brisbane_q109_2024-02": dict(device="ibm_brisbane", qubit=109, note="report_phase2 (RPC with DRAG), 4 Feb 2024",
        r01=dict(shape="drag", duration=120, sigma=30, amp=0.18093652143360275, beta=-1.2643134385128565),
        r12=dict(shape="drag", duration=64, sigma=16, amp=0.31419172290003516, beta=-0.7678179824177247)),
    "brisbane_q109_2024-05": dict(device="ibm_brisbane", qubit=109, note="ape_drag / sx12.json, 8 May 2024",
        x12=dict(shape="drag", duration=64, sigma=16, amp=0.31393693, beta=-0.44473),
        sx12=dict(shape="drag", duration=64, sigma=16, amp=0.156968465, beta=-0.48781)),
    "brisbane_q109_2024-07": dict(device="ibm_brisbane", qubit=109, note="phase_error / rotation_error, Jul 2024",
        sx12=dict(shape="drag", duration=120, sigma=30, amp=0.0828676, beta=-0.4601),
        x12_dur40=dict(shape="drag", duration=40, sigma=10, amp=0.479702)),
    # ---- 2024-25, PulsatingPulseShop_pending era --------------------------
    "brisbane_q109_2025-02": dict(device="ibm_brisbane", qubit=109, note="sx12_params.json / x12_params.json, Feb 2025 (paper)",
        f01=4.98498e9, anharmonicity=-0.30712e9, f12=4677857270.602841,
        sx01=dict(shape="drag", duration=120, sigma=30, amp=0.08782021117923207, beta=-1.2506749477226295,
                  angle=0.009780608897903031),
        sx12=dict(shape="drag", duration=40, sigma=10, amp=0.23678929765886286, beta=-0.41414141414141414),
        x12=dict(shape="drag", duration=40, sigma=10, amp=0.4797979797979798, beta=0),
        confusion_matrix=[[0.9771, 0.0184, 0.0045], [0.0188, 0.889, 0.0922], [0.0218, 0.1629, 0.8153]],
        T1_us=90.24),
}


def ej_over_ec(f01_hz, f12_hz):
    """
    E_J/E_C of a transmon from its two lowest transition frequencies
    (E_C = -h*anharmonicity, E_J = h^2 (f01 - anh)^2 / 8 E_C).  Used for the
    paper's "where does our qubit sit" figure: ibm_brisbane q109 gives 37.1,
    the UC Berkeley / Chinese / Stanford qutrits 60-112.
    """
    anhar = f12_hz - f01_hz
    EC = -h * anhar
    EJ = (h ** 2 * (f01_hz - anhar) ** 2) / (8 * EC)
    return EJ / EC


#: E_J/E_C values of other groups' qutrits, as collected in figure/picasso.ipynb
EJEC_OTHERS = {
    "ibm_brisbane q109 (this work)": ej_over_ec(4984973330.7, 4677857528.7),
    "UC Berkeley (Blok 2021)": [59.9, 65.4, 59.9],
    "Chinese parity (Dai 2018)": 60.2,
    "Chinese algorithms (Liu 2023)": 75.0,
    "Stanford two-qutrit (Roy 2022)": [112.5, 78.0],
}
