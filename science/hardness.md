# Pseudorandom logical frames from ordinary LWE

The logical task is a quotient problem: displacements differing by a stabilizer represent the same correction. A lower bound for finding a complete closest lattice vector does not by itself establish a lower bound for this quotient. The reduction below addresses the quotient directly. An integer Gaussian mask becomes a hidden logical parity vector, while two smoothing steps make the displacement law negligibly close to the required independent continuous Gaussian.

All public-code, basis, and input conventions are those in [the model](model.md). The statistical estimates are proved in [Gaussian smoothing](gaussian_smoothing.md); [finite precision](finite_precision.md) proves that the reduction is an ordinary polynomial-time computation on finite strings.

## 1. Statement and quantifiers

Let $`m=2n`$, let $`q=\Theta(n^2)`$ be an efficiently specified odd prime, and let $`A\in\mathbb F_q^{m\times n}`$ be uniform conditioned on full column rank. The associated basis is

```math
\mathcal B_A=\frac1{\sqrt{2q}}\mathrm{diag}(H_A,G_A),
\qquad G_A=qH_A^{-T}.
```

The basis matrices are the original-coordinate matrices defined in the model. In particular, reducing either modulo $`2`$ gives an invertible matrix. For an independent displacement $`\xi\sim N(0,\sigma_n^2I_{2m})`$, write

```math
a=\mathcal B_A^{-1}\xi,\quad
x=a-\lfloor a\rfloor,\quad
J=\lfloor2^b x\rfloor,\quad
Z=\lfloor a\rfloor\bmod2=(Z_Q,Z_P).
```

Here $`b=b(n)`$ is any nonnegative polynomially bounded, polynomial-time computable integer precision. The input syndrome has $`2mb`$ bits. The parameter $`b`$ and the public dimensions are implicit in every experiment.

Let $`R=\log n`$ and

```math
r_n^2=\frac{2q\sigma_n^2-2R^2}{4}.
```

The main schedule is $`\sigma_n=n^{-1/4}`$. The theorem also applies to $`\sigma_n=n^{-a}`$ for fixed $`0<a<1/2`$, and to fixed positive $`\sigma_n`$, under the corresponding explicit LWE assumption at width $`r_n`$. The parameters must have polynomial-time computable finite approximations. The Gaussian smoothing error $`\eta_n`$ and parity error $`\kappa_n`$ are those in Theorem S4 and are negligible.

**Theorem H1: full-frame pseudorandomness.** Assume quantum hardness of ordinary decisional LWE with uniform secret, $`m=2n`$ classical samples, modulus $`q`$, and independent errors $`D_{\mathbb Z,r_n}`$. Then the two classical distribution ensembles

```math
\mathsf{Real}_{n,b}=(A,J,Z)
\quad\text{and}\quad
\mathsf{Random}_{n,b}=(A,J,U_{2m})
\tag{H1}
```

are computationally indistinguishable by every uniform quantum polynomial-time algorithm. Here $`U_{2m}`$ is independent and uniform in $`\mathbb F_2^{2m}`$, and the marginal law of $`(A,J)`$ is identical in the two experiments.

The probability laws average over $`A`$, the physical noise, and all algorithmic randomness. Arbitrary polynomial-time preprocessing from $`A`$, including a retained polynomial-size quantum state, is allowed and counted in the total runtime. No arbitrary code-dependent auxiliary advice or trapdoor is supplied. The conclusion for a nonuniform adversary class requires the LWE assumption against that same class.

More quantitatively, for every efficient test $`T`$ of (H1), there are four efficient ordinary-LWE distinguishers $`D_1,\ldots,D_4`$ and a negligible implementation term $`\nu_n`$ such that

```math
\begin{aligned}
&\left|\Pr[T(\mathsf{Real}_{n,b})=1]
-\Pr[T(\mathsf{Random}_{n,b})=1]\right|\\
&\qquad\le
\sum_{i=1}^4\mathrm{Adv}_{\mathrm{LWE}}(D_i)
+4\eta_n+2\kappa_n+\nu_n.
\end{aligned}
\tag{H2}
```

The term $`\nu_n`$ includes the negligible rank-conditioning, bounded-sampling, and numerical errors. The assumption uses the point-mass integer Gaussian defined in the model, not an unstated rounding convention. Section 6 derives exact recovery, partial recovery, lists, postselection, and changes of logical labels from this theorem.

## 2. A syndrome-preserving masked LWE target

For this section, consider an ordinary LWE challenge $`(A,\mathbf b)`$ with $`A`$ full rank. In its LWE branch,

```math
\mathbf b=As+e\pmod q,
\qquad e\sim D_{\mathbb Z,r_n}^{\otimes m},
```

and in its uniform branch $`\mathbf b`$ is uniform in $`\mathbb F_q^m`$ independently of $`A`$. The secret $`s`$ is uniform in $`\mathbb F_q^n`$. Boldface distinguishes the challenge vector $`\mathbf b`$ from the syndrome precision $`b`$.

Sample independently

```math
u\sim D_{\mathbb Z,R}^{\otimes m},\qquad
g\sim N(0,R^2I_m),\qquad
p\sim N(0,\sigma_n^2I_m).
```

Using canonical representatives in $`\{0,\ldots,q-1\}`$, form

```math
y=(2\mathbf b+u)\bmod q,
\qquad
t=\left(\frac{y+g}{\sqrt{2q}},\ p\right).
\tag{H3}
```

Let $`k_t=\lfloor\mathcal B_A^{-1}t\rfloor`$, and compute the syndrome index of $`t`$ by the same torus quantizer used for $`\xi`$. A bar will denote reduction modulo $`2`$.

**Lemma H2: the computable position label.** In the LWE branch, define

```math
v_{\mathrm{int}}=y-(2e+u)\in\mathbb Z^m.
```

Then $`v_{\mathrm{int}}\in\Lambda_A`$ and

```math
t=\left(\frac{v_{\mathrm{int}}}{\sqrt{2q}},0\right)
+\Xi,
\qquad
\Xi=\left(\frac{2e+u+g}{\sqrt{2q}},p\right).
\tag{H4}
```

The shift before $`\Xi`$ belongs to $`K_A`$, so $`t`$ and $`\Xi`$ have exactly the same syndrome, at every precision. Moreover, the true frame of $`\Xi`$ is computable from the reduction's known data:

```math
\begin{aligned}
\widetilde Z_Q
&=\bar k_{t,Q}+\bar H_A^{-1}(\bar y+\bar u),\\
\widetilde Z_P
&=\bar k_{t,P}.
\end{aligned}
\tag{H5}
```

**Proof.** Modulo $`q`$,

```math
v_{\mathrm{int}}=y-(2e+u)=2As,
```

so the vector lies in $`\Lambda_A`$. Its $`K_A`$ coordinates are the integer vector

```math
k_v=(H_A^{-1}v_{\mathrm{int}},0).
```

Equation (H4) implies $`\mathcal B_A^{-1}t=k_v+\mathcal B_A^{-1}\Xi`$. Translation by an integer vector preserves the fractional part and shifts the floor by that vector. Hence $`Z(\Xi)=\bar k_t-\bar k_v`$. Since $`2e`$ is even,

```math
\bar k_{v,Q}=\bar H_A^{-1}(\bar y-\bar u)
=\bar H_A^{-1}(\bar y+\bar u).
```

Over $`\mathbb F_2`$, subtraction and addition coincide. This proves (H5). The reduction never needs to recover $`s`$, $`e`$, or the full lattice vector $`v_{\mathrm{int}}`$. $`\square`$

By Theorem S4, $`\Xi`$ is within $`\eta_n`$ in total variation of $`N(0,\sigma_n^2I_{2m})`$. Its law is independent of $`A`$. Therefore the LWE-generated joint law of the public code, syndrome, and labels in (H5) is within $`\eta_n`$ of the physical law, before the negligible finite-precision implementation error.

**Lemma H3: the uniform branch hides the position label.** In the uniform branch, $`y`$ is exactly uniform in $`\mathbb F_q^m`$ and independent of the entire integer vector $`u`$. Conditional on $`(A,y,g,p)`$, the law of $`\widetilde Z_Q`$ is within $`\kappa_n`$ of uniform. This remains true while retaining $`\widetilde Z_P`$ and the complete supplied syndrome.

**Proof.** Because $`q`$ is odd, multiplication by $`2`$ is invertible modulo $`q`$. For every fixed integer $`u`$, the map $`\mathbf b\mapsto(2\mathbf b+u)\bmod q`$ is a permutation of $`\mathbb F_q^m`$. Thus $`y`$ and $`u`$ are independent. Conditional on $`A,y,g,p`$, every part of (H5) except $`\bar u`$ is fixed, and $`\bar H_A^{-1}`$ is invertible. The position label is an affine bijection of $`\bar u`$. Lemma S3 gives distance at most $`\kappa_n`$ from uniform, uniformly under this conditioning. The momentum label and syndrome are functions of the conditioning variables. $`\square`$

The independence in Lemma H3 is exact before the negligible parity bias. It is not an entropy estimate for a compressed label, and it does not assume that a decoder finds the complete lattice displacement.

## 3. The first half of the hybrid: retain the true momentum frame

**Proposition H4.** Under the assumed LWE hardness,

```math
(A,J,Z_Q,Z_P)\ \approx_c\ (A,J,U_m,Z_P),
\tag{H6}
```

where $`U_m`$ is independent of all displayed physical variables.

**Proof.** Fix an efficient test for the two laws. Consider the following five transitions:

1. Replace the physical Gaussian experiment by the LWE branch of (H3)–(H5). The change is at most $`\eta_n`$ plus negligible numerical error.
2. Replace the LWE challenge value by a uniform value, retaining the computed labels. A distinguisher for this transition is an ordinary-LWE distinguisher: it performs the displayed sampling, computes the finite transcript, and runs the proposed test.
3. Replace $`\widetilde Z_Q`$ by an independent uniform $`U_m`$, while retaining the public code, supplied syndrome, and $`\widetilde Z_P`$. Lemma H3 bounds the change by $`\kappa_n`$.
4. Replace the uniform challenge value by an LWE value, now retaining the independent $`U_m`$ in place of the position label. This transition is bounded by a second ordinary-LWE advantage.
5. Return from the LWE-generated noise to the physical Gaussian law. The change is at most $`\eta_n`$ plus negligible numerical error. The retained momentum label has its true physical meaning, and the replacement position bits are independent.

The sum is at most the two LWE advantages plus $`2\eta_n+\kappa_n`$ and a negligible implementation term. The finite numerical simulator preserves the exact independence used in the middle transition, as proved in [finite precision](finite_precision.md). $`\square`$

Retaining the other sector is essential. A statement that each half is individually unpredictable would not by itself make the combined frame pseudorandom; correlations between the halves could remain visible.

## 4. The dual reduction: retain the true position frame

The public ensemble is closed under taking the dual code, but its public matrices also contain basis metadata. We account for that metadata explicitly.

Given an ordinary LWE challenge matrix $`A_0`$ of full rank, let $`C_0=\mathrm{im}A_0`$. Compute any fixed basis matrix $`N_0`$ for $`C_0^\perp`$ over $`\mathbb F_q`$, sample $`V`$ uniformly in $`\mathrm{GL}_n(\mathbb F_q)`$, and publish

```math
A=N_0V.
\tag{H7}
```

Since $`C_0`$ is a uniform $`n`$-dimensional subspace, its complement $`C_0^\perp`$ is a uniform $`n`$-dimensional subspace. Conditional on that subspace, multiplication by uniform $`V`$ selects a uniform ordered basis. Thus the resulting $`A`$ has exactly the public full-rank distribution in Theorem H1. The public matrix is not forced into systematic form. The basis computation in the model handles all row permutations in the original coordinates.

For this public $`A`$, the integer lattice with basis $`G_A`$ is

```math
\Lambda_{A,\perp}=\{v\in\mathbb Z^m:v\bmod q\in C_0\}.
```

Given the challenge value $`\mathbf b`$, use the same independent mask $`u`$, smoothing $`g`$, and Gaussian $`p`$, but put the challenge in the momentum sector:

```math
y=(2\mathbf b+u)\bmod q,
\qquad
t=\left(p,\frac{y+g}{\sqrt{2q}}\right).
\tag{H8}
```

The analogues of (H5) are

```math
\widetilde Z_Q=\bar k_{t,Q},\qquad
\widetilde Z_P=\bar k_{t,P}+\bar G_A^{-1}(\bar y+\bar u).
\tag{H9}
```

In the LWE branch, $`y-(2e+u)`$ lies in the integer lattice with basis $`G_A`$, so these are the true labels of the smoothed error. In the uniform branch, $`y`$ is independent of $`u`$, and $`\bar G_A`$ is invertible. The same proof as Sections 2–3 therefore gives

```math
(A,J,Z_Q,Z_P)\ \approx_c\ (A,J,Z_Q,U_m),
\tag{H10}
```

with the true position label retained and the same bound of two LWE advantages plus $`2\eta_n+\kappa_n`$ and negligible implementation error.

Only ordinary LWE with uniform matrices and a uniform secret has been used. There is no symmetric-matrix LWE assumption, prescribed systematic block, Gaussian secret, or reduction requiring coherent samples. Sampling $`V`$ uses finite-field linear algebra and rejection sampling; bounding the number of attempts introduces only negligible error.

## 5. Completing the full-frame proof

Apply (H6) first:

```math
(A,J,Z_Q,Z_P)\ \approx_c\ (A,J,U_m,Z_P).
```

From (H10), discard the true position label to obtain

```math
(A,J,Z_P)\ \approx_c\ (A,J,U_m).
```

Appending a fresh independent uniform position label is an efficient randomized operation, so

```math
(A,J,U_m,Z_P)\ \approx_c\ (A,J,U_m,U'_m),
```

where $`U_m,U'_m`$ are independent. The two replacement laws preserve the same physical marginal $`(A,J)`$. Adding their bounds proves (H1)–(H2).

This is computational indistinguishability of joint distributions. It does not assert a pointwise statistical bound on the conditional law of $`Z`$ for every realized syndrome. At the benchmark logarithmic syndrome precision, the geometric theorem shows that an unrestricted computation can usually identify the true frame from the syndrome.

## 6. Operational consequences

Every consequence below holds for the same public ensemble, Gaussian noise law, and supplied finite-precision syndrome. The negligible term can depend on the fixed efficient algorithm. All tests used to derive the consequences run the proposed decoder and compare its output with the label included in Theorem H1; they are efficient even when the decoder uses quantum internal computation.

### Exact recovery and lists

For every allowed decoder,

```math
\Pr[\widehat Z=Z]\le 2^{-2m}+\mathrm{negl}(n)
=4^{-m}+\mathrm{negl}(n).
\tag{H11}
```

In the independent-uniform experiment, any output computed from $`(A,J)`$ agrees with the label with probability exactly $`2^{-2m}`$ if it is a valid frame, and with probability zero if it is an erasure. An efficient equality test transfers this bound to the physical experiment.

If the decoder instead outputs a list of at most $`L(n)`$ frames, for polynomial $`L`$,

```math
\Pr[Z\text{ lies in the list}]
\le L(n)4^{-m}+\mathrm{negl}(n).
\tag{H12}
```

An output-size bound and an efficient list-membership test suffice; the list need not have any special structure.

### Linear information and partial prediction

Suppose an efficient procedure, using only $`A`$, $`J`$, and its own randomness, selects a rank-$`k`$ binary matrix $`M\in\mathbb F_2^{k\times2m}`$ and guesses $`MZ`$. Then

```math
\Pr[\widehat W=MZ]\le2^{-k}+\mathrm{negl}(n).
\tag{H13}
```

Conditional on the selected matrix and the public transcript, $`MU_{2m}`$ is uniform on $`k`$ bits. In particular, any efficiently selected nonzero linear parity has prediction advantage at most negligible over $`1/2`$. The selection must not be given the unknown true frame as auxiliary input.

For any efficient full bit-string prediction and any fixed $`\varepsilon>0`$, the chance of correctly predicting at least a fraction $`1/2+\varepsilon`$ of the $`2m`$ coordinates is at most

```math
\exp[-4\varepsilon^2m]+\mathrm{negl}(n).
\tag{H14}
```

This follows by applying the corresponding Hamming-agreement test and Hoeffding's inequality to independent uniform bits. These are statements about specified logical coordinates; arbitrary nonlinear predicates can have a nonuniform baseline and are governed by the full indistinguishability statement rather than an automatic $`1/2`$ bound.

### Postselection

Suppose a decoder outputs an acceptance bit and a frame. Let $`h_n`$ be its acceptance probability and $`c_n`$ its conditional correctness when accepted. Because acceptance is computed from the unchanged public marginal, the acceptance probability in the independent-uniform experiment is also $`h_n`$. Therefore

```math
h_nc_n\le h_n4^{-m}+\mathrm{negl}(n).
\tag{H15}
```

If $`h_n`$ is bounded below by an inverse polynomial, the conditional correctness is negligible. The theorem does not forbid a claim conditioned on a negligibly rare acceptance event; dividing by such an event would erase the useful computational bound.

### Efficient changes of logical labels

Let $`f_{A,J}`$ be any polynomial-time computable bijection of $`\mathbb F_2^{2m}`$, specified from the public matrix and the supplied syndrome. Then

```math
(A,J,f_{A,J}(Z))\ \approx_c\ (A,J,U_{2m}).
\tag{H16}
```

To prove this, apply the efficient map $`(A,J,z)\mapsto(A,J,f_{A,J}(z))`$ to both sides of (H1). A bijection sends a conditionally independent uniform label to the same uniform law. Computing the inverse of $`f_{A,J}`$ is not required.

This includes syndrome-dependent XOR offsets, invertible changes of logical basis, and an efficiently computed choice of reference correction expressible from the given inputs. It does not grant access to additional exact-real syndrome digits or an unbounded decoder hidden inside the label convention.

## 7. The computational and geometric conclusions together

For the main choice $`\sigma_n=n^{-1/4}`$ and $`b=\lceil4\log_2n\rceil+O(1)`$, [the geometric theorem](geometry.md) gives an unrestricted decoder with success $`1-\exp[-\Omega(n)]`$ on this same averaged ensemble. The typical error norm is $`\Theta(n^{1/4})`$, while a guaranteed correction ball has radius $`\Omega(n^{1/2})`$. Under the stated LWE assumption, Theorem H1 and (H11) simultaneously bound every permitted efficient decoder's exact logical-frame success by a negligible function.

The same reasoning applies to $`0<a<1/2`$ with the corresponding width $`r_n=\Theta(n^{1-a})`$. For a sufficiently small fixed positive $`\sigma`$, the geometric result also supplies reliable correction, while the computational theorem follows from its matched constant-noise LWE family. No claim that one such assumption implies all the others is needed.

The proof concerns explicit logical-frame inference from classical syndrome data in the ideal GKP model. It does not establish hardness for every coherent recovery channel acting on an unknown encoded state, nor does it establish finite-energy preparation or recovery fidelity. These physical boundaries and the relation to earlier work are detailed in [the interpretation](interpretation.md) and [related work](../references/RELATED_WORK.md).
