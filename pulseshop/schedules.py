"""
Qiskit-Pulse schedule and circuit builders used on the IBM machines.

These need `qiskit < 2` (qiskit.pulse was removed in Qiskit 2.0) and a real
backend object (`QiskitRuntimeService().backend('ibm_brisbane')`, or the old
`IBMProvider`).  Nothing here runs offline; the notebooks call these only
when a backend is available and otherwise show the code.

All builders follow the pattern of the 2024-25 notebooks: a subspace
rotation is a Gaussian or DRAG pulse at the transition frequency, played
inside `pulse.phase_offset(phi, channel)` so that phi sets the rotation axis
without touching the frame of the other subspace.
"""

import numpy as np

try:
    from qiskit import pulse
    from qiskit.circuit import Gate, QuantumCircuit, Parameter
    HAVE_PULSE = True
except Exception:  # pragma: no cover
    HAVE_PULSE = False


def _check():
    if not HAVE_PULSE:
        raise ImportError("qiskit<2 with qiskit.pulse is required for pulseshop.schedules")


# ------------------------------------------------------------ rotations ----
def rotation_schedule(backend, qubit, freq, duration, amp, sigma=None, beta=None, phi=0.0, name=None):
    """
    One pulse on `qubit` at frequency `freq`: Gaussian if beta is None,
    DRAG otherwise; `phi` is the phase offset (rotation axis).
    """
    _check()
    sigma = duration / 4 if sigma is None else sigma
    with pulse.build(backend=backend, name=name) as sched:
        ch = pulse.drive_channel(qubit)
        pulse.set_frequency(freq, ch)
        with pulse.phase_offset(phi, ch):
            if beta is None:
                pulse.play(pulse.Gaussian(duration=duration, amp=amp, sigma=sigma), ch)
            else:
                pulse.play(pulse.Drag(duration=duration, amp=amp, sigma=sigma, beta=beta), ch)
    return sched


def sched_01(backend, qubit, params, phi=0.0, sign=+1):
    """R01 pulse from a params dict {freq, dur, amp, beta}; sign=-1 plays the inverse."""
    return rotation_schedule(backend, qubit, params["freq"], params["dur"], sign * params["amp"],
                             sigma=int(params["dur"] / 4), beta=params.get("beta", 0), phi=phi)


def sched_12(backend, qubit, params, phi=0.0, sign=+1):
    return rotation_schedule(backend, qubit, params["freq"], params["dur"], sign * params["amp"],
                             sigma=int(params["dur"] / 4), beta=params.get("beta", 0), phi=phi)


def r_theta_phi(backend, qubit, freq, duration, pi_amp, theta, phi, beta=None):
    """R(theta, phi): amplitude scaled by theta/pi, axis set by phase_offset(-phi) (lagos/brisbane RPC convention)."""
    return rotation_schedule(backend, qubit, freq, duration, pi_amp * theta / np.pi, beta=beta, phi=-phi)


def schedule_builder(backend, qubit, params, name, frequency):
    """
    Several pulses in a row (2024 `schedule_builder`): params has keys
    num_pulse, angle[i], dur[i], amp[i], beta[i].
    """
    _check()
    with pulse.build(backend=backend, name=name) as sched:
        ch = pulse.drive_channel(qubit)
        pulse.set_frequency(frequency, ch)
        for i in range(params["num_pulse"]):
            with pulse.phase_offset(params["angle"][i], ch):
                pulse.play(pulse.Drag(duration=params["dur"][i], amp=params["amp"][i],
                                      sigma=int(params["dur"][i] / 4), beta=params["beta"][i]), ch)
    return sched


def gate(name, num_qubits=1, params=()):
    _check()
    return Gate(name, num_qubits, list(params))


# ------------------------------------------------------------- readout ----
def measure_schedule(backend, qubit, shift_frequency=0.0, amplitude=0.2385, angle=0.0,
                     duration=1440, sigma=32, width=1312, trailing_delay=1160):
    """Custom GaussianSquare readout pulse (MeasurePulseOptimization, 2024)."""
    _check()
    with pulse.build(backend=backend, name="measure") as sched:
        mch = pulse.measure_channel(qubit)
        ach = pulse.acquire_channel(qubit)
        pulse.shift_frequency(shift_frequency, mch)
        pulse.play(pulse.GaussianSquare(duration=duration, sigma=sigma, width=width, amp=amplitude, angle=angle), mch)
        pulse.acquire(duration, ach, pulse.MemorySlot(0))
        pulse.delay(trailing_delay, mch)
    return sched


# ------------------------------------------------------------ circuits ----
def discriminator_circuits(qubit, num_qubits, x12_sched, reset_after=True, x12_gate_name="x12"):
    """
    The three calibration circuits prepared in |0>, |1> (backend X), |2>
    (X then our X12 pulse) that precede every experiment package.
    """
    _check()
    x12 = Gate(x12_gate_name, 1, [])
    circs = []
    for level in range(3):
        qc = QuantumCircuit(num_qubits, 1)
        if level >= 1:
            qc.x(qubit)
        if level == 2:
            qc.append(x12, [qubit])
            qc.add_calibration(x12, [qubit], x12_sched)
        qc.measure(qubit, 0)
        if reset_after and level == 2:
            qc.append(x12, [qubit])  # unconditional reset of |2> after the measurement
        circs.append(qc)
    return circs


def pseudo_identity_circuits(qubit, num_qubits, sx12_plus, sx12_minus, reps_list, prepare_1=True):
    """
    Rotation-error amplifying sequence: |1> -> SX12 -> (SX12 -SX12)^reps  [or
    (SX12 SX12)^reps when sx12_minus is sx12_plus] -> X -> measure.
    """
    _check()
    plus, minus = Gate("sx12_plus", 1, []), Gate("sx12_minus", 1, [])
    circs = []
    for reps in reps_list:
        qc = QuantumCircuit(num_qubits, 1)
        if prepare_1:
            qc.x(qubit)
        qc.append(plus, [qubit])
        for _ in range(reps):
            qc.append(plus, [qubit]); qc.append(minus, [qubit])
        qc.x(qubit)
        qc.measure(qubit, 0)
        qc.add_calibration(plus, [qubit], sx12_plus)
        qc.add_calibration(minus, [qubit], sx12_minus)
        circs.append(qc)
    return circs


def drag_sweep_circuits(backend, qubit, freq, duration, amp, sigma, n_pairs, betas):
    """
    (X_pi X_-pi)^n with DRAG beta as a circuit Parameter (DRAG_calibration_01, 2022).
    Returns one circuit per beta.
    """
    _check()
    beta = Parameter("drive_beta")
    with pulse.build(backend=backend, default_alignment="sequential") as XX:
        ch = pulse.drive_channel(qubit)
        pulse.set_frequency(freq, ch)
        pulse.play(pulse.Drag(duration=duration, amp=amp, sigma=sigma, beta=beta), ch)
        pulse.shift_phase(-np.pi, ch)
        pulse.play(pulse.Drag(duration=duration, amp=amp, sigma=sigma, beta=beta), ch)
        pulse.shift_phase(-np.pi, ch)
    XXg = Gate("XX", 1, [beta])
    qc = QuantumCircuit(1, 1)
    qc.x(0)
    for _ in range(n_pairs):
        qc.append(XXg, [0])
    qc.measure(0, 0)
    qc.add_calibration(XXg, (0,), XX, [beta])
    return [qc.assign_parameters({beta: b}, inplace=False) for b in betas]


def rb_pulse_sequence(backend, qubit, f01, f12, pulse01, pulse12, params_sequence, alpha, beta, gamma):
    """
    Concatenate the three-pulse decompositions of a Clifford sequence with
    virtual-Z bookkeeping (irmb_run.ipynb `create_pulse_sequence`).
    pulse01/pulse12 = dict(duration, pi_amp, sigma, beta or None).
    """
    _check()
    from .clifford import pulse_sequence_phases
    pulses, _ = pulse_sequence_phases(params_sequence, alpha, beta, gamma)
    with pulse.build(backend=backend, default_alignment="sequential") as seq:
        ch = pulse.drive_channel(qubit)
        for sub, theta, phi in pulses:
            p = pulse01 if sub == "01" else pulse12
            pulse.set_frequency(f01 if sub == "01" else f12, ch)
            with pulse.phase_offset(-phi, ch):
                if p.get("beta") is None:
                    pulse.play(pulse.Gaussian(duration=p["duration"], amp=p["pi_amp"] * theta / np.pi, sigma=p["sigma"]), ch)
                else:
                    pulse.play(pulse.Drag(duration=p["duration"], amp=p["pi_amp"] * theta / np.pi, sigma=p["sigma"], beta=p["beta"]), ch)
    return seq
