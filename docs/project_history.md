# Project history, 2022–2025

How three repositories became this one, what happened when, and what to know before trusting a number.

## Timeline

| when | device | what |
|---|---|---|
| May–Jun 2022 | ibmq_manila q0 | first pulse gates and Rabi oscillations ("The emergence of Pulse Gate", `pulse-gate.ipynb`, `PPE_RabiOscillation.ipynb`) |
| Jul–Aug 2022 | ibmq_manila, ibmq_belem, ibm_oslo q0 | Qiskit-textbook calibrations, 1–2 Rabi, three-state LDA discriminator; SU(3) decomposition, 216 Cliffords, first qutrit Hadamard on ibm_oslo (25–26 Aug) |
| Aug–Sep 2022 | ibm_oslo, ibmq_manila | Ramsey-like X12 phase-tracking experiments, the "misrotation" over-rotation model |
| Oct–Nov 2022 | ibmq_manila, ibm_oslo | DRAG sweeps with (Xπ X−π)ⁿ, full Gaussian + DRAG calibration of 0–1 and 1–2 on ibm_oslo (OSLO-B parameters) |
| Jun–Aug 2023 | ibm_lagos q0 | randomised phase circuits (RPC), randomized benchmarking (p ≈ 0.96–0.98) and interleaved RB of the Hadamard (p = 0.964) |
| Nov 2023 | ibm_brisbane q0 | readout pulse optimisation (amplitude and frequency sweeps, LDA scores) |
| Dec 2023 | ibm_brisbane q109 | the "qutritium" workflow (`utility.DataAnalysis`), DRAG v1–v3 of the 96 dt X12, Y-only / Z-only / YZ maps, fine amplitude |
| Jan–Feb 2024 | ibm_brisbane q109 | RPC on brisbane with DRAG pulses (`report_phase2`), two/three-parameter phase models |
| Apr–May 2024 | ibm_brisbane q1, q109 | spectroscopy / Rabi / Ramsey characterisation of q1; Ramsey-v1 frame phases of q109; APE+DRAG of the 64 dt pulse; E_J/E_C figure |
| Jun–Aug 2024 | ibm_brisbane q109 | pulse-duration study (16–136 dt), rotation-error and APE on the 120 dt pulse; 16 Aug: the repository is pruned ("major update") |
| Sep 2024 – Feb 2025 | ibm_brisbane q109 | the paper campaign on the 40 dt pulse with Qiskit Runtime: rotation error, APE, DRAPE, phase advance α/β, T1, Ramsey, discriminator; figures 0–2 |
| Apr 2025 | — | last commits of `PulsatingPulseShop_pending` (phase advance, 10 Apr 2025) |

## The three repositories

* **PulsatingPulseLab** (99 commits, May 2022 – Nov 2023): the apprenticeship — 45 notebooks at HEAD plus 18 recoverable from git (`misc/original_notebooks/lab_2022/`, with the recovered ones under `recovered_from_git/`). Two tiny parameter files, `xp01.py` / `xp12.py`, are the ancestors of `pulseshop/constants.py`.
* **PulsatingPulseShop** (36 commits, Nov 2023 – Aug 2024): the systematic shop. The "major update 16 august" commit deleted 42 notebooks, 32 PDFs and the `constant.py`/`function.py` helpers; all of them were recovered from git history and are in `misc/original_notebooks/shop_2023_legacy/`, `literature/` and `misc/original_python/`. What survived at HEAD (17 notebooks, `utility.py`, `pulse.py`, 829 MB of pickles) is `misc/original_notebooks/shop_2024/` and `data/shop_2024/`.
* **PulsatingPulseShop_pending** (9 commits, Mar – Apr 2025): the paper repository, a fork of the shop moved to Qiskit Runtime / SamplerV2 (`utility.py` changed accordingly); 19 notebooks, 921 MB of pickles, the paper figures.

## Devices and pulse parameters

`pulseshop/constants.py` (`PARAMS`) records every calibrated pulse set with its date. The pulses got shorter over time — 544 → 320 → 160 → 96 → 64 → 40 samples (272 → 20 ns) — and DRAG became necessary from 96 dt on. The ibm_brisbane qubit 109 numbers of the paper: f01 = 4.985 GHz, anharmonicity −307 MHz, SX12 = 40 dt, amp 0.2368, β = −0.414, E_J/E_C ≈ 37.

## Things found while merging (worth knowing)

1. **Secrets.** Twenty-three copies of IBM Quantum API tokens (at least nine distinct ones) were committed in plain text in notebook cells and outputs, including `bank/asset.ipynb`. They are scrubbed in this repository (`<IBM_QUANTUM_TOKEN_REMOVED>`) but remain in the public history of the old repositories: revoke them.
2. **The 2022 Clifford table was wrong.** `Clifford/probe.ipynb` wrote `clifford_parameter.csv` after a `find_bug()` whose check sat outside its loop; only 31 of the 216 rows reconstruct a Clifford. Only row 0 (the Hadamard) was ever used. `pulseshop.su3` decomposes all 216 correctly (notebook 05).
3. **The 2022–24 readout mitigation used C instead of Cᵀ** in the cvxopt helper; the effect is at the percent level for these nearly symmetric matrices. `pulseshop.readout` uses the transpose (notebook 02).
4. **`TwoH3.ipynb` counted with the wrong index**, so its three printed results were identical; the experiment shots were never saved. The single-Hadamard counts of 25 Aug 2022 are the only Hadamard data (notebook 05).
5. **Several raw-data files have no notebook** (later re-runs): the 11–19 Dec 2023 DRAG maps, the 7 Rabi repeats of May 2024, three phase-advance job folders with `params.json` only. They are kept and indexed in `data/README.md`.
6. **Two conventions coexist** for the heuristic error model `rot_x12(a, p)`: `p` (rotation_script) vs `p/2` (paper/plot); `pulseshop.qutrit` uses `p/2` and says so. The virtual-Z sign convention also flipped between 2022 and 2023 (`Z01(φ) = diag(e^{+iφ},1,1)` vs `diag(e^{-iφ},1,1)`); `pulseshop.qutrit` uses the later one, which is why the 2022 `R01(phi, theta)` equals `R01(theta, phi)` here.
7. **Missing dependencies in the originals**: `constant.py` (only a `.pyc` at HEAD, source recovered from git), the `account.txt` / `bank.json` credential files (never committed, not needed), the `qiskit.tools.jupyter` / `IBMQ` APIs (Qiskit ≤ 0.45) and `qiskit.pulse` (Qiskit < 2) that the hardware cells require.

## Credits

Tien D. Nguyen (Hanoi University of Science / CQT NUS), with the collaborators named in the original notebooks (Linh's Clifford generator, Mingxuan's phase remark, the two IBM accounts of the Ramsey-v1 runs). Coffee shops around Hanoi.
