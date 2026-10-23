# Physical meaning and scope of the decoding separation

The [geometric theorem](geometry.md) and [computational theorem](hardness.md) address the same random public code and the same independent Gaussian displacement model. Together they separate the existence of a reliable logical correction from the computational ability to identify it.

## The central comparison

The code encodes $m=2n$ logical qubits in $m$ ideal oscillator modes. Its stabilizer lattice is built from a random balanced $q$-ary lattice and its Euclidean dual. At displacement width $\sigma_n=n^{-1/4}$, typical errors have norm $\Theta(n^{1/4})$, while a ball of radius $\Omega(n^{1/2})$ is geometrically correctable with overwhelming probability over the code.

An unrestricted nearest-point decoder can find the correct logical frame with probability $1-\exp[-\Omega(n)]$. Under the precise quantum-LWE assumption in [the model](model.md), every uniform polynomial-time decoder receiving the public code and finite-precision classical syndrome has negligible exact logical-frame success. Quantum internal processing is included in that statement.

The noise is physically small relative to the code's guaranteed correction radius. Its independent width per coordinate also tends to zero. The obstruction is computational: solving the logical task efficiently would distinguish the specified LWE distribution from uniform.

These are asymptotic ensemble statements. They do not establish a useful finite-size threshold, a runtime exponent, or the performance of a practical oscillator memory.

## Why logical degeneracy matters

Correcting a quantum code does not require reconstructing the original lattice error exactly. Displacements differing by a stabilizer have the same action on the encoded information. A lower bound for finding a full nearest lattice point therefore does not automatically lower-bound the logical task.

Here the relevant quotient is $K/(2K)$. The odd modulus makes the ambient parity map on the underlying integer lattice invertible on its quotient by twice that lattice. A correct logical correction consequently reveals the random mask parity embedded in the LWE challenge. This is the step that connects the actual logical task to the cryptographic assumption.

The full-frame theorem is also stronger than a small probability of recovering all bits. Conditioned on the public code and syndrome, the whole $2m$-bit correction label is computationally indistinguishable from independent uniform bits. An efficiently selected nonzero linear parity consequently has negligible prediction advantage. A polynomial-size list and inverse-polynomial-probability postselection do not provide an efficient route around the result.

## The label is tied to a specified section

An ideal syndrome identifies the displacement modulo $K$. The canonical basis selects a representative in one fundamental parallelepiped; the remaining integer parity is the logical frame. This convention makes the task mathematically precise.

Any efficiently computable bijective relabeling of the frame, allowed to depend on the public code and syndrome, preserves its pseudorandomness. In particular, choosing another efficiently computable reference correction adds a known frame and cannot reveal the unknown frame. The conclusion therefore does not depend on calling one fixed frame label zero.

An unbounded rule for selecting a reference correction could itself solve decoding. Such a rule would insert the missing computation into the interface and is not an efficient change of convention.

## Information supplied to the controller

The decoder receives a classical public matrix and a finite string representing the syndrome. It may perform classical or quantum polynomial-time computation and polynomial-time preprocessing from that public matrix. All such resources are counted. The proof uses ordinary classical LWE samples; it requires neither QRAM nor coherent access to a sample oracle.

The theorem does not allow an arbitrary free secret trapdoor or an exponentially expensive precomputed table specific to the sampled code. Giving such additional resources changes the decoding problem. Advice independent of the public code can be included only if the LWE assumption is stated against the matching nonuniform adversary class.

The hardness result concerns average success over the code and physical noise. It does not assert that every fixed code is hard, that all GKP codes are difficult to decode, or that a particular heuristic must fail on every input.

## Ideal oscillators and digital precision

Ideal GKP code states are mathematical lattice states. They are not normalizable finite-energy laboratory states. The code's polynomial-size public description and polynomially conditioned basis do not by themselves establish a finite-energy encoding or recovery theorem.

[Finite precision](finite_precision.md) removes a different potential artifact: an algorithm is not given arbitrary real-number access. Both the lower bound and a successful unbounded geometric benchmark can be formulated with finitely many syndrome bits, and logarithmic precision suffices for the benchmark.

The logical task assumes the usual ideal syndrome section and the corresponding conceptual analog displacement. It does not quantify residual analog error from an implemented feedforward circuit. Finite squeezing, an energy envelope, photon loss, syndrome measurement noise and approximate recovery fidelity require additional physical estimates.

Likewise, a completely general coherent recovery channel need not output a classical logical label. The present reduction has not established a lower bound for every such channel acting on an unknown finite-energy encoded state. This boundary is part of the theorem's interpretation, not a defect hidden by the phrase "quantum decoder."

## Relation to post-quantum cryptography

The argument is conditional on quantum hardness of a specified ordinary LWE family. The error is a point-mass discrete Gaussian with an explicitly stated width; it must not be silently equated with a rounded continuous Gaussian or with the parameter distribution of a deployed cryptosystem.

For $q=\Theta(n^2)$ and $\sigma_n=n^{-a}$ with $0<a<1/2$, the required LWE error width is $r_n=\Theta(n^{1-a})$. Different physical-noise schedules invoke their corresponding LWE assumptions. This result does not show that hardness at one noise width automatically implies hardness at every smaller width.

No attack on an existing cryptographic deployment follows. The direction of the reduction is that an efficient logical decoder for this public ensemble would contradict the stated LWE assumption.

## Contribution relative to existing work

Cryptographic constructions of GKP codes, geometric distance guarantees for symplectic lattices, and information/computation separations for quantum stabilizer decoding all have prior literature. The [related-work account](../references/RELATED_WORK.md) identifies those inputs and their exact scopes.

The contribution developed here is the direct reduction from ordinary LWE to the degenerate logical-frame task under independent continuous Gaussian shifts, with negligible distribution error, finite-precision classical input, full-frame pseudorandomness and a simultaneous geometric guarantee at vanishing physical noise.

This conjunction supports a precise physical conclusion: in the stated ideal model, the geometry can identify a region where recovery is possible while the appropriate logical operation remains computationally inaccessible to the specified efficient controller.

Return to [the scientific map](index.md) or follow [the learning milestones](../learning/MILESTONES.md).
