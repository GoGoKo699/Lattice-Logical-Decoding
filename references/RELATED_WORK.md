# Prior work, assumptions, and attribution

Literature checked through **23 October 2026**. Section and theorem numbers below refer to the explicitly identified manuscripts. Publication metadata and stable identifiers are collected in [references.bib](references.bib).

The [model](../science/model.md), [geometry](../science/geometry.md), and [hardness argument](../science/hardness.md) should be read together. The result concerns a public ensemble of ideal multimode GKP codes, independent continuous Gaussian displacements, a finite classical syndrome, and a controller that outputs a classical logical Pauli frame. The controller may use quantum computation.

## 1. What this project adds to an established connection

GKP codes encode finite-dimensional quantum information using displacement stabilizers of an oscillator; this originates with [Gottesman, Kitaev, and Preskill (2001)](https://arxiv.org/abs/quant-ph/0008040v3). Connections between good GKP lattices, computationally difficult lattice problems, and cryptographic constructions are also established. Conditional average-case difficulty of quantum logical decoding already has an LPN-based formulation, discussed below.

The contribution developed here is the conjunction of a more specific set of properties:

- The source assumption is ordinary, rectangular, decisional LWE with a uniform secret and an explicitly specified integer Gaussian error law.
- The physical displacement law is an independent, isotropic **continuous Gaussian** in the original phase-space coordinates.
- Its width can decrease polynomially, including $`\sigma_n=n^{-1/4}`$ in dimensionless Weyl coordinates.
- The conclusion concerns the **entire logical Pauli frame**, conditioned on the public matrix and any polynomial-bit syndrome precision.
- The same ensemble has a geometric decoding guarantee for a computationally unrestricted decoder.

These are claims about this repository's reduction and parameter regime, not an assertion that cryptography first creates a gap between geometric correctability and efficient quantum decoding here. The exact probability spaces, quantifiers, and computational assumptions are fixed in [model.md](../science/model.md); their physical interpretation is in [interpretation.md](../science/interpretation.md).

## 2. The closest prior results

### Cryptographic GKP codes: Conrad, Eisert, and Seifert

[Good Gottesman–Kitaev–Preskill codes from the NTRU cryptosystem](https://arxiv.org/html/2303.02432v4), Quantum **8**, 1398 (2024), is the closest GKP antecedent. It constructs NTRU-related code families, studies distance and decoding, and proposes quantum public-key communication.

The relevant distinctions are explicit in that paper. Section 3.1, Lemma 1 concerns an oracle evaluating logical-coset weights; the discussion after Eq. (25) says it has not proved hardness of returning the maximizing logical coset. Section 5.1 compares decoding radii obtained from public and secret bases using Babai's method; an algorithm comparison alone is not an all-algorithm lower bound. Section 5.2 uses a displacement distribution inherited from NTRU messages and randomizers, and makes an additional premise connecting recovery of logical content to finding a small syndrome-compatible error. Sections 5.2 and 6 leave quantum security and finite squeezing for further work.

Our reduction directly addresses the logical quotient under ordinary LWE and independent Gaussian displacement noise. It does not prove security of their communication protocol.

### Good randomized symplectic lattices: Blömer, Xiao, Raissi, and Soltan

[Symplectic Lattices and GKP Codes — Simple Randomized Constructions from Cryptographic Lattices](https://arxiv.org/html/2509.10183v2), arXiv:2509.10183v2 (23 March 2026), develops SIS, ring-SIS, and module-SIS based symplectic constructions with distance proportional to the square root of the number of modes. Sections 6–7 and 12–13 discuss decoding algorithms and numerical performance.

This is strong prior art for constructive good GKP lattices. Its geometric results and decoder analysis do not supply the ordinary-LWE, full-logical-frame pseudorandomness statement studied here. Distance growth and the use of cryptographic lattice constructions should therefore not be presented as this project's independent novelty.

### Average-case quantum decoding hardness: Khesin et al.

[Average-Case Complexity of Quantum Stabilizer Decoding](https://arxiv.org/html/2509.20697v1), published at STOC 2026, is the strongest conceptual antecedent. Theorem 6.6 of the September 2025 manuscript reduces LPN to the classical representation of Search LSN. Specifically, for $`p=\Omega(n^{-(1-\epsilon)})`$, fixed $`0<\epsilon<1`$, success $`2^{-k}+1/\mathrm{poly}(n)`$ at recovering the hidden $`k`$-bit logical string yields a distinguisher for

```math
\mathrm{LPN}\!\left(\left\lfloor\frac{np}{6}\right\rfloor,\,2n,\,\frac p6\right).
```

Their Sections 3–4 analyze degeneracy and the relation between classical and quantum input representations. The $`2^{-k}`$ baseline belongs to their hidden-string task; it should not be silently relabeled as guessing a full $`2k`$-bit Pauli frame.

Thus a generic LPN-based obstruction to efficient quantum logical decoding is already known. Our proposed distinction is a direct ordinary-LWE result for a GKP ensemble with a polynomially vanishing independent Gaussian noise width, and pseudorandomness of its complete Pauli frame given its digital syndrome.

### Cryptography built from stabilizer decoding: Lu et al.

[Post-Quantum Cryptography from Quantum Stabilizer Decoding](https://arxiv.org/html/2603.19110v2), arXiv:2603.19110v2 (6 October 2026), constructs public-key encryption, oblivious transfer, and one-way functions from stabilizer-decoding assumptions. Its reduction direction is therefore different: it develops cryptographic primitives from decoding assumptions, while this repository derives a particular GKP decoding obstruction from ordinary LWE.

The paper's LSN and state-LSN assumptions, and their parameter regimes, must be distinguished from the particular LPN hardness theorem above. We do not claim that all stabilizer-decoding assumptions used there follow from ordinary LWE or from Theorem 6.6 of Khesin et al.

## 3. Why the logical quotient matters

[Conrad, Eisert, and Arzani (2022), Section 6, Eqs. (98)–(101)](https://arxiv.org/html/2109.14645v3) give the lattice formulation of GKP decoding. In our notation, let $`\Gamma`$ be the stabilizer lattice and $`K=\Gamma^\times`$ its symplectic dual. A syndrome fixes an error modulo $`K`$. After choosing a representative $`\eta`$, the unresolved logical class lies in $`K/\Gamma`$.

For Gaussian noise, the probability of a logical class represented by $`\ell\in K`$ is proportional to

```math
\sum_{\gamma\in\Gamma}
\exp\!\left[-\frac{\|\eta+\ell+\gamma\|^2}{2\sigma^2}\right].
```

The sum includes all stabilizer-equivalent errors. Selecting the most likely individual lattice point and selecting the most likely stabilizer coset are therefore different optimization problems. A hardness reduction for full closest-point recovery does not, by itself, establish hardness of identifying the logical class.

Here the task is to output the true class of the sampled error, expressed as the canonical frame $`Z\in\mathbb F_2^{2m}`$. Any syndrome-based decision rule for that task is covered, including a rule that maximizes the posterior coset probability. The reduction does not require reconstructing the full nearest point or evaluating an infinite Gaussian sum. At finite precision, the theorem concerns the logical label; it does not identify quantized analogue feedforward with perfect physical recovery. See [the syndrome definition](../science/model.md#4-a-digital-syndrome-and-its-true-logical-frame).

## 4. The exact LWE distribution

This repository uses the pointwise integer Gaussian

```math
D_{\mathbb Z,r}(k)=
\frac{\exp[-k^2/(2r^2)]}
{\sum_{j\in\mathbb Z}\exp[-j^2/(2r^2)]}.
```

Here $`r`$ is an exponential width parameter, not the exact standard deviation. In the common cryptographic convention $`\rho_s(x)=\exp(-\pi x^2/s^2)`$, the same distribution has parameter

```math
s=\sqrt{2\pi}\,r.
```

It is not the distribution obtained by rounding a continuous $`N(0,r^2)`$ sample to the nearest integer: that rounded distribution assigns each integer the integral of the Gaussian density over a unit interval. Neither distribution is identified with the other without a reduction or an error estimate. Integer-Gaussian LWE is a standard formulation; see [Lindner and Peikert, Section 2.2](https://eprint.iacr.org/2010/613).

### Relation to the foundational LWE hardness results

[Regev's journal version](https://cims.nyu.edu/~regev/papers/qcrypto.pdf), Theorem 1.1 and Section 4, supplies the foundational worst-case-to-average-case and search/decision results. Its stated rounded-Gaussian convention must be tracked when applying it. The familiar condition $`\alpha q>2\sqrt n`$ does not itself identify every Gaussian variant.

An explicit bridge is in [Gordon, Katz, and Vaikuntanathan, full version, Section 2.2, Lemmas 1–2](https://www.cs.umd.edu/~jkatz/papers/latticeGroupSigs.pdf). Using the $`\rho_s`$ convention, Lemma 2 maps continuous-error LWE of width $`\alpha q`$ to point-discrete-Gaussian LWE of width $`\sqrt2\,\alpha q`$, with negligible statistical loss when $`\alpha q=\omega(\sqrt{\log n})`$. The uniform branch is exactly preserved, as are the matrix, secret, and number of samples. Lemma 1 records the Gaussian convolution statement used in that proof. These numbers refer to the author-hosted full version, rather than the shorter conference layout.

For our parameters, matching the target width requires

```math
\sqrt2\,\alpha q=\sqrt{2\pi}\,r,
\qquad\text{hence}\qquad
\alpha q=\sqrt\pi\,r.
```

With $`q=\Theta(n^2)`$ and $`\sigma_n=n^{-a}`$, $`0<a<1/2`$, the chosen

```math
r^2=\frac{2q\sigma_n^2-2(\log n)^2}{4}
```

satisfies $`r=\Theta(n^{1-a})\gg\sqrt n`$. Consequently both the smoothing requirement and the usual width condition are met asymptotically. This calculation explains compatibility with the established lattice-hardness regime. The theorem nevertheless states its exact decisional LWE assumption explicitly, for quantum polynomial-time distinguishers receiving classical samples. It does not assert unconditional LWE hardness, security of any standardized cryptosystem, or a transfer of hardness to arbitrary smaller noise widths.

[Peikert's survey](https://eprint.iacr.org/2015/939), Sections 2.2–2.3 and 4.2, provides a unified account of the lattice, Gaussian, and LWE terminology used here.

[Peikert's Gaussian-sampling paper](https://eprint.iacr.org/2010/088), CRYPTO 2010, is the convolution and sampling antecedent cited by Gordon, Katz, and Vaikuntanathan and by our [Gaussian-smoothing calculation](../science/gaussian_smoothing.md). Its author manuscript was last revised on 14 April 2011; the publication year remains 2010.

## 5. Physical scope and interpretation

The displacement variance is specified in dimensionless Weyl coordinates: with $`[\hat Q,\hat P]=i`$, a coordinate vector $`x`$ denotes a physical displacement $`\sqrt{2\pi}\,x`$. Thus the physical quadrature variance is $`2\pi\sigma_n^2`$. This is a choice of units, not an additional squeezing or state-preparation guarantee.

The computational claim permits polynomial-time quantum processing and public-matrix preprocessing, but its input and output are classical. It supplies neither coherent LWE samples nor a QRAM oracle. It is averaged over the public ensemble and noise, and is not a claim that every fixed code is hard.

Finite-energy encoding, noisy syndrome extraction, and arbitrary coherent recovery channels require additional arguments. These are substantive distinctions in bosonic error correction: [Terhal, Conrad, and Vuillot's review, Sections 2.3–2.4 and Appendix B](https://arxiv.org/html/2002.11008v3), treats approximate GKP states and repeated correction with finite squeezing. This repository does not promote its ideal frame-decoding theorem to such a theorem. Likewise, computational pseudorandomness of a classical logical label is not, without a separate quantum-state security reduction, a private quantum channel.

## 6. Version and citation ledger

| BibTeX key | Source used for statements or pedagogy | Publication / checked manuscript |
|---|---|---|
| GKP2001 | [Encoding a qubit in an oscillator](https://arxiv.org/abs/quant-ph/0008040v3) | Phys. Rev. A 64, 012310 (2001); arXiv v3, 13 May 2001 |
| ConradEisertArzani2022 | [GKP codes: A lattice perspective](https://arxiv.org/html/2109.14645v3) | Quantum 6, 648 (2022); arXiv v3, 8 February 2022 |
| ConradEisertSeifert2024 | [Good GKP codes from NTRU](https://arxiv.org/html/2303.02432v4) | Quantum 8, 1398 (2024); arXiv v4, 1 July 2024 |
| BloemerEtAl2025 | [Symplectic lattices and GKP codes](https://arxiv.org/html/2509.10183v2) | First posted 2025; checked v2, 23 March 2026 |
| KhesinEtAl2026 | [Average-case stabilizer decoding](https://arxiv.org/html/2509.20697v1) | STOC 2026; theorem numbering from arXiv v1, 25 September 2025 |
| LuEtAl2026 | [Cryptography from stabilizer decoding](https://arxiv.org/html/2603.19110v2) | arXiv v2, 6 October 2026 |
| Regev2009 | [LWE foundation](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) | J. ACM 56(6), Article 34 (2009); author manuscript dated 2 May 2009 |
| Peikert2010Gaussian | [Gaussian sampler](https://eprint.iacr.org/2010/088) | CRYPTO 2010, LNCS 6223, 80–97; ePrint revision 14 April 2011 |
| GordonKatzVaikuntanathan2010 | [Discrete-Gaussian conversion](https://www.cs.umd.edu/~jkatz/papers/latticeGroupSigs.pdf) | ASIACRYPT 2010; Lemmas 1–2 checked in the author-hosted full version |
| LindnerPeikert2011 | [LWE parameters and conventions](https://eprint.iacr.org/2010/613) | CT-RSA 2011; ePrint 2010/613, posted 30 November 2010 |
| Peikert2016 | [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939) | Foundations and Trends in Theoretical Computer Science 10(4), 283–424 (2016); manuscript dated 17 February 2016, ePrint revision 18 February 2016 |
| TerhalConradVuillot2020 | [Bosonic error-correction review](https://arxiv.org/html/2002.11008v3) | Quantum Science and Technology 5(4), 043001 (2020); arXiv v3, 1 June 2020 |
| Girvin2023 | [Introduction to Quantum Error Correction and Fault Tolerance](https://arxiv.org/html/2111.08894v4) | SciPost Physics Lecture Notes 70 (2023); arXiv v4, 6 January 2023 |

The bibliography records primary publications and author manuscripts; the comparisons above do not rely on secondary summaries.

## 7. Selected educational anchor

The selected anchor is **Chris Peikert, A Decade of Lattice Cryptography**, Foundations and Trends in Theoretical Computer Science **10**(4), 283–424 (2016), DOI [10.1561/0400000074](https://doi.org/10.1561/0400000074). The [publisher record](https://www.emerald.com/fttcs/article/10/4/283/1331264/A-Decade-of-Lattice-Cryptography) verifies the journal citation. The [author manuscript](https://eprint.iacr.org/2015/939.pdf) is dated **17 February 2016**; the [IACR record](https://eprint.iacr.org/2015/939) dates its revision to **18 February 2016**. Section pointers refer to that manuscript.

The reading route uses Section 2.2 for lattices and duality, Section 2.3 for Gaussian conventions, and Sections 4.2.1–4.2.2 for LWE definitions and hardness. The [local bridge](../learning/PEIKERT_BRIDGE.md) translates those conventions into the repository's notation; the [thirty milestones](../learning/MILESTONES.md) retain the full physical and mathematical narrative. GKP stabilizers, the logical quotient, finite syndrome precision, and this project's reduction are developed locally, rather than attributed to the survey.
