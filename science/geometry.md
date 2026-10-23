# Geometric recovery in the same code ensemble

The computational theorem concerns the public ensemble defined in [the model](model.md). This page proves that the same ensemble has a growing correction radius. The geometric decoder may perform an unrestricted nearest-lattice-point search; no efficient algorithm is assumed in this benchmark.

Let $m=2n$, let $q$ be an efficiently specified odd prime with $q=\Theta(n^2)$, and let $A\in\mathbb F_q^{m\times n}$ be uniform conditioned on full column rank. The least prime at least $n^2$ is one concrete choice for sufficiently large $n$. Write

$$
C=\operatorname{im}A,\qquad
\Lambda_C=\{z\in\mathbb Z^m:z\bmod q\in C\},\qquad
L=q^{-1/2}\Lambda_C.
$$

The stabilizer lattice is $\Gamma=\sqrt2(L\oplus L^*)$, and its symplectic dual is $K=(L\oplus L^*)/\sqrt2$. Logical displacements are the classes in $K/(2K)$. All distances below use the dimensionless physical displacement coordinates specified in the model.

## G1. Rank conditioning and balanced subspaces

A uniform $m\times n$ matrix is rank deficient with probability at most

$$
\sum_{i=0}^{n-1}q^{i-m}
<\frac{q^{-(n+1)}}{1-q^{-1}}.
$$

To see this, reveal its columns sequentially. Once $i$ independent columns have been revealed, their span contains $q^i$ of the $q^m$ possible next columns. A union bound gives the displayed expression. With polynomial $q$ and $m=2n$, this failure probability is negligible in $n$.

Conditioning on full rank makes $C$ uniform among the $n$-dimensional subspaces of $\mathbb F_q^m$: every such subspace has the same number of ordered bases. Its orthogonal complement $C^\perp$ is also a uniform $n$-dimensional subspace. The two are correlated; the proof below does not require their independence.

For a fixed nonzero $w\in\mathbb F_q^m$, symmetry and counting give

$$
\Pr[w\in C]
=\frac{q^n-1}{q^m-1}
=\frac1{q^n+1}
\leq q^{-n}.
$$

## G2. Both primal and dual lattices have large minimum distance

**Proposition G2.** Fix any $c$ satisfying $0<c<1/\sqrt{2\pi e}$. For all sufficiently large $n$,

$$
\Pr\!\left[\min\{\lambda_1(L),\lambda_1(L^*)\}\leq c\sqrt m\right]
\leq
2\left[\sqrt{2\pi e}\left(c+\frac1{2\sqrt q}\right)\right]^m.
$$

In particular, the failure probability is $\exp[-\Omega(n)]$.

**Proof.** Put $R=c\sqrt{mq}$. Eventually $R<q$ because $m=2n$ and $q=\Theta(n^2)$. Every nonzero integer vector with norm at most $R$ then has a nonzero residue modulo $q$: a nonzero vector in $q\mathbb Z^m$ has norm at least $q$.

For each integer point in the radius-$R$ ball, place the unit cube centered on it. Their interiors are disjoint, and their union lies in the radius-$(R+\sqrt m/2)$ ball. If $V_m$ denotes the volume of the unit ball, this yields

$$
\#\{z\in\mathbb Z^m:\|z\|\leq R\}
\leq V_m(R+\sqrt m/2)^m.
$$

The bound $V_m\leq(2\pi e/m)^{m/2}$ follows, for example, by integrating $\exp(-t\|x\|^2)$ over the unit ball and all of $\mathbb R^m$, and choosing $t=m/2$. Thus the expected number of nonzero vectors of $L$ of length at most $c\sqrt m$ is at most

$$
q^{-n}V_m(c\sqrt{mq}+\sqrt m/2)^m
\leq
\left[\sqrt{2\pi e}\left(c+\frac1{2\sqrt q}\right)\right]^m.
$$

Markov's inequality bounds the probability that at least one such vector exists by this expectation. The identity

$$
L^*=q^{-1/2}\Lambda_{C^\perp}
$$

gives the same estimate for the dual, because $C^\perp$ has the same marginal distribution as $C$. A union bound proves the proposition. The quantity in square brackets is eventually bounded strictly below one. $\square$

This proof is a direct random-subspace count for the precise ensemble used by the reduction. It does not import a distance claim for a different structured lattice family.

## G3. Logical distance and the correction ball

The minimum norm in a Euclidean direct sum is the smaller of the two component minima. Consequently, on the event in G2,

$$
\lambda_1(K)
=\frac1{\sqrt2}\min\{\lambda_1(L),\lambda_1(L^*)\}
>c\sqrt{m/2}.
$$

The shortest nonzero vector of $K$ cannot lie in $2K$: otherwise half of it would be a shorter nonzero vector of $K$. Therefore

$$
d_{\rm logical}
=\min\{\|v\|:v\in K\setminus2K\}
=\lambda_1(K).
$$

Nearest-point decoding is certainly logically correct whenever the physical error $\xi$ obeys

$$
\|\xi\|<\frac{\lambda_1(K)}2.
$$

Indeed, no other point of $K$ is as close to $\xi$ as the origin in this ball. The origin is the correct lattice displacement. This sufficient condition does not claim that every larger error is uncorrectable; logical degeneracy can permit recovery beyond the ball.

The ensemble has $\det L=1$ and $\det(L\oplus L^*)=1$. Hence $\det\Gamma=2^m$, and the ideal code encodes $m$ qubits in $m$ modes. The rate statement is a count of logical dimensions in the ideal GKP model, not a finite-energy storage-rate theorem.

## G4. Independent Gaussian displacement

Let $\xi\sim N(0,\sigma_n^2 I_{2m})$, independently of $A$. There are $2m=4n$ real phase-space coordinates, and

$$
\mathbb E\|\xi\|^2=2m\sigma_n^2.
$$

For a fixed $\sigma>0$ satisfying $\sigma<c/4$, the guaranteed correction radius exceeds the typical error norm by a fixed factor. More explicitly, let

$$
h=\left(\frac{c}{4\sigma}\right)^2>1.
$$

Since $\|\xi\|^2/\sigma^2$ is chi-squared with $2m$ degrees of freedom, its moment-generating function gives

$$
\Pr\!\left[\|\xi\|\geq c\sqrt m/(2\sqrt2)\right]
\leq \exp[-m(h-1-\log h)].
$$

Combining this tail with G2 gives exponentially small failure probability, averaged over the code and noise. Allowing any $c<1/\sqrt{2\pi e}$ establishes the nonoptimized sufficient fixed-noise region

$$
0<\sigma<\frac1{4\sqrt{2\pi e}}.
$$

This number is a conservative sufficient bound in the chosen dimensionless units. It is neither a sharp threshold nor a capacity value.

For $\sigma_n=n^{-a}$ with fixed $a>0$, the result is stronger geometrically:

$$
\|\xi\|=\Theta(n^{1/2-a})\quad\text{with high probability},
\qquad
\lambda_1(K)/2=\Omega(n^{1/2}).
$$

Their ratio is $O(n^{-a})$. The probability of exceeding the guaranteed ball, conditional on a good code, is at most $\exp[-\Omega(n^{1+2a})]$ for sufficiently large $n$. Including the bad-code probability still gives total success $1-\exp[-\Omega(n)]$.

The [computational reduction](hardness.md) uses $0<a<1/2$. That restriction comes from the matched LWE and smoothing parameters, not from this geometric argument. The reference choice $a=1/4$ places typical errors at scale $n^{1/4}$ inside a correction radius of scale at least $n^{1/2}$.

## G5. Logarithmic syndrome precision is enough for the benchmark

The decoder need not receive unlimited real precision. Let $B_K=\mathcal B_A$ be the canonical polynomially conditioned basis from [the model](model.md), and write

$$
B_K^{-1}\xi=z+x,\qquad z\in\mathbb Z^{2m},\quad x\in[0,1)^{2m}.
$$

Given the $b$-bit torus index $j=\lfloor2^b x\rfloor$, put $\widehat x=2^{-b}j$ and $t_0=B_K\widehat x$. The perturbation from the exact representative is bounded by

$$
\delta_b=\|B_K\|\sqrt{2m}\,2^{-b}.
$$

An unrestricted decoder finds a nearest point $B_K k$ to $t_0$ and returns $-k\bmod2$. If

$$
\|\xi\|+\delta_b<\lambda_1(K)/2,
$$

the unique nearest point has $k=-z$, so the returned label is exactly the true logical frame $z\bmod2$.

For $q=\Theta(n^2)$, the explicit basis bound is $\|B_K\|=O(n^2)$. Thus $b=\lceil4\log_2 n\rceil+O(1)$ makes $\delta_b=O(n^{-3/2})$. Choosing a slightly smaller fixed margin in G4 preserves the same asymptotic success guarantees. The geometric benchmark and efficient-decoder lower bound therefore coexist for the same finite, logarithmic syndrome precision.

This is a digital statement about the logical label. Exact analog feedforward and finite-energy state preparation are separate physical operations; [the interpretation](interpretation.md) states the resulting scope.

## Ensemble interpretation

The public sampler produces a geometrically good code with exponentially high probability. It is not required to certify the shortest-vector bound efficiently. Conditioning the joint distribution on the good-code event changes it by at most that exponentially small probability, so the computational indistinguishability result also survives this conditioning as a distributional statement. It does not supply an efficient good-code membership test or assert hardness for every fixed code.

Continue to [the Gaussian distribution transfer](gaussian_smoothing.md), [the logical-frame reduction](hardness.md), or [physical interpretation](interpretation.md).
