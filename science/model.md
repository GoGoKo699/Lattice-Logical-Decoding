# The code ensemble and the decoding task

The question is whether a small physical displacement is also easy to correct computationally. We study a public ensemble of multimode Gottesman–Kitaev–Preskill (GKP) codes. Its geometry admits reliable correction, while a classical controller's task of identifying the logical displacement can encode an ordinary learning-with-errors problem. The controller may itself use quantum computation.

This page fixes the ensemble, units, syndrome convention, and computational model. [Geometry](geometry.md) proves the unconstrained decoding guarantee. [Hardness](hardness.md) proves the conditional computational obstruction, using the distribution calculation in [Gaussian smoothing](gaussian_smoothing.md). [Finite precision](finite_precision.md) supplies the digital implementation of the reduction. [Interpretation](interpretation.md) explains the joint conclusion and its physical scope.

## 1. Parameters and Gaussian conventions

The asymptotic parameter is an integer $n$. There are

$$
m=2n
$$

bosonic modes and $2m$ real phase-space coordinates. Let $q=q_n$ be an efficiently specified odd prime satisfying $q=\Theta(n^2)$. For example, one may take the least prime at least $n^2$ for $n\ge2$. All asymptotic statements concern sufficiently large $n$.

For $t>0$, define the integer Gaussian

$$
\Pr_{X\sim D_{\mathbb Z,t}}[X=k]
=\frac{\exp[-k^2/(2t^2)]}{Z_t},
\qquad
Z_t=\sum_{k\in\mathbb Z}\exp[-k^2/(2t^2)].
$$

The symbol $t$ is the width parameter in this formula; it is not asserted to equal the distribution's exact standard deviation. In contrast, $N(0,t^2)$ denotes the continuous Gaussian with standard deviation exactly $t$.

The main physical noise family is

$$
\sigma_n=n^{-1/4}.
$$

We also state the same reduction for $\sigma_n=n^{-a}$ with fixed $0<a<1/2$, and for sufficiently small positive constant $\sigma_n$. Each choice invokes the corresponding explicit LWE assumption; hardness at one noise width is not silently transferred to every smaller width.

## 2. A uniform public code and its integer lattice

Choose

$$
A\ \leftarrow\ \{A\in\mathbb F_q^{m\times n}:\operatorname{rank}A=n\}
$$

uniformly, and let $C=\operatorname{im}A$. Thus $C$ is a uniform $n$-dimensional subspace of $\mathbb F_q^m$, and conditional on $C$, the columns of $A$ are a uniform ordered basis. The public description is the complete matrix $A$, containing $O(n^2\log q)$ bits.

Define

$$
\Lambda_A=\{v\in\mathbb Z^m:v\bmod q\in C\},
\qquad
L_A=q^{-1/2}\Lambda_A.
$$

Because $[\mathbb Z^m:\Lambda_A]=q^{m-n}=q^n$ and $m=2n$,

$$
\det L_A=q^{-m/2}q^{m-n}=1.
$$

Here and below, the determinant of a lattice means its positive covolume.

### Lemma M1: Euclidean dual

Let

$$
\Lambda_{A,\perp}=\{w\in\mathbb Z^m:w\bmod q\in C^\perp\}.
$$

Then

$$
L_A^*=q^{-1/2}\Lambda_{A,\perp}.
$$

**Proof.** For $v\in\Lambda_A$ and $w\in\Lambda_{A,\perp}$, their integer inner product is divisible by $q$, so $(v/\sqrt q)\cdot(w/\sqrt q)$ is an integer. The displayed lattice is therefore contained in $L_A^*$. Both have covolume one: $C^\perp$ has dimension $m-n=n$, and $\det L_A^*=(\det L_A)^{-1}=1$. Containment with equal covolume gives equality. ∎

### An explicit basis in the original physical coordinates

Choose a deterministic set of $n$ independent rows of $A$. Let $P$ be the corresponding coordinate permutation, placing these rows first. If $A_0$ is that invertible top block, then over $\mathbb F_q$,

$$
PAA_0^{-1}=\begin{pmatrix}I_n\\B\end{pmatrix}.
$$

Use entries in $\{0,\ldots,q-1\}$ for the integer representative $B$, and set

$$
H_A=P^T
\begin{pmatrix}I_n&0\\B&qI_n\end{pmatrix},
\qquad
G_A=qH_A^{-T}
=P^T\begin{pmatrix}qI_n&-B^T\\0&I_n\end{pmatrix}.
$$

The columns of $H_A$ form an integer basis of $\Lambda_A$, and the columns of $G_A$ form an integer basis of $\Lambda_{A,\perp}$. Both determinants have absolute value $q^n$. In particular, both matrices are invertible modulo $2$.

The permutation is part of computing a basis; it does **not** replace the public ensemble by matrices whose first block is invertible. The formulas for $H_A$ and $G_A$ remain in the original physical coordinates. An error drawn isotropically in those coordinates is the error used throughout the results.

## 3. The symplectic GKP code

Write a phase-space vector as $x=(x_Q,x_P)\in\mathbb R^m\oplus\mathbb R^m$, and use

$$
J=\begin{pmatrix}0&I_m\\-I_m&0\end{pmatrix},
\qquad
\omega(x,y)=x^TJy.
$$

We use dimensionless Weyl coordinates. With quadratures satisfying $[\hat Q_j,\hat P_k]=i\delta_{jk}$, a vector $x$ represents a physical displacement $\sqrt{2\pi}\,x$. The Weyl commutator is $\exp[-2\pi i\omega(x,y)]$. Thus two displacement operators commute when their symplectic pairing is an integer. In these units, the physical quadrature variance corresponding to the parameter $\sigma_n^2$ is $2\pi\sigma_n^2$.

For a full-rank phase-space lattice $T$, write

$$
T^\times=\{x:\omega(x,t)\in\mathbb Z\text{ for all }t\in T\}
$$

for its symplectic dual. Define

$$
S_A=L_A\oplus L_A^*,\qquad
\Gamma_A=\sqrt2\,S_A,\qquad
K_A=\Gamma_A^\times=S_A/\sqrt2.
$$

### Lemma M2: rate and logical classes

The lattice $S_A$ is symplectically self-dual. The stabilizer lattice $\Gamma_A$ defines an ideal GKP code encoding $m$ qubits in $m$ modes. Its logical displacement classes are

$$
K_A/\Gamma_A=K_A/(2K_A)\cong\mathbb F_2^{2m}.
$$

**Proof.** A vector $(x_Q,x_P)$ has integral symplectic pairing with $L_A\oplus L_A^*$ precisely when $x_Q\in(L_A^*)^*=L_A$ and $x_P\in L_A^*$. Hence $S_A^\times=S_A$. Scaling gives $\Gamma_A^\times=S_A/\sqrt2$ and $\Gamma_A=2K_A$. A basis for $K_A$ is

$$
\mathcal B_A=\frac1{\sqrt{2q}}
\begin{pmatrix}H_A&0\\0&G_A\end{pmatrix}.
$$

It satisfies $\mathcal B_A^TJ\mathcal B_A=J/2$. Consequently the corresponding stabilizer basis $2\mathcal B_A$ has symplectic Gram matrix $2J$, the normal form for $m$ encoded qubits. Equivalently, the logical displacement quotient has $2^{2m}$ elements, which is the Pauli-label set for a logical Hilbert space of dimension $2^m$. ∎

This is the standard lattice description of GKP stabilizers and logical operators; see the definitions and decoding discussion in [Conrad, Eisert, and Seifert](https://arxiv.org/abs/2303.02432). The new claims in this project concern the specified random ensemble and its computational decoding law.

### Lemma M3: ambient parity

For either $\Lambda=\Lambda_A$ or $\Lambda=\Lambda_{A,\perp}$, coordinate parity induces an isomorphism

$$
\Lambda/2\Lambda\longrightarrow\mathbb F_2^m.
$$

**Proof.** The index $[\mathbb Z^m:\Lambda]=q^n$ is odd, so multiplication by $2$ is invertible in $\mathbb Z^m/\Lambda$. If $2v\in\Lambda$, this implies $v\in\Lambda$, hence $\Lambda\cap2\mathbb Z^m=2\Lambda$. The parity map is therefore injective on $\Lambda/2\Lambda$. Its domain and codomain both have $2^m$ elements, so it is bijective. Equivalently, $H_A$ and $G_A$ are invertible modulo $2$. ∎

## 4. A digital syndrome and its true logical frame

Draw the physical displacement

$$
\xi\sim N(0,\sigma_n^2I_{2m})
$$

independently of $A$. Let

$$
a=\mathcal B_A^{-1}\xi,\qquad
z=\lfloor a\rfloor\in\mathbb Z^{2m},\qquad
x=a-z\in[0,1)^{2m}.
$$

All floors are coordinatewise. The ideal stabilizer syndrome specifies $\xi$ modulo $K_A$, equivalently the torus coordinate $x$. For an integer precision $b=b(n)\ge0$, the actual classical input is

$$
J_b(A,\xi)=\lfloor2^b x\rfloor
\in\{0,\ldots,2^b-1\}^{2m}.
$$

The **true logical frame** relative to this section of the syndrome torus is

$$
Z(A,\xi)=z\bmod2=(Z_Q,Z_P)\in\mathbb F_2^{2m}.
$$

A decoder outputs $\widehat Z$ and succeeds when $\widehat Z=Z$. The meaning is immediate from

$$
\xi=\mathcal B_A(x+z).
$$

If the exact torus representative were available for analogue feedforward, the correction $\mathcal B_A(x+\widehat Z)$ would leave a stabilizer displacement precisely on this event. With only the finite representative $\widehat x=2^{-b}J_b$, the residual also contains the known-resolution term $\mathcal B_A(x-\widehat x)$. The theorem concerns selecting the correct logical class. It does not identify quantized feedforward with exact physical recovery.

The choice of a fundamental cell fixes labels, not a new physical resource. [Hardness](hardness.md#6-operational-consequences) proves that efficiently computable bijective relabelings, including syndrome-dependent Pauli offsets, preserve the computational conclusion.

## 5. Computational access and assumptions

A permitted decoder is a uniform quantum polynomial-time algorithm receiving the classical strings $(A,J_b,b)$. It may first perform arbitrary polynomial-time preprocessing of $A$, retaining polynomial-size classical or quantum data. All preprocessing and decoding costs count toward the total polynomial bound. Classical randomized decoders are included. The algorithm may output an erasure or a polynomial-size list when that output convention is stated.

The hardness assumption is ordinary decisional LWE with **classical** samples, a uniform secret, and the explicitly defined $D_{\mathbb Z,r_n}$ error law. Put $R_n=\log n$ for $n\ge3$ and

$$
r_n^2=\frac{2q\sigma_n^2-2R_n^2}{4}.
$$

This is positive for all sufficiently large $n$ in the regimes considered. For the main choice $\sigma_n=n^{-1/4}$,

$$
r_n=\Theta(n^{3/4}),\qquad r_n\gg\sqrt n.
$$

The assumption states that no uniform quantum polynomial-time distinguisher separates

$$
(A,As+e\bmod q)
\quad\text{from}\quad
(A,w),
$$

with nonnegligible advantage, where $A$ is initially uniform in all of $\mathbb F_q^{m\times n}$, $s$ is uniform in $\mathbb F_q^n$, $e\sim D_{\mathbb Z,r_n}^{\otimes m}$, and $w$ is uniform in $\mathbb F_q^m$. These variables are independent before forming the LWE value. The probability of rank deficiency is at most

$$
\sum_{i=0}^{n-1}q^{i-m}<\frac{q^{-n}}{q-1},
$$

so conditioning on full rank changes the experiments negligibly.

Discrete Gaussian errors are a standard LWE formulation; see Section 2.2 of [Lindner and Peikert](https://eprint.iacr.org/2010/613.pdf). The original [Regev formulation](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) also uses a rounded continuous Gaussian in its stated reduction. This account assumes the exact integer-Gaussian family above and does not identify those two distributions without a conversion argument. No claim about breaking a standardized cryptosystem follows from this conditional result.

Arbitrary code-dependent trapdoor advice, exponential preprocessing, and a decoding oracle are outside the model. A version allowing nonuniform advice independent of $A$ follows if the LWE assumption is strengthened to the same nonuniform adversary class. The quantum polynomial-time allowance already covers quantum computation on the supplied classical data; it does not supply QRAM or coherent LWE samples.

The results are averaged over the public code, Gaussian noise, preprocessing randomness, and all subsequent classical or quantum randomness. They do not assert that every individual code is hard. They also do not establish an obstruction for arbitrary coherent recovery channels that never produce a logical-frame label. The ideal GKP description specifies no finite-energy encoding or noisy syndrome-extraction implementation.
