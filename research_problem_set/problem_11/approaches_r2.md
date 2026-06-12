# Approach survey — Round 2 (problem_11): closing the sole gap (Lemma B3)

Spec review: **REQUIRED** for whichever top angle is built. Round 1 reached "complete modulo one
inequality"; B3 has resisted two prior surveys, the proof-builder, and the critic. Any angle that
claims to close it rests on a non-obvious aggregate fact and must be pre-build reviewed.

## What is fixed and what the gap actually is

Settled (independently re-derived by the critic): S0, S1, A1, A2 (odds-squaring `o↦o²`, the ONLY
use of `mb<1/2`), A3, A3a (whole-collapse reduces iff `A1/A0 < √(mb/(1-mb))`), A3b/Rule R, B1
(cyclic k=n equal marginals), B2 (`b*_{mn} → ham(O*)/n`, O* = geometric-mean-maximizing cyclic
orbit). Combined construction: 0 failures / 30,000+ adversarial trials.

> **Lemma B3 (open).** Residual hypothesis [no k=2 set-partition of the 2n coords reduces maxbias]
> ⇒ tie-averaged `ham(O*)/n < mb`, where `O*` maximizes `G(O)=(∏_{y∈O}P(y))^{1/|O|}` over cyclic
> orbits.

### New diagnostics run this round (n=3, residuals isolated by full Bell-lattice k=2 search)

- **D1.** On EVERY residual found, the geomean maximizer `O*` is the **weight-1 orbit**
  (ham(O*)/n = 1/3), and **mb > 1/3** with min margin ≈ 0.074 (8/8 and 21/21 across two seeded
  sweeps). So at n=3, B3 ⟺ the conjunction {(a) `O*` is the weight-1 orbit} ∧ {(b) `mb > 1/3`}.
- **D2 (the load-bearing reason).** On residuals, `P(0^n)` and `P(1^n)` are essentially **0**, and
  the mass sits on intermediate (weight-1, weight-2) patterns. The weight-1 orbit wins the geomean
  not via a monotone ordering but because the antipodal/extreme patterns are rare. This is exactly
  the "anti-correlation concentrates mass on low-weight patterns" intuition, now numerically pinned.
- **D3 (kills the naive proof).** The clean ordering "max geomean over orbits is monotone
  non-increasing in orbit Hamming weight" is **FALSE on residuals** (0/21), even though the global
  maximizer is weight-1. So there is no termwise/rearrangement proof of B3; it is genuinely an
  aggregate fact about where the residual puts its mass. (Confirms R1's refuted orbit-vs-complement
  rearrangement, from a different direction.)
- **D4 (Angle B viability).** "Best over ALL coordinate-permutations σ of the cyclic glue, k∈{2,3}"
  fails only **1/382** at n=3 (vs ~5% for single-coord and the case split's residual). A richer
  uniform σ-family is nearly universal — but its limit argument still bottoms out in the same
  concentration fact, so it does not dissolve B3 for free (see Angle 3).

---

## Angle 1 (top pick) — Close B3 via the mass-concentration mechanism: residual ⇒ P(0ⁿ),P(1ⁿ) small ⇒ geomean max is an interior orbit, and interior orbit ham/n < mb

  **Proves:** Lemma B3 in full (hence the whole theorem, since everything else is closed).

  **The mechanism (named, not a label).** Decompose the residual hypothesis into the family of
  whole-block-collapse failures (A3a). For EVERY block `B` (in particular `B`={all coords}, and
  every singleton-grown block), the k=2 collapse failed, which by A3a means
  `A1(B)/A0(B) ≥ √(mb/(1-mb))`, i.e. `P(all-ones-on-B) ≥ √(mb/(1-mb))·P(all-zeros-on-B)` is NOT the
  binding direction — rather the collapse's resulting bias `A1²/Z ≥ mb`. The simultaneous failure of
  the whole-collapse for BOTH target values (forcing-to-0 and forcing-to-1 are both available since
  conditioning is symmetric) squeezes `P(0ⁿ)` and `P(1ⁿ)` from both sides: each of them, were it the
  dominant orbit, would itself be a successful collapse. Concretely:
    - If `P(1ⁿ)` were the geomean max among singletons, the whole-collapse to value 1 would give bias
      `P(1ⁿ)²/(P(1ⁿ)²+P(0ⁿ)²)`, and residual-failure of THIS collapse bounds `P(1ⁿ)/P(0ⁿ)` below
      `√(mb/(1-mb)) < 1` — contradiction with `P(1ⁿ)` dominating. (mb<1/2 ⇒ threshold <1 enters here.)
    - Symmetrically `P(0ⁿ)` cannot dominate, because the all-zeros singleton orbit has ham 0 and a
      successful k=2 move (Rule R on the argmax) would have reduced — residual rules it out.
  So the geomean maximizer `O*` is an **interior** orbit (0 < ham(O*) < n). For n=3 interior orbits
  are weight-1 and weight-2; D2 shows weight-1 wins, giving ham(O*)/n = 1/3.

  **Skeleton:**
    1. Reduce B3 to: residual ⇒ ham(O*)/n < mb. (Given; B2.)
    2. Residual ⇒ the singleton orbits {0ⁿ}, {1ⁿ} are NOT the geomean maximizer — by A3a applied to
       the whole-collapse (both target values), each contradicting a successful k=2 reduction.
    3. Residual ⇒ for each coordinate i, Rule-R termination-failure bounds the conditional reweighting
       (A1/A3 closed forms), giving a quantitative lower bound `mb > τ(n)` where τ(n) is the smallest
       interior-orbit normalized Hamming weight relevant — conjecturally `τ(n)=` (something ≥ 1/n that
       still beats ham(O*)/n). For n=3, prove `mb > 1/3`.
    4. Combine: ham(O*)/n ≤ (max interior normalized weight below the mb-bound) < mb.

  **Hard step:** Step 3 — "residual ⇒ mb strictly exceeds the normalized weight of the dominant
  interior orbit." Mechanism: the residual is a conjunction of A1/A3a polynomial-sign failures; the
  argmax-glue (A2) drops `o_{i*}↦o_{i*}²` but is blocked only because a riser `j` (anti-correlated
  with i*) satisfies `bias_j(P') = (a1 p+a0 q)/Z ≥ mb`. Writing out this single inequality for the
  argmax glue, together with `Σ_i bias_i = E[ham]`, should force `mb` above the geomean-orbit weight.
  This is the genuinely unproven link and is an **aggregate** inequality (D3: not termwise).

  **Check:** (i) Prove Step 2 rigorously from A3a (this is essentially a one-line corollary — verify
  symbolically that residual ⇒ neither singleton dominates the geomean). (ii) For Step 3, derive the
  scalar inequality at general n: residual riser condition `(a1 p+a0 q)/(p²+q²) ≥ mb` for the
  blocking j, summed/combined over coordinates, implies `mb > ham(O*)/n`. Verify the derived
  inequality on the 21+ isolated n=3 residuals and on freshly hunted n=4 residuals (margin must stay
  positive). (iii) Confirm `O*` interior on n=4 residuals (harness `cyclic_orbits` + geomean).

  **Tractability:** Medium. Step 2 looks genuinely closable now (it is a direct A3a corollary that
  prior rounds did not isolate — the singleton-can't-dominate observation is new and is the cleanest
  partial win available). Step 3 is the real risk: it is the same aggregate fact that resisted R1,
  now reframed as a scalar inequality. Reframing to "neither singleton dominates + a weight bound"
  is more tractable than the orbit-vs-complement rearrangement (which D3 confirms is dead).

  **Recorded dead end?** No. The orbit-vs-complement rearrangement IS a recorded dead end and Step 2
  deliberately avoids it (it uses singleton non-domination via A3a, not pairing each orbit with its
  complement). The mass-concentration framing is new this round.

## Angle 2 — Replace the cyclic backstop with an explicit polynomial-sign residual move (dissolve the limit)

  **Proves:** The theorem, by giving the residual its own finite-k move whose reduction is a signed
  polynomial inequality (like A3a), so B2's asymptotic geomean limit is never invoked. This is the
  critic's explicit suggested-fix (b).

  **Mechanism.** On the residual, mass concentrates on interior (weight-1 at n=3) patterns (D2).
  Force a partition that collapses onto the **rarest** interior pattern. The generalization of A3a:
  for a block `B` and a *chosen target pattern* `t∈{0,1}^|B|` (not just all-0/all-1), conditioning
  copies to agree on `B` with the value being one of the support patterns gives, for a coordinate
  `u∈B`, a marginal of the form `(∑_{t:t_u=1} P(block=t)²)/(∑_t P(block=t)²)` — a "squared-mass"
  ratio. Since residual mass is on weight-1 patterns of `B`, the all-ones pattern is rarest, so this
  squared-mass ratio is `< mb`. The reduction condition is an explicit polynomial-sign inequality in
  the `P(block=t)`.

  **Skeleton:**
    1. Closed form for "collapse B onto its support patterns via k copies" (generalize A3 from the
       2-pattern {all-0,all-1} case to all 2^|B| patterns). The k=2 version: bias_u =
       (∑_{t_u=1} P(block=t)²)/(∑_t P(block=t)²).
    2. Residual ⇒ for B = full copy, the squared-mass ratio of every coordinate is < mb, because the
       residual forces P concentrated on weight-1 patterns (mass on {e_i}), and for each coordinate
       u, ∑_{t_u=1}P(t)² ≈ P(e_u)² is small relative to the total.
    3. That collapse reduces maxbias — a finite k=2 move, no limit.

  **Hard step:** Step 2 — proving the squared-mass ratio `< mb` from the residual. Mechanism: same
  concentration fact as Angle 1 (residual ⇒ mass on low-weight patterns), but now expressed as a
  CLEAN polynomial inequality `∑_{t_u=1}P(t)² < mb·∑_t P(t)²` rather than a geomean limit — this is
  the advantage. The risk: the residual might concentrate on weight-1 patterns only at n=3; at larger
  n it could spread over a band of interior weights, and "rarest pattern is all-ones" must be made
  precise per coordinate.

  **Check:** (i) Derive and brute-force-verify the k=2 generalized-block closed form (extend
  Certificate 3). (ii) On isolated residuals, check `∑_{t_u=1}P(t)² < mb·∑_t P(t)²` for every u with
  B=full copy. (iii) Confirm it holds at n=4 residuals (must hunt some — Bell(8) is slow; bias
  sampling toward interior-weight mass as in the round-2 probe).

  **Tractability:** Medium-high IF the squared-mass collapse closed form is clean and the inequality
  in Step 2 holds — it would be a fully signable, limit-free proof matching the user's "explicit sign
  condition" preference. This is the single best route to ALSO satisfying the elegance request, since
  it deletes the cyclic backstop AND its asymptotic limit. Note: the squared-mass collapse with
  B=full copy reduces to whole-collapse only when the support is {0ⁿ,1ⁿ}; in general it is richer and
  may already be in the existing k=2 search space (so verify it is genuinely not covered, else
  residual-by-definition kills it).

## Angle 3 — One uniform σ-cyclic family for ALL P (dissolve the case split)

  **Proves:** The theorem via a single uniform construction: best over coordinate-permutations σ of
  the σ-cyclic glue, escalating k. D4: fails only 1/382 at n=3, far cleaner than the documented case
  split.

  **Mechanism.** For a permutation σ of {1..n}, gluing copy `c+1` = σ applied to copy `c` over k
  copies makes feasible configs = σ-orbit tuples; the geomean limit picks the σ-orbit maximizing
  `(∏ P over the σ-orbit)^{1/len}`. Choosing σ to be the cycle structure that puts the dominant orbit
  at low Hamming weight gives reduction. The case split dissolves because the family is uniform in
  form (one parametric family, P-dependent choice of σ — explicitly allowed by the existential
  Rules).

  **Hard step:** Prove SOME σ always yields a geomean-max orbit with normalized weight < mb. Same
  aggregate concentration fact as Angle 1, but now we get to CHOOSE σ to help — strictly more
  freedom than the fixed full-cycle backstop. Mechanism: for the residual, choose σ = identity, which
  makes σ-orbits = singletons and the move = the k=2 collapse family (so identity-σ recovers Move II);
  for the anti-correlated case choose the full cycle. The hard part is a uniform statement that the
  per-P-optimal σ exists and reduces — which is essentially re-deriving the case split as a max over σ.

  **Check:** confirm best-over-σ (k up to ~n) at n=3,4 has 0 failures (round-2 probe showed 1/382 at
  k∈{2,3}; must push k or σ-family); prove the limit reduction for the chosen σ.

  **Tractability:** Lower. Elegant in FORM, but the proof still requires the B3-type concentration
  fact, just dressed as "∃σ". It does not actually remove the hard step — it generalizes it. Pursue
  only if Angles 1/2 stall and the user's elegance preference outweighs proof completeness risk.
  WARNING (Rules): "no fixed/uniform gadget works for all P" is a recorded dead end; this survives
  only because σ is P-DEPENDENT (best-over-σ), which the existential Rules permit — but a reviewer
  must confirm it is not re-treading the refuted "full-cycle symmetrize" (which failed 4/3000).

---

## Ranking and recommendation

**Build Angle 1, with Angle 2 developed in parallel as the limit-free alternative.**

- **Angle 1** is ranked first because it isolates a NEW, likely-closable partial win (Step 2:
  residual ⇒ neither singleton orbit dominates, a direct A3a corollary that prior rounds missed),
  shrinking B3 to a single scalar inequality `mb > ham(O*)/n` whose only hard content (Step 3) is the
  aggregate concentration fact. It works WITH the existing settled machinery (B1/B2), so a partial
  result (Step 2 proven, Step 3 reduced to a clean scalar claim) is itself logged progress even if
  Step 3 resists again.

- **Angle 2** is the best route to the user's stated elegance goal: it replaces the asymptotic cyclic
  backstop with a finite k=2 squared-mass collapse whose reduction is an explicit polynomial-sign
  inequality (the A3a analogue the critic asked for). If the generalized-block closed form is clean
  and Step 2's inequality holds at n=4, this dissolves the limit AND gives a signable certificate. It
  shares Angle 1's hard fact but in a more checkable algebraic form. Develop its closed form first
  (cheap, brute-forceable) — if the inequality verifies on residuals, promote it to top.

- **Angle 3** is the most elegant in form but does not actually remove the hard step (it re-expresses
  the case split as max-over-σ). Reserve as fallback; flag dead-end risk to reviewer.

**Key tradeoff:** All three hinge on the SAME aggregate fact — residual ⇒ P's mass concentrates on
low/interior-Hamming-weight patterns, so the geomean-dominant orbit has normalized weight < mb. D3
confirms this is NOT termwise (no rearrangement). The fork is purely about which DRESS makes that
fact provable: a scalar weight inequality (Angle 1), a squared-mass polynomial sign condition
(Angle 2, most user-aligned), or a max-over-σ existence statement (Angle 3). Angle 2's algebraic
form is the most likely to yield a clean, reviewable, limit-free certificate.

**Pre-build review: REQUIRED.** The load-bearing concentration inequality is unproven and aggregate;
Step 2 of Angle 1 / the closed form of Angle 2 should be sanity-checked by the approach-critic before
a full build, given B3 defeated round 1.
