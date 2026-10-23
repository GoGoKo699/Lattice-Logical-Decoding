# From Peikert's lattice cryptography to logical GKP decoding

**Shared reading anchor:** Chris Peikert, [*A Decade of Lattice Cryptography*](https://eprint.iacr.org/2015/939), published in 2016. The [author manuscript](https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf) is dated 17 February 2016. The parts used most directly here are §2.2, *Lattices*; §2.3, *(Discrete) Gaussians and Subgaussians*; and §4.2, *Learning With Errors*, including its definitions and hardness subsections.

This bridge connects those foundations to a specific quantum error-correction question: **when a small displacement is geometrically correctable, can an efficient controller identify its logical correction from a public code and its syndrome?** For the ensemble in this repository, an unrestricted decoder succeeds with overwhelming probability, while the complete logical frame is computationally pseudorandom under the stated quantum-LWE assumption. The physical noise can even decrease with dimension.

The survey supplies the lattice and cryptographic language. The symplectic code, logical quotient, Gaussian transfer, and full-frame theorem are the project's additional argument. The canonical statements and proofs remain in [the scientific map](../science/index.md). This page explains their connections and works through two small examples.

## 1. Where the selected reading enters

| Selected part of Peikert | Connection developed here | Existing milestone IDs |
| --- | --- | --- |
| §2.2: lattices, fundamental domains, duality | A public modular code becomes an integer lattice; pairing it with its dual produces a symplectic code. | M03–M07, M16–M19 |
| §2.3: Gaussian conventions and smoothing | An integer Gaussian mask hides parity; a continuous Gaussian removes the remaining discrete support. | M08, M12–M14, M23, M26 |
| §4.2.1: LWE definitions and its lattice interpretation | The noisy modular equation becomes a lattice displacement whose logical class contains a hidden mask. | M10–M11, M21–M22, M24–M25 |
| §4.2.2: hardness and the direction of reductions | A hypothetical efficient decoder would distinguish the specified LWE family from uniform. | M09, M15, M27–M30 |
| The project's physical extension | Displacement commutation, ideal GKP stabilizers, and the recovery benchmark give the lattice statements their quantum meaning. | M01–M02, M05–M09, M17, M20, M29–M30 |

These IDs refer to the [thirty-milestone map](MILESTONES.md). The map separates 15 background topics from 15 steps in the contribution; the bridge supplies a continuous account across that boundary.

## 2. A notation dictionary that prevents two common mistakes

### Lattice columns and LWE sample columns are different conventions

A lattice basis matrix has its basis vectors as columns. If $`B`$ is an invertible real $`d\times d`$ matrix, then

```math
L(B)=B\mathbb Z^d
=\{Bz:z\in\mathbb Z^d\},
\qquad
\det L=|\det B|,
\qquad
L^*=B^{-T}\mathbb Z^d.
```

The dual formula follows directly from $`\langle B^{-T}u,Bz\rangle=u^Tz\in\mathbb Z`$. Replacing $`B`$ by $`BU`$ for an integer matrix $`U`$ of determinant $`\pm1`$ changes coordinates but leaves the lattice unchanged. These are the lattice conventions of Peikert §2.2 and of the repository.

For LWE, Peikert §4.2.1 collects sample vectors as columns of a matrix. To keep that matrix distinct from ours, call it $`A_{\mathrm{P}}`$:

```math
A_{\mathrm{P}}=[a_1\ \cdots\ a_m]\in\mathbb Z_q^{n\times m},
\qquad
\mathbf b^T=s^TA_{\mathrm{P}}+e^T\pmod q.
```

For this project's prime modulus, $`\mathbb Z_q`$ is the field $`\mathbb F_q`$. The repository stores the transposed matrix and all vectors as columns:

```math
A=A_{\mathrm{P}}^T\in\mathbb F_q^{m\times n},
\qquad
\mathbf b=As+e\pmod q.
```

This is a transpose of the same equations, with the same samples and secret. It does not require a different LWE assumption. Peikert's integer LWE lattice, Eq. (4.2.1), becomes our $`\Lambda_A`$ after that transpose. [Source: Peikert §4.2.1](https://eprint.iacr.org/2015/939).

| Symbol here | Meaning |
| --- | --- |
| $`n`$ | LWE secret dimension and asymptotic parameter |
| $`m=2n`$ | Number of LWE samples; also number of oscillator modes |
| $`2m=4n`$ | Real phase-space dimension and number of logical-frame bits |
| $`A`$ | Public $`m\times n`$ finite-field matrix; its columns span a code $`C`$ |
| $`H_A,G_A`$ | Square integer basis matrices, each of size $`m\times m`$ |
| $`\mathcal B_A`$ | Square basis of the syndrome-invisible phase-space lattice, size $`2m\times2m`$ |
| $`b`$ | Bits per syndrome coordinate; the bold vector $`\mathbf b`$ is an LWE value |

### Gaussian width is not always standard deviation

Peikert §2.3 uses the Gaussian function

```math
\rho_w(x)=\exp(-\pi\|x\|^2/w^2).
```

We use $`w`$ for that parameter here to avoid confusing it with the LWE secret $`s`$. The continuous distribution proportional to $`\rho_w`$ has standard deviation $`w/\sqrt{2\pi}`$ in each coordinate. The repository writes its integer Gaussian as

```math
\Pr_{X\sim D_{\mathbb Z,r}}[X=k]
=\frac{e^{-k^2/(2r^2)}}{\sum_{j\in\mathbb Z}e^{-j^2/(2r^2)}}.
```

Equating exponents gives the exact conversion

```math
w=\sqrt{2\pi}\,r.
```

For a continuous Gaussian, $`r`$ is its standard deviation in this convention. For the point-mass integer Gaussian, it is a width parameter; its exact variance need not equal $`r^2`$. No variance approximation is needed in the proof.

Peikert's usual LWE choice has discrete-Gaussian width $`\alpha q`$. Its direct specialization to our assumed error law therefore uses

```math
\alpha q=\sqrt{2\pi}\,r_n.
```

The survey's footnote in §4.2.1 also distinguishes a true discrete Gaussian from rounding a continuous one. Those distributions assign different masses to integers. That distinction will matter when the cryptographic error is converted to physical noise. [Source: Peikert §§2.3 and 4.2.1](https://eprint.iacr.org/2015/939).

Here $`\alpha`$ parameterizes an already-discrete LWE error. The continuous-to-discrete transfer attributed to Gordon, Katz, and Vaikuntanathan in [related work](../references/RELATED_WORK.md) starts instead with $`\alpha_{\mathrm{cont}}q=\sqrt\pi\,r_n`$ and produces integer-Gaussian width $`\sqrt2\,\alpha_{\mathrm{cont}}q=\sqrt{2\pi}\,r_n`$. The factor $`\sqrt2`$ belongs to that distribution conversion; the survey translation above is a change of width notation for the same point-mass law.

## 3. From the noisy equation to the public lattice

For each sufficiently large $`n`$, choose an odd prime $`q=\Theta(n^2)`$ and sample $`A\in\mathbb F_q^{m\times n}`$ uniformly conditioned on full column rank. Let $`C=\mathrm{im}(A)`$. Define

```math
\Lambda_A=\{v\in\mathbb Z^m:v\bmod q\in C\},
\qquad
L_A=q^{-1/2}\Lambda_A.
```

The finite code tells us which residue classes are allowed, and each residue class lifts to infinitely many integer vectors. Because $`C`$ has $`q^n`$ of the $`q^m`$ possible residues, the index of $`\Lambda_A`$ in $`\mathbb Z^m`$ is $`q^{m-n}=q^n`$. Rescaling all $`m=2n`$ coordinates by $`q^{-1/2}`$ therefore gives $`\det L_A=1`$.

For an LWE value $`\mathbf b=As+e\pmod q`$, the integer lift $`\mathbf b-e`$ belongs to $`\Lambda_A`$. This is the geometric connection behind the noisy linear equation. Finding a nearby full lattice vector is a natural search problem, but our quantum task will ask only for a logical class of such a vector.

The Euclidean dual has a particularly useful description:

```math
L_A^*=q^{-1/2}\Lambda_{C^\perp},
\qquad
\Lambda_{C^\perp}
=\{w\in\mathbb Z^m:w\bmod q\in C^\perp\}.
```

Indeed, if the residues of $`v`$ and $`w`$ are orthogonal, then $`v^Tw`$ is divisible by $`q`$, so $`(v/\sqrt q)^T(w/\sqrt q)`$ is an integer. The candidate dual has the correct covolume, which completes the equality.

An explicit basis is needed for a finite controller. Select independent rows of the sampled $`A`$, and let $`P`$ move them to the top. If $`A_0`$ is that invertible block, write

```math
PAA_0^{-1}=\begin{pmatrix}I_n\\B\end{pmatrix}\pmod q.
```

With entries of $`B`$ represented by integers from $`0`$ to $`q-1`$, set

```math
H_A=P^T\begin{pmatrix}I_n&0\\B&qI_n\end{pmatrix},
\qquad
G_A=qH_A^{-T}
=P^T\begin{pmatrix}qI_n&-B^T\\0&I_n\end{pmatrix}.
```

The columns generate $`\Lambda_A`$ and $`\Lambda_{C^\perp}`$, respectively. The factor $`P^T`$ restores the original physical coordinates. Selecting pivots inside a sampled matrix preserves the original ensemble; requiring a particular predetermined block to be invertible would be a different sampling rule. The full-rank conditioning itself costs only negligible statistical distance from an unrestricted uniform matrix.

These details connect M03–M04 to M18. The proofs and exact sampling convention are in [the model](../science/model.md).

## 4. The extra quantum structure: two quotients, two kinds of equivalence

An $`m`$-mode displacement has position and momentum parts $`\xi=(\xi_Q,\xi_P)\in\mathbb R^{2m}`$. Its size is measured by the Euclidean norm. Its commutation with another displacement is controlled by the symplectic pairing

```math
\omega(x,y)=x^TJy,
\qquad
J=\begin{pmatrix}0&I_m\\-I_m&0\end{pmatrix}.
```

In the repository's dimensionless convention, the Weyl commutator is $`e^{-2\pi i\omega(x,y)}`$. A coordinate vector $`x`$ means a physical quadrature displacement $`\sqrt{2\pi}\,x`$, with quadrature commutator $`[\hat Q_j,\hat P_k]=i\delta_{jk}`$. Thus the physical quadrature variance corresponding to our noise parameter is $`2\pi\sigma_n^2`$.

Pair the lattice with its Euclidean dual:

```math
S_A=L_A\oplus L_A^*,
\qquad
\Gamma_A=\sqrt2\,S_A,
\qquad
K_A=S_A/\sqrt2.
```

The lattice $`S_A`$ is symplectically self-dual: integral pairing with its position part forces the momentum part into $`L_A^*`$, and integral pairing with its momentum part forces the position part into $`L_A`$. Consequently, $`\Gamma_A`$ is a commuting stabilizer lattice and $`K_A`$ is its symplectic dual. Here $`\Gamma_A=2K_A`$.

There are two different identifications:

| Quotient | What it identifies | What remains visible |
| --- | --- | --- |
| $`\mathbb R^{2m}/K_A`$ | Displacements differing by an element of $`K_A`$ | Their common stabilizer syndrome |
| $`K_A/\Gamma_A=K_A/(2K_A)`$ | Syndrome-invisible displacements differing by a stabilizer | Their logical Pauli operation, ignoring global phase |

The second quotient is $`\mathbb F_2^{2m}`$: it supplies two Pauli-label bits for each of $`m`$ encoded qubits. The ideal code therefore encodes $`m`$ qubits in $`m`$ modes. This logical-dimension statement is separate from energy cost or laboratory preparation.

The canonical basis of $`K_A`$ is

```math
\mathcal B_A=\frac1{\sqrt{2q}}
\begin{pmatrix}H_A&0\\0&G_A\end{pmatrix}.
```

For an error $`\xi`$, split its basis coordinates into integer and fractional parts:

```math
\mathcal B_A^{-1}\xi=z+x,
\qquad
z=\lfloor\mathcal B_A^{-1}\xi\rfloor,
\qquad x\in[0,1)^{2m}.
```

The fractional part $`x`$ labels a chosen representative of the syndrome. The remaining logical frame is $`Z=z\bmod2`$. A controller receives only

```math
J_b=\lfloor2^b x\rfloor.
```

Its task is to output the true $`Z`$. With conceptual exact analogue feedforward, subtracting $`\mathcal B_A(x+Z)`$ leaves an element of $`2K_A`$, hence a stabilizer. With $`\widehat x=2^{-b}J_b`$, a small analogue residual $`\mathcal B_A(x-\widehat x)`$ also remains. Correctly choosing a logical class and removing every analogue error are distinct statements.

Peikert's fundamental-domain language makes this decomposition natural. Quantum degeneracy supplies the second quotient. This is the connection across M01–M07 and M16–M17; [the model](../science/model.md) fixes the physical normalization and [the interpretation](../science/interpretation.md) states its scope.

## 5. Worked example: a syndrome, its frame, and a quantized correction

Take the **toy** values $`n=1`$, $`m=2`$, $`q=5`$, and

```math
A=\begin{pmatrix}1\\3\end{pmatrix},
\qquad
H=\begin{pmatrix}1&0\\3&5\end{pmatrix},
\qquad
G=\begin{pmatrix}5&-3\\0&1\end{pmatrix}.
```

Here $`H^TG=5I_2`$ and $`\det H=\det G=5`$. For example, $`(-1,2)^T=H(-1,1)^T`$ lies in the integer lattice because $`2=3(-1)\pmod5`$.

The same lattice has the orthogonal integer basis $`(1,-2)^T,(2,1)^T`$. Both vectors have length $`\sqrt5`$ and their determinant is $`5`$, so $`L=\Lambda/\sqrt5`$ is a rotation of $`\mathbb Z^2`$. In this special example $`L=L^*`$ and

```math
\lambda_1(K)=\frac1{\sqrt2},
\qquad
\frac{\lambda_1(K)}2=\frac1{2\sqrt2}\approx0.354.
```

Choose the following basis coordinates for an error, ordered as two position coordinates followed by two momentum coordinates:

```math
a=\left(\frac1{10},-\frac1{10},\frac1{10},-\frac1{10}\right),
\qquad
\xi=\mathcal B a
=\frac1{\sqrt{10}}\left(\frac1{10},-\frac15,\frac45,-\frac1{10}\right).
```

Their integer and fractional parts are

```math
z=(0,-1,0,-1),
\qquad
x=\left(\frac1{10},\frac9{10},\frac1{10},\frac9{10}\right),
\qquad
Z=(0,1,0,1).
```

The negative coordinates matter: the floor of $`-1/10`$ is $`-1`$, not zero. The frame does not record the sign or magnitude of every integer coordinate; it records their parity. For instance, changing $`z`$ by $`2(1,0,0,0)`$ changes the lattice displacement but preserves the logical operation.

At four syndrome bits per coordinate,

```math
J_4=(1,14,1,14),
\qquad
\widehat x=\left(\frac1{16},\frac78,\frac1{16},\frac78\right).
```

An unrestricted geometric decoder forms $`t_0=\mathcal B\widehat x`$ and looks for its nearest point in $`K`$. The correct point has coefficients $`-z=(0,1,0,1)`$:

```math
\begin{aligned}
t_0&=\frac1{16\sqrt{10}}(1,73,-37,14),\\
\mathcal B(-z)&=\frac1{\sqrt{10}}(0,5,-3,1),\\
t_0-\mathcal B(-z)&=\frac1{16\sqrt{10}}(1,-7,11,-2).
\end{aligned}
```

The last vector has norm $`\sqrt{35/512}\approx0.261`$, below $`\lambda_1(K)/2`$, so that nearest point is unique. Returning minus its coefficient parity gives $`Z=(0,1,0,1)`$, as required. The original physical error also lies inside the correction ball: $`\|\xi\|=\sqrt7/10\approx0.265`$.

Applying the finite representative with the correct frame leaves, modulo a stabilizer, the residual

```math
\mathcal B(x-\widehat x)
=\frac1{80\sqrt{10}}(3,19,9,2).
```

This explicit residual explains why the digital theorem concerns the logical label. The example is an easily decoded two-mode lattice, chosen for transparent arithmetic. It is not evidence of large-dimension hardness, an asymptotic Gaussian experiment, or a finite-energy recovery result. It illustrates M06–M07, M17, and M20.

## 6. Why the geometry permits recovery

The high-dimensional ensemble uses the same construction with a random balanced code $`C\subset\mathbb F_q^{2n}`$. For a fixed nonzero residue $`w`$,

```math
\Pr[w\in C]=\frac{q^n-1}{q^{2n}-1}=\frac1{q^n+1}.
```

Counting integer vectors in a ball and applying this membership probability shows that $`L_A`$ rarely has a short nonzero vector. The orthogonal complement $`C^\perp`$ has the same marginal distribution as $`C`$, so the same argument controls $`L_A^*`$. Their independence is unnecessary: a union bound controls both bad events.

For any fixed $`0<c<1/\sqrt{2\pi e}`$, with probability $`1-e^{-\Omega(n)}`$ over the code,

```math
\lambda_1(K_A)>c\sqrt{m/2}.
```

A shortest nonzero vector of $`K_A`$ cannot belong to $`2K_A`$, since halving it would produce a shorter nonzero vector. Thus this minimum is also the shortest nontrivial logical displacement. Nearest-point decoding is certainly correct when $`\|\xi\|<\lambda_1(K_A)/2`$.

At the main physical width $`\sigma_n=n^{-1/4}`$, there are $`2m=4n`$ independent Gaussian coordinates. Hence

```math
\mathbb E\|\xi\|^2=4n\sigma_n^2=4n^{1/2},
\qquad
\|\xi\|=\Theta(n^{1/4})\ \text{with high probability}.
```

The guaranteed correction radius is $`\Omega(n^{1/2})`$. The typical error occupies a decreasing fraction of that radius. Logarithmic syndrome precision preserves this margin, and an unrestricted decoder succeeds with probability $`1-e^{-\Omega(n)}`$.

This establishes existence of a successful rule. Evaluating a nearest-point rule efficiently is a separate question. That separation is familiar from the role of lattice problems in cryptography, but a quantum decoding lower bound still has to address the logical quotient rather than assume that every successful decoder finds the entire lattice point. [Full proof: geometry](../science/geometry.md). This is the link from M08–M09 and M19–M20 to the reduction below.

## 7. Why a logical class can reveal a hidden mask

The useful algebraic fact is that the index $`[\mathbb Z^m:\Lambda_A]=q^n`$ is odd. If $`2w\in\Lambda_A`$, then multiplication by two is invertible in the finite group $`\mathbb Z^m/\Lambda_A`$, so $`w\in\Lambda_A`$. Therefore

```math
\Lambda_A\cap2\mathbb Z^m=2\Lambda_A,
\qquad
\Lambda_A/2\Lambda_A\cong\mathbb F_2^m.
```

In words, two lattice vectors have the same ambient coordinate parities exactly when they represent the same class modulo twice the lattice. A logical decoder can reveal all those parities without recovering the full vector. This is the quotient-aware step required by M21.

Start with an ordinary LWE challenge $`(A,\mathbf b)`$. The challenge value is either $`As+e\pmod q`$ or independent uniform. Sample an independent integer mask $`u`$, a continuous Gaussian vector $`g`$, and an independent physical Gaussian momentum error $`p`$. Their precise widths are specified in Section 9. Form

```math
y=(2\mathbf b+u)\bmod q,
\qquad
t=\left(\frac{y+g}{\sqrt{2q}},p\right),
```

where $`y`$ is represented by integers from $`0`$ to $`q-1`$. In the LWE branch,

```math
v_{\mathrm{int}}=y-(2e+u)\in\Lambda_A,
\qquad
t=\left(\frac{v_{\mathrm{int}}}{\sqrt{2q}},0\right)
+\left(\frac{2e+u+g}{\sqrt{2q}},p\right).
```

The first term is in $`K_A`$. Thus the target $`t`$ and the error in the second term, call it $`\Xi`$, have exactly the same syndrome. The reduction can compute

```math
k_t=\lfloor\mathcal B_A^{-1}t\rfloor
```

from known values. Although $`v_{\mathrm{int}}`$ is unknown, its parity is known because $`2e`$ is even:

```math
\overline{v_{\mathrm{int}}}=\bar y+\bar u.
```

Bars denote reduction modulo two. Since $`\det H_A=\pm q^n`$ is odd, $`\bar H_A`$ is invertible. The true position frame of $`\Xi`$ is consequently

```math
Z_Q=\bar k_{t,Q}+\bar H_A^{-1}(\bar y+\bar u).
```

This expression is computable without the secret or error vector. It follows by subtracting the integer coordinates of the lattice shift from $`k_t`$; subtraction equals addition modulo two.

In the uniform branch, multiplication by two modulo odd $`q`$ is a permutation. For every fixed integer $`u`$, the vector $`y`$ is therefore uniform, and it is independent of the entire mask. Once $`A,y,g,p`$ are fixed, the displayed frame is an affine bijection of $`\bar u`$. Making the mask parity nearly uniform then makes the position frame nearly uniform, even while retaining the known momentum frame and the supplied syndrome.

This algebra turns a successful logical decoder into an LWE distinguisher. It uses a class in $`\Lambda_A/2\Lambda_A`$, rather than an oracle that reconstructs the complete lattice point. [Proof: hardness, Sections 2–3](../science/hardness.md). It connects M21–M22 to M24.

## 8. Worked example: the mask survives in the logical class

Use the same toy $`q=5`$, $`A=(1,3)^T`$, and $`H`$ as in Section 5. Choose

```math
s=2,
\qquad e=(1,-1),
\qquad u=(1,0).
```

The two modular operations give

```math
\mathbf b=As+e\pmod5=(3,0),
\qquad
y=2\mathbf b+u\pmod5=(2,0).
```

For checking the decomposition by hand,

```math
2e+u=(3,-2),
\qquad
v_{\mathrm{int}}=y-(2e+u)=(-1,2)=H(-1,1).
```

Take the displayed position dither to be $`g=(1/2,1/4)`$. In position basis coordinates, the target and its underlying error are

```math
\begin{aligned}
H^{-1}(y+g)&=\left(\frac52,-\frac{29}{20}\right),\\
H^{-1}(2e+u+g)&=\left(\frac72,-\frac{49}{20}\right).
\end{aligned}
```

Their difference is $`(-1,1)`$, the integer lattice-shift coordinates. Both have fractional part $`(1/2,11/20)`$. Their floors differ:

```math
k_{t,Q}=(2,-2),
\qquad
z_Q=(3,-3),
\qquad
Z_Q=(1,1).
```

The reduction obtains that same true frame using only known parities:

```math
\bar H=\bar H^{-1}
=\begin{pmatrix}1&0\\1&1\end{pmatrix},
\qquad
\bar y+\bar u=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
\bar k_{t,Q}+\bar H^{-1}(\bar y+\bar u)
=\begin{pmatrix}1\\1\end{pmatrix}.
```

Conversely, a correct logical frame and the known target floor give the lattice-shift coefficient parity $`(1,1)`$. Multiplying by $`\bar H`$ gives the ambient lattice parity $`(1,0)`$. Adding $`\bar y=(0,0)`$ recovers the hidden mask parity $`\bar u=(1,0)`$.

The hand calculation displayed the full lattice vector to verify the identities. The actual reduction uses only its parity and never learns $`e`$ or $`s`$. This example shows one position sector; the independent momentum sector is retained in the full argument. Its chosen small numbers illustrate the algebra and are not assigned the theorem's asymptotic Gaussian-width schedule.

## 9. The two smoothing operations and the third parity estimate

The masked error just constructed contains integers. The physical noise model requires independent continuous Gaussians. Matching that model is a quantitative part of the reduction.

First keep three laws separate:

| Law | Support | How a probability is assigned |
| --- | --- | --- |
| Point-mass integer Gaussian $`D_{\mathbb Z,r}`$ | $`\mathbb Z`$ | Normalize the weights $`e^{-k^2/(2r^2)}`$. |
| Rounded continuous Gaussian | $`\mathbb Z`$ | Integrate a continuous density over each rounding interval. |
| Physical Gaussian $`N(0,\sigma^2)`$ | $`\mathbb R`$ | Use the continuous density with variance $`\sigma^2`$. |

Only the first is the LWE error assumed here. Peikert's distinction between Gaussian conventions makes it possible to track this exactly; a change of the numerical width alone does not identify the first two laws.

### First operation: smooth the doubled integer error

Let $`E\sim D_{\mathbb Z,r}`$ and $`U\sim D_{\mathbb Z,R}`$ independently. Doubling $`E`$ alone gives support only on even integers. The mask fills the parity classes and also smooths their relative weights. Completing the square gives

```math
\Pr[2E+U=z]
\ \propto\
e^{-z^2/(2s_0^2)}\,
\Theta\!\left(v_0,\frac{2r^2z}{s_0^2}\right),
\qquad
s_0^2=4r^2+R^2,
\qquad
v_0^2=\frac{r^2R^2}{s_0^2},
```

where

```math
\Theta(t,c)=\sum_{k\in\mathbb Z}e^{-(k-c)^2/(2t^2)}.
```

The first factor is the desired integer-Gaussian weight. The theta factor is its remaining periodic modulation. Poisson summation rewrites it as

```math
\frac{\Theta(t,c)}{\sqrt{2\pi}\,t}
=1+2\sum_{\ell\ge1}e^{-2\pi^2t^2\ell^2}\cos(2\pi\ell c).
```

When $`t`$ is sufficiently large, all nonconstant Fourier terms are small, uniformly in the center $`c`$. Thus $`2E+U`$ is close in total variation to $`D_{\mathbb Z,s_0}`$. This is the concrete one-dimensional use of the smoothing idea in Peikert §2.3. The proof samples only product Gaussians on the integers; it does not require an oracle for sampling on the public hard lattice.

### Second operation: pass to a continuous law

Add an independent $`G\sim N(0,R^2)`$. Another completed-square identity shows that

```math
D_{\mathbb Z,s_0}+G
\quad\text{is close to}\quad
N(0,s_0^2+R^2).
```

Again, a theta factor controls the discrepancy. Its effective width is

```math
v_1^2=\frac{s_0^2R^2}{s_0^2+R^2}.
```

The first operation controls integer weights after doubling; the second produces a continuous density. Both estimates are needed. With natural logarithms, choosing

```math
R=\log n,
\qquad
r_n^2=\frac{2q\sigma_n^2-2R^2}{4}
```

makes the variance of the continuous comparison law exactly $`2q\sigma_n^2`$. Hence

```math
\frac{2E+U+G}{\sqrt{2q}}
\quad\text{is negligibly close to}\quad
N(0,\sigma_n^2).
```

This variance identity specifies the comparison law; it does not assert that the point Gaussian's exact variance is $`r_n^2`$. For the stated schedules, both effective theta widths grow proportionally to $`\log n`$. The error per coordinate is $`e^{-\Omega((\log n)^2)}`$, and multiplying by $`m=2n`$ keeps it negligible: it eventually becomes smaller than every fixed inverse power of $`n`$.

### The mask must also hide parity

Smoothness of the sum alone would not establish mask secrecy. A separate Fourier calculation gives

```math
\left|\mathbb E[(-1)^U]\right|
\le\frac{2e^{-\pi^2R^2/2}}{1-e^{-4\pi^2R^2}}.
```

For $`R=\log n`$, the parity vector of $`m`$ independent masks is negligibly close to $`m`$ independent uniform bits. This is the estimate used in the uniform branch of Section 7.

At $`q=\Theta(n^2)`$ and $`\sigma_n=n^{-1/4}`$, the required LWE width is $`r_n=\Theta(n^{3/4})`$. More generally, $`\sigma_n=n^{-a}`$ with $`0<a<1/2`$ gives $`r_n=\Theta(n^{1-a})\gg\sqrt n`$. Each schedule invokes its own matched LWE assumption. The compatibility of the exact point-Gaussian convention with foundational hardness reductions is discussed in [related work](../references/RELATED_WORK.md); it is not inferred by treating rounded and point Gaussians as identical.

[Full calculation and constants: Gaussian smoothing](../science/gaussian_smoothing.md). This section joins M12–M13 to M23 and M28.

## 10. From a hidden sector to a pseudorandom complete frame

A small probability of guessing all bits would be weaker than the theorem. For example, many bits might be easy even if a few are hard. The reduction instead compares complete joint distributions.

For position, retain the true momentum frame $`Z_P`$ as side information. The reduction can do this because it samples the momentum error itself. The successive experiments are:

1. Replace the physical Gaussian experiment by the negligibly close masked LWE construction.
2. Replace the LWE value by a uniform value, using the decisional LWE assumption.
3. Replace the position label by fresh uniform bits, using mask independence and its negligible parity bias.
4. Change the challenge back from uniform to LWE, while retaining those independent replacement bits.
5. Return to the physical Gaussian experiment by the smoothing estimate.

The two LWE replacements restore the original physical syndrome marginal. The result is

```math
(A,J_b,Z_Q,Z_P)
\ \approx_c\
(A,J_b,U_m,Z_P),
```

where $`U_m`$ is independent uniform and $`\approx_c`$ means indistinguishability by the permitted efficient algorithms. Statistical replacements are justified by analytical total-variation bounds; computational replacements use an assumption. These are different reasons for two experiments to look alike.

Momentum uses ordinary LWE again. Given a challenge matrix $`A_0`$, compute a basis $`N_0`$ of $`\mathrm{im}(A_0)^\perp`$ and select a uniform invertible $`V\in\mathrm{GL}_n(\mathbb F_q)`$. Publish $`A=N_0V`$. A uniform balanced subspace has a uniform balanced orthogonal complement, and multiplication by $`V`$ gives a uniform public generator basis. Thus the public matrix has exactly the required ensemble law, including its basis metadata.

For this public code, the challenge lattice is the momentum lattice with integer basis $`G_A=qH_A^{-T}`$. Place the masked challenge there and retain the sampled true position label. The same argument hides momentum. Composing the two sector comparisons gives

```math
(A,J_b,Z)
\ \approx_c\
(A,J_b,U_{2m}).
```

Retaining the other sector makes the reasoning about the entire frame explicit. The right-hand side has the same public-code and syndrome distribution as the left, with the full label replaced by independent uniform bits. This is an ensemble statement about efficient tests, not a claim of statistical independence for each fixed code and syndrome. At the benchmark logarithmic syndrome precision, an unbounded decoder can distinguish the two experiments by using the geometric recovery rule.

The hypothetical controller may use quantum computation and polynomial-time preprocessing from $`A`$. The input transformation is classical, so composing it with that controller gives a quantum polynomial-time LWE distinguisher. It supplies classical LWE samples and finite strings; it does not supply coherent samples, QRAM, or a free code-dependent trapdoor. This is the reduction direction relevant to Peikert §4.2.2: a successful algorithm for the new task would solve the assumed-hard problem.

[Full proof and quantifiers: hardness](../science/hardness.md). This connects M11–M12, M24–M25, and M30.

## 11. Why finite precision does not hide a computational resource

The exact-real expressions explain the construction, but the controller and reduction are algorithms on finite strings. Two precautions make the transition rigorous.

First, the basis is polynomially conditioned uniformly over the public ensemble:

```math
\|\mathcal B_A\|,\|\mathcal B_A^{-1}\|
\le M_n:=3n\sqrt q.
```

This keeps ordinary arithmetic errors under control. Second, floors are discontinuous: even an extremely accurate approximation can change a bit if the exact coordinate lies sufficiently close to a grid boundary. The proof therefore bounds the probability of those boundary events.

For $`a=\mathcal B_A^{-1}\xi`$, every coordinate is a Gaussian with standard deviation at least $`\sigma_n/M_n`$. Its density modulo one is bounded by

```math
F_n=1+\frac{M_n}{\sqrt{2\pi}\sigma_n}.
```

There are $`2^b`$ syndrome boundaries per unit interval. For $`0<\rho<2^{-b-1}`$, a union bound over all $`2m`$ coordinates gives

```math
\Pr\!\left[
\min_i\mathrm{dist}(a_i,2^{-b}\mathbb Z)\le\rho
\right]
\le2m\,2^{b+1}\rho F_n.
```

Choosing $`\rho`$ on the order of $`2^{-(b+n)}/(mF_n)`$ makes that probability negligible. Polynomially many working bits suffice to approximate every coordinate more accurately than $`\rho/2`$. Off the boundary event, both the finite syndrome and the integer-parity frame are exactly unchanged.

A finite Gaussian sampler is coupled to an ideal Gaussian so that their numerical values are close with overwhelming probability. The comparison is then applied to the finite outputs after boundary control. It would be false to say that a finitely supported sampler is close in total variation to the raw continuous law: their supports already distinguish them perfectly.

The masked target differs from the physical error by an integer vector in basis coordinates. Such translations preserve the grid-boundary distances, even when the translation and error are correlated. In the uniform LWE branch, the actual digital syndrome and target floor depend only on $`A,y`$ and independent Gaussian random bits, so rounding preserves the exact independence from the mask.

The controller's syndrome precision and the reduction's internal working precision serve different purposes. The benchmark needs only

```math
b=\lceil4\log_2n\rceil+O(1)
```

bits per syndrome coordinate. The reduction uses more internal bits to make numerical mistakes negligible, but gives the controller only the declared syndrome string. This does not grant extra syndrome information.

[Full proof: finite precision](../science/finite_precision.md). This resolves the interface in M14 and M26.

## 12. What the complete comparison says

The public ensemble, noise law, logical target, and syndrome precision must agree on both sides. For the principal schedule, they are

```math
m=2n,\qquad q=\Theta(n^2),\qquad
\sigma_n=n^{-1/4},\qquad
r_n^2=\frac{2q\sigma_n^2-2(\log n)^2}{4}.
```

Under the precise quantum-LWE assumption with errors $`D_{\mathbb Z,r_n}`$, the comparison is:

| Decoder or prediction task | Established behavior, averaged over the public code and physical noise |
| --- | --- |
| Unrestricted geometric decoder with the stated logarithmic syndrome precision | Exact frame success $`1-e^{-\Omega(n)}`$ |
| Uniform quantum polynomial-time decoder, including charged polynomial preprocessing | Exact frame success at most $`4^{-m}+\mathrm{negl}(n)`$ |
| Efficient prediction of an efficiently selected nonzero linear parity of the frame | Success at most $`1/2+\mathrm{negl}(n)`$ |
| Efficient output of a list of at most $`L(n)`$ candidate frames, for polynomial $`L`$ | Inclusion probability at most $`L(n)4^{-m}+\mathrm{negl}(n)`$ |

These consequences follow by efficiently checking a prediction against the label in the joint-distribution theorem. In the uniform-label experiment, the corresponding random-guess baseline is exact. For postselection, if acceptance has probability $`h_n`$ and conditional correctness is $`c_n`$, then

```math
h_nc_n\le h_n4^{-m}+\mathrm{negl}(n).
```

Thus inverse-polynomial acceptance cannot yield substantial conditional success. The bound does not justify dividing by an arbitrarily tiny acceptance probability.

The label convention also has a precise invariance. Any efficiently computed bijection of the frame labels, allowed to depend on $`A`$ and the supplied $`J_b`$, preserves uniformity and computational indistinguishability. This includes adding a known syndrome-dependent Pauli frame. An unbounded choice of reference correction could itself solve the missing decoding problem, so it is outside that efficient relabeling statement.

Several boundaries remain part of the result. It assumes ordinary LWE hardness for the explicit error law and parameter schedule. It is averaged over a public ensemble, rather than asserting hardness for every fixed code. It permits quantum computation by a controller that outputs a classical logical label, but does not prove a lower bound for every coherent recovery channel. Ideal GKP states require a separate finite-energy treatment; finite squeezing, loss, noisy syndrome extraction, and implemented recovery fidelity have not been established here. The theorem also does not imply an attack on a deployed cryptographic system or an optimal physical threshold.

The resulting connection to the selected reading is concrete. The survey's fundamental-domain language is used here to choose a GKP syndrome representative; the additional quotient by twice the lattice identifies a logical operation. Its Gaussian tools control the difference between the cryptographic and physical error laws. Its LWE formulation supplies the computational assumption. Pairing a public lattice with its dual lets those ingredients coexist with a growing geometric correction radius, even while the physical width tends to zero.

This comparison connects M15 and M27–M30. The [model](../science/model.md) is the reference for definitions, [geometry](../science/geometry.md) for recoverability, [hardness](../science/hardness.md) for the computational statement, and [interpretation](../science/interpretation.md) for physical scope. The [related-work account](../references/RELATED_WORK.md) attributes the scientific ingredients and distinguishes the present conjunction from earlier lattice, GKP, and stabilizer-decoding results. The [shared milestone map](MILESTONES.md) remains the common index for the whole argument.
