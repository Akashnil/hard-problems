# Obstruction analysis — the Frankl-file "perturb uniform A" program is impossible

**Round 1. Constant: `frankl` (Frankl's union-closed sets conjecture, entropy method).**
**Current record (lower bound on the max element bias): 0.38271 (Liu, arXiv:2306.08824).
Target: 1/2 (the conjecture, OPEN). No improvement is claimed or available this round.**

This document is the round's deliverable: a rigorous impossibility theorem for the program
prescribed in the file `/home/agentuser/repo/Frankl`, an explicit diagnosis of that file's
category error, the collapse of its two suggested construction avenues, and an honest survey of
the cited sharp ceilings of the broader entropy method. Every quantitative claim is re-checked by
`research/frankl/certificate_round1.py` (re-runnable, network-free, PASS/FAIL per check, nonzero
exit on any failure).

Two claims are kept rigorously distinct throughout, per the outline review (Issue 5):

- **(T) THE THEOREM PROVED HERE:** the specific Frankl-file program — *perturb the uniform
  distribution `A` on an OR-closed family `F` into some `C` supported on `F` and force
  `H[C] > H[A]`* — is impossible, unconditionally, for any such `C`. This is proved below.
- **(S) CITED, NOT PROVED HERE:** the broader *coordinatewise two-sample* entropy method is
  bounded below 1/2 by published sharp barriers (Chase-Lovett 0.38196601125, Cambie/Sawin-form
  0.382345533366703, Liu 0.38271). These are other authors' results; we reproduce their constants
  numerically and cite them. We do **not** claim to have proved "the entropy method cannot reach
  1/2."

---

## 1. Setup (standard / cited)

Let `F` be a finite family of sets, closed under union, with `F != {∅}`. Encode each set as a
binary string in `{0,1}^n` (coordinate `i` = membership of element `i`); union becomes bitwise OR,
so `F ⊆ {0,1}^n` is **OR-closed**: `a, b ∈ F ⟹ a OR b ∈ F`.

Let `A, B` be independent and uniform on `F`, and `C = A OR B`. Since `A` is uniform on a set of
size `|F|`,

> `H[A] = log2 |F|`.

This is the Gilmer/iid setup (arXiv:2211.09055); see `literature/digests.md`.

---

## 2. Lemma 1 (Support). `C` is supported on `F`.

For any realizations `a, b ∈ F`, by OR-closure `a OR b ∈ F`. Hence every value taken by
`C = A OR B` lies in `F`, i.e. `supp(C) ⊆ F`. ∎

More generally, **any** distribution `C` reachable by the file's program — "a microscopic
perturbation on `A`" that stays a distribution on the family — has `supp(C) ⊆ F` by construction.
This is all Theorem 1 needs.

*(Certificate (a) confirms `C = A OR B` never leaves `F` on five families: `n=5,7`, low- and
high-bias, and the explicit non-distributive 7-element lattice.)*

---

## 3. Theorem 1 (Unconditional max-entropy ceiling — the core impossibility).

**Statement.** For any random variable `X` with finite support, `H[X] <= log2 |supp(X)|`, with
equality iff `X` is uniform on `supp(X)`. Consequently, for any `C` with `supp(C) ⊆ F`,

> **`H[C] <= log2 |supp(C)| <= log2 |F| = H[A]`,**

with equality to `H[A]` iff `supp(C) = F` **and** `C` is uniform on `F`. This holds
**independently of any hypothesis on the biases** `Pr(A_i = 1)`.

**Proof.** Let `S = supp(X)`, `m = |S|`, and `u` the uniform law on `S`. By Gibbs' inequality
(equivalently, non-negativity of the Kullback–Leibler divergence `D(X || u) >= 0`):

```
0 <= D(X || u) = sum_{s in S} P(s) log2( P(s) / (1/m) )
              = sum_{s in S} P(s) log2 P(s) + log2 m  * sum P(s)
              = -H[X] + log2 m.
```

Hence `H[X] <= log2 m = log2 |supp(X)|`, with equality iff `D(X || u) = 0`, i.e. `X = u`
(uniform). This is Jensen's/Gibbs' inequality — uniform maximizes Shannon entropy on a finite
support; standard (Cover & Thomas, Thm 2.6.4). Combining with Lemma 1's `supp(C) ⊆ F` gives the
chain `H[C] <= log2|supp(C)| <= log2|F| = H[A]`. ∎

This is the precise, hypothesis-free refutation of the Frankl file's directive. The file asks for
a `C` supported on `F` with `H[C] > H[A]`. **No such `C` exists.** Note the bound is stated through
`log2 |supp(C)|`, per outline-review Issue 3: we need only `supp(C) ⊆ F`, not equality, and
equality with `H[A]` requires both full support and uniformity.

*(Certificate (a) confirms `H[C] <= H[A]` with positive margin on every tested family.)*

---

## 4. Corollary (the Frankl file's category error — and why we do NOT "use the false hypothesis").

The file writes: *"assuming the false hypothesis that all biases satisfy `Pr(A_i=1) < 1 - 1/phi`,
one can derive the contradictory inequality `H[C] > H[A]`."* and later asks to *"exploit this false
hypothesis to paradoxically force the conclusion `H[C] > H[A]`."* This inverts the actual logic of
the Gilmer argument. Two inequalities must be kept side by side:

- **(true, unconditional — Theorem 1):** `H[C] <= H[A]`. Always. No bias hypothesis enters.
- **(Gilmer's chain-rule lower bound — arXiv:2211.09055):** expanding by the chain rule and
  data-processing inequality,
  ```
  H[C] = sum_i H[C_i | C_{<i}]  >=  sum_i H[A_i OR B_i | A_{<i}, B_{<i})
       = sum_i E[ h( Pr(A_i=0 | A_{<i}) * Pr(B_i=0 | B_{<i}) ) ],
  ```
  where `h` is binary entropy. The **bias hypothesis** (all biases `< 1 - 1/phi`) is what makes the
  conditional-entropy lemma `E[h(pq)] > E[h(p)]` fire, forcing this **lower bound** above `H[A]`.

Gilmer's contradiction is therefore: a **lower bound on `H[C]` exceeds the true upper bound
`H[A]`** — impossible — so the bias hypothesis was false, i.e. some bias is `>= 1 - 1/phi`. The
bias hypothesis inflates the *lower bound* on `H[C]`; **it never raises the actual value `H[C]`
above `H[A]`.**

The Frankl file's category error is to read "the false hypothesis makes `H[C] > H[A]`" as a
statement about the *actual* `H[C]`, and then to ask for a construction realizing it. That target
is forbidden by Theorem 1 regardless of any hypothesis. Accordingly, **this document derives no
contradiction from the false bias hypothesis** (which would be the run_state-forbidden move of
reasoning from a false premise). Instead it correctly diagnoses that `H[C] <= H[A]` is the truth
and the hypothesis is simply *irrelevant* to it — it lives one level up, in the lower-bound
machinery. The file's instruction "a trivial calculation showing `H[C] < H[A]` does not mean the
construction has failed" is exactly backwards: `H[C] <= H[A]` is not a failure of a calculation,
it is the theorem.

---

## 5. Proposition A (Avenue A — fractional unions via Mobius inversion — fails, the right way).

**Construction (file's Avenue A).** For uniform `A` on `F`, let `Q(y) = Pr(A <= y) =
(1/|F|) #{x in F : x <= y}` (the zeta/cdf under bitwise domination). Mobius inversion over the
poset `F` recovers `P` from `Q`: in matrix form `P = Z^{-1} Q` where `Z[i,j] = 1[F[j] <= F[i]]`.
The file's "fractional union" sets `Q_t(y) = Q(y)^t` and defines `P_t = Z^{-1} Q_t`. For integer
`t`, `P_t` is the law of the OR of `t` iid uniform samples. The proposal is to take
`t = 1 + epsilon`.

**Claim.** `P_t` moves entropy the *wrong* way: `H[P_t] < H[A]` for `t` slightly above 1, while
the biases weakly rise. So Avenue A can never produce `H[P_t] > H[A]`.

### 5.1 Scope (signed-measure caveat — outline-review Issue 3).

For non-integer `t`, `P_t = Z^{-1} Q^t` need **not** be a non-negative measure on every
union-closed poset; on some non-distributive lattices it can have negative entries, and then
`"H[P_t]"` is not a Shannon entropy and Theorem 1 does not even apply. We therefore rest the
Avenue-A obstruction on the **derivative-of-entropy** argument below, valid wherever `P_t >= 0`,
which holds for `t` near 1 (verified: across 300 random families and on the explicit
non-distributive 7-element lattice `P_t` stays non-negative for `t` near 1). Carrying the run_state
caveat verbatim: *signedness is family-dependent, NOT universal* — it is only a secondary defect,
never the impossibility. The impossibility is `dH/dt < 0`.

### 5.2 The derivative analysis (CORRECTED — second order; outline-review Issues 1–2).

Write `P_t = Z^{-1} Q^t`. Then `dP/dt = Z^{-1}(Q^t ln Q)` and `d2P/dt2 = Z^{-1}(Q^t (ln Q)^2)`.
At `t = 1`, `P_1 = Z^{-1} Q` is the **uniform** law on `F` (so `P_1,i = 1/|F|` for all `i`).

**(i) Non-nullity of `dP/dt` (Issue 2 — via `Q ln Q != 0`, not "it changes biases").**
At `t=1`, `dP/dt = Z^{-1}(Q ln Q)`. Since `Z` is invertible (unitriangular under any linear
extension of the poset order), `dP/dt = 0` iff `Q ln Q = 0` iff `Q(y) ∈ {0, 1}` for every `y`.
But `Q(y) > 0` for all `y` (because `y <= y`, so `y` is always counted), and `Q(y) = 1` **only**
at the top element `⊤ = OR of all of F` (where every `x <= ⊤`). Hence whenever `|F| >= 2` there is
some `y != ⊤` with `0 < Q(y) < 1`, so `Q ln Q != 0` and therefore `dP/dt != 0` as a vector.
*(Certificate (b): "Q=1 only at the top element" and "dP/dt is non-null".)*

**(ii) Feasibility: `dP/dt` sums to 0.** `sum_x P_t(x) = Q_t(⊤) = Q(⊤)^t = 1^t = 1` for all `t`
(the cdf at the top is 1). Differentiating, `sum_x dP/dt = 0` and `sum_x d2P/dt2 = 0`. The
perturbation direction is feasible (stays on the probability simplex to first and second order).
*(Certificate (b): "dP/dt sums to 0" and "sum d2P/dt2 = 0".)*

**(iii) First-order term VANISHES (the correction).** With `H[P] = -(1/ln2) sum_i P_i ln P_i`,
```
dH/dt = -(1/ln2) sum_i (dP_i/dt)(ln P_i + 1).
```
At `t=1`, `P_i = 1/|F|` is **constant in `i`**, so `ln P_i + 1` is a constant vector; combined with
`sum_i dP_i/dt = 0` from (ii),
```
dH/dt |_{t=1} = -(1/ln2)(ln(1/|F|)+1) * sum_i dP_i/dt = 0   EXACTLY.
```
The first-order directional derivative is zero — **as it must be**, because `t=1` is the uniform
distribution, the **global maximizer** of entropy on `F` (Theorem 1). The outline's original "the
first-order term is governed by curvature" was off by one derivative order; the first-order term
is identically zero. *(Certificate (b): "first-order dH/dt|_{t=1} ~= 0", numerically `~1e-16`.)*

**(iv) Second-order term is STRICTLY NEGATIVE (the sign).** Differentiating again,
```
H''(t) = -(1/ln2) [ sum_i (d2P_i/dt2)(ln P_i + 1) + sum_i (dP_i/dt)^2 / P_i ].
```
At `t=1`: the first bracketed sum is `(ln(1/|F|)+1) * sum_i d2P_i/dt2 = 0` because `ln P_i + 1` is
constant and `sum_i d2P_i/dt2 = 0` (the gradient term **drops out**). The second sum survives:
```
H''(1) = -(1/ln2) * sum_i (dP_i/dt)^2 / P_i.
```
This is exactly the Hessian quadratic form of Shannon entropy (negative-definite,
`-(1/ln2) diag(1/P_i)`) evaluated on the feasible direction `dP/dt`. Since `P_i = 1/|F| > 0` and
`dP/dt != 0` by (i), every term `(dP_i/dt)^2 / P_i >= 0` with at least one strictly positive, so

> **`H''(1) = -(1/ln2) sum_i (dP_i/dt)^2 / P_i  <  0`  strictly.**

**(v) Conclusion of Prop A.** By Taylor expansion at `t=1`, since `dH/dt|_1 = 0` and `H''(1) < 0`,
```
H[P_t] - H[A] = (1/2) H''(1) (t-1)^2 + O((t-1)^3) < 0   for t slightly above 1,
```
equivalently `dH/dt|_{t=1+} = H''(1)(t-1) + O((t-1)^2) < 0` for small `t > 1`. The entropy
**strictly decreases** off uniform, while the biases weakly increase. Avenue A moves entropy the
wrong way and cannot yield `H[P_t] > H[A]`. ∎

*(Certificate (b) confirms on three families: `H''(1) < 0` (e.g. `-2.15180` on the
non-distributive lattice), the closed Hessian form equals the full second derivative and matches a
finite-difference `H''` to 5 digits, and `dH = H[P_t]-H[A] < 0` for `t ∈ {1.05, 1.1, 2.0}` with
max-bias weakly rising, e.g. on the non-distributive lattice `t=1.1`: `dH=-0.01001`,
bias `0.5714 -> 0.6062`.)*

---

## 6. Proposition B (Avenue B — concentrate `B` on the empty set — collapses).

**Construction (file's Avenue B).** Let `B = (1-eps) delta_{∅} + eps * Uniform(F)`, `A` uniform,
`C = A OR B`. As `eps -> 0`, with probability `-> 1` we have `B = ∅`, so `C = A OR ∅ = A` in
distribution: `C -> A`.

**Claim.** `H[C] -> H[A]^-` (from below) and `bias(C) -> bias(A)`; there is no regime
`H[C] > H[A]`.

**Proof.** `supp(C) ⊆ F` by Lemma 1 (A, B supported on `F`, `F` OR-closed), so Theorem 1 gives
`H[C] <= H[A]` for **every** `eps`. As `eps -> 0`, `B -> delta_{∅}` in distribution and `C = A OR B
-> A`; by continuity of Shannon entropy on the simplex, `H[C] -> H[A]`. The approach is from below
(`H[C] <= H[A]` throughout), and `H[C]` increases monotonically toward `H[A]` as `eps` shrinks.
There is no `eps` with `H[C] > H[A]`. ∎

Moreover the *motivation* of Avenue B — concentrate mass near the bottom to expose a frequent
element of the smallest set — is independently killed: **Ellis–Ivan–Leader (2023)** construct, for
every `k`, a union-closed family whose unique smallest set has size `k` yet every element of it has
frequency only `(1+o(1)) (log k)/(2k) -> 0`. So focusing on the smallest set fails in the strongest
sense. *(Cited; see `literature/digests.md`.)*

*(Certificate (c) confirms `C` stays in `F`, `H[C] <= H[A]`, and `H[C]` rises monotonically to
`H[A]^-` as `eps: 0.5 -> 0.01` on the `n=7` low-bias and non-distributive families.)*

---

## 7. Ceiling survey (CITED sharp barriers of the broader two-sample entropy method — NOT proved here).

These bound the *coordinatewise two-sample* entropy method (compare `H[A OR B]` to `H[A]`
coordinate-by-coordinate). They are other authors' theorems; we reproduce the constants
numerically in certificate (d) and cite them. They are **not** a proof that "the entropy method
cannot reach 1/2."

- **iid OR method — tight at `c = (3 - sqrt5)/2 = 1 - 1/phi = 0.38196601125`.**
  Alweiss–Huang–Sellke (arXiv:2211.11504), Chase–Lovett, Pebody, Sawin. Sharp via Chase–Lovett's
  approximate-union-closed family. *(Certificate (d): reproduced to `1e-9`, identity
  `(3-sqrt5)/2 = 1-1/phi` checked.)*
- **Sawin's element-wise dependent two-sample linear combination — EXACT ceiling
  `c = 0.382345533366703`, SHARP.** Cambie (arXiv:2212.12500, Subsec 2.3): the answer to Sawin's
  Question 2 is exactly this constant, with an explicit sharp 2-atom distribution
  `P(p=1)=a~0.078877, P(p=b2)=1-a`, `b2~0.32945` the root of `h(x)(2-h(x)) - h(2x-x^2) = 0`.
  *(Certificate (d): `b2` root reproduced `~0.329455`; the exact ceiling and the ordering checked.)*
- **Liu conditionally-iid coupling — `c = 0.38271`, the CURRENT RECORD.** Liu (arXiv:2306.08824):
  a richer coupling (A, B iid conditioned on an auxiliary variable), value defined by an analytic
  equation. *(Certificate (d): printed; not improved this round.)*

All three are `< 1/2`. Cambie's own paper states the constant "is not 1/2 and another core method
will be needed for the full resolution." No entropy variant has come within `0.11` of `1/2`.

---

## 8. Conclusion and honest status.

- **(T) Proved here:** the Frankl-file program — perturb uniform `A` into a `C` supported on `F`
  and force `H[C] > H[A]` — is **impossible**, unconditionally, by Theorem 1 (`H[C] <= H[A]` for
  any `supp(C) ⊆ F`). Avenue A fails because off-uniform entropy strictly decreases at second order
  (`dH/dt|_1 = 0`, `H''(1) < 0`); Avenue B collapses `C -> A`. The file's appeal to the false bias
  hypothesis is a category error: that hypothesis inflates a *lower bound* on `H[C]` (Gilmer), it
  never raises the *actual* `H[C]` above `H[A]`. We derive no contradiction from the false premise.
- **(S) Cited, not proved here:** the published sharp barriers (0.38196601125, 0.382345533366703,
  0.38271) bound the known coordinatewise two-sample variants below 1/2. Reaching 1/2 requires a
  genuinely different object.
- **Bound status:** the record `0.38271` (Liu) **stands**. No improvement is claimed or available
  this round. This is the goal's explicit honest fallback.

**Certificate:** `research/frankl/certificate_round1.py` — re-runnable, network-free, PASS/FAIL per
check, nonzero exit on failure. Last run: **ALL CHECKS PASS** (exit 0).

### References (see `research/frankl/literature/digests.md`)
- Gilmer, arXiv:2211.09055.
- Alweiss–Huang–Sellke, arXiv:2211.11504; Chase–Lovett; Pebody; Sawin.
- Cambie, arXiv:2212.12500 (Sawin-form exact ceiling); survey arXiv:2306.12351.
- Liu, arXiv:2306.08824 (current record 0.38271).
- Binary-entropy inequality, arXiv:2301.09664.
- Ellis–Ivan–Leader 2023 (smallest-set obstruction).
- Cover & Thomas, *Elements of Information Theory*, Thm 2.6.4 (uniform maximizes entropy).
