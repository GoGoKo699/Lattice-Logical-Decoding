# Reproducible finite verification

Run from the repository root with Python 3.10 or newer:

```sh
python3 verification/run_all.py
```

The suite uses only the Python standard library. It prints one JSON report and exits with a nonzero status if any check fails. All checks remain enabled under `python -O`. An optional output path saves the same report:

```sh
python3 verification/run_all.py --output /tmp/lattice-logical-decoding-verification.json
```

[`expected_results.json`](expected_results.json) records a successful run. Integer counts and seeds are deterministic. Small differences in the last floating-point digits are expected across platforms; numerical checks use explicit tolerances, rather than requiring byte-identical output.

## What is checked

| Check | Method and concrete risk addressed |
| --- | --- |
| Masked LWE target and parity | Exhaustively checks 48,000 cases at odd primes 3, 5, and 7. Verifies the target's lattice membership and exact mask-parity recovery, including modular wraparound. |
| Uniform challenge | For binary and signed integer masks, verifies that multiplication by two followed by masking is a permutation of the entire finite challenge space. |
| Dual public ensemble | In dimension one, enumerates all challenge generators and all basis randomizations; checks that the dual public generators are exactly uniformly distributed. This is a finite example of the ensemble symmetry, not its general proof. |
| Primal and dual bases | Checks 120 instances using exact integers and rational arithmetic, including covolumes, membership in the intended code lattices, and `H^T G = qI`. |
| Symplectic normalization | Checks `T^T J T = qJ` exactly. For `K=T/sqrt(2q)` and `Gamma=2K`, this gives pairings `J/2` and `2J`, respectively. The determinant identities give one encoded qubit per mode. |
| Original-coordinate dual frame | Forces nontrivial pivot-row permutations in at least half the basis cases. Checks both position and momentum reductions against the actual original-coordinate bases, including signed masks and the computed logical label. This catches using a systematic-coordinate dual basis without undoing the physical permutation. |
| Finite syndrome precision | Uses exact rational coordinates to check translation invariance of the quantized syndrome and the associated logical-frame shift. Compares 48-bit arithmetic rounding with an 8-bit syndrome when the exact point has a certified boundary margin. Also checks explicit grid and integer crossings, where a rounding guarantee must fail. |
| Gaussian smoothing | Checks direct versus Poisson theta sums, both completed-square identities, finite-sum discrete TV, numerical continuous TV, and the half-integer Poisson formula for mask parity. |

The exact algebra uses the fixed seed `20261023`. Deliberately forced pivot cases are algebraic edge cases, not a proposed random-code distribution or empirical hardness sample.

## Interpreting the numerical results

The error convention is

```math
D_{\mathbb Z,r}(k)\propto\exp[-k^2/(2r^2)].
```

The smoothing checks use `(r,R,R2)` equal to `(4,1,1)`, `(4,2,2)`, `(8,2,2)`, and `(8,3,3)`. They include weak enough smoothing to produce a visible nonzero error, as well as cases where the theoretical error falls below ordinary double-precision resolution.

Direct Gaussian sums use finite windows of 9 or 12 width parameters; continuous TV uses trapezoidal quadrature over a 9-width interval with 16,000 subintervals. The output also records the change on halving the quadrature resolution. These are numerical diagnostics, not interval-certified integrals or rigorous tail bounds. In the strongest-smoothing cases, an apparent numerical error near `1e-16` is a floating-point floor; it does not contradict a much smaller analytic theta bound. The checks include explicit small tolerances for that floor.

## What is not established by running the suite

The analytical arguments must establish the general quotient isomorphism, ensemble symmetry, Gaussian approximation, finite-precision boundary probability, and high-dimensional geometric success. A finite test cannot replace those proofs. In particular, exact boundary examples here test implementation logic; they do not establish the probability of approaching a boundary under a Gaussian distribution.

No result from this suite is evidence for LWE hardness, an asymptotic quantum decoding lower bound, or a physical finite-energy GKP implementation. The computational theorem remains conditional on its explicit discrete-Gaussian quantum-LWE assumption and concerns the stated classical-syndrome-to-classical-logical-frame interface.

## Documentation structure

A separate quick check validates local Markdown links and section anchors, the exact ordered milestone IDs `M01` through `M30`, the 15-background/15-narrative split, and their earlier-only dependency references. It reads the public `Dependencies and story role` fields and expands ranges such as `M03–M05`:

```sh
python3 verification/check_repository.py
```

This command checks structure only. It does not contact external websites, assess the scientific claims, or assume that any particular learning milestone has been completed.
