# From integer LWE errors to continuous Gaussian shifts

The reduction must match the physical noise law, including its small tails. An inverse-polynomial approximation would suffice for some distinguishing statements, but it would not establish negligible logical-frame success. We therefore use two Gaussian smoothing steps with negligible statistical error. The random integer mask also has almost uniform parity, which is the hidden logical information.

This page proves all distribution estimates used in [the hardness theorem](hardness.md). The lattice and physical units are fixed in [the model](model.md). Throughout, logarithms are natural unless a base is shown, and total variation is

$$
\operatorname{TV}(P,Q)=\sup_E|P(E)-Q(E)|.
$$

For a countable law it equals one half the $\ell_1$ distance; for densities it equals one half the $L^1$ distance.

## 1. A uniform theta estimate

Define

$$
\Theta(t,c)=\sum_{k\in\mathbb Z}\exp\!\left[-\frac{(k-c)^2}{2t^2}\right],
\qquad
\delta(t)=2\sum_{\ell\ge1}\exp[-2\pi^2t^2\ell^2].
$$

The normalization of $D_{\mathbb Z,t}$ is $Z_t=\Theta(t,0)$. Poisson summation for the Gaussian gives

$$
\frac{\Theta(t,c)}{\sqrt{2\pi}\,t}
=1+2\sum_{\ell\ge1}e^{-2\pi^2t^2\ell^2}\cos(2\pi\ell c).
$$

Consequently, uniformly for every real center $c$,

$$
\left|\frac{\Theta(t,c)}{\sqrt{2\pi}\,t}-1\right|\le\delta(t).
\tag{S1}
$$

Since $\ell^2\ge1+3(\ell-1)$ for $\ell\ge1$,

$$
\delta(t)\le
\frac{2e^{-2\pi^2t^2}}{1-e^{-6\pi^2t^2}}.
\tag{S2}
$$

The estimates below use only (S1) and elementary completion of the square. Widths will grow with $n$, so all denominators containing $1-\delta(t)$ are positive for sufficiently large $n$.

## 2. Doubling an integer Gaussian and adding a mask

**Lemma S1.** Let $E\sim D_{\mathbb Z,r}$ and $U\sim D_{\mathbb Z,R}$ be independent. Put

$$
s^2=4r^2+R^2,
\qquad
v_0^2=\frac{r^2R^2}{s^2}.
$$

If $\delta(v_0)<1$, then

$$
\operatorname{TV}(2E+U,D_{\mathbb Z,s})
\le\eta_0,
\qquad
\eta_0=\frac{2\delta(v_0)}{1-\delta(v_0)}.
\tag{S3}
$$

**Proof.** For every $z\in\mathbb Z$, complete the square in the convolution sum:

$$
\begin{aligned}
\Pr[2E+U=z]
&=\frac1{Z_rZ_R}\sum_{k\in\mathbb Z}
e^{-k^2/(2r^2)-(z-2k)^2/(2R^2)}\\
&=\frac{e^{-z^2/(2s^2)}}{Z_rZ_R}\,
\Theta\!\left(v_0,\frac{2r^2z}{s^2}\right).
\end{aligned}
$$

Relative to the probability mass function of $D_{\mathbb Z,s}$, the extra theta factor is divided by its average under that same law. By (S1), both this factor and its average lie between $\sqrt{2\pi}v_0(1-\delta(v_0))$ and $\sqrt{2\pi}v_0(1+\delta(v_0))$. The resulting likelihood ratio lies between $(1-\delta(v_0))/(1+\delta(v_0))$ and its reciprocal. Its deviation from one is at most $2\delta(v_0)/(1-\delta(v_0))$. Integrating this bound proves (S3), with a harmless factor of two to spare. $\square$

The mask is not uniform over a finite interval. Its Gaussian law is what permits a negligible distribution error after addition to the doubled LWE noise.

## 3. Continuous Gaussian smoothing

**Lemma S2.** Let $V\sim D_{\mathbb Z,s}$ and $G\sim N(0,R_2^2)$ be independent. Define

$$
T^2=s^2+R_2^2,
\qquad
v_1^2=\frac{s^2R_2^2}{T^2}.
$$

If $\delta(s)<1$, then

$$
\operatorname{TV}(V+G,N(0,T^2))\le\eta_1,
\qquad
\eta_1=\frac{\delta(v_1)+\delta(s)}{1-\delta(s)}.
\tag{S4}
$$

**Proof.** If $f$ is the density of $V+G$ and $\phi_T$ is the density of $N(0,T^2)$, a second completion of the square gives

$$
\frac{f(w)}{\phi_T(w)}
=\frac{
\Theta(v_1,s^2w/T^2)/(\sqrt{2\pi}v_1)
}{
\Theta(s,0)/(\sqrt{2\pi}s)
}.
$$

By (S1), the absolute difference of this ratio from one is at most the right-hand side of (S4). Integrating establishes the stated total-variation bound. $\square$

Convolution with an independent random variable cannot increase total variation. Combining Lemmas S1 and S2 therefore gives

$$
\operatorname{TV}(2E+U+G,N(0,4r^2+R^2+R_2^2))
\le\eta_0+\eta_1.
\tag{S5}
$$

This comparison is between continuous laws after adding $G$. A finitely supported numerical sampler is never claimed to be close in total variation to an unrounded continuous Gaussian. [Finite precision](finite_precision.md) instead couples their finite digital outputs.

## 4. The mask hides its parity

**Lemma S3.** For $U\sim D_{\mathbb Z,R}$, let $\beta_R=|\mathbb E[(-1)^U]|$. Then

$$
\beta_R
\le\frac{2e^{-\pi^2R^2/2}}{1-e^{-4\pi^2R^2}}.
\tag{S6}
$$

For $m$ independent copies $U_1,\ldots,U_m$, their parity vector $\bar U\in\mathbb F_2^m$ satisfies

$$
\operatorname{TV}(\bar U,\mathcal U_m)\le\frac{m\beta_R}{2},
\qquad
\max_u\Pr[\bar U=u]\le\left(\frac{1+\beta_R}{2}\right)^m,
\tag{S7}
$$

where $\mathcal U_m$ denotes the uniform law on $m$ bits.

**Proof.** Poisson summation with the factor $(-1)^k$ gives the exact expression

$$
\mathbb E[(-1)^U]
=\frac{\sum_{\ell\in\mathbb Z}e^{-2\pi^2R^2(\ell+1/2)^2}}
{\sum_{\ell\in\mathbb Z}e^{-2\pi^2R^2\ell^2}}.
$$

The denominator is at least one. Pairing the two equal tails in the numerator and using $j(j+1)\ge2j$ for $j\ge0$ yields (S6). A single parity bit has total-variation distance $\beta_R/2$ from uniform and maximum mass $(1+\beta_R)/2$. Tensorization by a product coupling gives the first part of (S7); independence gives the second. $\square$

## 5. The matched physical parameters

**Theorem S4.** Let $m=2n$, $q=\Theta(n^2)$, $R=R_2=\log n$, and let $\sigma_n$ be either $n^{-a}$ for a fixed $0<a<1/2$, or a fixed positive constant. Set

$$
r_n^2=\frac{2q\sigma_n^2-2R^2}{4}.
$$

For all sufficiently large $n$ this is positive. Draw independent vectors

$$
E\sim D_{\mathbb Z,r_n}^{\otimes m},\quad
U\sim D_{\mathbb Z,R}^{\otimes m},\quad
G\sim N(0,R^2I_m),\quad
P\sim N(0,\sigma_n^2I_m).
$$

Then

$$
\Xi=\left(\frac{2E+U+G}{\sqrt{2q}},\ P\right)
$$

satisfies

$$
\operatorname{TV}\bigl(\Xi,N(0,\sigma_n^2I_{2m})\bigr)
\le\eta_n:=m(\eta_0+\eta_1),
\tag{S8}
$$

with $\eta_0,\eta_1$ as in (S3)–(S4). Also

$$
\operatorname{TV}(\bar U,\mathcal U_m)
\le\kappa_n:=\frac{m\beta_R}{2}.
\tag{S9}
$$

Both $\eta_n$ and $\kappa_n$ are negligible functions of $n$; more precisely, each is at most $n\exp[-\Omega((\log n)^2)]$.

**Proof.** The matched variance is exact:

$$
4r_n^2+R^2+R_2^2=2q\sigma_n^2.
$$

Thus (S5), rescaling, and the product total-variation bound establish (S8). The untouched sector $P$ already has the required independent Gaussian law. Equation (S9) is Lemma S3.

In these regimes, $r_n=\Theta(n^{1-a})$ for the power-law schedule and $r_n=\Theta(n)$ for the constant schedule. In particular, eventually $r_n\ge R$. This gives

$$
v_0\ge R/\sqrt5,\qquad s\ge2R,\qquad v_1\ge R/\sqrt2.
$$

Equations (S2) and (S6) therefore bound all errors by a polynomial factor times $\exp[-c(\log n)^2]$ for a positive constant $c$. Such functions are smaller than $n^{-d}$ for every fixed $d$ once $n$ is sufficiently large. $\square$

The restriction $a<1/2$ is convenient for the standard LWE parameter regime $r_n\gg\sqrt n$ used in this project. The smoothing calculation itself only needs the displayed widths to grow fast enough; its validity is distinct from a hardness assumption at those widths.

Gaussian theta estimates and discrete-Gaussian convolution are established tools; see, for example, [Peikert, *An Efficient and Parallel Gaussian Sampler for Lattices*](https://eprint.iacr.org/2010/088). The proofs above record the exact constants, width convention, and independent masking law required here. The next step is the [logical-frame reduction](hardness.md).
