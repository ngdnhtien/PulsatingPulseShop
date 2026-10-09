# data/

Every measurement kept over the three years, converted from Python pickles to plain files so that nothing here needs Qiskit to open:

* `iq_data.npy` — complex array `(n_circuits, n_shots)` of single-shot kerneled IQ points (`meas_level=1`), or `(n_circuits,)` of averaged values;
* `params.json` — what was swept and with which pulses (backend, qubit, date, duration, amplitude, DRAG beta, repetitions, phases, shots);
* small `.npy` — populations, fitted centres, confusion matrices, as the original notebooks saved them.

Load with `pulseshop.io.load_job("<era>/<experiment>/data/<job_id>")`, `io.load_npy(...)`, `io.load_json(...)`. Four eras, one folder each.

## `lab_2022/` — PulsatingPulseLab (ibmq_manila, ibm_oslo; 2022)

| file | what | made by |
|---|---|---|
| `oslo_2022-08-25_discriminator_shots.npy` | `(3, 20000)` IQ shots prepared in \|0⟩, \|1⟩, \|2⟩ on ibm_oslo q0 (544 dt pulses) | `Pulses/discr.ipynb` |
| `oslo_2022-08-26_two_h3_shots.npy` | `(3, 20000)` calibration shots of the two-Hadamard job of 26 Aug | `QuantumExperiment/Hadamard/TwoH3.ipynb` |
| `clifford_parameter_2022.csv` | 216 × 9 pulse angles of the Cliffords as computed in 2022 — only row 0 (the Hadamard) is correct, see notebook 05 | `Clifford/probe.ipynb` |
| `manila_2022-09-20_ramsey_8gates_populations.csv` | 4 × 3 populations: three calibration circuits and the Ramsey-like sequence with 8 X12(π/2) | `QuantumExperiment/Ramseyy_ver2/Harvester.ipynb` |
| `oslo_2022-08-27_find_phase_random_angles.csv` | 95 random angle triples of the first randomised phase experiment (its populations were not kept) | `Pulses/find_phase.ipynb` |

Most 2022 experiments retrieved their data straight from IBM jobs and never wrote files; their results live in `figures/lab_2022/` and in the original notebooks (`misc/original_notebooks/lab_2022/`).

## `shop_2023_legacy/` — deleted from PulsatingPulseShop in Aug 2024, recovered from git (ibm_brisbane q0 / q109, ibm_lagos; Nov 2023 – May 2024)

| folder | what | made by |
|---|---|---|
| `calibrator/dragv1/data/{9dec,14dec,15dec,19dec}` | mitigated P0/P1/P2 of the (X12 X12⁻¹)ⁿ DRAG-beta sweeps, one file per state and repetition; 9/14 Dec: 30 betas in −5…5, 15/19 Dec: 100 betas in −3…0 | `calibrator/dragv1/drag12.ipynb`, `dragv1.ipynb` |
| `calibrator/dragv1/data/11dec` | same for the detuning sweep −5…5 MHz (70 points), repetitions 1…20 | `calibrator/dragv1/drag12.ipynb` |
| `calibrator/dragv3/data/*/YZ_data_2D*.npy` | 2-D maps of P2 vs (detuning, beta) of the APE sequence; 22 Dec: 15 detunings (−4.5…1.9 MHz) × 30 betas (−5…3); 15–19 Dec: 25 × 20 grids whose axes are only visible in the saved figures (17 Dec: detuning −0.5…0.25 MHz × β −0.8…0) | `calibrator/dragv3/YZ.ipynb` |
| `calibrator/onlyY/data/19dec`, `onlyZ/data/19dec` | APE with only the Y (beta) or only the Z (detuning) correction, 100 points, ±5 or ±10 MHz, with/without DRAG | `calibrator/onlyY/Y.ipynb`, `onlyZ/Z.ipynb` |
| `calibrator/fine_amplitude/data/27nov` | P0/P1/P2 after 0…22 repetitions of the 1–2 half-pi pulse + `param.txt` note | `calibrator/fine_amplitude/amplitude.ipynb` |
| `calibrator/rabi/data/{14dec,23dec}` | averaged 1–2 Rabi traces of the 80/96 dt pulses | `calibrator/rabi/rabi12_*.ipynb` |
| `calibrator/ape_drag/data/rabi_osc` | 7 repeats of the 1–2 Rabi oscillation (64 dt pulse, amp −0.75…0.75, P2) | `calibrator/ape_drag/ape_drag.ipynb` |
| `calibrator/ape_drag/data/rough_x12` | X12 pseudo-identity beta sweeps, raw and mitigated, reps 1/3/5/7 | same |
| `calibrator/ape_drag/data/ape_drag` | APE+DRAG beta sweeps of SX12: `pop{1,2}_sx12_<job>_-2_to_1_357{7,9}` = reps (3,5,7,9) × 150 betas in −2…1; `_0_to_5_357` = reps (3,5,7) × 150 betas in 0…5 | same |
| `calibrator/ape_drag_sim/data/rabi_osc` | the Rabi job of `ape_drag_sim/main.ipynb` | `calibrator/ape_drag_sim/main.ipynb` |
| `experiment/optimal_duration/data` | Rabi (80 dt) and APE+DRAG populations of the pulse-duration study | `experiment/optimal_duration/optimal_duration.ipynb` |
| `rb/data/Clifford3_unique.npy` | the 216 Clifford matrices `(216, 3, 3)` | `rb/clifford_gen.ipynb` |
| `rb/rb_lagos_2023-08_avg_p0_lengths_1_to_97_49jobs.npy` | RB survival P0 vs sequence length 1…97, averaged over 49 jobs (recovered from a printed output) | `rb/RMB.ipynb` |
| `rb/irb_hadamard_lagos_2023-08-29_avg_p0_lengths_1_to_97.npy` | interleaved-RB (Hadamard) survival, 50 jobs | `experiment/interleaved_rb/irmb_result.ipynb` |

## `shop_2024/` — PulsatingPulseShop as of Aug 2024 (ibm_brisbane q1 and q109; Apr – Aug 2024)

| folder | what | made by |
|---|---|---|
| `characterization/spectroscopy01/data`, `spectroscopy12/data` | averaged spectroscopy traces of q1, rounds 1–3 (±25 MHz / 1 MHz, ±50 MHz / 2 MHz) | `characterization/spectroscopy*/main.ipynb` |
| `characterization/rabi01/data` | averaged 0–1 Rabi traces of q1, amp −0.75…0.75 (100), 32 dt and 120 dt | `characterization/rabi01/main.ipynb` |
| `characterization/ramseyv0_01/data`, `ramseyv0_12/data` | averaged Ramsey traces, delays 8…2000 dt step 8 (rounds 1–2: 3 and 10 MHz detuning), round 3: 80…4800 dt step 48 | `characterization/ramseyv0_*/ramsey_freq.ipynb` |
| `characterization/rabi12/qubit109/data` | 1–2 Rabi of q109 vs pulse duration: `batch1_mapping/<dur>_{average,single}` (amp −1…1), `batch2_mapping/<dur>_<max>_*`, `batch3_mapping` (−0.1…1.0, with/without active reset, rep delays), `batch4_zoomed`, `batch5_vary_rep_delay`, and the reference clouds `IQ_data_state{0,1,2}_single` | `characterization/rabi12/qubit109/script.ipynb`, `data.ipynb` |
| `calibrator/phase_error/qubit109/data/{48dt,56dt,mapping}` | single-shot IQ of the APE and APE+DRAG runs on the 120 dt SX12: 3 calibration circuits + reps × 100 angles/betas (`round8_ad_7_9_11_13_15_pi`: betas −1…0) | `calibrator/phase_error/qubit109/main.ipynb` |
| `calibrator/rotation_error/qubit109/data/{dur48,dur56,fast_reset,mapping}` | single-shot IQ of the rotation-error sequence, 3 calibration circuits + N = 0…40 (step 2) SX12 pulses; `afterDRAG` rounds on 17 Jul | `calibrator/rotation_error/qubit109/main.ipynb` |
| `experiment/ramseyv1/data/round{1..4}*` | mitigated (and raw) populations of the Ramsey-v1 frame-phase experiment: `alpha`/`beta` × `01234`/`56789` repetitions × 100 phases → `(500, 3)`; `job_id.txt` lists the IBM jobs | `experiment/ramseyv1/ramseyv1.ipynb` |

## `pending_2025/` — PulsatingPulseShop_pending (ibm_brisbane q109; Sep 2024 – Feb 2025, the paper)

One folder per IBM job: `iq_data.npy` + `params.json` (+ `result.json` for the Rabi job that defined the discriminator).

| folder | what | notebook |
|---|---|---|
| `characterization/rabi/data` | 1–2 Rabi with the 40 dt pulse: `cxpsz544…` (two π/2 pulses, 10k shots), `cxsfpfsw…` (one π pulse), `cyb4se57…` (SamplerV2, source of `sx12_params.json`, `x12_params.json`, `rabi_discrim.json`) | 01, 02 |
| `characterization/discrim/data` | 10 000 shots each prepared in \|0⟩, \|1⟩, \|2⟩ (12 Jan 2025) → `central_clusters.npy`, `confusion_matrix.npy` | 02 |
| `characterization/T1/data` + `*_t1_012.npy`, `delay_time_mu.npy` | T1 of \|1⟩ (`cy5we10…`) and \|2⟩ (`cy5wyv30…`), 100 log-spaced delays 4 ns…360 µs; the saved mitigated populations and delay axis (µs) | 09 |
| `characterization/ramsey/data` | 1–2 Ramsey, 250 delays 4 ns…100 µs at 1 / 0.5 / 0.1 MHz detuning | 09 |
| `characterization/ape/data` | APE fringes, 75 phases × reps (1,3) or (5,7), without (`cw0sjvk…`, `cw0t1qe…`) and with (`cw0twsk…`, `cw0v840…`) DRAG | 04 |
| `calibrator/rotation/data` | rotation-error sequence, N = 0…40 pairs of SX12: uncorrected, DRAG-Y, DRAG + rescaled amplitude (3 runs), scaled without DRAG | 04 |
| `calibrator/drape/data` | DRAPE: APE P2 vs DRAG beta for several repetition counts; 21 runs from Sep 2024 to Feb 2025 (`cybdjk2c…`, `cyf2m287…` are the paper's) | 03 |
| `experiment/phase_advance/data` | α and β phase-advance Ramsey runs, 70–75 phases × reps; the comments in the original notebook give: β 1-2-3 `cw38s6wv…`, 4-5-6 `cwa2ffd9…`, 7-8-9 `cwa31j6g…`; α 1-2-3 `cw39nky7…`, 4-5-6 `cwa14zvj…`, 7-8-9 `cwabjrkj…`; Berry α `cwafq3w9…`, β `cwahpkaj…` (three folders have `params.json` only — their IQ data were never saved) | 08 |
| `simulation/re_pop2_*.npy` | measured P2 of the rotation-error runs copied for the master-equation fit | 10 |
| `misc/amp_dt/` | (SX12 amplitude, duration) pairs of the duration study, Oct 2024 | 01 |
| `sx12_params.json`, `x12_params.json`, `rabi_discrim.json`, `central_clusters.npy`, `confusion_matrix.npy` | the pulse parameters and discriminator of the paper | 01–04, 08–09 |

The e-mail addresses that were in `job_id.txt` were removed; the IBM job ids are kept so that the original jobs can be found in the IBM Quantum dashboard.
