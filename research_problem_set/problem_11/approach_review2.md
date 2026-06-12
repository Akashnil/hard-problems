Verdict: CHANGES REQUESTED

Angle reviewed: CORRECTED spec — P-dependent construction = (primary) best k=2 partition
minimizing the power-mean-of-odds potential Φ_p, plus (backstop) k=n full-cycle cyclic glue
when no k=2 partition reduces maxbias.

## Headline

The corrected spec is a genuine improvement over the refuted Angle 1 and its diagnosis is
correct: I independently confirmed (a) k=2 is genuinely insufficient (the stated n=3
counterexample is real), (b) the dispatch's two "cleaner" alternatives are dead, and (c) the
k=n cyclic backstop fixes every k2-insufficient case found. The theorem is true and the
construction is the right *shape*.

BUT the spec as written does NOT hand the builder a complete proof. It hands two
0-failure-but-UNPROVEN inequalities, and the one mechanism that is empirically airtight (the
Central Lemma on Φ_p) is provably the WRONG target: I found explicit cases where the
Φ_p-MINIMIZING k=2 partition does not reduce maxbias and can even RAISE it. So neither route's
bridge to maxbias currently has a mechanism. This is fixable — there is a clean, verified, and
genuinely *constructive* target the builder should pursue instead (Sec "single cleanest
target" below) — hence CHANGES REQUESTED rather than RETHINK.

## The 7 checks

1. Proves the right thing: CONCERN — the Central Lemma proves Φ_p decreases, but the theorem
   asks for maxbias (= Φ_∞) to decrease, and the spec's bridge from Φ_p to Φ_∞ is not valid
   for the partition the lemma produces (see check 2 / verified data).

2. Hard step has a mechanism: FAIL — Route A's bridge ("a multiplicative drop in Φ_p forces
   the max strictly below maxbias") is FALSE for the Φ_p-minimizer. Verified (n=3, p=2): the
   Φ_2-minimizing k=2 partition fails to reduce maxbias in 7/324 trials (2.16%), with cases
   where Φ_2 drops 0.90→0.67 while maxbias RISES 0.4974→0.4998. At p=4 still 2/316 fail; at
   p=8, 1/314. Decreasing the power-mean does not pin the max for the partition that achieves
   the decrease. Route B's k=3 orbit bound (b* < 1/2) is only ASSERTED — the spec itself says
   "the proof-builder must turn this chain into an inequality (candidate: ...)" and offers a
   heuristic, not a proof.

3. Missing cases: CONCERN — (a) the backstop is specified as "k = n full cycle," not literally
   k=3; for n=2 that is k=2 (a subset of the k=2 partitions already searched), so the backstop
   would be vacuous if n=2 ever needed it — verified it never does (0/14977), so this is safe
   but the spec's "k=3" labeling is imprecise. (b) The b*<1/2 bound and "every k2-fail fixed"
   evidence is n=3-only in the spec; generality across n is not established mechanistically.

4. No circular reasoning: PASS — no step assumes the conclusion; the gaps are unproven
   inequalities, not circularity.

5. Certifiable: FAIL (as written) — both delivered routes bottom out in an inequality with no
   stated proof mechanism: Route A's Φ→max bridge is numerically false for the minimizer;
   Route B's orbit-density bound is "must turn this chain into an inequality." A builder handed
   these will get stuck exactly where Angle 1 got stuck — controlling the max, not a proxy.

6. Avoids dead ends: PASS — genuinely routes around the refuted fixed cyclic gadget by making
   the construction P-dependent and by isolating the k=2-insufficient residual; does not
   re-encounter the all-equal / parity dead ends.

7. Small-case sanity: PASS — independently verified: (i) the k=2-insufficient counterexample
   P=[.0352,.3315,.4299,.00033,.0545,.1069,.00028,.0415] has biases [.2032,.472,.4802], NO
   k=2 partition reduces maxbias (best stays .4802 over all 203 partitions), k=3 cyclic glue →
   .3347; (ii) diagonal P(x)^2 collapse fails 15.1%/32.3%/47.2% at n=2/3/4; (iii) best single
   free-coordinate glue fails ~4.5–5.1%; (iv) the Sec-3 orbit formula matches brute k=n maxbias
   80/80 and b*<1/2 in all 80 k2-insufficient n=3 cases (b* clusters at 1/3, max .4086);
   (v) the k=n cyclic backstop fixes 60/60 collected k2-insufficient n=3 cases.

## Why this is CHANGES REQUESTED, not RETHINK

The spec correctly identifies the construction (P-dependent: k=2 generically, k=n cyclic on a
measure-tiny anti-correlated residual). What is broken is only the chosen *proof lever* (the
Φ_p potential). The fix does not change the construction — it changes which lemma the builder
proves about it. There is a directly-verified, constructive replacement lever (below).

## Issues to fix (the single cleanest target for the builder)

DROP the Φ_p potential entirely as the load-bearing object. Φ_p is a red herring: it is
0-failure-decreasable but its decrease does not control maxbias (check 2). The honest crux is
the maxbias-of-the-riser inequality from Sec 4, attacked directly. Build exactly this:

- TARGET LEMMA (k=2, direct on maxbias). For every full-support P on {0,1}^n with
  maxbias(P)<1/2 that admits a maxbias-reducing k=2 partition, there is an EXPLICIT rule
  selecting such a partition. Recommended explicit rule to prove: take i* = argmax bias, glue
  coordinate i* across the two copies (diagonal o_{i*} ↦ o_{i*}² < o_{i*}, the only use of
  maxbias<1/2), and — this is the load-bearing addition — for every "riser" coordinate j whose
  conditional bias_j(P') would exceed maxbias(P), ALSO place j in i*'s block (force j,i*
  jointly constant, which kills the q_i/p_i reweighting on j). Prove that after grouping all
  such risers into one constant block, no coordinate exceeds maxbias(P) and i*'s bias strictly
  drops. The Sec-4 closed form bias_j(P') = [P(X_j=1,X_i=1)p_i + P(X_j=1,X_i=0)q_i]/Z is exact
  (verified) and the joint-constant block has the clean form
  P(block=1)·.../(P(block=0)+P(block=1)) — make the riser bound an explicit polynomial sign
  condition in the joint masses. The builder should first re-run this exact rule over the
  harness to confirm 0 failures BEFORE writing, then sign the polynomial.

- BACKSTOP LEMMA (the genuine open inequality, for the k2-insufficient residual). Prove the
  Sec-3 orbit bound directly: when NO k=2 partition reduces maxbias, the k=n full-cycle glue
  gives common marginal b* = (Σ_x w(x)ham(x)/n)/(Σ_x w(x)) with w(x)=Π_c P(S^c x), and b*<1/2.
  The orbit formula is exact (verified 80/80). The missing inequality is precisely
  Σ_{ham(x)<n/2} w(x) > Σ_{ham(x)≥n/2} w(x) under the k2-fail condition. The builder must show
  k2-insufficiency forces the cyclic-product weight w onto low-Hamming-weight orbits. This is
  the one honestly-open sub-lemma; it is small (cyclic-product weights, symmetric, n-variable)
  and should be attacked with the symmetry of w under S directly, not via Φ_p.

Recommended build order: prove the TARGET LEMMA first (it covers ~99.8%+ of P and is a finite
explicit polynomial-sign check — the most likely to close cleanly), then the BACKSTOP LEMMA for
the residual. Together they give maxbias(P')<maxbias(P) with k∈{2,n}, P-dependent, which is
exactly the existential statement. Do NOT route the proof through Φ_p decrease; it does not
imply the conclusion.

If, while building, the riser-block rule shows ANY failure on the harness (re-test before
proving), fall back to "best over all k=2 partitions" as the existence claim and prove
non-emptiness of the reducing set via the same riser bound — but the explicit
glue-i*-and-absorb-risers rule is the cleanest constructive candidate and should be tried
first.
