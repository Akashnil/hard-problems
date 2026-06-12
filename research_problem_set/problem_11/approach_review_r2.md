# Approach review — Round 2 (problem_11): closing Lemma B3

Verdict: **CHANGES REQUESTED**

Angle reviewed: Angle 1 (mass-concentration close of B3) as primary; Angle 2 (k=2 squared-mass
collapse) as parallel alternative.

**Headline directives for the builder:**
1. **Angle 2 is DEAD as proposed.** Its "squared-mass collapse" finite move is (a) literally inside
   the k=2 residual search space, so non-reducing by definition, and (b) a recorded dead end
   (the `P(x)²` collapse). Do NOT build it. The cyclic backstop (Move III) is what genuinely escapes
   the residual; B3 cannot be dissolved by a finite collapse.
2. **Build Angle 1, but its Step 2 mechanism as written in the survey is WRONG (backwards A3a
   direction).** The conclusion of Step 2 is true but for the mass-concentration reason, not as an
   A3a corollary. Step 3 remains the real, still-open aggregate fact. Proceed only with the corrected
   obligations below; do not log Step 2 as a "free partial win."

---

## The 7 checks

1. **Proves the right thing:** PASS — B3 is the sole gap; closing it (tie-averaged `ham(O*)/n < mb`
   on the residual) completes the theorem, since B2 then yields a finite `k=mn` with `b* < mb`. The
   surveyor's `Proves:` for Angle 1 matches the open lemma exactly.

2. **Hard step has a mechanism:** FAIL for Angle 2; CONCERN for Angle 1. Angle 2's Step-2 inequality
   `∑_{t_u=1}P(t)² < mb·∑_t P(t)²` is FALSE on residuals (verified: it RAISES maxbias, e.g.
   0.42→0.45, 0.49→0.57, often above 1/2). Angle 1's Step 3 mechanism ("residual riser condition
   summed over coords forces `mb > ham(O*)/n`") is named but is the same aggregate fact that
   defeated R1; the survey admits this. Angle 1's Step 2 stated mechanism is incorrect (see below).

3. **Missing cases:** CONCERN — Angle 1 Step 4 ("ham(O*)/n ≤ max interior weight below the mb-bound
   < mb") tacitly assumes "interior ⇒ ham/n < mb". This is FALSE at general n: at n=4, 114/1188
   valid mb<1/2 instances have O* = weight-2 orbit with ham/n = 0.5 ≥ mb. So ruling out the two
   extremes (Step 2) is necessary but far from sufficient; Step 3 must bound ham(O*)/n strictly
   below mb on the residual, which is the whole difficulty.

4. **No circular reasoning:** PASS — no angle assumes the conclusion. (Angle 1 Step 2's *stated*
   reasoning is simply wrong, not circular.)

5. **Certifiable:** Angle 2: N/A (move is non-reducing/dead). Angle 1: CONCERN — Step 3 is closeable
   only if genuinely new structure is supplied (see "what must be added"); as framed it is a
   relabeling of the open fact and the builder could spend the round without closing it.

6. **Avoids dead ends:** FAIL for Angle 2 (re-treads the `P(x)²` collapse, a recorded dead end, and
   the orbit-vs-complement issue is irrelevant since the move never escapes the k=2 search). PASS for
   Angle 1 (P-dependent; not Φ_p; Step 2 deliberately avoids orbit-vs-complement — though its stated
   reason is wrong).

7. **Small-case sanity:** PASS (computations all run, n=3 residuals; n=4 interior counterexample).

---

## Detailed findings (all computationally verified this round)

### Angle 2 self-defeat — CONFIRMED dead (highest-priority check)

- The k=2 "squared-mass collapse onto block B" = glue `(0,j)~(1,j)` for `j∈B` = a k=2 set-partition
  of the 2n coords. The full-copy version's marginal `(∑_{t_u=1}P(t)²)/(∑_t P(t)²)` equals the
  marginal of the k=2 full-diagonal glue **to machine precision** (maxerr 1.1e-16 over 2000 trials).
- The residual is defined as `all_k_partitions_search(P,n,k=2)` finding no reduction over the FULL
  Bell lattice of 2n coords. Therefore every k=2 collapse — full or partial block, any target — is
  inside it and CANNOT reduce on a residual by definition. Verified: 0/11 residuals reduced; the
  move RAISED maxbias on all (0.42→0.45, …, 0.49→0.57, several above 1/2).
- The k>2 escape (force all k copies to agree on full block, `∑P(t)^k` ratio) is WORSE: it
  concentrates on the argmax pattern, which on residuals is weight-1 (e.g. (1,0,0)), so maxbias rises
  toward 1 as k grows (k=2:0.45 → k=10:0.60; one case k=10:0.96). This is the recorded `P(x)²`-collapse
  dead end.
- What actually escapes the k=2 residual: the **cyclic orbit glue** (Move III). On n=3 residuals the
  best k=3 set-partition is `[[1,5,6],[2,3,7],[0,4,8]]` — one coord per copy, cyclically shifted —
  reducing to exactly 1/3. That IS the existing backstop, not Angle 2's squared-mass move. **Angle 2
  provides no new finite move and cannot delete the limit.**

### Angle 1 Step 2 — stated mechanism is WRONG; conclusion true for a different reason

- Survey lines 51–53 claim residual-failure of the whole-collapse bounds `P(1ⁿ)/P(0ⁿ)` BELOW
  `√(mb/(1-mb)) < 1`, contradicting `P(1ⁿ)` dominating. This is **backwards**. A3a: whole-collapse
  REDUCES iff `A1/A0 < √(mb/(1-mb))`; residual = it FAILED = `P(1ⁿ)/P(0ⁿ) ≥ √(mb/(1-mb))`. Data: on
  15 residuals `P1/P0` ranges 1.03–8913, always `≥` threshold. So the claimed contradiction does not
  exist; Step 2 is **not** a one-line A3a corollary.
- The conclusion (neither singleton is the geomean max) IS empirically true (15/15), but because BOTH
  `P(0ⁿ)` and `P(1ⁿ)` are tiny in absolute value (1e-7…3e-2), so their geomeans lose to the weight-1
  orbit's geomean (0.07…0.32). This "extremes are rare" fact is precisely a piece of the open
  concentration content — not a free win. **Do not present Step 2 as proved-from-A3a.**

### Angle 1 Step 3 — still the relabeled open fact; needs new structure

- "Interior ⇒ ham/n < mb" is false at general n (n=4 weight-2 example, ham/n=0.5≥mb, 114/1188). So
  Step 3 must do the real work: bound ham(O*)/n strictly below mb USING the residual. The survey's
  proposed mechanism (write the argmax-glue riser inequality `(a1 p+a0 q)/Z ≥ mb` for the blocking j,
  combine with `∑bias_i = E[ham]`) is plausible but unproven and is exactly the R1 wall reframed.

---

## Issues to fix (CHANGES REQUESTED — builder absorbs these as obligations)

- **DROP Angle 2 entirely.** It is inside the k=2 residual (verified) and a recorded dead end. Keep
  the cyclic backstop as the residual handler. (If the builder wants a limit-free residual move, it
  must be k≥3 and orbit-structured, i.e. a finite-m truncation of Move III with an explicit
  finite-m bias bound — NOT a squared-mass collapse. This is a possible salvage but does not avoid
  B3; it would still need ham(O*)/n < mb to make the finite-m bound work.)
- **Re-derive Angle 1 Step 2 correctly.** The correct statement is: on the residual,
  `P(0ⁿ),P(1ⁿ)` are small in absolute value (Step-2's real content), so the singleton orbits lose
  the geomean to interior orbits. The A3a "both-sides squeeze" story as written is invalid (wrong
  inequality direction). Either prove the absolute-smallness of `P(0ⁿ),P(1ⁿ)` from the residual
  (this is itself part of the concentration fact, so it is NOT free), or drop Step 2's claim to be a
  standalone corollary and fold it into Step 3.
- **Step 3 is the gate.** Before claiming closure, the builder must supply a genuine new mechanism
  that bounds `ham(O*)/n < mb` aggregately on the residual. Two concrete sub-targets that would
  constitute real progress:
  (a) Residual ⇒ for every coordinate, the geomean-orbit weight contribution is controlled by the
      A1/A3a polynomial failures in a way that sums to `< n·mb`; produce and **brute-force-verify**
      the scalar inequality on the 15+ n=3 residuals (margin must stay positive) AND on any hunted
      n=4 residual. (n=4 residuals are rare under random sampling — 0/4000 here — so target the
      search: bias mass toward interior-weight patterns and large `P(1ⁿ)/P(0ⁿ)`.)
  (b) If (a) does not close, the honest deliverable is "B3 reduced to a stated scalar inequality,
      verified numerically, mechanism named" — log it as progress, do not claim the theorem proved.
- **Presentational:** apply the A3b reword (property of the Rule-R loop, not a single absorption) per
  the R1 critic.

---

## Bottom line for the builder

Build **Angle 1 only**, with Step 2 re-derived (its survey mechanism is wrong) and full effort on
Step 3 (the real, still-open aggregate concentration inequality). **Do not build Angle 2** — verified
self-defeating (inside the k=2 residual) and a recorded dead end. Do not build Angle 3 (re-expresses
the same hard fact). If Step 3 resists again, the correct outcome is a precisely-stated, numerically
certified scalar reduction of B3 — not a claimed proof.
