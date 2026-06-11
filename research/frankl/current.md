# Frankl — current status

## Constant
Frankl's union-closed sets conjecture, max element bias. Entropy method.
- Record (lower bound): **0.38271** (Liu, arXiv:2306.08824). Target 1/2 (OPEN).
- `held` (reviewer-verified): R2 — GLOBAL obstruction upgrade. Avenue-A ceiling
  H[P_t] <= H[A] is now UNCONDITIONAL at every integer t (P_m = law of OR of m iid
  uniform) on every family, with additivity P_{a+b}=P_a(*)P_b, the single-lemma reduction
  (all-real-t>=1 nonneg ⇔ lemma (L)), and the Pick reduction (L)->(L') all re-derived from
  scratch. Supersedes R1's local (Taylor/small-n) obstruction. Still no bound improvement
  (goal's honest fallback). The all-real-t extension rests on lemma (L)/(L'), which is
  CONJECTURAL (certified numerically, unproven) and is NOT part of the held/verified claim.
- R3 CORRECTION (VERIFIED, proof-reviewer R3 APPROVE): the SURROGATE (L') [B_l(x)>=0 for all l>0] is FALSE in
  general — explicit frozen union-closed witness F* (n=9, |F*|=52), min B_l = -0.0112 at
  l≈0.126, confirmed at 60-dps mpmath, cond(Z*)≈129. (L)≠(L') separation recorded: the true
  lemma (L) [P_{1+s}>=0] survives on the SAME witness (+3.7e-4). (L) honesty DOWNGRADED to
  "unproven AND eroding-margin evidence it may be FALSE at scale" (min P_{1+s} drifts
  +4.2e-4→+1.9e-4 as swept n grows). The Pick IMPLICATION (L')=>(L) stays valid (premise now
  known false). UNCHANGED and machine-checked ON the witness: integer-t core, additivity,
  M_F column-stochasticity, the single-lemma reduction, the §8 verdict, record 0.38271 (Liu).
  The obstruction never depended on (L)/(L') and is NOT weakened. No bound moves.
- VERIFIED R2 (proof-review-round2.md, APPROVE): GLOBAL upgrade of the Avenue-A obstruction.
  PROVEN unconditionally — integer-t core (P_m = law of OR of m iid uniform, so H[P_m] <= H[A]
  on every family, every integer m), additivity P_{a+b}=P_a(*)P_b, and the single-lemma
  reduction (all-real-t>=1 nonnegativity ⇔ lemma (L): (P_1(*)P_s)(x)>=0, s in [0,1)),
  plus a Pick-representation reduction of (L) to the exponent-free inequality B_l>=0.
  CONJECTURE (certified-numerically-but-UNPROVEN): lemma (L)/(L') on every union-closed
  family. So the global H[P_t] <= H[A] ceiling is UNCONDITIONAL at integer t and
  CONDITIONAL (on (L)) at non-integer t>=1. No bound moved; record 0.38271 (Liu) stands.

## Bounds
- Lower bound on max element bias (record): 0.38271 (Liu, arXiv:2306.08824) — UNCHANGED.
- This work claims NO numeric bound; deliverable is the global obstruction upgrade only.

## Status: improved

## Progress log
- R1: VERIFIED obstruction — Theorem 1 (H[C] <= H[A] for any supp(C) ⊆ F, hypothesis-free, Gibbs/KL) re-derived from scratch; Avenue A H''(1) = -(1/ln2)·Σ(dP/dt)²/Pᵢ < 0 confirmed (closed form == finite-diff, -2.1518 on nondistributive lattice); Avenue B collapse C→A confirmed; certificate reproduced (exit 0) and shown non-vacuous (perturbing core checks → exit 1). Record 0.38271 (Liu) stands, correctly cited not improved.
- R2: VERIFIED global upgrade — integer anchor P_m = law(OR of m iid uniform) ⇒ H[P_m] <= H[A] on every family at every integer t (unconditional); additivity P_{a+b}=P_a(*)P_b and the single-lemma reduction (all-t>=1 nonneg ⇔ (L)) re-derived from scratch; Pick reduction of (L) to exponent-free B_l>=0 verified independently; lemma (L)/(L') honestly CONJECTURAL (certified numerically, unproven). Non-vacuity re-confirmed (AND-conv / wrong-power / Q^1 numerator all FAIL). Record 0.38271 (Liu) stands, unchanged.
- R3: VERIFIED CORRECTION + CLARIFICATION — retracts the round-2 narrative/cert R2-7(ii) generalization "B_l>=0 on the sweep": the SURROGATE (L') is FALSE in general. Explicit RNG-INDEPENDENT frozen witness F* (n=9, |F*|=52; round-2's randint(2,7) does NOT reproduce it — needs wider randint(2,12), so masks are hard-coded), min_x B_l(x) = -0.0112 at l≈0.126, float64 + 60-dps mpmath agree to 6e-17, cond(Z*)≈129 (not ill-conditioning). (L)≠(L') separation: the TRUE lemma (L) [P_{1+s}>=0] survives on the SAME witness (+3.7e-4) — negative B_l mass at small l is downweighted by l^{s-1} (s→1), verified via the Pick integral. (L) downgraded to "unproven AND eroding-margin evidence it may be FALSE at scale" (min P_{1+s} drifts +4.2e-4→+1.9e-4 as swept n→10; (L') onset OBSERVED ~n≈8, stated seed/grid-dependent). Integer-t core, additivity, M_F column-stochasticity machine-checked ON the n=9 witness (insulated from (L') failure). Pick IMPLICATION (L')=>(L) still valid (premise false). §8 verdict, single-lemma reduction, record 0.38271 (Liu) UNCHANGED; obstruction never depended on (L)/(L'), NOT weakened. New `certificate_round3.py` exit 0; round-1/round-2 certs left intact (both still exit 0).
