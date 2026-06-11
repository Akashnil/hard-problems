# Round 2 — Global upgrade of the Avenue-A obstruction (Frankl-file entropy approach)

**Constant: `frankl` (Frankl's Union-Closed Sets Conjecture, entropy method).**
**Current record (lower bound on the max element bias): 0.38271 (Liu, arXiv:2306.08824).
Target: 1/2 (the conjecture, OPEN). No bound is moved this round; the record stands.**

This document upgrades the round-1 Avenue-A obstruction from a **local** second-order
statement (`dH/dt|_1 = 0`, `H''(1) < 0`, verified on small families near `t = 1`) to a
**global, family-independent** statement: for the entire fractional-union family
`P_t = Z^{-1} Q^t`, wherever `P_t` is a genuine probability distribution, Theorem 1 of
round 1 gives `H[P_t] <= H[A]` *unconditionally, for every union-closed family and every
`t`, with no derivative, no curvature, and no small-`n` numerics*. The only thing standing
between this and an unconditional all-`t` theorem is the nonnegativity of `P_t` for real
`t >= 1`.

**Honest status, stated up front (this is an Angle-3 deliverable per the approved
outline):**

- **PROVEN, unconditionally:** (i) the integer-`t` core — for every integer `m >= 1`,
  `P_m` is the genuine law of `A_1 OR ... OR A_m` (`m` iid uniform copies), hence a bona
  fide distribution, hence `H[P_m] <= H[A]` for **every** union-closed family with no
  conjecture; (ii) the exact additivity / join-convolution identity
  `P_{a+b} = P_a (*) P_b`; (iii) the **single-lemma reduction** — the all-real-`t >= 1`
  nonnegativity is *equivalent* to one inequality, the base-case lemma
  `(P_1 (*) P_s)(x) >= 0` for `s in [0,1)`; (iv) a genuine analytic **reduction of that
  lemma** to a rational, exponent-free inequality `B_l(x) >= 0` for all `l > 0` via the
  Pick/Stieltjes representation of `u^{1+s}`.
- **CERTIFIED NUMERICALLY BUT NOT PROVEN (conjecture):** the base-case lemma itself —
  equivalently `B_l(x) >= 0` for all `l > 0` on **every** union-closed lattice including
  non-distributive ones. Verified with zero failures across ~57 families (n = 3..7) and a
  dense `s`- and `l`-grid, margin bounded away from zero, but **a finite enumeration cannot
  settle a for-all-`t`, for-all-`F` claim**, and I did not find a closed family-independent
  derivation within budget. It is presented as a conjecture, never as a theorem.

Two claims are kept rigorously distinct throughout (round-1 guard, run_state Rule):

- **(T) SELF-PROVEN HERE:** the specific Frankl-file program — perturb the uniform law `A`
  on an OR-closed family `F` into a `C` supported on `F` and force `H[C] > H[A]` — is
  impossible. Round-1 Theorem 1 settles it; this round globalizes the Avenue-A instance.
- **(S) CITED, NOT PROVED HERE:** the broader coordinatewise two-sample entropy method is
  capped below 1/2 by published sharp barriers (Chase–Lovett 0.38196601125, Cambie/Sawin
  0.382345533366703, Liu 0.38271). Those are other authors' results; we reproduce the
  constants numerically and cite them. We do **not** claim to have proved "the entropy
  method cannot reach 1/2."

Every quantitative claim below is re-checked by `research/frankl/certificate_round2.py`
(re-runnable, network-free, PASS/FAIL per check, nonzero exit on any failure; it reuses the
round-1 helpers and does not duplicate or break round-1's own checks in
`certificate_round1.py`).

---

## 1. Setup (round 1, cited)

`F` is a finite union-closed family, `F != {∅}`, encoded OR-closed in `{0,1}^n` (union =
bitwise OR). `A` is uniform on `F`, so `H[A] = log2 |F|`. Domination order `x <= y` is
bitwise. Define the domination-CDF of `A`,

> `Q(y) = Pr(A <= y) = (1/|F|) #{x in F : x <= y}`,

the zeta vector. With the zeta matrix `Z[i,j] = 1[F[j] <= F[i]]` (unitriangular under any
linear extension, hence invertible), Mobius inversion gives `P = Z^{-1} Q`, and the
Frankl-file "fractional union" is

> `P_t := Z^{-1} Q^t`, i.e. `P_t(x) = sum_{y <= x} mu(y, x) Q(y)^t`,

where `mu` is the Mobius function of the poset `F`. `P_1 = Z^{-1} Q` is the **uniform** law
on `F` (certificate (b), round 1; re-checked here). Note `Z P_s = Q^s` by definition: **the
cumulative of `P_s` along the order is exactly `Q^s`** — used repeatedly below.

---

## 2. Theorem 1 (round 1, cited): the unconditional max-entropy ceiling

For any random variable `X` with finite support, `H[X] <= log2 |supp(X)|`, equality iff
`X` is uniform on its support (Gibbs / `D(X || uniform) >= 0`; Cover–Thomas Thm 2.6.4).
Hence for any `C` with `supp(C) ⊆ F`,

> **`H[C] <= log2 |supp(C)| <= log2 |F| = H[A]`,** hypothesis-free,

with equality iff `supp(C) = F` and `C` is uniform. (Full proof: round 1, §3.)

**Corollary (the entire round-2 entropy content, one line).** *The instant `P_t` is a
genuine probability distribution supported on `F`, Theorem 1 gives `H[P_t] <= H[A]` —
for every family and every such `t`, with equality iff `P_t = uniform`, i.e. `t = 1`.* No
derivative, no curvature, no small-`n` numerics enter. The round-1 `dH/dt|_1 = 0`,
`H''(1) < 0` calculation is retained only as a *local shadow* / consistency check (the
entropy margin `H[A] - H[P_t]` vanishes quadratically as `t -> 1+`; certificate R2-6).

So the global obstruction reduces to one question: **for which `t` is `P_t` a genuine
distribution?** Sections 3–6 answer it.

---

## 3. Integer anchor (PROVEN, unconditional)

**Proposition 3.1.** For every integer `m >= 1`, `P_m = Z^{-1} Q^m` is exactly the law of
`A_1 OR ... OR A_m`, where `A_1, ..., A_m` are iid uniform on `F`. In particular `P_m` is a
genuine probability distribution on `F`.

*Proof.* For iid uniform `A_1, ..., A_m`, the join `M = A_1 OR ... OR A_m` satisfies
`M <= y` iff every `A_i <= y`, so `Pr(M <= y) = Pr(A <= y)^m = Q(y)^m`. The map "pmf ↦
domination-CDF" is left-multiplication by `Z`; it is a bijection with inverse `Z^{-1}`
(Mobius inversion). Hence the pmf of `M` is `Z^{-1}(Q^m) = P_m`. Being the law of an
explicit `F`-valued random variable, `P_m >= 0` and sums to 1. ∎

**Corollary 3.2 (unconditional global statement at every integer `t`).** By Proposition 3.1
and Theorem 1, `H[P_m] <= H[A]` for **every** union-closed family and **every** integer
`m >= 1`, with no conjecture. The Frankl-file's "union of `t` independent samples" is, at
every integer `t`, a bona fide distribution that obeys the ceiling.

*Certificate R2-3: `Z^{-1} Q^m` equals the brute-force OR-of-`m` law (`np.allclose`) for
`m = 2,3,4` on the non-distributive 7-element lattice and many random families; the
brute-force law is nonnegative and sums to 1 by construction.*

---

## 4. Additivity / join-convolution identity (PROVEN, exact)

Define the **join-convolution** of two real vectors `mu, nu` indexed by `F`:

> `(mu (*) nu)(z) = sum_{x | y = z} mu(x) nu(y)`.

**Proposition 4.1.** For all real `a, b`, `P_{a+b} = P_a (*) P_b`.

*Proof.* `Q^{a+b} = Q^a · Q^b` entrywise. The key fact is that left-multiplication by `Z`
(taking a measure to its domination-CDF) turns join-convolution into the *entrywise*
product of CDFs: if `R = mu (*) nu`, then for every `z`,
`(ZR)(z) = sum_{w <= z} R(w) = sum_{w <= z} sum_{x|y=w} mu(x) nu(y)
= sum_{x|y <= z} mu(x) nu(y) = sum_{x <= z} sum_{y <= z} mu(x) nu(y)
= (Z mu)(z) · (Z nu)(z)`,
using `x | y <= z  iff  x <= z and y <= z`. Apply this with `mu = P_a`, `nu = P_b`:
`Z(P_a (*) P_b) = (Z P_a)(Z P_b) = Q^a Q^b = Q^{a+b} = Z P_{a+b}`. Since `Z` is invertible,
`P_a (*) P_b = P_{a+b}`. ∎

In matrix form, convolving with the uniform measure `P_1` is left-multiplication by the
operator

> `M_F[z, y] = (1/|F|) #{x in F : x | y = z}`,

i.e. `M_F · P_s = P_1 (*) P_s = P_{1+s}`. `M_F` has **nonnegative entries** and **every
column sums to exactly 1** (for fixed `y`, `x | y` ranges over `F` as `x` does, so the
column counts a partition of `F` weighted by `1/|F|`): `M_F` is column-stochastic and maps
the probability simplex into itself.

*Certificate R2-1 (`P_{a+b} == P_a (*) P_b` for 8 pairs `(a,b)` across 20 families) and
R2-2 (`M_F` column-stochastic, nonnegative, `M_F P_s == P_{1+s}`).*

---

## 5. The single-lemma reduction (PROVEN) and the cutoff `t >= 1`

**Proposition 5.1 (reduction).** The statement "`P_t >= 0` for all real `t >= 1` on a fixed
union-closed `F`" is **equivalent** to the single base-case inequality

> **(L)  `(P_1 (*) P_s)(x) >= 0` for all `s in [0,1)` and all `x in F`.**

*Proof.* (⇐) Assume (L). Write `t = m + s` with integer `m = floor(t) >= 1` and
`s = t - m in [0,1)`.
- If `s = 0`, `P_t = P_m >= 0` by Proposition 3.1.
- If `s > 0`: by Proposition 4.1, `P_{1+s} = P_1 (*) P_s >= 0` by (L), and it sums to 1, so
  `P_{1+s}` is a genuine distribution. Now induct on `k >= 1`: `P_{k+s} = P_1 (*) P_{(k-1)+s}`
  is the join-convolution of the nonnegative measure `P_1` (uniform) with the nonnegative
  measure `P_{(k-1)+s}` (induction hypothesis); a join-convolution of two nonnegative
  measures is nonnegative (every term `mu(x) nu(y) >= 0`), and sums to
  `(sum mu)(sum nu) = 1`. Hence `P_{k+s} >= 0` for all `k >= 1`, i.e. `P_t >= 0` for all
  `t >= 1`.

(⇒) If `P_t >= 0` for all `t >= 1`, then in particular `P_{1+s} = P_1 (*) P_s >= 0` for all
`s in [0,1)`, which is (L). ∎

So the *entire* all-real-`t >= 1` nonnegativity collapses to **one** inequality (L) on the
fractional shell `t in [1,2)`; the integer steps `t -> t+1` are then nonnegativity-for-free
(convolution of two nonnegative measures). This is the reviewer's suggested reduction, and
it is rigorous.

**Why `t >= 1` is exactly the cutoff (not `t > 0`).** The fractional remainder `P_s` for
`s in (0,1)` is in general a **signed** measure (`P_0.3.min() = -0.0231` on the
non-distributive lattice). So `Q` is *not* generally max-infinite-divisible, and the
classical Balkema–Resnick / max-inf-div characterizations do **not** apply as a black box
(this was the round-1-review Issue-2 warning, and it is respected here: we do not invoke
them). The cutoff arises structurally: one factor of `P_1` — one full smoothing pass by the
column-stochastic `M_F` — is what lifts the signed remainder into the cone. `t >= 1`
guarantees at least one such pass; `t < 1` has none. Branch `t < 1` is the WRONG direction
for the conjecture anyway (it lowers the bias), and where `P_t` is signed, `"H[P_t]"` is not
a Shannon entropy and the construction is not even probabilistic.

*Certificate R2-4 (base lemma (L) on a dense `s`-grid, ~57 families, min `+1.6e-3`; step
lemma "nonneg (*) nonneg = nonneg" structurally) and R2-5 (non-vacuity of the signed
`t < 1` branch: 32/57 families signed for some `s < 1`; largest observed signed `t < 1`).*

---

## 6. Status of lemma (L): genuine analytic reduction, but NOT closed (conjecture)

Lemma (L) is the one open analytic step. I made real progress on it and report exactly how
far it goes; **I do not present it as proven.**

### 6.1 A clean probabilistic form

Expanding `M_F`, for `a <= x` set `G_a(x) = sum_{y : a | y = x} P_s(y)` (the `P_s`-measure
of the join-preimage of `x` under `a`). Then

> `(P_1 (*) P_s)(x) = (1/|F|) sum_{a in F} G_a(x)`,  and  `G_a(x) = sum_{a <= x' <= x} mu(x', x) Q(x')^s`,

(the second identity because `sum_{y : a|y <= x'} P_s(y) = sum_{y <= x'} P_s(y) = Q^s(x')`
for `a <= x'`, then Mobius-invert over the interval `[a, x]`). Two facts are immediate and
worth recording:

- The `a = x` term is `G_x(x) = Q^s(x) > 0` (a positive CDF power): there is always a
  strictly positive contribution.
- Individual `G_a(x)` **can be negative** (verified: 1165 negatives in a 11450-cell sweep);
  only the average over `a` is provably nonnegative. **So (L) is genuinely a smoothing
  statement, not a term-by-term one** — confirming the outline-review finding that `M_F`
  does not map arbitrary signed vectors into the cone (it maps ~76% of random signed
  vectors to a negative vector), and that the *specificity* of `P_s` is essential.

### 6.2 The Pick/Stieltjes reduction (PROVEN reduction, to an exponent-free inequality)

Using `Z P_s = Q^s` we have `P_{1+s}(x) = sum_{y <= x} mu(y, x) Q(y)^{1+s}`. The function
`u ↦ u^{1+s}` (for `s in (0,1)`) admits the Stieltjes/Pick representation, valid for all
`u > 0`:

> `u^{1+s} = (sin(pi s)/pi) * int_0^inf  u^2 / (u + l) * l^{s-1} dl`

(standard: from `u^s = (sin(pi s)/pi) int_0^inf u/(u+l) l^{s-1} dl`, multiply by `u`;
convergence holds since the integrand is `~u l^{s-1}` at `l -> 0` and `~u^2 l^{s-2}` at
`l -> inf`, both integrable for `s in (0,1)`; substituting `l = u m` gives
`u^{1+s} int_0^inf m^{s-1}/(1+m) dm = u^{1+s} · pi/sin(pi s)`). Substituting into `P_{1+s}`
and exchanging the finite Mobius sum with the integral,

> `P_{1+s}(x) = (sin(pi s)/pi) int_0^inf B_l(x) · l^{s-1} dl`,  where
> `B_l(x) = sum_{y <= x} mu(y, x) Q(y)^2 / (Q(y) + l)`.

Since `sin(pi s)/pi > 0` and `l^{s-1} > 0`, **(L) for all `s in (0,1)` would FOLLOW from the
single, exponent-free family of inequalities**

> **(L')  `B_l(x) >= 0` for all `l > 0` and all `x in F`.**

This is genuine progress: (L') removes the exponent `s` entirely and replaces a continuum of
power inequalities with one rational-function inequality. The boundary cases are clean
(`x = bottom` gives `B_l = Q(0)^2/(Q(0)+l) > 0`; for non-bottom `x` the constant term of the
partial-fraction expansion drops by `sum_{y<=x} mu(y,x) = 0`, leaving
`B_l(x) = P_1(x) + l^2 sum_{y<=x} mu(y,x)/(Q(y)+l)`).

### 6.3 The remaining gap (honest)

I did **not** close (L'). The residual term `sum_{y<=x} mu(y,x)/(Q(y)+l)` is itself a
sign-indefinite Mobius/resolvent sum on an arbitrary (possibly non-distributive) lattice,
and I found no family-independent reason it must dominate correctly. There is no black-box
theorem available here (the `t >= 1` vs `t > 0` cutoff, §5, shows `Q` is not max-inf-div, so
the standard positivity theorems do not apply). **(L') / (L) is therefore a CONJECTURE,
supported by:** zero failures of `B_l(x) >= 0` across ~57 families and a 10-point `l`-grid
(min `+2.7e-5`), and zero failures of `(P_1 (*) P_s)(x) >= 0` across the same families on a
dense `s`-grid (min `+1.6e-3`); both bounded away from zero, not on a knife edge. **But a
finite enumeration cannot settle a for-all-`l`, for-all-`F` claim**, and I will not dress it
as a theorem.

*Certificate R2-7: the Pick representation is verified numerically
(`P_{1+s} = (sin/pi) int B_l l^{s-1} dl` to integration tolerance on the non-distributive
lattice via a log-spaced quadrature), and `B_l(x) >= 0` is verified on the sweep. The check
is non-vacuous: replacing the `Q^2` numerator by `Q^1` (the wrong exponent) produces 111
negative-`B_l` events, so the certificate genuinely tests the inequality.*

---

## 7. The global Avenue-A dichotomy (the round-2 statement)

Assembling §§2–6, for every union-closed family `F` and every real `t`:

- **(i) `t >= 1`, integer or, conditionally on lemma (L), any real `t >= 1`:** `P_t` is a
  genuine probability distribution on `F`, so by Theorem 1
  **`H[P_t] <= H[A]`, unconditionally and family-independently**, with equality iff `t = 1`
  (uniform). *Unconditional at every integer `t` (Prop 3.1). For non-integer `t >= 1`,
  conditional on (L) — which is certified numerically but unproven.*
- **(ii) `t < 1`:** `P_t` may be a **signed** measure (non-vacuous: many families;
  largest observed signed `t < 1` below 1), in which case `"H[P_t]"` is not a Shannon
  entropy and Avenue A is **not even a probabilistic construction**. This branch is also the
  wrong direction (it lowers the bias, away from `>= 1/2`).

Either way, the Frankl-file's `t = 1 + epsilon` proposal lands in branch (i): a bona fide
distribution with `H[P_t] <= H[A]`. **Avenue A cannot produce `H[P_t] > H[A]`.** The
round-1 caveat ("we rest the obstruction on the local `dH/dt` argument valid only where
`P_t >= 0` near `t = 1`") is replaced by: *wherever `P_t` is a distribution, the ceiling is
global and exact; the only open point is the universally-quantified nonnegativity for
non-integer `t`, which is the single reduced lemma (L), proven only at integer `t`.*

**This globalizes the obstruction without moving any numeric bound.** The record `0.38271`
(Liu) is unchanged; no "perturb uniform `A`" entropy scheme can move it (round 1, Theorem 1).

---

## 8. PLAIN-LANGUAGE VERDICT — can Frankl's conjecture be solved via the Frankl-file approach?

*(Consolidating rounds 1 and 2. This section answers the user's actual question directly.)*

**Short answer: No.** The Frankl-file approach asks you to take the uniform distribution `A`
on the family and *perturb* it into a new distribution `C` (living on the same family) whose
entropy is *higher* — `H[C] > H[A]` — to manufacture a contradiction with the false
assumption "no element is in half the sets." That target is impossible for a structural
reason that has nothing to do with the false assumption:

1. **Uniform already has the most entropy possible.** Among all distributions supported on
   a finite set, the uniform one has the strictly largest Shannon entropy (a textbook fact).
   The family `F` is a finite set, `A` is uniform on it, and any `C` the program builds still
   lives on `F`. So `H[C] <= H[A]` **always**, with equality only when `C` is uniform again.
   Every in-family perturbation pushes entropy **down**, never up. (Round 1, Theorem 1 —
   self-proven, hypothesis-free.)

2. **The file's own Avenue A confirms it, now globally.** Avenue A's "fractional union"
   `P_t` is, for every whole number of samples `t = 1, 2, 3, ...`, exactly the distribution
   of the OR of `t` independent uniform draws — a perfectly ordinary distribution, which
   therefore has entropy `<= H[A]` with **no exceptions, on every family** (proven this
   round). For fractional `t` just above 1 — the file's actual proposal — `P_t` is again a
   genuine distribution (overwhelmingly supported numerically; reducible to one clean
   inequality we verified on ~57 families but did not fully prove in general), and it too
   obeys `H[P_t] <= H[A]`. For `t < 1` it stops being a probability distribution at all
   (it goes negative), so there is nothing to maximize. Avenue B (concentrating mass on the
   empty set) simply collapses `C` back to `A`. **Every avenue the file suggests moves
   entropy the wrong way or off the table.**

3. **The file's "exploit the false hypothesis" instruction is a category error.** In
   Gilmer's real proof, the false bias assumption inflates a *lower bound* on `H[C]` until it
   exceeds the true ceiling `H[A]` — *that* is the contradiction, and it forces the
   assumption to be false. The assumption never makes the *actual* entropy `H[C]` exceed
   `H[A]`. Asking for a construction that realizes `H[C] > H[A]` misreads which quantity the
   hypothesis touches. We derive nothing from the false premise (and must not); we show the
   target it asks for is forbidden outright.

4. **The broader entropy method is separately capped well below 1/2** — by other authors'
   sharp results, not ours: the coordinatewise two-sample method tops out around
   `0.382` (iid OR is tight at `1 - 1/phi = 0.38197`; Sawin's dependent two-sample at
   `0.38235`; Liu's coupling at the current record `0.38271`). Reaching `1/2` provably needs
   a genuinely different object than "compare `H[A OR B]` to `H[A]`." *(Cited, not proved
   here; constants reproduced numerically.)*

So the specific program in the Frankl file is a **provable dead end** for reaching `1/2`:
its core move is mathematically impossible (self-proven), and the wider entropy family it
belongs to is capped near `0.382` by the literature. The honest, verified deliverable of
this work is the **obstruction**, now in global form — not a proof of `1/2`, and not an
improvement on the record.

---

## 9. Conclusion and honest status

- **(T) Proven here, unconditionally:** the Frankl-file program (perturb uniform `A` into
  `C` on `F` with `H[C] > H[A]`) is impossible (Theorem 1); Avenue A's `P_t` is, at every
  integer `t`, a genuine distribution obeying `H[P_t] <= H[A]` on every family; the
  additivity identity `P_{a+b} = P_a (*) P_b` and the single-lemma reduction
  (all-`t >= 1` nonnegativity ⇔ lemma (L)) hold exactly; lemma (L) reduces analytically to
  the exponent-free inequality (L') via the Pick representation.
- **(Conjecture, certified-but-unproven):** lemma (L) / (L') — `(P_1 (*) P_s)(x) >= 0` for
  `s in [0,1)` (equiv. `B_l(x) >= 0` for `l > 0`) on **every** union-closed family. Zero
  numerical failures with positive margin, but no family-independent analytic proof. Hence
  the *all-real-`t >= 1`* global ceiling is conditional on (L); the *integer-`t`* global
  ceiling is unconditional.
- **(S) Cited, not proved here:** the published sharp barriers (0.38196601125,
  0.382345533366703, 0.38271) cap the known two-sample variants below 1/2.
- **Bound status:** the record `0.38271` (Liu) **stands**. No improvement is claimed or
  available; this is the goal's explicit honest fallback, now upgraded from a local to a
  (largely) global obstruction.

**Certificate:** `research/frankl/certificate_round2.py` — re-runnable, network-free,
PASS/FAIL per check, nonzero exit on failure; reuses round-1 helpers without breaking
`certificate_round1.py`. Last run: **ALL CHECKS PASS** (exit 0).

### References (see `research/frankl/literature/digests.md`)
- Gilmer, arXiv:2211.09055.
- Alweiss–Huang–Sellke, arXiv:2211.11504; Chase–Lovett; Pebody; Sawin.
- Cambie, arXiv:2212.12500 (Sawin-form exact ceiling); survey arXiv:2306.12351.
- Liu, arXiv:2306.08824 (current record 0.38271).
- Cover & Thomas, *Elements of Information Theory*, Thm 2.6.4 (uniform maximizes entropy).
- Stanley, *Enumerative Combinatorics* Vol. 1, Ch. 3 (Mobius inversion on posets / zeta).
- Stieltjes/Pick representation of `u^a`, `a in (0,1)` (e.g. Bhatia, *Matrix Analysis*, Ch. V).
