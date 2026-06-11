# Round 3 — Exploration of the one open gap: lemma (L)/(L') in the Avenue-A obstruction

**Constant: `frankl` (Frankl's Union-Closed Sets Conjecture, entropy method).**
**Record (lower bound on max element bias): 0.38271 (Liu, arXiv:2306.08824). Target: 1/2 (OPEN).**
**This round moves NO bound and does not re-attempt the conjecture (settled dead end, rounds 1–2).**

Scope: assess *only* the single remaining open technical gap inside the verified
Avenue-A obstruction — the family-independent nonnegativity of the fractional-union
measures `P_t` for non-integer `t >= 1`, i.e. lemma **(L)** and its Pick surrogate **(L')**.

---

## HEADLINE FINDING (new, decisive, numerically hard-verified at 50–60 digit precision)

**(L') is FALSE.** The exponent-free surrogate inequality

> (L')  `B_l(x) = sum_{y<=x} mu(y,x) Q(y)^2/(Q(y)+l) >= 0`  for all `l>0`, all `x in F`

**fails on real union-closed families.** Concrete witness: the union-closure of a random
generator set on `n=9` ground elements (reproducible: `rand_family(9, seed=1711)` in the
round-2 certificate's RNG convention, `|F| = 52`). At `l ≈ 0.127`,

> `min_x B_l(x) = -0.011219839...`  (verified to 60 significant digits with mpmath;
> `cond(Z) ≈ 129`, so this is NOT an ill-conditioning artifact).

Prevalence: B_l goes negative on **122 of 3735** union-closed families (~3.3%) in a sweep of
`n = 3..10`, all with negative minima around `l ≈ 0.08–0.11`. The failures begin at `n ≈ 8`.
**The round-2 certificate only swept `n = 3..7` (~57 families) on a coarse 10-point l-grid and
therefore never reached the regime where (L') breaks.** Round 2's claim that "(L') is certified
numerically with zero failures, margin bounded away from zero" is contradicted at modest scale.

**The actual lemma (L) STILL HOLDS.** In the same and larger sweeps (8000 families, `n` up to 11):

> `min_x P_{1+s}(x) >= +6.7e-5 > 0`  for all `s in (0,1)`,
> with the minimum pushed to `s -> 1^-` (50-digit confirmation on the worst family,
> `rand_family(10, seed=1035)`, `|F|=122`).

So **(L) is true on everything tested, but (L') — the surrogate Round 2 reduced it to — is
not.** The Pick implication `(L') => (L)` is a valid *sufficient* condition, but (L') is
*strictly stronger* than (L) and *false*. The negative mass of `B_l` sits at small `l` where
the weight `l^{s-1}` (with `s` near 1) downweights it enough that the integral
`P_{1+s} = (sin(pi s)/pi) int_0^infty B_l(x) l^{s-1} dl` stays nonnegative.

**Consequence for the program:** the round-2 reduction chain `(L) <= (L')` is *not the right
target*. Any future attempt must attack (L) directly (or find a different, *true* surrogate);
proving (L') is impossible because it is false, and disproving (L') does NOT disprove (L).
The verified round-2 deliverable is unaffected — (L)/(L') was always labelled CONJECTURAL and
is explicitly NOT part of the verified claim — but the certificate's specific assertion
"`B_l >= 0` on the sweep" is only true because the sweep was too small, and should be
corrected or relabelled (see Recommendation).

---

## 1. Analytic frameworks for proving (L) family-independently — assessment

The target to assess is now **(L): `P_{1+s} = Z^{-1}(Q^{1+s}) >= 0` for `s in (0,1)`,
every union-closed `F`** (the (L') route is dead, see Headline). Equivalently: the
column-stochastic smoothing operator `M_F` (join-convolution with the uniform law) maps the
signed fractional remainder `P_s` into the nonnegative cone, for every `F`. Candidates:

- **Total positivity / sign-regularity of the kernel `(x,y) -> mu(y,x) u^{...}`.**
  PLAUSIBLE-BUT-UNLIKELY-AS-BLACKBOX. TP would need a sign-regularity structure on the Mobius
  kernel of an arbitrary (possibly non-distributive) lattice. The §6.1 finding that individual
  `G_a(x)` terms are sign-indefinite (1165 negatives in an 11450-cell sweep) shows there is no
  termwise / single-minor positivity; only the average over `a` is nonnegative. TP theory
  (Karlin) gives positivity of *determinants/compound* quantities, not of a single averaged
  signed sum, so it does not obviously apply. The fresh fact that (L') (a per-`l` resolvent
  positivity, exactly the kind of statement TP would deliver) is FALSE is strong evidence that
  **no per-`l`/per-minor sign-regularity holds** — the positivity is genuinely an *integrated*
  (s-dependent, weight-averaged) phenomenon, not a kernel-level one. Likely a dead end.

- **Complete monotonicity in `l`.** OBSTRUCTED. The natural CM statement would be exactly
  `B_l(x) >= 0` (or that `l -> P_{1+s}` derivatives alternate). (L') being false kills the
  clean CM-in-`l` route. The function `u -> u^{1+s}` is a Bernstein/Pick function of `u`, but
  the issue is not the scalar `u^{1+s}` (whose representation we verified) — it is that
  applying `Z^{-1}` (a signed Mobius operator) does not preserve the per-`l` positivity of the
  Pick integrand. CM does not survive `Z^{-1}`.

- **Operator / matrix (Löwner) monotonicity.** OBSTRUCTED for the same root cause. `t -> Q^t`
  is operator-monotone-friendly as a *scalar* power, but `Z^{-1}(Q^{1+s})` is the image under
  a non-positive linear map. Löwner theory requires the map preserve the positive-semidefinite
  / positive cone; `Z^{-1}` does not (it maps the all-ones CDF cone to a signed measure cone).
  No version of "`Z` and `(Q+l)^{-1}` are lattice/poset operators" rescues this, precisely
  because (L') — the most operator-theoretic phrasing — is false. Dead end.

- **Pick / Nevanlinna class membership.** This is exactly the round-2 route and it produced
  the (now-falsified) (L'). The scalar Pick representation of `u^{1+s}` is correct and verified;
  the failure is that membership of the *scalar* function in the Pick class does not transfer
  positivity through `Z^{-1}`. So Pick gives a *sufficient* surrogate (L') that is too strong.
  A *refined* Pick/Stieltjes route that keeps the `s`-dependent weight `l^{s-1}` coupled to the
  sign of `B_l` (rather than demanding `B_l >= 0` pointwise) is the only Pick-flavoured hope,
  and it is essentially "prove (L) directly with an integral-sign bookkeeping" — i.e. no longer
  a black box. PARTIALLY OPEN, but hard.

- **Mobius-function sign patterns on union-closed posets.** OPEN and the most promising *native*
  framework, but no general theorem exists. The quantity is `sum_{y<=x} mu(y,x) Q(y)^{1+s}` with
  `Q` the (normalized) zeta-count of `A`. Union-closed families are exactly meet-closed under the
  dual (join-semilattices with a top), and `Q(y)` is a *monotone* function of `y`
  (`Q(y) = |{x in F: x<=y}|/|F|`). The structural lever not yet exploited: `Q` is itself a
  *rank-like / valuation-like* monotone on the lattice, and `Q^{1+s}` is a *convex increasing*
  transform of it. There may be a "Mobius inversion of a convex monotone is eventually-positive
  after one smoothing pass" statement. No citable theorem found, but this is where a real proof,
  if any, lives. OPEN — proof-shaped, not black-box.

**Net on §1:** every *black-box* framework (TP, CM-in-l, Löwner, Pick-as-stated) routes through
or implies the per-`l` positivity (L'), which is now known FALSE. So **there is no off-the-shelf
theorem that closes (L)**, and round 2's hope that one might exist is now refuted in the
strongest form: the cleanest surrogate is false. A proof of (L), if it exists, must be a native
combinatorial argument about Mobius sums of convex-monotone valuations on join-semilattices that
crucially uses the `s`-averaging, not a pointwise/operator positivity.

## 2. Is (L) even TRUE family-independently? Candidate counterexamples

- **(L) survives every test.** 8000+ families, `n` up to 11, `|F|` up to ~800, `s` swept to
  `0.99999`; min `P_{1+s} >= +6.7e-5`, always positive, at 50-digit precision on the worst case.
  No counterexample found. (L) is a *bona fide* conjecture with strong numerical support.
- **(L') is FALSE (this round).** So one must NOT conflate the two: the surrogate has explicit
  counterexamples from `n=8` up. Anyone "certifying (L')" on small families is being misled by
  the size cutoff.
- **Reason for cautious doubt about (L) at larger scale.** The (L) margin is *shrinking* and
  *concentrating at `s -> 1^-`* (min driven from `~1e-3` at `n<=7` down to `~6.7e-5` at `n=10`).
  This monotone erosion with `n`, combined with the fact that the closely-related (L') *does*
  cross zero at comparable `n`, means **(L) could plausibly fail at larger `n` / for a cleverly
  constructed adversarial lattice** (e.g. a deep distributive chain-product, or a non-distributive
  lattice engineered to put large negative Mobius mass at small `Q`). The numerics have NOT
  reached the regime where the margin would hit zero if it ever does, and the trend is the wrong
  direction. **I would not bet heavily that (L) is true; the shrinking margin is a genuine red
  flag, mirroring exactly how (L') looked positive until n=8.** This is a conjecture with a
  non-trivial chance of being false at scale.
- It does NOT matter for the verified obstruction either way: the integer-`t` ceiling
  (`H[P_m] <= H[A]`) is unconditional and is what carries the Avenue-A dead-end conclusion.
  (L) only governs the *non-integer* `t`, which is the file's `t=1+epsilon` proposal — and even
  if `P_t` went signed there, that branch is *not even a probability construction*, which is
  already an obstruction (round 2 §7(ii)). So (L) failing would not rescue the Frankl-file
  approach; it would just change the *reason* the `t=1+eps` proposal is barred.

## 3. Recommendation for round 3: (a) prove (L), (b) harden certificate, or (c) report

**Honest tractability assessment: round 3 should be (b)+(c), NOT (a).**

- **(a) Attempt the analytic proof of (L): NOT RECOMMENDED.** All black-box frameworks are
  refuted (the per-`l` surrogate (L') is false; TP/CM/Löwner/Pick-as-stated all imply it). A
  proof would require a brand-new native combinatorial lemma about `s`-averaged Mobius sums of
  convex-monotone valuations on arbitrary join-semilattices, for which no literature theorem
  exists and for which the *target itself may be false at scale* (§2 red flag). High effort,
  low probability, and — critically — **even if proven it changes NO bound and does not affect
  the verified conclusion** (the obstruction rests on the unconditional integer-`t` core). The
  ROI is essentially zero against the stated goal.

- **(b) Harden / CORRECT the numerical certificate: RECOMMENDED, and partly MANDATORY.** The
  round-2 certificate makes a now-FALSE assertion (`B_l >= 0` on the sweep "with margin bounded
  away from zero"). That assertion is only true because the sweep stopped at `n=7`. This should
  be corrected for ledger hygiene: either (i) relabel the (L') check as "holds on small families
  but is FALSE in general — explicit counterexample `rand_family(9,1711)`, `min B_l = -0.0112`",
  and (ii) replace the load-bearing numerical claim with the *actual* lemma (L)
  (`P_{1+s} >= 0`), swept to `n>=10` with the documented shrinking-margin caveat. This is honest,
  cheap, re-runnable, and *raises* the integrity of the verified artifact rather than overstating
  it. It also records a genuine new mathematical fact (the (L)/(L') separation), which is a real
  if small advance.

- **(c) Declare the work complete and report: RECOMMENDED as the primary outcome.** The user's
  question — *can the Frankl-file approach reach 1/2?* — is fully and rigorously answered NO
  (rounds 1–2, verified). The only open morsel (non-integer-`t` nonnegativity) is (i) immaterial
  to that conclusion, (ii) governed by a conjecture (L) that may itself be false at scale, and
  (iii) reduces to a surrogate (L') that this round proved false. There is nothing here whose
  resolution would move the record or change the verdict. The correct round-3 deliverable is:
  finalize the obstruction, correct the certificate's (L') overclaim, document the (L)≠(L')
  separation as a clarifying result, and report.

**One-line idea (for the outliner, not to be attempted as a proof here):** the only mathematically
honest "advance" left is to (b) *correct* the certificate and *record the new separation* `(L')
is false while (L) holds`, narrowing the open conjecture to its true form; (a) is a poor target.

---

## Reproduction
- Counterexample to (L'): `rand_family(9, seed=1711)` (round-2 RNG), `|F|=52`,
  `min_x B_l(x) = -0.01122` at `l ≈ 0.127`; verified 60-digit mpmath, `cond(Z)≈129`.
- (L') fails on 122/3735 families, `n=3..10`, onset at `n≈8`, all near `l≈0.08–0.11`.
- (L) holds: 8000+ families `n<=11`, `min P_{1+s} = +6.7e-5` at `s->1` (50-digit on worst,
  `rand_family(10,1035)`, `|F|=122`). Probe scripts: `/tmp/probe*.py` (transient; logic above
  is self-contained, uses only round-1 helpers + numpy + mpmath).

## Bottom line
- (L') (round-2 Pick surrogate) is **FALSE** — explicit, high-precision counterexample. The
  round-2 certificate missed it due to a small-`n` cutoff; correct/relabel it.
- (L) (the true lemma) holds numerically but with an **eroding margin** and a non-trivial chance
  of failing at scale — a genuine conjecture, not a near-theorem.
- No black-box analytic framework can close (L) (all imply the false (L')). A proof would be a
  hard, novel, native combinatorial lemma with zero impact on the goal.
- **Recommend (b)+(c): correct the certificate, record the (L)≠(L') separation, and report the
  complete, honest answer. Do NOT spend the round attempting (a).** Record 0.38271 (Liu) stands.
