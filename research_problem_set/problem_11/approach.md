# Problem 11 — Approach record

## Angle tried (Round 1)
**Angle 1:** existence via an enlarged realizable family — within-copy block collapse (Lemma 1) +
cross-copy identity matching on a subset (Lemma 2), composed at `k=2` (asymmetric: collapse copy 0 by
`Π_0`, copy 1 by `Π_1`, match a subset `T` of common block-representatives). Plus the AND-tree
realization of squaring (Lemma 4) for the mode route.

## What was established (fully rigorous)
- **Lemma 0** conditioning = component collapse (`P'∝∏_c P(copy_c)` on component-constant atoms).
- **Lemma 1** within-copy collapse closed form (restrict to block-constant strings).
- **Lemma 2** identity matching `T`: both copies get `P_T(x)∝P(x)·m_T(x_T)`; maxbias = max coord bias
  of one `n`-coordinate law.
- **Lemma 3** AND-amplifier `b→b²/(b²+(1-b)²)<b` for `b<1/2` (correlation-free), with the **exact**
  collateral formula `b'_j=[(1-b)b_j+(2b-1)p_{11}]/[b²+(1-b)²]` and the **covariance dichotomy**
  `b'_j<b_j ⟺ Cov(x_j,x_{i*})>0`.
- **Lemma 4** AND-tree on `2^t` copies realizes `P^{2^t}/Z` as a single conditioning.
- **Proposition A** unique mode `0^n`: explicit `k=2^t`. Tie to a `1`-heavy co-mode breaks it.
- **Proposition B** `n=2` complete: `k=1`, `S={(0,1)}`; reduces to proved inequality `p₁₁p₀₁<p₁₀p₀₀` (★).
- **Proposition C** worst coord non-negatively correlated with all others ⟹ matching `{i*}` reduces.

## What blocks completion (the exact gap, sharpened R2)
**Residual inequality (single remaining obligation, §9 of proof-attempt-r2.md).** When a firing move
(symmetric-Gram or full-collapse) drops the worst pair but RAISES a third coordinate `ℓ≥β`, prove `ℓ`'s
rise is itself a firing configuration for another family member (no cyclic frustration defeating all of
{full-collapse, symmetric-Gram, sub-collapse, identity-match} at once). Closure routes: (i) a potential
`Φ` tied to the 1-side mass of high coords (NOT `ψ=log ΣP²` — refuted, decoupled from maxbias), some
member provably decreasing `Φ`; or (ii) lexicographic well-foundedness on the at/near-β coordinate
multiset. Neither established. 0 failures / 4850 frustrated cases (oracle, regression only).

## NEW in Round 2 (verified, exact rational — see /tmp/round-2/survey-problem11-r2.md)
- **Gram / triangle operator** (NEW realizable move): a 3-cycle matching on the worst PAIR {i*,j}
  across 3 copies realizes the all-copies-identical single-copy marginal `P'(x) ∝ P(x)·(QQᵀ)[x_{i*},x_j]`,
  `Q` = 2×2 joint of the worst pair. It pulls the pair toward the agreement diagonal {00,11}. This is the
  closed form behind the k=3 litmus rescue (verified EXACT). Distinct from identity-match `P·m_T` (which
  RAISES maxbias on the litmus). Gram is the missing move for STRONGLY anti-correlated pairs.
- Iterated full squaring `P^m/Z` PROVABLY fails the litmus (mode=010 ⇒ middle coord bias→1). The
  Prop-A/AND-tree route is the wrong move in the frustrated regime — do not use it there.
- NO single move with a fixed selection rule is exhaustive (3-move fixed rule leaves 7/622). The family
  {collapse, identity-match, Gram-pair} over ALL pairs/subsets, all-copies-identical: 0/426 frustrated
  n=3 + litmus reduced (regression backstop only — NOT a proof).

## Round 2 RESULT (built, see proof-attempt-r2.md)
Committed to the realizable-operator disjunction with a DIAGONAL-ORIENTATION analysis (per critic).
NEW proven this round:
- **Lemma 5 (Gram realizable):** the cross-coordinate 3-cycle `S={(idx(a,i),idx(b,i)),(idx(a,j),idx(c,i)),
  (idx(b,j),idx(c,j))}` on `P³` (k=3, PERMUTED matching) realizes copy-0 marginal `P·(QQᵀ)[x_i,x_j]/Z`.
  Verified exact n=3,4 all pairs.
- **Lemma 5′ (safety):** all-copies-identical (full maxbias = single-copy) HOLDS iff the pair is
  SYMMETRIC `P(01)=P(10)` (206/206 safe; 273/540 UNSAFE for general pairs — the survey's F4
  "all-copies-identical for Gram" was OVERSTATED; it is true only for symmetric pairs).
- **Lemma 6 (Gram reduction, PROVEN):** for a symmetric pair `Q=[[a,b],[b,d]]`, `bias_i(Gram)<bias_i
  ⟺ a>d` (P00>P11). Proof: numerator `=−(a−d)·g`, `g=b·q+ad(a+b+d)`, `q` is a PSD quadratic form
  (matrix eigenvalues 1,1±√2/2>0). Rigorous SOS — verified sympy.
- **Lemma 7 (full collapse (★) lifted, PROVEN):** k=1 collapse → merged bias `γ=P(1ⁿ)/(P(0ⁿ)+P(1ⁿ))`,
  reduces iff `P(1ⁿ)<β(P(0ⁿ)+P(1ⁿ))`. Fails when 1ⁿ heavy (litmus γ=0.75).
- **Prop D:** frustrated symmetric `0`-dominated pair with residual `<β` → reduced by Gram. PROVES THE
  LITMUS rigorously (0.47465→0.45437, exact), not by search.

## Key NEGATIVE findings this round (dead ends ruled out, exact rational)
- NO clean two-branch dichotomy (full-collapse XOR Gram) is exhaustive: 13/1793 "neither" frustrated
  n=3 cases (rescued only by identity-match). Designated-pair orientation rule fails 59/3584.
- Gram reduction has NO clean covariance characterization (57 Cov<0 don't reduce, 4368 Cov>0 do).
- General Gram is NOT all-copies-identical (only symmetric pairs are safe).
- Full family {collapse,match,gram} with ORACLE selection: 0 fail / 4085 frustrated n=3, 765 n=4 —
  but oracle search is forbidden as proof.

## Chosen direction (Round 2)
**Primary = Angle 2 (finite exhaustive disjunction with a covariance-MAGNITUDE case split).**
Three proven operators (Collapse, identity-Match, Gram-pair), all realized all-copies-identical so full
maxbias = single-copy maxbias. Case split on worst coord i*:
- (C1) all Cov(i*,·)≥0 → Prop C (done).
- (C2) some Cov(i*,j)<0 STRONG → Gram/Collapse the pair; pair-merge bias `<β` by the (★)-lifted 2×2
  inequality; bound residual coords via Lemma 3 collateral + convex-combination bound (the threshold
  gives the firing move slack — this is the new leverage over round 1).
- (C3) Cov<0 but WEAK → AND-amplifier `Match_{i*}` (Lemma 3) drops i* and weak Cov keeps collateral <β.
The hard step is the (C2) residual bound (where round 1 stalled); the threshold split is the new lever.

**Hedge = Angle 1 (non-constructive existence via free-energy / fixed-point contradiction).** Prove that
a full-support P with maxbias<1/2 cannot be a simultaneous fixed point of {Collapse, Match, Gram}; the
only common fixed points are point masses, and the only point mass compatible with maxbias<1/2 is δ_{0ⁿ}
which is itself a strict reduction — contradiction. Uses ψ(t)=log Σ P(x)^{1+t} convexity. MUST avoid the
full-squaring trap (its fixed point is the wrong mode). Invoke this the moment (C2)'s residual won't
reduce to a scalar — it needs only that SOME operator reduces, exactly the theorem's weak requirement.

Spec review REQUIRED before build (top angle is novel non-constructive; the obvious instantiation fails
the litmus). Litmus P/217 MUST be reduced by any constructive claim (Gram on {0,1} → 0.4544).

## Round 5 RESULT (built Angle 2; see proof-attempt-r5.md)
**Angle chosen: Angle 2** (non-constructive existence on the bounded symmetric residual — committed by
approach-critic R5, `/tmp/round-5/approach-critic-problem11-r5.md`, which RETHINK-killed Angle 1: F3 is
FALSE as a closed form (Litmus C) and the matching-family contraction is non-uniform).

NEW proven this round:
- **Lemma 8 (NEW, fully proven, one line + sympy).** Exact identity `Pr(x_i=1,x_j=1)−Pr(x_i=0,x_j=0)
  = b_i+b_j−1`. Hence under `β<1/2`, EVERY pair (symmetric or not) is strictly 0-dominated
  `Pr(00)>Pr(11)`, i.e. `Φ_{ij}=1−b_i−b_j>0`. Strengthens the critic's empirical "all-1-dominated stall
  empty (0/110k)" into a LOGICAL IMPOSSIBILITY needing no sweep.
- **C1 (necessary half of Angle-2 contradiction): proved.** The "γ≥β ∧ all symmetric pairs 1-dominated"
  premise cannot occur under β<1/2 — by Lemma 8, no pair is ever 1-dominated. The would-be contradiction
  class is empty by a closed identity.
- **C2: proved.** Lemma 6's firing condition `a>d` holds AUTOMATICALLY on every symmetric pair (Lemma 8),
  so symmetric-Gram always reduces the targeted PAIR's two biases unconditionally. Pair level is never
  the obstruction.
- **C3:** `Φ_{ij}=1−b_i−b_j` is the verified maxbias-IMPLYING potential the critic required (b_i,b_j<1/2
  ⟺ Φ_{ij}>0); it is none of the forbidden ψ=log ΣP² / sum-odds / Lᵖ-odds.
- Litmus A/B/C each DISCHARGED by a NAMED operator (A: k=3 cyclic →746/1987; B: match{1}→0.45215;
  C: match{0,2}→0.42495). C and B are non-symmetric residuals cleared by identity-match (NOT F3).

## What blocks completion (the EXACT gap, R5 — supersedes the R2 "Residual inequality")
**Bridge Lemma / stall-set incompatibility (OPEN).** Need: for frustrated P, β<1/2, γ≥β, SOME member of
F={collapse, identity-match on a subset T, symmetric-Gram on a symmetric pair, k≤3 permuted/cyclic}
drives ALL n single-copy biases <β. The pairwise potential Φ>0 (Lemma 8) and the pair reduction
(Lemma 6) are proven, but the descent from "Φ>0 on every pair" to "FULL maxbias drops" is NOT closed:
a pair-reducing move can raise a THIRD coordinate ℓ≥β (exact witnesses: seeds 8356, 9350 — Gram on every
pair fails on the third coord). Empirically the clearing move on the named-family stalls is a PAIR
identity-match T={i,j}, but the winning pair is selected by NO tested named criterion (NOT most-negative
covariance: seed 9350 clears on cov −0.099 while the most-negative pair −0.122 fails). So the closure is
an un-routed oracle over 2ⁿ−1 subsets — FORBIDDEN as proof. This is the recurring "true union, false
mechanism" wall (4th round). Closure routes still open: (a) a CLOSED-FORM named pair-selection + its
collateral inequality (Lemma 3 collateral for pair-match bounds the third coord in closed form — the
missing step is a uniform "some named pair makes all three <β"); or (b) a monotone descent on Φ
(increase min_{ij}Φ_{ij}) by some F-member — tied-set iteration is NOT it (diverges 67/7420).

## CONJECTURE (labelled, NOT used in any proof step)
Empirical-with-exception (28/29 over 20k seeds, the exception being the non-symmetric Litmus-C residual):
when match-{i*} fails, the rising offender j sits in a symmetric pair with i*. This is the F3-shape the
critic forbade asserting as a closed form; recorded only as a conjecture.

## Round 6 RESULT (Angle 1 = iterated M_argmax — KILLED pre-build by approach-critic)
A candidate "breakthrough" (problem-scout): iterate `M_argmax` — match the current worst coordinate
across two fresh copies, realize as a nested `k=2^T` AND-tree. It appeared to clear 100% of all
in-hypothesis + adversarial cases with only termination open, "dissolving" the subset-selection wall.
**REFUTED (approach-critic R6, exact-rational):** the load-bearing realizability step "all `2^T` copies
share the single-copy law `P_T`, so `maxbias(P')=maxbias(P_T)`" is FALSE whenever the matched coordinate
SWITCHES between steps (`i_t≠i_{t-1}`, the dominant case). Copy-0's law equals `P_T`, but the other
copies keep intermediate marginals (tied to copy-0 only on the EARLIER coordinate), so the FULL maxbias
of the realized conditioning exceeds `maxbias(P_T)`; in 38/42 multi-step n=3 cases it stays ABOVE the
original β. The scout/surveyor "100% clearance" measured the single-copy iterate `P_T` — a fiction, not
the maxbias of any realizable `(k,S)` (violates the round-1 standing rule). The ONLY all-copies-identical
nested repeat is the SAME-coordinate one, which equals the dead L^k all-agreement tilt (Angle 4, diverges
to the mode). **The argmax rule does NOT dissolve the wall — coordinate-switching destroys realizability
and relocates the third-coordinate bridge into a "full ≠ single-copy maxbias" gap.** DEAD: do not revive.
- NEW verified byproduct (keep): **Lemma 9** — one `M_i` step keeps every collateral coord `<1/2`
  (`(1−b_i)b_j/Z ≤ (1−b_i)b_i/Z < 1/2 ⟺ b_i(1−b_i)<1/4`, one line; 0/20000). Step inequality
  (`b_i↦b_i²/Z=b_i·ρ(b_i)`, ρ<1 increasing on [0,1/2)) and the signed collateral bound are correct, but
  concern only the single-copy iteration.
- Separable convex potentials `Σf(b_i)` (f∈{b,b²,b/(1−b)}, ∏1/(1−2b_i), 2-largest) ALL INCREASE under one
  `M_argmax` step on the adversarial anti-correlated family (n7 1123/1123, n10 777/777) — DEAD as descent.
- Next: Angle 2 (non-constructive) targeting FULL realized maxbias over the all-copies-identical family;
  prove the STALL set empty (not just the all-1-dominated subset). See run_state.md Next(R7).
- Files: `/tmp/round-6/scout-problem11-r6.md`, `survey-problem11-r6.md`, `approach-critic-problem11-r6.md`.

## Round 8 RESULT (γ-dichotomy restructuring + Lemma 10; see proof-attempt-r8.md)
**Angle chosen: Angle 1 of the R8 survey (the γ-dichotomy scaffold + Lemma 10), approved by the R8
approach-critic gate.** Angle 2 (minΦ-increase / involution fixed-point) was RETHINK-gated and NOT
built (refuted on the exact γ≥β stall set — see below).

NEW proven this round (exact rational, built on r5 without regression):
- **γ-DICHOTOMY (restructuring).** Exhaustive split on `γ=P(1ⁿ)/(P(0ⁿ)+P(1ⁿ))`:
  - **Branch 1 (γ<β): FULLY CLOSED by Lemma 7.** B1 full-collapse (k=1, spanning path on one copy)
    gives full realized n-maxbias `= γ`; so `γ<β ⟹ maxbias(P')=γ<β`. This is the direct content of a
    PROVEN lemma (not a sweep). Covers ~95% of frustrated n=3 stalls (1805/1903 scale16; 653/685
    scale12), incl. the R7 over-count witness seed 770 (γ=1/8<β=20/41; B1 realized maxbias=1/8 EXACT).
  - **Branch 2 (γ≥β): OPEN** (the 1ⁿ-heavy ~5% residual).
- **LEMMA 10 (NEW, fully proven, exact-verified).** For an INVOLUTION `π=π⁻¹` and `S={(i,n+π(i))}` on
  `P²`, BOTH copies share the law `P(x)·P(π·x)/Z`, hence full 2n-realized maxbias = single-copy maxbias
  of `P(x)·P(π·x)`. Mechanism: Lemma-0 per-edge collapse fixes copy-1 = `π⁻¹·x`; involution gives
  `π⁻¹=π`; and `w(z)=P(z)P(π·z)` is π-symmetric (`w(π·z)=w(z)`) so the copy-0 and copy-1 marginals
  coincide AS FUNCTIONS (this is where `π=π⁻¹` is load-bearing). Verified: all 4 involutions × 10-seed
  battery, full2n==closed-form, copies identical. NON-involutions (3-cycles) are NOT copy-identical
  (`copies_identical=False`); those require the k=3 cyclic B5 (Lemma 5), NEVER Lemma 10's k=2 form.
- **B4 added to family F→F⁺, repairing a non-exhaustiveness defect.** Scale-16 seed 16832 (β=21/47,
  γ=2/3≥β, NO symmetric pair) stalls EVERY member of old F={B1,B2,B3} (`family_reduces=None`); cleared
  ONLY by B4 involution revperm `(2,1,0)` → full 2n-maxbias `79/204≈0.3873<β`, all 6 coords <β (EXACT).
  B4 is load-bearing, not optional.

## What blocks completion (the EXACT gap, R8 — Branch 2 / γ≥β)
**γ≥β Closure (OPEN).** For frustrated P, β<1/2, γ≥β, some member of F⁺={B1,B2,B3,B4,B5} reduces full
maxbias. NOT closed:
- NO named single-member selection: AND-match{i*} clears only 54–72% of γ≥β stalls (27/97 have
  match{i*}≥β); named-pair rules clear 7–11/20 (most-neg-cov 11/20, two-non-worst 8/20, two-smallest 7/20,
  triple 7/20). 4th recurrence of the "true union, false mechanism" wall, now in Branch 2.
- **minΦ-increase lever REFUTED (DEAD LEVER #7).** The Angle-2 plan "SOME involution strictly increases
  minΦ_{ij}; only common fixed point is a point mass" fails on the EXACT γ≥β stall set: 2/97 (scale12),
  5/106 (scale8), 3/98 (scale16). On those (seed 1219 biases (25/51,8/17,25/51), β=25/51<1/2, γ=10/19≥β)
  EVERY involution-reweight gives minΦ≤baseline and maxbias≥0.50; the clearing move is match{1}, a
  NON-involution. minΦ (=1−two-largest-biases) joins ψ, Σf(b_i), Φ-magnitude, Σb_i, tied-core averaging,
  single-copy M_argmax on the dead-lever list. Do NOT use minΦ-increase or involution-orbit fixed-points.
- F⁺ clears 0/20000 γ≥β stalls ×3 scales — DISCLOSED REGRESSION BACKSTOP ONLY, used in NO proof step.
- Suggested future route (NOT built): a γ≥β-specific lower bound on singleton-match collateral via the
  Lemma-3 formula (γ≥β lower-bounds the 11-corner mass p^{(ℓ)}_{11}) PAIRED with a routed fallback to a
  named other member with a proved inequality. Not a separable sum / Σb_i / Φ-magnitude / minΦ; mover not
  restricted to involutions.
- Files: `/tmp/round-8/survey-problem11-r8.md`, `approach-critic-problem11-r8.md`; `/tmp/r8lib.py`,
  `/tmp/r8probe*.py`.

## Files
- `research_problem_set/problem_11/proof-attempt-r8.md` — Round 8 attempt (γ-dichotomy; Lemma 10; B4; gap).
- `research_problem_set/problem_11/proof-attempt-r5.md` — Round 5 attempt (Angle 2; Lemma 8; gap).
- `research_problem_set/problem_11/proof-partial.md` — proof of all proven components + sharp gap.
- `/tmp/round-2/survey-problem11-r2.md` — full R2 survey (3 angles, mechanisms, checks).
- Verifying scripts: `/tmp/scout2.py`, `/tmp/r5lib.py`, `/tmp/r2probe*.py`.
