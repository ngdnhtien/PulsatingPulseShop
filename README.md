# PulsatingPulseShop

Welcome to PPS quantum mechanic shop. For over 3 years, PulsatingPulseShop has never been a leader in the field of quantum maintenance and repair industry. However, we have young and ambitious people with a wide range of specialties.

We have experience with all sorts of superconducting quantum machines, ranging from the classic 1990's Cooper-pair box to the 2007's everyone-knows-and-loves transmon qubits. Unlike most shops that restrict themselves within a two-dimensional Hilbert space, we made substantial efforts to expand to a much larger marketplace called qudit. We're currently stopping at $d = 3$.

In short, we calibrate microwave pulses to steer the dynamics of these objects, run foundational experiments on them, and learn a thing or two every day about how noisy they are.

## What is in the shop

Four years (2022–2026) of pulse-level control of IBM transmon qutrits — `ibmq_manila`, `ibm_oslo`, `ibm_lagos`, `ibm_brisbane` — merged from three repositories (PulsatingPulseLab, PulsatingPulseShop, PulsatingPulseShop_pending) into one, plus the archive folder found afterwards (the 2025 consolidated analysis, the 2025–26 DRAPE study, the 2023 QOC-group material).

| folder | what |
|---|---|
| `notebooks/` | the story, in twelve notebooks: pulse gates and Rabi → readout → DRAG → coherent errors → virtual Z, SU(3) and the Cliffords → randomized benchmarking → phase tracking → phase advance → T1 and Ramsey → simulation → the paper → what came after (qutrit RB with corrected pulses, DRAPE) |
| `pulseshop/` | the Python toolbox the notebooks use (fitting, readout discrimination, qutrit matrices, Clifford group, phase models, QuTiP simulations, Qiskit-Pulse schedules) |
| `data/` | every measurement kept over the years, as plain `.npy` / `.json` files, indexed in `data/README.md`; the 1.5 GB of raw single-shot arrays are in the `v1.0-data` release (two zip files), to be unzipped into the repository root |
| `figures/` | every plot ever produced, renamed by device, date and content, indexed in `figures/README.md` |
| `images/` | sketches that are not data plots |
| `literature/` | the 39 papers we kept at hand, with a reading list |
| `docs/` | the project history, the lab log, the paper's story, the log of IBM job ids, the bachelor thesis (2024), the QOC proposal (2023) and the DRAPE notes (2026) |
| `misc/` | the original notebooks and scripts, untouched except for the removal of API tokens |

## Running the notebooks

```bash
pip install numpy scipy matplotlib scikit-learn qutip cvxopt sympy jupyter
jupyter lab notebooks/
```

Everything runs offline on the saved data (first download `PulsatingPulseShop_raw_data.zip` and `PulsatingPulseShop_raw_data_2.zip` from the `v1.0-data` release and unzip them in the repository root, or run `sh data/get_raw_data.sh`). Sending new pulses to IBM hardware needs `qiskit<2` (Qiskit Pulse was removed in Qiskit 2.0), `qiskit-ibm-runtime` and an IBM Quantum account; those cells are marked and skipped otherwise.

## Acknowledgement

We thank coffee shops around Hanoi for letting us cook in their place.

## License

MIT — see `LICENSE`. Tien D. Nguyen, 2022–2026.
