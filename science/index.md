# Scientific map

This project proves a conditional separation between geometric recoverability and efficient logical decoding for an ensemble of ideal oscillator codes. The same public construction supports both sides of the comparison.

The reference regime has $`m=2n`$ oscillator modes, one encoded qubit per mode, an odd prime modulus $`q=\Theta(n^2)`$, and independent Gaussian displacement width $`\sigma_n=n^{-1/4}`$. With an appropriate logarithmic number of syndrome bits per coordinate, an unrestricted geometric decoder succeeds with probability $`1-\exp[-\Omega(n)]`$. Under the specified discrete-Gaussian quantum-LWE assumption, every uniform polynomial-time syndrome decoder has negligible success in recovering the complete logical frame.

The computational statement is stronger: the full $`2m`$-bit frame is computationally indistinguishable from independent uniform bits given the public code and the syndrome. The result includes quantum computation of a classical answer and charged polynomial preprocessing.

## Reading routes

| Aim | Route |
|---|---|
| Understand the physical claim and its limits | [Interpretation](interpretation.md), then [model](model.md) |
| Check the exact construction and assumption | [Model](model.md), then [hardness](hardness.md) |
| Verify recoverability for the same ensemble | [Geometry](geometry.md), especially G2–G5 |
| Check the distribution transfer | [Gaussian smoothing](gaussian_smoothing.md) |
| Audit the reduction and full-frame hybrids | [Hardness](hardness.md), with the smoothing and precision lemmas |
| Check that no real-number oracle is supplied | [Finite precision](finite_precision.md), then geometry G5 |
| Assess the relation to previous results | [Related work](../references/RELATED_WORK.md) |
| Reproduce finite algebra and numerical checks | [Verification](../verification/README.md) |
| Build the prerequisites systematically | [Thirty milestones](../learning/MILESTONES.md) |

## Proof structure

The [model](model.md) fixes the public code ensemble, the original-coordinate basis, the logical quotient and the computational assumption. Every theorem uses those conventions.

The [geometric argument](geometry.md) counts short vectors in the random primal lattice and its dual. It yields a growing correction radius and a successful unrestricted decoder, including a finite-precision version. It does not establish an efficient decoding algorithm.

The [smoothing argument](gaussian_smoothing.md) converts a masked discrete-Gaussian LWE error into independent continuous Gaussian displacement with negligible statistical error. It also makes the hidden mask parities nearly uniform.

The [hardness proof](hardness.md) uses odd-index parity to extract a hidden mask from a successful logical correction. A dual-ensemble construction applies the same mechanism to momentum, and the sector hybrids hide the full frame. The [precision argument](finite_precision.md) implements the reduction using finite samples and arithmetic, controlling discontinuities at syndrome and frame boundaries.

Finally, the [interpretation](interpretation.md) combines the two conclusions, states the charged resources and distinguishes this ideal logical-decoding task from finite-energy physical recovery.

## Main distinctions to preserve

- A logical class modulo the stabilizer is less information than a full closest lattice point. The parity reduction explicitly handles this degeneracy.
- Statistical closeness of distributions and computational indistinguishability are different tools. Smoothing supplies the first; the LWE assumption supplies the second.
- Geometric success is an existence result for an unrestricted decoder. It does not contradict the computational lower bound.
- The frame theorem is average-case over the code ensemble and Gaussian error. It is not a claim about every fixed code or every bosonic code family.
- A finite syndrome string removes unlimited numerical precision from the algorithm. It does not make an ideal GKP state normalizable or establish an arbitrary coherent-recovery theorem.

Each proof and definition has one authoritative home in the pages above. The [bibliography](../references/references.bib) records source identities; the verification suite checks finite instances without replacing the analytical arguments.
