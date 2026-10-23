# Finite syndrome precision and a digital reduction

The decoder in [the model](model.md) receives a finite string, not exact real-number access. This page proves that every reduction used in [the hardness theorem](hardness.md) can generate the required digital transcript in polynomial time, with negligible error. The proof controls the only discontinuities: the integer floors defining the logical frame and the grid boundaries defining the syndrome.

The underlying physical experiment remains the ideal independent continuous Gaussian displacement model. A digital sampler is compared with that experiment only after the finite syndrome and frame maps have been applied. A discrete approximation to a real Gaussian is not close to the unrounded Gaussian in total variation, and no such assertion is needed.

## 1. Polynomial bounds on the canonical basis

Let $m=2n$ and use the original-coordinate matrices from [the model](model.md):

$$
H_A=P^T\begin{pmatrix}I&0\\B&qI\end{pmatrix},
\qquad
G_A=P^T\begin{pmatrix}qI&-B^T\\0&I\end{pmatrix},
\qquad
\mathcal B_A=\frac1{\sqrt{2q}}\operatorname{diag}(H_A,G_A).
$$

Every entry of $B$ lies between $0$ and $q-1$, so $\|B\|\le n(q-1)$. The permutation is orthogonal. Splitting each block matrix into its diagonal and off-diagonal parts gives

$$
\|H_A\|,\|G_A\|\le2nq,
\qquad
\|H_A^{-1}\|,\|G_A^{-1}\|\le2n.
$$

For example,

$$
H_A^{-1}=\begin{pmatrix}I&0\\-B/q&I/q\end{pmatrix}P,
\qquad
G_A^{-1}=\begin{pmatrix}I/q&B^T/q\\0&I\end{pmatrix}P.
$$

It follows that the single bound

$$
\|\mathcal B_A\|,\|\mathcal B_A^{-1}\|
\le M_n:=3n\sqrt q
\tag{F1}
$$

holds for every public code in the ensemble. These are worst-case bounds over the full-rank public matrices; they do not assume that the code satisfies the distance guarantee in [geometry](geometry.md).

Finite-field elimination, row selection, and the integer and rational matrices above all have polynomial bit complexity. The only irrational lattice scale is $\sqrt{2q}$, which can be approximated to polynomially many bits in polynomial time. For $q=\Theta(n^2)$, both basis norms are $O(n^2)$.

## 2. Gaussian mass near quantization boundaries

Let $d=2m$, draw $\xi\sim N(0,\sigma_n^2I_d)$, and put $a=\mathcal B_A^{-1}\xi$. The coordinates of $a$ need not be independent. Each individual coordinate is nevertheless a centered Gaussian with standard deviation

$$
\tau_i=\sigma_n\|\text{row}_i(\mathcal B_A^{-1})\|,
\qquad
\frac{\sigma_n}{M_n}\le\tau_i\le\sigma_nM_n.
\tag{F2}
$$

The lower bound follows from the smallest singular value of $\mathcal B_A^{-1}$, which is $1/\|\mathcal B_A\|$.

**Lemma F1: a periodic density bound.** If $X\sim N(0,\tau^2)$, its density modulo one is bounded by

$$
\sup_{x\in[0,1)}\sum_{k\in\mathbb Z}\phi_\tau(x+k)
\le1+\frac1{\sqrt{2\pi}\tau},
\tag{F3}
$$

where $\phi_\tau$ is its ordinary real density.

**Proof.** Poisson summation gives the Fourier series

$$
\sum_{k\in\mathbb Z}\phi_\tau(x+k)
=1+2\sum_{\ell\ge1}e^{-2\pi^2\tau^2\ell^2}\cos(2\pi\ell x).
$$

The sum of positive terms is bounded by the corresponding Gaussian integral because the integrand decreases on the positive half-line:

$$
2\sum_{\ell\ge1}e^{-2\pi^2\tau^2\ell^2}
\le2\int_0^\infty e^{-2\pi^2\tau^2t^2}\,dt
=\frac1{\sqrt{2\pi}\tau}.
$$

This proves (F3). $\square$

For a precision $b\ge0$, all relevant discontinuities lie on the grid $2^{-b}\mathbb Z$. Integer floor boundaries are included in this grid. Define

$$
F_n=1+\frac{M_n}{\sqrt{2\pi}\sigma_n}.
$$

For any $0<\rho<2^{-(b+1)}$, each coordinate is within $\rho$ of a grid boundary with probability at most $2^{b+1}\rho F_n$. There are $2^b$ boundaries per unit period and each contributes an interval of length at most $2\rho$. A union bound, with no independence assumption, yields

$$
\Pr\!\left[\min_{1\le i\le2m}
\operatorname{dist}(a_i,2^{-b}\mathbb Z)\le\rho\right]
\le 2m\,2^{b+1}\rho F_n.
\tag{F4}
$$

This estimate is uniform in $A$. For the power-law and constant schedules in the theorem, $F_n$ is polynomial in $n$.

For example, choose any positive dyadic $\rho$ no larger than

$$
\frac{2^{-(b+n+4)}}{mF_n}.
\tag{F5}
$$

Then (F4) is at most $2^{-n-2}$. An efficiently computed polynomial upper bound on $F_n$ suffices to choose such a dyadic number; the algorithm does not need exact access to $F_n$. The number of bits needed to specify $\rho$ is

$$
O\bigl(b+n+\log(nq)+|\log\sigma_n|\bigr).
$$

If a computed approximation $\widehat a$ satisfies $\|\widehat a-a\|_\infty\le\rho/2$ and the event in (F4) does not occur, then both

$$
\lfloor\widehat a\rfloor\bmod2=\lfloor a\rfloor\bmod2
$$

and

$$
\left\lfloor2^b\bigl(\widehat a-\lfloor\widehat a\rfloor\bigr)\right\rfloor
=\left\lfloor2^b\bigl(a-\lfloor a\rfloor\bigr)\right\rfloor
\tag{F6}
$$

hold exactly. Floor computations on the rational approximation are ordinary finite arithmetic.

## 3. Sampling and arithmetic with polynomially many bits

The reduction samples an integer mask $u$, two independent continuous Gaussian vectors, and, in the dual construction, a uniform invertible finite-field matrix. All of these have bounded-time finite approximations with negligible error of the appropriate kind.

### The integer mask

For $R=\log n$, truncate $D_{\mathbb Z,R}$ to $|u|\le\lceil nR\rceil$. The omitted probability is $\exp[-\Omega(n^2)]$, by the elementary Gaussian tail bound and the normalization $Z_R\ge\sqrt{2\pi}R$. The remaining support has polynomial size. Its weights $e^{-u^2/(2R^2)}$ can be evaluated to sufficiently many bits, normalized, and sampled by a cumulative distribution using a finite uniform bit string. Approximating the probabilities to total error at most $2^{-2n}$ gives a sampler whose law is negligibly close to the exact mask. A coupling therefore makes the sampled integer mask equal to its ideal value except with negligible probability.

Sampling masks coordinatewise changes the total error by at most a factor of $m$. Their random bits are independent of those used for all other variables.

### Continuous Gaussians as coupled approximations

For any target precision $p$, one can couple a finite computation $\widehat X$ to $X\sim N(0,1)$ so that

$$
|\widehat X-X|\le2^{-p}
$$

except with probability $2^{-\Omega(n)}$, using $O(p+n)$ random bits and polynomial-time arithmetic. One explicit construction uses Box–Muller sampling from two independent ideal uniforms and evaluates the same formula on sufficiently long binary prefixes. Exclude the event that the first uniform is within $2^{-n}$ of either endpoint. This event has probability at most $2^{1-n}$; off it, the derivatives of the square-root, logarithm, and trigonometric formula are at most $2^{O(n)}$. An additional $O(n)$ input bits therefore control the output to $p$ bits. Standard algorithms evaluate these elementary functions at that precision in polynomial time.

This is a coupling bound on numerical error, not total-variation closeness of an unrounded discrete and continuous law. Scaling by the polynomially bounded widths $R$ and $\sigma_n$, and taking a union bound over the polynomial number of coordinates, preserves negligible failure. Off the excluded tail event, every sampled coordinate has polynomial magnitude.

### Arithmetic in the masked target

For the position-sector target

$$
t=\left((y+g)/\sqrt{2q},p\right),
$$

the coordinates to be quantized simplify to

$$
\mathcal B_A^{-1}t
=\left(H_A^{-1}(y+g),\ \sqrt{2q}\,G_A^{-1}p\right).
\tag{F7}
$$

The momentum-sector target has the analogous formula with the sectors interchanged. The finite vector $y$ has entries in $\{0,\ldots,q-1\}$. By (F1), approximating the Gaussian draws and arithmetic to a polynomial factor more precision than $\rho$ ensures that (F7) is computed within $\rho/2$ in every coordinate, except with negligible sampling probability. The needed working precision is polynomial in $n$ and $b$; one may take $b+O(n+\log(nq)+|\log\sigma_n|)$ fractional bits with sufficiently large fixed constants.

The integer components of the computed floors also have polynomial bit length. All reductions use exact finite-field arithmetic for $y$, exact binary arithmetic for mask parity, and a separately computed approximation to (F7). In particular, the computation of the approximate syndrome and floor vector depends only on $A$, $y$, and the Gaussian random bits. It never consults $u$ again until adding the known parity offset to the candidate frame.

### Public basis randomization

In the dual reduction, a uniform matrix in $\mathrm{GL}_n(\mathbb F_q)$ is obtained by sampling uniform $n\times n$ matrices until one is invertible. The success probability per attempt is

$$
\prod_{i=1}^n(1-q^{-i})\ge1-\sum_{i=1}^nq^{-i}>1/2
$$

for the odd moduli under consideration. Truncating after $2n$ attempts therefore introduces failure probability at most $2^{-2n}$. Conditional on success, the resulting invertible matrix is exactly uniform. A fixed output on failure changes the overall law negligibly.

## 4. Why the rounding argument survives the LWE embedding

In the LWE branch of the position-sector reduction, the target has the exact decomposition

$$
t=v+\Xi,\qquad v\in K_A,
$$

where $\Xi$ is the smoothed error of Theorem S4. If $k_v=\mathcal B_A^{-1}v\in\mathbb Z^{2m}$, then

$$
\mathcal B_A^{-1}t=k_v+\mathcal B_A^{-1}\Xi.
$$

Translation by an integer preserves distances to $2^{-b}\mathbb Z$, the torus index, and the relation between the two integer floors. This statement holds even though $v$ is correlated with the error and mask. No conditional independence of $v$ and $\Xi$ is used.

Couple $\Xi$ to a physical Gaussian $\xi$ that remains independent of $A$, so that $\Xi=\xi$ except with probability at most $\eta_n$; this is possible by the total-variation estimate in Theorem S4, uniformly in the independent public code. On equality, the boundary bound (F4) applies to the target through the integer translation above. Combine this coupling with the numerical couplings from Section 3. Outside an event of probability at most

$$
\eta_n+\operatorname{negl}(n),
\tag{F8}
$$

the finite simulator's syndrome and computed labels agree exactly with the desired physical Gaussian transcript. The same reasoning applies to the dual momentum construction, including the independently sampled true label in the other sector.

In the uniform challenge branch, a separate continuous boundary estimate is unnecessary. For every integer mask value, the vector $y=(2\mathbf b+u)\bmod q$ is uniform and independent of $u$. The finite syndrome and approximate floor are functions of $A,y$ and independent Gaussian random bits. Thus they remain independent of $u$ in precisely the conditioning used by Lemma H3. Adding the affine mask-parity offset hides the chosen logical sector up to $\kappa_n$ and the negligible mask-sampling error. Numerical rounding does not introduce a dependency on the hidden mask.

This distinction is useful: the LWE branch is coupled to the physical task, while the uniform branch is handled by exact algebraic independence in the actual finite implementation.

## 5. Finite-input simulation theorem

**Theorem F2.** Fix a polynomially bounded precision $b(n)$ and one of the efficiently computable noise schedules in Theorem H1. There is a bounded-time classical polynomial-time simulator for each of the two sector reductions with the following properties:

1. On an LWE challenge conditioned on full-rank matrix, its joint public-code, syndrome, and frame transcript is within $\eta_n+\operatorname{negl}(n)$ in total variation of the specified physical Gaussian transcript. Replacing the selected frame sector by fresh independent uniform bits gives the corresponding statement with that sector replaced.
2. On a uniform challenge, the computed selected-sector frame is within $\kappa_n+\operatorname{negl}(n)$ of uniform independently of the supplied public code, syndrome, and retained other-sector label.
3. All output strings, random bit counts, arithmetic precision, and runtime are polynomial in $n$ and $b$.

**Proof.** Sections 1–3 provide bounded-time sampling and arithmetic. Section 2 provides a negligible bound on unstable quantization boundaries at the chosen working precision. Section 4 combines these facts with the smoothed-error coupling in the LWE branch and exact mask independence in the uniform branch. The finite-field matrix constructions are exact conditional on their negligible abort event. A union bound over these events proves the stated errors. $\square$

The negligible full-rank conditioning loss is accounted for separately in Theorem H1. A distinguisher for a conditioned challenge yields one for the ordinary challenge by testing rank and using an input-independent output on rank deficiency. The deficiency probability is negligible, and rank testing is efficient.

Theorem F2 supplies the finite implementation term in the four-hybrid bound (H2). The auxiliary simulator is classical; composing it with a quantum polynomial-time decoding test remains quantum polynomial time. The reduction therefore assumes no real-RAM arithmetic, oracle for exact Gaussian reals, or free data-loading primitive.

## 6. Precision of the unconstrained geometric benchmark

The computational reduction allows any polynomially many syndrome bits. The matching geometric benchmark needs only logarithmically many. Specifically, for $\widehat x=2^{-b}J$,

$$
\|\mathcal B_A(x-\widehat x)\|
\le\|\mathcal B_A\|\sqrt{2m}\,2^{-b}.
$$

Since $\|\mathcal B_A\|=O(n^2)$, taking

$$
b=\lceil4\log_2n\rceil+O(1)
$$

makes this error $O(n^{-3/2})$. [Section G5](geometry.md#g5-logarithmic-syndrome-precision-is-enough-for-the-benchmark) proves that an unrestricted nearest-point search on that quantized representative returns the exact logical frame with the stated high probability.

This result concerns which logical class to choose. It does not turn finite syndrome precision into exact analogue feedforward, nor does it supply an energy envelope, a finite-squeezing model, or a physical syndrome-extraction circuit. Those questions require additional estimates beyond the ideal model, as explained in [the interpretation](interpretation.md).
