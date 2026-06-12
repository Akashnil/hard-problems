Verdict: RETHINK

Angle reviewed: Angle 1 — Symmetrize-then-contract via a cyclic / averaging glue, with a potential argument.

## Summary

Angle 1 is not buildable as stated. Its load-bearing inequality is numerically REFUTED (not merely
unproven), and its proposed repair ("extra contraction = take k a larger multiple / one extra cyclic
layer") does not work as a mechanism. The cyclic/symmetrizing family is provably non-uniform: it
misses near-boundary cases that are rescued only by genuinely NON-cyclic partitions. The theorem
itself is true, but a correct proof must use a P-dependent partition (Angle 2 or Angle 3 framing),
not a single fixed-form symmetrizing gadget. The user's wish for "one elegant uniform construction"
cannot be met by the cyclic family — that is the central finding.

## The 7 checks

1. Proves the right thing: CONCERN — the angle targets the full theorem, but its construction
   (full-cycle glue, k=n) only equalizes marginals; equalization does not imply reduction.

2. Hard step has a mechanism: FAIL — the stated mechanism ("symmetrized b* <= maxbias, equality iff
   all biases equal; otherwise an extra contraction layer drives it down") is false. See counterexample
   below: a P with both biases ALREADY equal to 0.49 has the k=2 cyclic glue RAISE the common bias to
   0.4949 > 0.49. The "weighted average of conditional biases dominated by maxbias" claim is wrong
   because the reweighting can push the average ABOVE the max, and the conditional reweighting has no
   1/2 cap (this is exactly the scout's central obstruction, which Angle 1 does not actually resolve).

3. Missing cases: FAIL — (a) anti-correlated P: full-cycle symmetrize OVERSHOOTS in >50% of
   anti-correlated n=2 trials (105/199), and 9/739 of uniform-random n=2 trials. (b) The "extra
   contraction = larger k" fix is NON-MONOTONE: for n=2 the cyclic glue at EVEN k pushes bias toward
   1/2 (k=4 -> 0.499, k=6 -> 0.4999), while ODD k drops it; growing k does not uniformly help.
   (c) For n=2, odd-k cyclic glue collapses to "force the whole vector constant," giving
   bias = P(1^n)^k/(P(0^n)^k+P(1^n)^k) — a SCOUT-RECORDED DEAD END that fails when P(1^n) >= P(0^n).
   I verified such P exist for n>=3 (529/100000 random samples with maxbias<1/2 and P(111)>=P(000)).
   (d) Full cyclic-perm-glue family (all sigma, k<=5) still FAILS 2/235 near-boundary n=3 cases
   (mb~0.493, 0.499) — reproducing the surveyor's own 2/20000 finding.

4. No circular reasoning: PASS — no circularity; the gap is a false lemma, not circular logic.

5. Certifiable: FAIL — the angle's check item (iii) "in the equality case exhibit the extra
   contraction step and prove strict drop using o_common<1" cannot be carried out: in the equal-bias
   counterexample the glue moves the WRONG way, and there is no proven contraction step that fixes it.
   Closing this would require proving a new inequality that my tests show is false.

6. Avoids dead ends: FAIL — at n=2 the odd-k limit of the proposed family IS the recorded
   "force all coordinates equal / all-equal large-k" dead end (scout dead-end #4, approaches.md line 24),
   re-encountered under the name "extra cyclic layer." It hits the same wall (fails when P(1^n)>=P(0^n)).

7. Small-case sanity: FAIL — explicit counterexample to the hard step:
   P(00)=0.10, P(01)=0.41, P(10)=0.41, P(11)=0.08 (n=2). biases = (0.49, 0.49), maxbias = 0.49.
   Full-cycle glue (k=2, groups {0,3},{1,2}) gives all marginals = 0.49489 > 0.49. The symmetrized
   value EXCEEDS maxbias even though the biases were already equal — directly contradicting Angle 1's
   stated inequality and its equality condition.

## Reason for RETHINK

- Step 3, regime (a) of Angle 1's skeleton (the load-bearing "averaging inequality b* <= maxbias")
  is FALSE. Verified counterexample (n=2, biases equal at 0.49 -> b* = 0.4949). The reweighting in the
  conditioned distribution is a conditional-probability average with no 1/2 cap, so it can and does
  overshoot the max. This is the exact obstruction the scout flagged; Angle 1 renames it rather than
  resolving it.
- Step 3, regime (b)'s repair ("take k a larger multiple / one extra cyclic layer applies o->o^2 to
  the common coordinate") is FALSE as a mechanism: larger k is non-monotone (parity-dependent for
  n=2), and the only-helpful branch (odd k) reduces to the recorded all-equal dead end that fails when
  P(1^n) >= P(0^n) (which occurs for n>=3). There is no proven contraction that uniformly fixes the
  overshoot cases.
- Structural fact (verified, and consistent with the surveyor's exhaustive search): NO fixed-form
  cyclic/symmetrizing gadget is uniform. The 2 stubborn n=3 cases are rescued ONLY by non-cyclic
  partitions: e.g. single cross-copy pair S=[[1,4]] drops mb 0.49278 -> 0.48454, and a mixed
  cross-coordinate partition S=[[0,5],[2,3]] drops mb 0.49945 -> 0.48205. The winning S is genuinely
  P-dependent and outside the proposed family. Therefore Angle 1's promise of a single uniform
  construction is unachievable.

## Suggested direction

Build Angle 2 (induction on n / global potential) or Angle 3 (limiting-compactness), with the
following corrected, evidence-backed target. Both reduce to the SAME single inequality, which is the
only place maxbias<1/2 is used (the n=1 odds-squaring contraction o->o^2 with o<1). The builder's job
is to make that one inequality rigorous; do NOT pursue a fixed uniform gadget.

Concrete corrected construction to pursue:

1. Work with general k=2 partitions (free choice of pairs, not the cyclic family). My tests show
   general k=2 partitions with |S|<=3 cover 0/125 stressed cases AND rescue both near-boundary n=3
   failures — a far more tractable and likely-universal target than the cyclic family. Recommend the
   builder first test, at high resolution near the mb->1/2 boundary, whether "best general k=2
   partition" is universal; if so the whole problem collapses to k=2.

2. Candidate potential: Phi(P) = sum_i p_i/(1-p_i) (sum of odds), or its product/log. Under the
   single argmax cross-copy glue, Phi fails to decrease in only ~1/380 trials, and in that single
   violation choosing the BEST coordinate to glue (not argmax) restores the decrease. So the
   provable lemma to target is: "there exists a coordinate i and a glue such that Phi strictly
   decreases," with a termination/strict-drop argument. This is an honest open inequality (NOT yet
   proven) but is the cleanest lever and is the genuine crux for all of Angles 2/3.

3. The hypothesis maxbias<1/2 enters ONLY as: every per-coordinate odds o_i = p_i/(1-p_i) < 1, so the
   diagonal odds-squaring o->o^2 strictly contracts. The proof must show this diagonal contraction
   dominates the (uncapped) conditional riser growth, either after finitely many glues (induction +
   strictly decreasing Phi) or in a k->infinity limit on the compact set {maxbias <= 1/2 - eps}
   (Angle 3). The builder should pick whichever framing makes "contraction dominates riser growth"
   cleanest, and must treat it as the one obligation to discharge.

Note for the builder: do not promise "one uniform construction" in the writeup — it provably does
not exist. Frame the deliverable as a P-dependent construction (the partition is chosen as a function
of P via the potential/argmax rule), which still fully satisfies the theorem's existential statement
("there exists k and S").
