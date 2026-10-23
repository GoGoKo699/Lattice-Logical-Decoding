# Lattice Logical Decoding

**Geometrically recoverable oscillator codes can have computationally hidden logical corrections, even as physical noise vanishes.**

This repository develops a conditional separation for ideal Gottesman–Kitaev–Preskill (GKP) codes built from random lattices. The code's geometry permits reliable recovery from independent Gaussian displacements. Under an explicit quantum-hard Learning With Errors (LWE) assumption, every polynomial-time controller receiving the public code and a finite-precision classical syndrome has negligible probability of finding the complete logical correction.

The result concerns the logical equivalence class of the correction, accounting for stabilizer degeneracy. It permits quantum computation of that classical answer.

## Principal results

Let $`m=2n`$ be the number of oscillator modes and choose an odd prime $`q=\Theta(n^2)`$. A uniformly sampled full-rank matrix defines a balanced $`q`$-ary lattice $`L`$ and its dual. The stabilizer lattice is $`\sqrt2(L\oplus L^*)`$.

| Result | Statement | Authoritative account |
|---|---|---|
| Rate and geometry | One encoded qubit per ideal mode; logical distance at least of order $`\sqrt n`$ with exponentially high probability | [Model](science/model.md), [geometry](science/geometry.md) |
| Geometric recovery | At Gaussian width $`\sigma_n=n^{-1/4}`$, an unrestricted decoder succeeds with probability $`1-\exp[-\Omega(n)]`$ | [Geometry G4–G5](science/geometry.md) |
| Computational separation | Under the specified discrete-Gaussian quantum-LWE assumption, the entire logical frame is pseudorandom given the public code and finite syndrome | [Hardness theorem and proof](science/hardness.md) |
| Strong consequences | Exact decoding and polynomial-size lists succeed only negligibly; each efficiently selected nonzero frame parity is unpredictable beyond random guessing | [Hardness consequences](science/hardness.md) |
| Finite input | The reduction uses polynomially bounded finite precision; logarithmic precision already supports the geometric benchmark | [Finite precision](science/finite_precision.md), [geometry G5](science/geometry.md) |

In the reference regime, typical displacement norm is $`\Theta(n^{1/4})`$, while the guaranteed correction radius is $`\Omega(n^{1/2})`$. The computational obstruction therefore persists increasingly far inside the geometrically correctable region. All probability statements average over the stated public code ensemble and physical noise.

## Read the science

Start with [the physical interpretation](science/interpretation.md) for the question and its limits, or [the scientific map](science/index.md) for the complete proof route.

The analytical core has five parts:

1. [Model and exact assumptions](science/model.md): the code, displacement units, logical frame, and matched LWE distribution.
2. [Geometry](science/geometry.md): primal and dual distance, correction balls, and Gaussian recovery.
3. [Gaussian smoothing](science/gaussian_smoothing.md): negligible-error transfer to independent continuous displacement.
4. [Logical hardness](science/hardness.md): the hidden parity reduction, dual symmetry, and full-frame hybrids.
5. [Finite precision](science/finite_precision.md): finite sampling and arithmetic without a real-number oracle.

[Related work](references/RELATED_WORK.md) distinguishes existing cryptographic GKP constructions and quantum-decoding hardness results from this logical-frame reduction. Source metadata are collected in [the bibliography](references/references.bib).

## Learning route

The single educational anchor is **Chris Peikert, *A Decade of Lattice Cryptography* (2016)**, using the [author's revised survey](https://eprint.iacr.org/2015/939). The [Peikert bridge](learning/PEIKERT_BRIDGE.md) identifies the relevant sections, translates the matrix and Gaussian conventions, and develops the connection from noisy lattice equations to GKP logical corrections through worked examples.

[The thirty-milestone map](learning/MILESTONES.md) gives a common route through the project. Its **15 background/preliminaries milestones** connect oscillator errors, lattice geometry, and cryptographic indistinguishability. Its **15 narrative/innovation milestones** assemble the geometric benchmark, both logical-sector reductions, the finite-precision result, and their physical meaning. Each target has earlier dependencies and pointers to the anchor, bridge, and authoritative scientific account.

Use the bridge alongside the milestone map for self-directed study. [The LLM reading guide](llms.txt) maps questions to these explanations and the specialist proofs.

## Reproduce the finite checks

From the repository root, run:

```bash
python3 verification/run_all.py
```

The suite uses Python 3.10 or later and its standard library. It checks modular masking, exact primal/dual basis identities, logical labels in original physical coordinates, finite-precision boundaries, and Gaussian-theta formulas. See [verification instructions and expected output](verification/README.md).

Finite checks support the algebra and implementation. The asymptotic result rests on the analytical proofs and the explicit computational assumption; numerical checks do not establish LWE hardness.

## Scope

The theorem uses ideal GKP lattice codes and a classical syndrome-to-logical-frame interface. It includes efficient quantum processing and charged polynomial preprocessing, with no QRAM or coherent LWE sample oracle. It does not establish finite-energy state preparation, recovery under noisy syndrome measurements, or a lower bound for arbitrary coherent physical recovery. The ensemble average and exact LWE parameters remain part of the statement.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
