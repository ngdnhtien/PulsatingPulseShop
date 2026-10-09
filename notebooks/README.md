# notebooks/

Twelve notebooks, in reading order. Each one imports `pulseshop` from the folder above and loads the saved data in `data/`; the plots they make go to `figures/generated/`. Cells that would talk to IBM hardware are guarded by `backend = None`.

| # | notebook | years | what it does |
|---|---|---|---|
| 01 | `01_pulse_gates_rabi_spectroscopy` | 2022–25 | how a pulse gate is built; spectroscopy and Rabi; the π amplitude vs pulse duration |
| 02 | `02_readout_discrimination` | 2022–25 | three generations of IQ discriminators, confusion matrices, readout mitigation |
| 03 | `03_drag_calibration` | 2022–25 | four ways to find the DRAG coefficient, ending with DRAPE (β = −0.41) |
| 04 | `04_coherent_errors_rotation_ape` | 2022–25 | over-rotation and phase error of the 1–2 pulse; the paper's Fig. 1 and Fig. 2 |
| 05 | `05_virtual_z_su3_clifford_hadamard` | 2022–23 | virtual Z, SU(3) three-pulse decomposition, the 216 Cliffords, the qutrit Hadamard |
| 06 | `06_randomized_benchmarking` | 2023 | RB and interleaved RB on ibm_lagos |
| 07 | `07_phase_tracking` | 2022–24 | frame phases between the subspaces: Ramsey-like, randomised circuits, pseudo-identity Ramsey |
| 08 | `08_phase_advance` | 2024–25 | the paper's phase-advance measurement of α and β with the 20 ns pulses |
| 09 | `09_coherence_t1_ramsey` | 2024–25 | T1 of |1⟩ and |2⟩, Ramsey fringes, the 1–2 frequency doublet |
| 10 | `10_transmon_simulation` | 2024–25 | Cooper-pair box, rotating frames, pulse trains, the drive-frame qutrit model |
| 11 | `11_paper_figures_and_story` | 2025 | the paper's argument, figure gallery, headline numbers, E_J/E_C |
| 12 | `12_qutrit_rb_2025_and_drape_2026` | 2023, 2025–26 | what the archive folder added: drive strengths λ, AAE/APE/DRAPE reduced data, qutrit RB with corrected vs uncorrected pulses, Lindblad T1 and Ramsey fits, the QOC-group session of 2023 |
