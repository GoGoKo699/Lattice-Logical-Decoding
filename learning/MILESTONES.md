# Thirty milestones for lattice logical decoding

This map organizes the project's understanding targets into **15 background milestones** and **15 narrative milestones**. The background joins two bodies of ideas: oscillator error correction and cryptographic lattice problems. The narrative then builds the reduction from its local parity mechanism to the full geometric and computational separation.

Within each phase, the order moves from individual objects to the combined argument. Dependencies refer to earlier milestones. The source pointers lead to authoritative project definitions and proofs, with scholarly attribution in [related work](../references/RELATED_WORK.md). The map is common to all readers; it records neither a reader's progress nor an assessment procedure.

## Selected anchor and the local bridge

The selected educational anchor is **Chris Peikert, A Decade of Lattice Cryptography**. Its [author manuscript](https://eprint.iacr.org/2015/939) supplies the lattice, Gaussian, and LWE foundations. The core route is Section 2.2 (lattices), Section 2.3 (Gaussian distributions), Section 4.2.1 (LWE definitions), and Section 4.2.2 (hardness).

The [Peikert-to-project bridge](PEIKERT_BRIDGE.md) translates conventions and connects those foundations to this project. The oscillator, GKP stabilizer, logical-frame, and new reduction arguments are supplied by the local scientific pages. A Peikert pointer below identifies prerequisite material; it does not attribute the project's quantum construction or theorem to the survey. [Anchor provenance and versions](../references/RELATED_WORK.md#7-selected-educational-anchor) distinguish the manuscript from its journal publication.

## Phase I — Background and preliminaries

### M01 — Oscillator phase space

**Central question.** What does a displacement error change in an oscillator?

**Understanding target.** Explain position and momentum coordinates, distinguish an oscillator from an encoded qubit, and interpret the width of a Gaussian displacement in the declared units.

**Dependencies and story role.** No earlier milestone. Establishes the physical object before introducing its encoding.

**Conceptual connection.** A vector in a real phase space describes the error whose logical effect the decoder must infer.

**Source pointers.** [Model and displacement convention](../science/model.md); [physical interpretation](../science/interpretation.md); [local bridge](PEIKERT_BRIDGE.md).

### M02 — Displacements and symplectic pairing

**Central question.** Why does the order of two displacements matter?

**Understanding target.** Read the Weyl commutation phase and explain how symplectic pairing controls whether two displacement operations commute.

**Dependencies and story role.** M01. Supplies the local algebra behind commuting stabilizers.

**Conceptual connection.** The geometry used by quantum stabilizers is symplectic, while the size of a noise vector is measured by the Euclidean norm.

**Source pointers.** [Model](../science/model.md); [normalization checks](../verification/README.md); [local bridge](PEIKERT_BRIDGE.md).

### M03 — Lattices, bases and Euclidean duality

**Central question.** What information does a lattice basis specify, and what changes when that basis changes?

**Understanding target.** Distinguish a lattice from one basis, interpret covolume and the shortest nonzero vector, and define the Euclidean dual through integer inner products.

**Dependencies and story role.** M01. Introduces the geometric objects before combining them with the quantum algebra.

**Conceptual connection.** Basis coordinates organize a syndrome, but distances and lattice points describe the physical code independently of that bookkeeping.

**Source pointers.** [Peikert Section 2.2: lattice foundations](https://eprint.iacr.org/2015/939); [Model](../science/model.md); [geometry](../science/geometry.md); [local bridge](PEIKERT_BRIDGE.md).

### M04 — Finite-field codes and integer lattices

**Central question.** How can a finite linear subspace specify an infinite lattice?

**Understanding target.** Explain the construction $`\Lambda_C=\{z\in\mathbb Z^m:z\bmod q\in C\}`$, the role of the modulus, and the difference between a generating matrix and its image subspace.

**Dependencies and story role.** M03. Connects elementary linear constraints to the lattice ensemble used later.

**Conceptual connection.** The same public matrix describes both an LWE problem and the oscillator code's integer lattice.

**Source pointers.** [Peikert Section 4.2.1: the lattice associated with LWE](https://eprint.iacr.org/2015/939); [Model](../science/model.md); [balanced subspaces in geometry G1](../science/geometry.md); [local bridge](PEIKERT_BRIDGE.md).

### M05 — Commuting lattice stabilizers

**Central question.** Which displacement lattices define mutually compatible stabilizer conditions?

**Understanding target.** Use symplectic integrality to explain commuting lattice displacements and distinguish a stabilizer lattice from its symplectic dual.

**Dependencies and story role.** M02–M03. Joins the physical algebra with lattice geometry.

**Conceptual connection.** Commuting stabilizers identify a code; their symplectic dual identifies displacements invisible to the syndrome.

**Source pointers.** [GKP construction in the model](../science/model.md); [related work](../references/RELATED_WORK.md); [local bridge](PEIKERT_BRIDGE.md).

### M06 — Logical operations and degeneracy

**Central question.** Why can different displacement errors require the same logical correction?

**Understanding target.** Distinguish syndrome-equivalent errors, stabilizer-equivalent corrections, and nontrivial logical operations. Explain the quotient $`K/(2K)`$ in this construction.

**Dependencies and story role.** M05. Identifies the actual decoding target.

**Conceptual connection.** Recovering a logical class requires less information than reconstructing a full nearest lattice point; the reduction must respect that distinction.

**Source pointers.** [Model](../science/model.md); [logical degeneracy](../science/interpretation.md); [local bridge](PEIKERT_BRIDGE.md).

### M07 — Syndrome sections and logical frames

**Central question.** How does a continuous error become a torus coordinate plus a finite logical label?

**Understanding target.** Interpret $`B_K^{-1}\xi=z+x`$ with integer $`z`$ and fractional $`x`$, and explain why $`x`$ specifies the syndrome while $`z\bmod2`$ specifies the remaining logical frame.

**Dependencies and story role.** M03, M06. Defines the interface shared by geometry and computation.

**Conceptual connection.** Choosing a fundamental cell sets a reference correction; it does not solve the unknown integer-parity problem.

**Source pointers.** [Model](../science/model.md); [finite precision](../science/finite_precision.md); [local bridge](PEIKERT_BRIDGE.md).

### M08 — Gaussian width and total error size

**Central question.** How does independent noise in many coordinates combine into the norm of an error?

**Understanding target.** Distinguish per-coordinate standard deviation from total displacement norm and explain why the relevant real dimension is $`2m`$ for $`m`$ modes.

**Dependencies and story role.** M01, M03. Makes the physical scaling comparison meaningful.

**Conceptual connection.** Small noise per mode does not alone specify the total error; the total norm must be compared with the code's correction radius.

**Source pointers.** [Peikert Section 2.3: Gaussian background](https://eprint.iacr.org/2015/939); [Geometry G4](../science/geometry.md); [interpretation](../science/interpretation.md); [local bridge](PEIKERT_BRIDGE.md).

### M09 — Existence and computational efficiency

**Central question.** How can a decoding rule exist without an efficient algorithm for evaluating it?

**Understanding target.** Separate an unrestricted nearest-point rule from a polynomial-time decoder, and distinguish ensemble-average success from success on every fixed code.

**Dependencies and story role.** M06–M08. Establishes the two performance notions compared by the project.

**Conceptual connection.** Geometric recoverability can coexist with a computational lower bound because the two statements quantify over different decoder resources.

**Source pointers.** [Peikert Section 4.2.2: computational hardness background](https://eprint.iacr.org/2015/939); [Geometry](../science/geometry.md); [interpretation](../science/interpretation.md); [local bridge](PEIKERT_BRIDGE.md).

### M10 — Learning With Errors

**Central question.** What must a decisional LWE algorithm distinguish?

**Understanding target.** Identify the public matrix, hidden secret, error distribution and uniform alternative in $`(A,As+e\bmod q)`$. Keep sample count, modulus and error width explicit.

**Dependencies and story role.** M04. Introduces the computational problem to which decoding will be reduced.

**Conceptual connection.** The public lattice is generated by the same matrix that hides the secret in noisy modular linear equations.

**Source pointers.** [Peikert Section 4.2.1: LWE definitions](https://eprint.iacr.org/2015/939); [Exact assumption in the model](../science/model.md); [LWE conventions in related work](../references/RELATED_WORK.md); [local bridge](PEIKERT_BRIDGE.md).

### M11 — Post-quantum reductions and charged resources

**Central question.** What does a reduction establish when the hypothetical decoder itself uses quantum computation?

**Understanding target.** Explain how a decoder can be used inside a distinguisher, what quantum hardness assumes, and why code-dependent preprocessing must be included in the resource budget.

**Dependencies and story role.** M09–M10. Fixes the logical direction and adversary model before the proof.

**Conceptual connection.** A classical transformation of inputs can remain valid against a quantum algorithm; no coherent sample oracle is thereby supplied.

**Source pointers.** [Peikert Section 4.2.2: hardness reductions](https://eprint.iacr.org/2015/939); [Model](../science/model.md); [hardness](../science/hardness.md); [resource scope](../science/interpretation.md); [local bridge](PEIKERT_BRIDGE.md).

### M12 — Statistical and computational indistinguishability

**Central question.** Which distribution replacements require a numerical error bound, and which require a hardness assumption?

**Understanding target.** Distinguish total variation distance from efficient distinguishability, explain deterministic data processing, and understand why a bounded number of negligible errors remains negligible.

**Dependencies and story role.** M10–M11. Supplies the language for the proof's successive distribution changes.

**Conceptual connection.** Gaussian smoothing is statistical; replacing LWE samples by uniform samples is computational.

**Source pointers.** [Peikert Section 4.2.1: the decisional LWE comparison](https://eprint.iacr.org/2015/939); [Gaussian smoothing](../science/gaussian_smoothing.md); [hybrids in hardness](../science/hardness.md); [local bridge](PEIKERT_BRIDGE.md).

### M13 — Discrete Gaussians and Poisson summation

**Central question.** When can a Gaussian sampled on integers behave smoothly under addition?

**Understanding target.** Distinguish continuous, point-mass discrete and rounded continuous Gaussians. Explain how a theta sum measures the periodic modulation left by a lattice and why its nonzero Fourier terms become small.

**Dependencies and story role.** M03, M08, M12. Provides the analytic mechanism that links a cryptographic error to physical noise.

**Conceptual connection.** The Fourier estimate also controls the bias of an integer Gaussian's parity.

**Source pointers.** [Peikert Section 2.3: Gaussian background](https://eprint.iacr.org/2015/939); [Gaussian smoothing](../science/gaussian_smoothing.md); [distribution conventions](../references/RELATED_WORK.md); [local bridge](PEIKERT_BRIDGE.md).

### M14 — Finite precision and discontinuous labels

**Central question.** Why is accurate real-number approximation insufficient unless boundary crossings are controlled?

**Understanding target.** Explain how floor and quantization can change abruptly, why raw discrete samples cannot be close in total variation to a continuous distribution, and how coupling plus anti-concentration controls the resulting finite outputs.

**Dependencies and story role.** M07–M08, M12. Makes the computational interface finite and explicit.

**Conceptual connection.** The proof must control changes in syndrome bits and logical bits, rather than assert impossible closeness of raw discrete and continuous samples.

**Source pointers.** [Finite precision](../science/finite_precision.md); [boundary regressions](../verification/README.md); [local bridge](PEIKERT_BRIDGE.md).

### M15 — The shared framework

**Central question.** What must be matched for a geometric recovery theorem and a cryptographic hardness theorem to describe one physical task?

**Understanding target.** Assemble the public ensemble, noise law, logical target, syndrome precision and charged decoder model into one statement; identify a mismatch in any of those ingredients as a substantive problem.

**Dependencies and story role.** M01–M14. Completes the background phase by joining its physical, geometric and computational components.

**Conceptual connection.** The narrative phase must prove both sides without changing the problem between them.

**Source pointers.** [Scientific map](../science/index.md); [model](../science/model.md); [local bridge](PEIKERT_BRIDGE.md).

## Phase II — Narrative and contribution

### M16 — Pairing a lattice with its dual

**Central question.** Why does $`L\oplus L^*`$ provide the required symplectic structure?

**Understanding target.** Explain symplectic self-duality of the paired lattice and the consequences of scaling it by $`\sqrt2`$ for stabilizers and logical displacements.

**Dependencies and story role.** M03–M05, M15. Starts the construction from a single structural choice.

**Conceptual connection.** Euclidean primal/dual pairing supplies the quantum commutation relations while preserving a route back to an ordinary random linear code.

**Source pointers.** [Model](../science/model.md); [exact symplectic checks](../verification/README.md); [local bridge](PEIKERT_BRIDGE.md).

### M17 — Logical rate and distance

**Central question.** How do covolume and shortest vectors determine the code's logical dimensions and correction scale?

**Understanding target.** Explain why the code encodes $`m`$ qubits, why its frame has $`2m`$ bits, and why a shortest nonzero vector of $`K`$ cannot be a stabilizer in $`2K`$.

**Dependencies and story role.** M06, M16. Converts the construction into operational geometric quantities.

**Conceptual connection.** The number of logical labels and the shortest harmful displacement are different properties of the same quotient.

**Source pointers.** [Model](../science/model.md); [geometry G3](../science/geometry.md); [local bridge](PEIKERT_BRIDGE.md).

### M18 — A public basis without changing the ensemble

**Central question.** How can a useful systematic basis be found while keeping the original public matrix distribution?

**Understanding target.** Explain pivot-row selection, column-basis change, restoration of original physical coordinates, and the polynomial bounds on the basis and its inverse.

**Dependencies and story role.** M04, M07, M16. Makes the construction usable by a finite algorithm.

**Conceptual connection.** Conditioning a predetermined square block to be invertible would alter the distribution; selecting pivots avoids that unnecessary change.

**Source pointers.** [Peikert Section 2.2: bases and coordinates](https://eprint.iacr.org/2015/939); [Canonical basis in the model](../science/model.md); [finite precision](../science/finite_precision.md); [local bridge](PEIKERT_BRIDGE.md).

### M19 — Simultaneous primal and dual geometry

**Central question.** Why are both $`L`$ and $`L^*`$ unlikely to contain a short nonzero vector?

**Understanding target.** Follow the random-subspace membership count, integer-ball volume bound and union bound. Explain why primal/dual independence is unnecessary.

**Dependencies and story role.** M04, M16–M17. Establishes the code's geometric quality for the exact public ensemble.

**Conceptual connection.** A balanced finite-field subspace and its complement have identical marginals, allowing one argument to control both displacement sectors.

**Source pointers.** [Peikert Section 2.2: primal and dual lattice background](https://eprint.iacr.org/2015/939); [Geometry G1–G3](../science/geometry.md); [local bridge](PEIKERT_BRIDGE.md).

### M20 — The unrestricted Gaussian decoder

**Central question.** What condition guarantees correct logical recovery from a Gaussian shift?

**Understanding target.** Compare the noise norm with half the minimum lattice distance, interpret the Gaussian tail bound, and explain why logarithmic syndrome precision preserves the success margin.

**Dependencies and story role.** M08–M09, M14, M19. Completes the information-theoretic side of the separation.

**Conceptual connection.** Quantization changes the representative by a small physical vector; the geometric margin absorbs that perturbation.

**Source pointers.** [Peikert Section 2.3: Gaussian background](https://eprint.iacr.org/2015/939); [Geometry G4–G5](../science/geometry.md); [local bridge](PEIKERT_BRIDGE.md).

### M21 — Odd modulus and logical parity

**Central question.** Why does a logical lattice class determine every ambient coordinate parity?

**Understanding target.** Explain the odd-index identity $`\Lambda_C\cap2\mathbb Z^m=2\Lambda_C`$ and the isomorphism between the logical quotient and binary parity labels.

**Dependencies and story role.** M04, M06, M17. Introduces the local mechanism that respects logical degeneracy.

**Conceptual connection.** The reduction can learn a hidden binary mask without demanding reconstruction of the whole lattice point.

**Source pointers.** [Parity lemma in hardness](../science/hardness.md); [exact masking checks](../verification/README.md); [local bridge](PEIKERT_BRIDGE.md).

### M22 — The masked LWE challenge

**Central question.** What changes between the real and uniform branches of $`y=(2b+u)\bmod q`$?

**Understanding target.** Explain why the real branch equals a lattice vector plus structured noise, while the uniform branch is independent of the mask. Identify the parity a successful logical decoder would reveal.

**Dependencies and story role.** M10–M12, M21. Turns the local parity fact into a computational reduction.

**Conceptual connection.** Multiplication by two is invertible modulo odd $`q`$, but parity still records the hidden mask after an even LWE error is subtracted.

**Source pointers.** [One-call reduction](../science/hardness.md); [verification](../verification/README.md); [local bridge](PEIKERT_BRIDGE.md).

### M23 — From cryptographic error to Gaussian displacement

**Central question.** How do masking and continuous dither produce the required physical noise law?

**Understanding target.** Explain the two completed-square identities, the purpose of widths $`R=R_2=\log n`$, the negligible statistical error, and the separate bound on mask parity bias.

**Dependencies and story role.** M12–M13, M22. Matches the reduction to independent continuous Gaussian physical noise.

**Conceptual connection.** The discrete mask makes its parity hidden, and the continuous dither removes the residual discrete support; both roles need explicit estimates.

**Source pointers.** [Peikert Section 2.3: Gaussian background](https://eprint.iacr.org/2015/939); [Gaussian smoothing](../science/gaussian_smoothing.md); [theta verification](../verification/README.md); [local bridge](PEIKERT_BRIDGE.md).

### M24 — Hiding the position frame

**Central question.** Why does the reduction imply pseudorandomness of an entire logical sector rather than only small block-decoding success?

**Understanding target.** Follow the computation of the true position label from known challenge data and the two hybrids that restore the same syndrome marginal while replacing that label by uniform bits.

**Dependencies and story role.** M11–M12, M18, M21–M23. Establishes the first full logical-sector statement.

**Conceptual connection.** The other sector can be retained as side information because the reduction samples it itself.

**Source pointers.** [Position-sector hybrids](../science/hardness.md); [local bridge](PEIKERT_BRIDGE.md).

### M25 — Dual symmetry and the complete frame

**Central question.** How is the momentum sector reduced to ordinary LWE without assuming a new structured cryptographic problem?

**Understanding target.** Explain orthogonal complementation of the challenge code, uniform randomization of its generator basis, the integer dual basis $`G=qH^{-T}`$, and composition of the two sector hybrids.

**Dependencies and story role.** M16, M18–M19, M24. Extends the local mechanism to the complete logical correction.

**Conceptual connection.** The balanced ensemble gives exactly the same public-matrix law after dualization, including the basis coordinates used by the decoder.

**Source pointers.** [Peikert Section 2.2: Euclidean duality background](https://eprint.iacr.org/2015/939); [Full-frame theorem](../science/hardness.md); [dual-ensemble checks](../verification/README.md); [local bridge](PEIKERT_BRIDGE.md).

### M26 — Implementing the reduction with finite strings

**Central question.** How are the continuous construction and exact floor labels represented by a polynomial-resource reduction?

**Understanding target.** Explain Gaussian truncation, fine-grid sampling, arithmetic error, bounded periodized marginal densities and the union bound over quantization boundaries.

**Dependencies and story role.** M14, M18, M23–M25. Closes the computational-access part of the proof.

**Conceptual connection.** Negligible error is asserted for the resulting finite syndrome and labels, where the boundary estimate applies.

**Source pointers.** [Finite precision](../science/finite_precision.md); [boundary checks](../verification/README.md); [local bridge](PEIKERT_BRIDGE.md).

### M27 — What full-frame pseudorandomness rules out

**Central question.** What can be concluded about partial predictions, candidate lists and postselection?

**Understanding target.** Derive the meaning of random-guess baselines for a nonzero parity or complete frame, understand the polynomial-list bound, and keep unconditional success distinct from postselected conditional success.

**Dependencies and story role.** M11–M12, M25–M26. Converts indistinguishability into operational consequences.

**Conceptual connection.** Efficient public relabeling does not remove pseudorandomness; changing the label convention is not a decoding shortcut.

**Source pointers.** [Hardness consequences](../science/hardness.md); [reference-frame interpretation](../science/interpretation.md); [local bridge](PEIKERT_BRIDGE.md).

### M28 — Vanishing noise with matched LWE parameters

**Central question.** Why can the physical noise shrink while both halves of the separation remain valid?

**Understanding target.** Explain the schedules $`\sigma_n=n^{-a}`$ and $`r_n=\Theta(n^{1-a})`$, the restriction $`0<a<1/2`$, and the distinction between the geometric condition and the computational assumption for each schedule.

**Dependencies and story role.** M20, M23, M25–M26. Establishes the central scaling regime of the project.

**Conceptual connection.** Noise becomes small relative to the correction radius while the corresponding LWE width remains in the stated hardness regime.

**Source pointers.** [Peikert Section 4.2.2: LWE hardness background](https://eprint.iacr.org/2015/939); [Model](../science/model.md); [geometry G4](../science/geometry.md); [hardness](../science/hardness.md); [local bridge](PEIKERT_BRIDGE.md).

### M29 — Physical scope and scientific attribution

**Central question.** Which stronger physical or originality claims do the established theorems actually support?

**Understanding target.** Distinguish ideal logical decoding from finite-energy arbitrary recovery, matched assumptions from unconditional hardness, and the present contribution from prior cryptographic GKP constructions and stabilizer-decoding barriers.

**Dependencies and story role.** M15, M20, M25–M28. Places the result within its physical and scholarly setting.

**Conceptual connection.** A precise bounded result gains meaning from explicit resource and literature comparisons; a possible extension does not count as a proved theorem.

**Source pointers.** [Interpretation](../science/interpretation.md); [related work](../references/RELATED_WORK.md); [local bridge](PEIKERT_BRIDGE.md).

### M30 — The complete separation

**Central question.** How do geometry, parity, smoothing, duality and finite precision jointly establish the result?

**Understanding target.** Explain the full chain from one public ensemble and one noise law to reliable unrestricted recovery and pseudorandom efficient logical corrections. Identify where each assumption enters and which conclusion would change if it were removed.

**Dependencies and story role.** M16–M29. Completes the narrative by assembling the argument and its limits.

**Conceptual connection.** Geometric protection and computational accessibility are separate properties of the same encoded system; the proof exhibits that separation without changing the decoder's task between the two comparisons.

**Source pointers.** [Scientific map](../science/index.md); [hardness](../science/hardness.md); [geometry](../science/geometry.md); [interpretation](../science/interpretation.md); [local bridge](PEIKERT_BRIDGE.md).

## Dependency structure

The background phase first develops the oscillator and lattice objects, then the computational and distributional tools, and finishes by matching their interfaces. The narrative has two initially separate branches: M16–M20 establish geometry, while M21–M27 establish logical pseudorandomness using the same construction. M28 joins them in the vanishing-noise regime; M29–M30 supply attribution, scope and synthesis.

The map does not replace every technical lemma or cover every neighboring subject. Detailed proofs remain in the canonical scientific pages, and [finite verification](../verification/README.md) has its own explicitly bounded role.
