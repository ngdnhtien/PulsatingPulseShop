# misc/

The original material, untouched except that IBM Quantum API tokens were replaced by `<IBM_QUANTUM_TOKEN_REMOVED>` (25 occurrences in 23 notebooks; none were found in the notebooks added from the archive folder). Nothing here is needed to run the curated notebooks; it is the archive.

* `original_notebooks/lab_2022/` — PulsatingPulseLab at its last commit (Nov 2023); `recovered_from_git/` holds the 18 notebooks deleted earlier in its history.
* `original_notebooks/shop_2023_legacy/` — the 42 notebooks deleted from PulsatingPulseShop on 16 Aug 2024, recovered from git.
* `original_notebooks/shop_2024/` — PulsatingPulseShop at its last commit (Aug 2024).
* `original_notebooks/pending_2025/` — PulsatingPulseShop_pending at its last commit (Apr 2025).
* `original_notebooks/unified_2025/` — the `unifiedPPS` analysis of 2025 (`paper.ipynb` makes the paper figures from the reduced data; `master_eqn`, `sim`, `transmon_sim`, `fourier`, `phase_advance`, `sensitivity`, `rb_plot`), from the archive folder.
* `original_notebooks/qutrit_error_2026/` — the DRAPE study of Oct 2025 – Jan 2026 (`extract_lambdas`, `error_amplification`, `simulation`, `fourier`, `fourier_2`, `old_code` = the May-2025 reduction of the raw pickles, `unitary`, `figures`).
* `original_notebooks/qoc_2023/rough_rabi_12.ipynb` — the 5 Feb 2023 Rabi on ibm_oslo (old `IBMQ` provider); `original_notebooks/pending_2025/ramsey_script_2025-01-28.ipynb` — the Jan-2025 Ramsey script.
* `original_python/` — `xp01.py`, `xp12.py` (2022), `constant.py`, `function.py` (2023, recovered), `utility.py` + `pulse.py` (2024), `utility.py` (2025), `unified_2025/utility.py` (the 2025 variant), `qoc_2023/{unitary_gate,utility,constant}.py` (Feb 2023), the two original READMEs.

## Where each original notebook's content went

| era | original notebook | curated notebook(s) that cover it |
|---|---|---|
| `lab_2022` | `Clifford/probe.ipynb` | 05 |
| `lab_2022` | `Gell-Mann/VZ-proof.ipynb` | 05 |
| `lab_2022` | `Phase tracking protocols/data_processing.ipynb` | — (empty / stub) |
| `lab_2022` | `Phase tracking protocols/ramsey_like_data_processing.ipynb` | — (empty / stub) |
| `lab_2022` | `Phase tracking protocols/ramsey_like_protocol.ipynb` | 07 |
| `lab_2022` | `Phase tracking protocols/randomized_circuit_protocol.ipynb` | 07 |
| `lab_2022` | `Pulses/DRAG N-site/DRAG.ipynb` | 03 |
| `lab_2022` | `Pulses/DRAG N-site/DRAG_12.ipynb` | 03 |
| `lab_2022` | `Pulses/DRAG N-site/Oslo/DRAG.ipynb` | 03 |
| `lab_2022` | `Pulses/DRAG N-site/Oslo/DRAG_12.ipynb` | 03 |
| `lab_2022` | `Pulses/DRAG N-site/Oslo/DRAG_12_fIBM.ipynb` | 03 |
| `lab_2022` | `Pulses/DRAG N-site/Oslo/DRAG_12_fIBM_backup.ipynb` | 03 |
| `lab_2022` | `Pulses/DRAG N-site/Oslo/full_calibration_01.ipynb` | 01, 03 |
| `lab_2022` | `Pulses/DRAG N-site/Oslo/rabi01_oslo.ipynb` | 01, 03 |
| `lab_2022` | `Pulses/DRAG N-site/Oslo/rabi01_oslo_qubit0.ipynb` | 01, 03 |
| `lab_2022` | `Pulses/DRAG N-site/Oslo/rabi12_oslo.ipynb` | 01, 03 |
| `lab_2022` | `Pulses/DRAG N-site/discriminator.ipynb` | 02, 03 |
| `lab_2022` | `Pulses/DRAG N-site/rabi12_manila.ipynb` | 01, 03 |
| `lab_2022` | `Pulses/Full Calibration/DRAG_calibration_01.ipynb` | 01, 03 |
| `lab_2022` | `Pulses/Full Calibration/DRAG_calibration_12.ipynb` | 01, 03 |
| `lab_2022` | `Pulses/Full Calibration/drag_ramsey_exp_12.ipynb` | 01, 03, 07 |
| `lab_2022` | `Pulses/Full Calibration/full_calibration.ipynb` | 01 |
| `lab_2022` | `Pulses/Full Calibration/gaussian_calibration_01.ipynb` | 01 |
| `lab_2022` | `Pulses/Full Calibration/gaussian_calibration_12.ipynb` | 01 |
| `lab_2022` | `Pulses/ibmq_belem/rabi_01.ipynb` | 01 |
| `lab_2022` | `Pulses/ibmq_manila/qubit=0/DRAG.ipynb` | 03 |
| `lab_2022` | `Pulses/ibmq_manila/qubit=0/Qiskit-Experiments-Calibrating.ipynb` | 01 |
| `lab_2022` | `Pulses/ibmq_manila/qubit=0/Rabi (0-1).ipynb` | 01 |
| `lab_2022` | `Pulses/ibmq_manila/qubit=0/Rabi (1-2).ipynb` | 01 |
| `lab_2022` | `Pulses/rabi01_belem.ipynb` | 01 |
| `lab_2022` | `Pulses/rabi12_belem.ipynb` | 01 |
| `lab_2022` | `QuantumExperiment/AmplitudeCorrection/amplitude_correction.ipynb` | 01, 04 |
| `lab_2022` | `QuantumExperiment/Hadamard/OneH3.ipynb` | 05 |
| `lab_2022` | `QuantumExperiment/Hadamard/TwoH3.ipynb` | 05 |
| `lab_2022` | `QuantumExperiment/Misrotation/Cryostat.ipynb` | 04 |
| `lab_2022` | `QuantumExperiment/Misrotation/ErrorModel_Epsilon.ipynb` | 04 |
| `lab_2022` | `QuantumExperiment/Ramsey/ramsey_ansatz_01.ipynb` | 07, 09 |
| `lab_2022` | `QuantumExperiment/Ramsey/ramsey_data_processing_01.ipynb` | 07, 09 |
| `lab_2022` | `QuantumExperiment/Ramsey/ramsey_exp_12.ipynb` | 07, 09 |
| `lab_2022` | `QuantumExperiment/Ramsey/ramsey_exp_result_01.ipynb` | 07, 09 |
| `lab_2022` | `QuantumExperiment/Ramseyy_ver2/Cryostat.ipynb` | 04, 07 |
| `lab_2022` | `QuantumExperiment/Ramseyy_ver2/Harvester.ipynb` | 07 |
| `lab_2022` | `QuantumExperiment/Ramseyy_ver2/Painter.ipynb` | 07 |
| `lab_2022` | `QuantumExperiment/Sheldon2015/Cryostat.ipynb` | — (empty / stub) |
| `lab_2022` | `QuantumExperiment/Virtual-Z/vz.ipynb` | 05 |
| `lab_2022` | `PPE_RabiOscillation.ipynb` | 01 |
| `lab_2022` | `Pulses/calibrating_real_device.ipynb` | 01 |
| `lab_2022` | `Pulses/disciminator.ipynb` | — (kept for reference only) |
| `lab_2022` | `Pulses/discr.ipynb` | 02 |
| `lab_2022` | `Pulses/find_phase.ipynb` | 01, 07 |
| `lab_2022` | `Pulses/fitting.ipynb` | 07 |
| `lab_2022` | `Pulses/ibmq_belem/rabi_01-Copy1.ipynb` | 01 |
| `lab_2022` | `Pulses/ibmq_belem/rabi_12.ipynb` | 01 |
| `lab_2022` | `Pulses/ibmq_manila/qubit=0/rabi_01.ipynb` | 01 |
| `lab_2022` | `Pulses/rabi12.ipynb` | 01 |
| `lab_2022` | `Pulses/ramsey_find_phase.ipynb` | 01, 07 |
| `lab_2022` | `Pulses/ramsey_fitting.ipynb` | 07 |
| `lab_2022` | `QuantumExperiment/RamseyExperiment/ramsey_data_processing.ipynb` | — (empty / stub) |
| `lab_2022` | `QuantumExperiment/RamseyExperiment/ramsey_exp_result.ipynb` | 07 |
| `lab_2022` | `Untitled.ipynb` | — (empty / stub) |
| `lab_2022` | `phase.ipynb` | 01 |
| `lab_2022` | `pulse-gate.ipynb` | 01 |
| `lab_2022` | `su3_decomposition.ipynb` | 05 |
| `shop_2023_legacy` | `calibrator/ape_drag/ape_drag.ipynb` | 01, 03, 04 |
| `shop_2023_legacy` | `calibrator/ape_drag/data/fit.ipynb` | 01, 03, 04 |
| `shop_2023_legacy` | `calibrator/ape_drag_sim/main.ipynb` | 01, 03, 04 |
| `shop_2023_legacy` | `calibrator/ape_drag_sim/processing.ipynb` | — (empty / stub) |
| `shop_2023_legacy` | `calibrator/drag/drag.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/dragv1/drag01.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/dragv1/drag12.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/dragv1/dragv1.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/dragv2/dragv2.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/dragv3/YZ.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/fine_amplitude/amplitude.ipynb` | 01, 04 |
| `shop_2023_legacy` | `calibrator/meas_pulse/meas_pulse.ipynb` | 01, 02 |
| `shop_2023_legacy` | `calibrator/onlyY/Y.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/onlyZ/Z.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/rabi/rabi01.ipynb` | 01 |
| `shop_2023_legacy` | `calibrator/rabi/rabi12_DRAG.ipynb` | 01, 03 |
| `shop_2023_legacy` | `calibrator/rabi/rabi12_woDRAG.ipynb` | 01, 03 |
| `shop_2023_legacy` | `experiment/Generalize phase tracking protocol (brisbane).ipynb` | 07 |
| `shop_2023_legacy` | `experiment/Track_phase/Generalize_phase_tracking_protocol.ipynb` | 07 |
| `shop_2023_legacy` | `experiment/Track_phase/rabi01.ipynb` | 01, 07 |
| `shop_2023_legacy` | `experiment/Track_phase/rabi12-checkpoint.ipynb` | 01, 07 |
| `shop_2023_legacy` | `experiment/Track_phase/report_phase2.ipynb` | 07 |
| `shop_2023_legacy` | `experiment/Track_phase/rpc_data_processing.ipynb` | — (empty / stub) |
| `shop_2023_legacy` | `experiment/Track_phase/rpc_data_processing_halfpi.ipynb` | 07 |
| `shop_2023_legacy` | `experiment/Track_phase/rpc_protocol.ipynb` | 07 |
| `shop_2023_legacy` | `experiment/Track_phase/rpc_protocol_1_halfpi_gate.ipynb` | 07 |
| `shop_2023_legacy` | `experiment/ampvdrag/ampvdrag.ipynb` | 01, 03 |
| `shop_2023_legacy` | `experiment/ampwdrag/ampwdrag.ipynb` | 01, 03 |
| `shop_2023_legacy` | `experiment/berry/berry.ipynb` | 05 |
| `shop_2023_legacy` | `experiment/berry/decomposer_numpy.ipynb` | 05 |
| `shop_2023_legacy` | `experiment/berry/decomposer_sympy.ipynb` | 05 |
| `shop_2023_legacy` | `experiment/interleaved_rb/irmb_result.ipynb` | 06 |
| `shop_2023_legacy` | `experiment/interleaved_rb/irmb_run.ipynb` | 06 |
| `shop_2023_legacy` | `experiment/optimal_duration/optimal_duration.ipynb` | 01 |
| `shop_2023_legacy` | `experiment/optimized_meas_pulse/meas_amp_tuning.ipynb` | 01, 02 |
| `shop_2023_legacy` | `experiment/optimized_meas_pulse/meas_freq_tuning.ipynb` | 02 |
| `shop_2023_legacy` | `experiment/ramseyv0/ramseyv0_freq12.ipynb` | 09 |
| `shop_2023_legacy` | `experiment/specify measure frequency.ipynb` | 02 |
| `shop_2023_legacy` | `experiment/trade_off/trade-off.ipynb` | — (empty / stub) |
| `shop_2023_legacy` | `figure/picasso.ipynb` | 07, 11 |
| `shop_2023_legacy` | `rb/RMB.ipynb` | 06 |
| `shop_2023_legacy` | `rb/clifford_gen.ipynb` | 05, 06 |
| `shop_2024` | `MeasurePulseOptimization.ipynb` | 02 |
| `shop_2024` | `bank/asset.ipynb` | — (credential handling; not carried over) |
| `shop_2024` | `calibrator/phase_error/qubit109/main.ipynb` | 01, 03, 09 |
| `shop_2024` | `calibrator/rotation_error/qubit109/main.ipynb` | 01, 04, 09 |
| `shop_2024` | `characterization/rabi01/main.ipynb` | 01 |
| `shop_2024` | `characterization/rabi12/qubit109/data.ipynb` | 01, 09 |
| `shop_2024` | `characterization/rabi12/qubit109/script.ipynb` | 01, 09 |
| `shop_2024` | `characterization/ramseyv0_01/ramsey_freq.ipynb` | 09 |
| `shop_2024` | `characterization/ramseyv0_12/ramsey_freq.ipynb` | 09 |
| `shop_2024` | `characterization/spectroscopy01/main.ipynb` | 01 |
| `shop_2024` | `characterization/spectroscopy12/main.ipynb` | 01 |
| `shop_2024` | `experiment/ramseyv1/data/round1/alpha/picasso.ipynb` | 07, 11 |
| `shop_2024` | `experiment/ramseyv1/ramseyv1.ipynb` | 07 |
| `shop_2024` | `log.ipynb` | docs/lab_log_2024.md |
| `shop_2024` | `simulation/frame.ipynb` | 10 |
| `shop_2024` | `simulation/full_transmon.ipynb` | 10 |
| `shop_2024` | `simulation/pulse_train.ipynb` | 10 |
| `pending_2025` | `bank/asset.ipynb` | — (credential handling; not carried over) |
| `pending_2025` | `calibrator/drape/drape_script.ipynb` | 01, 03, 04 |
| `pending_2025` | `calibrator/rotation/rotation_script.ipynb` | 01, 04 |
| `pending_2025` | `characterization/T1/T1_script.ipynb` | 09 |
| `pending_2025` | `characterization/ape/ape.ipynb` | 04 |
| `pending_2025` | `characterization/ape/data_processing.ipynb` | — (empty / stub) |
| `pending_2025` | `characterization/discrim/discrim.ipynb` | 02 |
| `pending_2025` | `characterization/rabi/rabi_script.ipynb` | 01 |
| `pending_2025` | `characterization/ramsey/ramsey_script.ipynb` | 09 |
| `pending_2025` | `experiment/phase_advance/phase_advance.ipynb` | 08 |
| `pending_2025` | `experiment/phase_advance/phase_advance_plot.ipynb` | 08, 11 |
| `pending_2025` | `experiment/phase_advance/simulation.ipynb` | 08, 10 |
| `pending_2025` | `paper/experiment_ids.ipynb` | 04, 11 |
| `pending_2025` | `paper/plot.ipynb` | 04, 11 |
| `pending_2025` | `paper/story.ipynb` | 04, 11 |
| `pending_2025` | `simulation/fig0.ipynb` | 10 |
| `pending_2025` | `simulation/frame.ipynb` | 10 |
| `pending_2025` | `simulation/full_transmon.ipynb` | 10 |
| `pending_2025` | `simulation/pulse_train.ipynb` | 10 |

## Added from the archive folder (Oct 2026)

| era | original notebook | curated notebook(s) that cover it |
|---|---|---|
| `unified_2025` | `paper.ipynb` (paper figures 1–6 from the reduced data) | 11, 12 |
| `unified_2025` | `rb_plot.ipynb` (per-seed RB curves, post-selection, bounded fit) | 12 |
| `unified_2025` | `master_eqn.ipynb` (Lindblad T1 chain, Ramsey three-frequency fits) | 12 |
| `unified_2025` | `sim.ipynb`, `transmon_sim.ipynb` (first five-level pulse simulations, gate-based AAE fit) | 10, 12 |
| `unified_2025` | `fourier.ipynb` (FFT of DRAG pulses, E_J/E_C, charge dispersion, leakage toy) | 10, 11 |
| `unified_2025` | `phase_advance.ipynb` = `simulation.ipynb` (phase-advance note simulation) | 08 |
| `unified_2025` | `sensitivity.ipynb` (two-level AAE toy) | 12 |
| `qutrit_error_2026` | `extract_lambdas.ipynb` | 12 |
| `qutrit_error_2026` | `error_amplification.ipynb`, `simulation.ipynb` (DRAPE closed form, ε/β₀/ξ extraction) | 12 |
| `qutrit_error_2026` | `old_code.ipynb` (raw pickles → reduced npz, May 2025) | 04, 12 |
| `qutrit_error_2026` | `fourier.ipynb`, `fourier_2.ipynb`, `unitary.ipynb`, `figures.ipynb` | — (scratch) |
| `qoc_2023` | `rough_rabi_12.ipynb` | 12 |
| `pending_2025` | `ramsey_script_2025-01-28.ipynb` | 09, 12 |
