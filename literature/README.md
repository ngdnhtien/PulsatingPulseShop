# literature/

The 32 papers that were kept in the shop's `paper/` folder (deleted from the repository in Aug 2024, recovered from git history), plus 7 from the 2023 QOC-group reading list found in the archive folder. Files are renamed `Author Year _ short title.pdf`; the original file names are listed for reference. `references.bib` has one BibTeX key per paper.

## The device

- **`koch2007`** -- Koch et al., Charge-insensitive qubit design derived from the Cooper pair box, Phys. Rev. A 76, 042319 (2007). *the transmon Hamiltonian, E_J/E_C, anharmonicity and charge dispersion; Fig. 0 of the paper reproduces its charge-basis picture.*  (`pdf/Koch2007_transmon_charge_insensitive_qubit.pdf`, was `2007transmon_theory.pdf`)
- **`schreier2008`** -- Schreier et al., Suppressing charge noise decoherence in superconducting charge qubits, Phys. Rev. B 77, 180502 (2008). *first transmon experiment.*  (`pdf/Schreier2008_suppressing_charge_noise_transmon.pdf`, was `first_exp_transmon.pdf`)
- **`peterer2015`** -- Peterer et al., Coherence and decay of higher energy levels of a superconducting transmon qubit, Phys. Rev. Lett. 114, 010501 (2015). *T1/T2 of |2>, the Ramsey-on-1-2 protocol we copied, charge dispersion of the 1-2 transition.*  (`pdf/Peterer2015_coherence_decay_higher_levels_transmon.pdf`, was `coherent_decay_higherlevels.pdf`)

## Calibrating single-qubit (and qutrit) pulses

- **`lucero2008`** -- Lucero et al., High-fidelity gates in a single Josephson qubit, Phys. Rev. Lett. 100, 247001 (2008). *metrology of a single-qubit gate; repeated-pulse amplification.*  (`pdf/Lucero2008_high_fidelity_gates_josephson_qubit.pdf`, was `2008_josephson_qubit.pdf`)
- **`lucero2010`** -- Lucero et al., Reduced phase error through optimized control of a superconducting qubit, Phys. Rev. A 82, 042339 (2010). *the amplified phase error (APE) sequence: pi/2 then n pseudo-identities then pi/2 at a swept phase -- used for every DRAG calibration here.*  (`pdf/Lucero2010_reduced_phase_error_optimized_control_arxiv.pdf`, was `lucero10_reduced_phase_error.pdf`)
- **`lucero2010pra`** -- same, journal version. *journal version of the APE paper.*  (`pdf/Lucero2010_reduced_phase_error_optimized_control_PRA.pdf`, was `lucero10_reduced_phase_error_journal.pdf`)
- **`sheldon2016`** -- Sheldon et al., Characterizing errors on qubit operations via iterative randomized benchmarking, Phys. Rev. A 93, 012301 (2016). *coherent errors grow quadratically, incoherent linearly; the rotation-error amplifying sequence (SX SX)^N of the 2024-25 paper.*  (`pdf/Sheldon2016_errors_iterative_randomized_benchmarking.pdf`, was `fine_tuning_amplitude.pdf`)
- **`chen2016`** -- Chen et al., Measuring and suppressing quantum state leakage in a superconducting qubit, Phys. Rev. Lett. 116, 020501 (2016). *leakage vs phase error trade-off of DRAG (Y vs Z corrections).*  (`pdf/Chen2016_measuring_suppressing_leakage.pdf`, was `simultaneous_suppression.pdf`)
- **`wood2018`** -- Wood and Gambetta, Quantification and characterization of leakage errors, Phys. Rev. A 97, 032306 (2018). *how to define and measure leakage.*  (`pdf/Wood2018_quantification_characterization_leakage.pdf`, was `theory_leakage.pdf`)
- **`martinis2014`** -- Martinis and Geller, Fast adiabatic qubit gates using only sigma_z control, Phys. Rev. A 90, 022307 (2014). *pulse shaping with only Z control.*  (`pdf/Martinis2014_fast_adiabatic_gates_sigmaz.pdf`, was `martinis_sigmaz.pdf`)
- **`li2023`** -- Li et al., Error per single-qubit gate below 10^-4 in a superconducting qubit, npj Quantum Inf. 9, 111 (2023). *state of the art of single-qubit calibration; motivated the DRAG v1-v3 campaign.*  (`pdf/Li2023_error_below_1e-4_single_qubit_gate_arxiv.pdf`, was `error10e-4.pdf`)
- **`li2023npj`** -- same, journal version. *journal version.*  (`pdf/Li2023_error_below_1e-4_single_qubit_gate_npjQI.pdf`, was `error10e-4_2.pdf`)
- **`ma2022`** -- Ma et al., Experimental implementation of noncyclic and nonadiabatic geometric quantum gates in a superconducting circuit, arXiv:2210.03326 (2022). *geometric gates ('thamkhao' = reference).*  (`pdf/Ma2022_noncyclic_nonadiabatic_geometric_gates.pdf`, was `geometric_gate_thamkhao.pdf`)

## Randomized benchmarking

- **`chow2009`** -- Chow et al., Randomized benchmarking and process tomography for gate errors in a solid-state qubit, Phys. Rev. Lett. 102, 090502 (2009). *RB on superconducting qubits.*  (`pdf/Chow2009_randomized_benchmarking_process_tomography.pdf`, was `chow09_RB_PT.pdf`)
- **`morvan2021`** -- Morvan et al., Qutrit randomized benchmarking, Phys. Rev. Lett. 126, 210504 (2021). *the qutrit Clifford group C3 and its RB; our RB notebook follows it (216 Cliffords, r = (1-p)(d-1)/d).*  (`pdf/Morvan2021_qutrit_randomized_benchmarking.pdf`, was `berkeley_rbqutrit.pdf`)
- **`kononenko2021`** -- Kononenko et al., Characterization of control in a superconducting qutrit using randomized benchmarking, Phys. Rev. Research 3, L042007 (2021). *qutrit RB with the pulse-level decomposition into 0-1 and 1-2 rotations.*  (`pdf/Kononenko2021_qutrit_control_randomized_benchmarking.pdf`, was `qutrit_rb_waterloo.pdf`)

## Qutrit control, gates and experiments

- **`bianchetti2010`** -- Bianchetti et al., Control and tomography of a three level superconducting artificial atom, Phys. Rev. Lett. 105, 223601 (2010). *first full qutrit control and tomography.*  (`pdf/Bianchetti2010_control_tomography_three_level_atom.pdf`, was `control_tomography.pdf`)
- **`yurtalan2020`** -- Yurtalan et al., Implementation of a Walsh-Hadamard gate in a superconducting qutrit, Phys. Rev. Lett. 125, 180504 (2020). *the qutrit Hadamard we implemented with three pulses (OneH3 / TwoH3).*  (`pdf/Yurtalan2020_walsh_hadamard_gate_qutrit.pdf`, was `WH_gate.pdf`)
- **`neeley2009`** -- Neeley et al., Emulation of a quantum spin with a superconducting phase qudit, Science 325, 722 (2009). *spin-1 emulation and Berry phase in a qutrit; basis of our berry/ notes.*  (`pdf/Neeley2009_emulation_quantum_spin_phase_qudit.pdf`, was `neeley2009_berry.pdf`)
- **`neeley2009som`** -- same, supporting online material. *pulse sequences for the spin emulation.*  (`pdf/Neeley2009_emulation_quantum_spin_supplement.pdf`, was `neeley-som.pdf`)
- **`fischer2022`** -- Fischer et al., Ancilla-free implementation of generalized measurements for qubits embedded in a qudit space, Phys. Rev. Research 4, 033027 (2022). *IBM Zurich, pulse-level qutrit control on the same hardware.*  (`pdf/Fischer2022_generalized_measurements_qudit_space.pdf`, was `ibm_qutrit_measurement.pdf`)
- **`fischer2023`** -- Fischer et al., Universal qudit gate synthesis for transmons, PRX Quantum 4, 030327 (2023). *virtual-Z phases between subspaces (our 'phase advance') treated systematically.*  (`pdf/Fischer2023_universal_qudit_gate_synthesis_transmons.pdf`, was `ibm_universal_synthesis.pdf`)
- **`galda2021`** -- Galda et al., Implementing a ternary decomposition of the Toffoli gate on fixed-frequency transmon qutrits, arXiv:2109.00558 (2021). *qutrit gates on IBM devices with Qiskit Pulse.*  (`pdf/Galda2021_ternary_toffoli_transmon_qutrits.pdf`, was `ibm_qutrit_toffoli.pdf`)
- **`goss2022`** -- Goss et al., High-fidelity qutrit entangling gates for superconducting circuits, Nat. Commun. 13, 7481 (2022). *two-qutrit gates.*  (`pdf/Goss2022_high_fidelity_qutrit_entangling_gates.pdf`, was `entangling_gate.pdf`)
- **`cervera2022`** -- Cervera-Lierta, Krenn, Aspuru-Guzik, Galda, Experimental high-dimensional GHZ entanglement with superconducting transmon qutrits, Phys. Rev. Applied 17, 024062 (2022). *qutrit experiments on IBM hardware.*  (`pdf/CerveraLierta2022_high_dimensional_GHZ_transmon_qutrits.pdf`, was `expGHZ_alba.pdf`)
- **`blok2021`** -- Blok et al., Quantum information scrambling on a superconducting qutrit processor, Phys. Rev. X 11, 021010 (2021). *Berkeley qutrit processor (E_J/E_C comparison).*  (`pdf/Blok2021_information_scrambling_qutrit_processor.pdf`, was `qutrit_blackhole.pdf`)
- **`roy2022`** -- Roy, Li, Kapit, Schuster, Realization of two-qutrit quantum algorithms on a programmable superconducting processor, arXiv:2211.06523 (2022). *Chicago qutrits (E_J/E_C comparison).*  (`pdf/Roy2022_two_qutrit_algorithms_superconducting_processor.pdf`, was `two_qutrit_algorithms.pdf`)
- **`dai2018`** -- Dai et al., Demonstration of quantum permutation parity determine algorithm in a superconducting qutrit, Chin. Phys. B 27, 060305 (2018). *qutrit algorithm (E_J/E_C comparison).*  (`pdf/Dai2018_permutation_parity_algorithm_qutrit.pdf`, was `parity_chinese.pdf`)
- **`liu2023`** -- Liu et al., Performing SU(d) operations and rudimentary algorithms in a superconducting transmon qudit for d = 3 and d = 4, Phys. Rev. X 13, 021028 (2023). *SU(3)/SU(4) control and decompositions (E_J/E_C comparison).*  (`pdf/Liu2023_SUd_operations_transmon_qudit_d3_d4.pdf`, was `qudit_chinese.pdf`)
- **`campbell2012`** -- Campbell, Anwar, Browne, Magic-state distillation in all prime dimensions using quantum Reed-Muller codes, Phys. Rev. X 2, 041021 (2012). *why qutrits are interesting for fault tolerance.*  (`pdf/Campbell2012_magic_state_distillation_prime_dimensions.pdf`, was `qutrit_magic_state.pdf`)
- **`nguyen2023`** -- H. C. Nguyen, B. G. Bach, T. D. Nguyen, D. M. Tran, D. V. Nguyen, H. Q. Nguyen, Simulating neutrino oscillations on a superconducting qutrit, Phys. Rev. D 108, 023013 (2023). *our own group's qutrit experiment on IBM hardware (the author of this repository is a co-author).*  (`pdf/Nguyen2023_simulating_neutrino_oscillations_qutrit.pdf`, was `qutrit_neutrino.pdf`)

## Optimal control and qudit RB (the 2023 QOC-group reading list)

- **`abdelhafez2019`** -- Abdelhafez et al., Universal gates for protected superconducting qubits using optimal control, Phys. Rev. A 101, 022321 (2020), arXiv:1908.07637. *GRAPE-style optimal control of superconducting qubits; the "QOC" in the group's name.*  (`pdf/Abdelhafez2019_universal_gates_protected_qubits_optimal_control.pdf`, was `qoc_archive/papers/optimal-control/1908.07637.pdf`)
- **`wittler2021`** -- Wittler et al., Integrated tool set for control, calibration, and characterization of quantum devices applied to superconducting qubits (C3), Phys. Rev. Applied 15, 034080 (2021). *model-based calibration; both the arXiv (2009.09866) and journal versions.*  (`pdf/Wittler2021_c3_integrated_toolset_control_calibration_PRApplied.pdf`, `…_arxiv.pdf`)
- **`jafarzadeh2020`** -- Jafarzadeh, Wu, Sanders, Feng, Randomized benchmarking for qudit Clifford gates, New J. Phys. 22, 063014 (2020). *RB theory for d-level Cliffords.*  (`pdf/Jafarzadeh2020_randomized_benchmarking_qudit_clifford_gates.pdf`)
- **`morvan2021prl`**, **`blok2021prx`**, **`lucero2008prl`** -- the journal versions of three papers already listed above (the earlier copies are the arXiv versions).  (`pdf/Morvan2021_qutrit_randomized_benchmarking_PRL.pdf`, `pdf/Blok2021_information_scrambling_qutrit_processor_PRX.pdf`, `pdf/Lucero2008_high_fidelity_gates_josephson_qubit_PRL.pdf`)

## Qudits in general

- **`strauch2011`** -- Strauch, Quantum logic gates for superconducting resonator qudits, Phys. Rev. A 84, 052313 (2011). *qudit gate constructions.*  (`pdf/Strauch2011_quantum_logic_gates_resonator_qudits.pdf`, was `qudit_using_QHO.pdf`)

