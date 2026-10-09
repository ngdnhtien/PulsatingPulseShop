# High-fidelity control in higher dimensions of charge-sensitive transmon devices

*Project proposal of the QOC group, 2023 (text of `qoc_proposal_2023.docx`).*

## Abstract

The widely used transmon devices are well-suited for the realization of three-level systems, also known as superconducting qutrits. While high-fidelity single qutrit gates have been realized on several architectures [MRB+21] [YSK+20], detailed descriptions of dominant noise processes are often overlooked or bypassed by choice of parameters. For example, [MRB+21] employed an EJ/EC ratio that was beyond typical values of transmon devices (30-50), resulting in the insensitivity of charge-noise at the expense of lowering anharmonicity. On the other hand, [YSK+20] operates at the optimal flux-symmetry point of a capacitively-shunted flux transmon, complicating the physical implementation in exchange for the retention of both anharmonic and non-dephasing features.

The goal of this project is to explore how well we can control standard fixed-frequency transmon qutrits, which are ubiquitous due to their simplicity and scalability in terms of design/fabrication. To control such devices, standard Gaussian-shaped pulses were employed. Given a set of native un-optimized gates, we then characterize errors in superconducting qutrits and show that it is possible to obtain high-fidelity operation with a judicious choice of control parameters. We quantify these improvements using qutrit randomized benchmarking as well as monitoring leakage out of qutrit’s manifold. Specifically,

Figure 1: We show that AC Stark shifts in qubit languages are in fact logical errors in qutrit language, which manifests themselves as level repulsion, leading to additional phases that can be measured using a Ramsey-like experiment and corrected in an algorithmic fashion using virtual Z-gates [MWS+17].

Figure 2a, 2b: We experimentally verify that 1/f noises are the dominant sources of decoherence in our devices. This can be done by performing a standard detuned-Ramsey experiment which shows the splitting of transition frequency of higher subspace [PBJ+14], thereby confirming the increasing charge dispersion of the transmon ladder. Large charge dispersion consequently leads to strongly dependent gate fidelity on pulse duration, which will also be verified. The result is an optimal gate duration that is short enough to accommodate a broader range of frequencies due to charge dispersion.
Note: We may add novelty by replacing the Ramsey experiment with a recently demonstrated technique to measure transmon charge noise called spin-locking spectroscopy [SVB+21].

Figure 3a, 3b: With the gate duration being optimized, we employ DRAG correction with two additional control degrees of freedom. [CKQ+15] showed that by introducing a small detuning to the DRAG envelope 𝜹f, the phase error can be further suppressed which can be verified by performing qubit state tomography. We experimentally verify this and analyze if it works well with our optimal gate duration.

Figure 4: Next, since we are using short pulses, we expect leakage to be more pronounced in our driving scheme, and we hypothesize that such leakage rate is overlooked with qutrit randomised benchmarking protocol. To this end, we perform interleaved qutrit RB while varying DRAG scaling parameters and simultaneously measure leakage (Supplementary: How to measure state 3 with high accuracy) out of computational subspace.

References

