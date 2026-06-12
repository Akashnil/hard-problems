# Proof review — Round 1 (problem_11)
Verdict: CHANGES REQUESTED

The conclusion targeted matches the theorem EXACTLY: exhibit k>=1 and pair set S so that
P' = P^k | {X_u=X_v on S} has maxbias(P') < maxbias(P), for every full-support P on {0,1}^n
with maxbias(P) < 1/2. The reduction to "force a partition constant" (S0) is correct and the
conclusion is the right existential statement. The proof is structurally sound and substantially
correct, but is INCOMPLETE: it bottoms out in one genuinely open inequality (Lemma B3). I
independently confirmed every other lemma and could not close B3 (nor refute it).

### Step verdicts
- S0 (S <-> force connected components constant): VERIFIED — transitive closure of X_u=X_v is
  exactly component-constancy; standard and correct.
- S1 (positive probability via all-0^n config): VERIFIED — full support gives P(0^n)^k>0, in
  every conditioning event; well-definedness holds for all moves.
- A1 (single-glue closed form bias_i=p^2/Z, bias_j=(a1 p+a0 q)/Z): VERIFIED — re-derived with my
  own brute-force conditioning, max error 3.3e-16 over 30 random n=3 instances (independent of the
  builder's harness).
- A2 (diagonal odds-squaring o->o^2, strict drop, sole use of mb<1/2): VERIFIED — symbolic
  factorization p - p^2/(p^2+q^2) = p(p-1)(2p-1)/(2p^2-2p+1) reproduced; sign is + for 0<p<1/2.
- A3 (absorb-block closed form, u in B: A1^2/Z; u not in B: (A0 Su0+A1 Su1)/Z): VERIFIED —
  re-derived independently, max error 5.6e-16 over 30 random n=4 instances with random blocks.
- A3a (block contraction iff A1/A0 < sqrt(mb/(1-mb)); whole-collapse): VERIFIED — algebra correct;
  mb<1/2 makes threshold <1, so whole-collapse can apply.
- A3b ("absorbing kills the riser reweighting"): VERIFIED with a CAVEAT (see below) — the
  mechanism is real but the one-line narrative is imprecise; the Rule-R loop is what is actually
  correct.
- Rule R (start B={argmax}, absorb all coords >= mb, repeat): VERIFIED — terminates in <=n rounds
  (B strictly grows on every non-terminal round: 0 growth violations in 30000 trials); when it
  stops with all marginals < mb it genuinely gives maxbias(P')<mb.
- B1 (cyclic k=n equal marginals + orbit formula b*): VERIFIED — Certificate 4 reproduces
  (all-equal 20/20, formula 20/20).
- B2 (geometric-mean limit b*_{mn} -> ham(O*)/n): VERIFIED — Certificate 5 reproduces (8/10 within
  1e-3, slack is finite-m rate near ties; on the spec residual b* already drops at k=n).
- B3 (residual => tie-avg ham(O*)/n < mb): GAP (OPEN) — strong numerical support, no proof.

### Hard step re-derivation
(1) Riser control (Move II / Rule R) — CLOSED, with a correction to the builder's narrative.
I independently re-derived A1 and A3 to machine precision. I then tested whether absorbing a
riser can RAISE a previously-below-mb coordinate above mb (i.e. create a NEW riser). It CAN:
65 such events in 30000 trials. So A3b's claim that absorbing "kills the riser" is not monotone
coordinate-wise. HOWEVER Rule R re-checks ALL coordinates each round and re-absorbs any new
risers, and B strictly grows each non-terminal round, so the procedure still terminates in <=n
rounds and, when it stops with all marginals < mb, correctly yields maxbias(P')<mb. The
load-bearing claim ("Rule R is a correct, terminating procedure that reduces maxbias whenever it
stops below mb") is therefore VERIFIED. The fix needed is presentational: A3b should be restated
as a property of the loop, not of a single absorption.

(2) Backstop (B3) — I attempted to close it and FAILED, but extracted structure.
Across 67+122 independently-found n=3 residuals (P where my full Bell-lattice k=2 search reduces
nothing), the geometric-mean-maximizing cyclic orbit is ALWAYS the weight-1 orbit, ham(O*)/n =
1/3 EXACTLY, and every residual has mb in [0.373, 0.493] > 1/3 (min margin mb - 1/3 = 0.0395).
So for n=3, B3 reduces to two concrete sub-claims: (a) residual => dominant geomean orbit is
weight-1 (ham/n=1/3), and (b) residual => mb > 1/3. I could prove neither in general, and the
proof's documented obstruction stands: the natural orbit-vs-complement rearrangement is FALSE on
the residual (so b* < mb is an aggregate weighted fact, not termwise). B3 remains open.

### Missing cases
- Dispatch exhaustiveness: VERIFIED — combined construction = (best k=2 partition if it reduces;
  else cyclic backstop). The "residual" is well-defined (full Bell-lattice search over 2n coords).
  Every P is in exactly one branch. Conditional on B3, all P are covered.
- n=1, n=2 (backstop vacuous / never needed): consistent with proof; n=2 never hits residual.
- Ties at argmax: handled — Rule R's test uses >= mb so coords tied at mb are absorbed,
  guaranteeing STRICT final inequality. VERIFIED.
- Z=0 / degenerate blocks: full support => A0,A1>0 for whole-collapse; for partial blocks A_v can
  be 0 but A3 handles via Z=A0^2+A1^2>0 unless block has no all-0 AND no all-1 pattern; full
  support guarantees both exist, so Z>0. Fine.

### Hidden assumptions
- A3b non-monotonicity (above) — flagged, not fatal.
- B2 consequence uses the LIMIT being < mb to get a finite m; this is valid (limit strictly below
  => some finite m below), and verified directly on the spec residual (b*<mb already at k=n).
- No circularity: no step uses the conclusion. The residual hypothesis is genuinely load-bearing,
  CONFIRMED: B3's conclusion (ham(O*)/n < mb) FAILS for general mb<1/2 P in 23/2012 trials, so it
  truly needs "no k=2 reduces." This rules out a lazy proof of B3 from mb<1/2 alone.

### Computational checks (all re-run by me)
- Certificate suite final_verify.py: all 5 reproduce (C1 symbolic, C2/C3/C4 20/20, C5 8/10).
- Independent A1 brute-force: max err 3.3e-16. Independent A3 brute-force: max err 5.6e-16.
- Rule R: terminates, 0 growth violations / 30000; 2837/2850 succeed, 13 -> backstop.
- New-riser-creation: 65 events (A3b non-monotone) — re-check loop handles it.
- Spec n=3 residual P=[.0352,.3315,.4299,.00033,.0545,.1069,.00028,.0415]: full k=2 search best =
  identity (0.4802 = mb, NO reduction) -> genuine residual; cyclic b* = 0.3347 at k=3 -> reduces.
- n=3 residual B3 test: 122/122 and 67/67 satisfy ham(O*)/n < mb, 0 violations.
- B3 conclusion WITHOUT residual hyp: fails 23/2012 -> hypothesis load-bearing.
- Combined construction total-failure search: 0 failures / 8424 valid n in {2,3}.
- n=4 residual hunt: no residuals surfaced in sampling (Bell(8) search slow; consistent with the
  proof's own "0 residual at n=4").

### Counterexample search
Attempted to refute (a) the overall theorem and (b) B3. Targeted strongly anti-correlated /
weight-1-concentrated / 1^n-boosted near-boundary P at n=2,3,4. No counterexample to the theorem
(0/8424 combined failures) and no counterexample to B3 (0 violations on every residual found).
The theorem is almost certainly true and the construction is correct conditional on B3.

### Flaw (CHANGES REQUESTED)
- Step: Lemma B3 (the BACKSTOP inequality).
- Claim: if no k=2 set-partition of the 2n coordinates reduces maxbias, then the tie-averaged
  normalized Hamming weight of the geometric-mean-maximizing cyclic orbit is < mb.
- Why it fails to close: the implication is an aggregate weighted-average fact, not termwise; the
  orbit-vs-complement rearrangement is false on the residual; no derivation of "residual =>
  geomean maximizer has low Hamming weight" exists. (It is TRUE numerically — 0 violations — and
  the hypothesis is provably load-bearing, so this is a real gap, not a wrong step.)
- Suggested fix: prove the two concrete n=3 sub-facts and generalize: (a) residual => the
  geomean-maximizing orbit is supported on patterns of Hamming weight < n*mb; most promising via
  the cyclic-product weight symmetry (w is S-invariant) combined with the explicit failure of
  EVERY whole-block collapse (A3a threshold violated for all blocks) forcing P's mass onto
  low-weight patterns; (b) residual => mb > ham(O*)/n directly. Alternatively replace the cyclic
  backstop with a residual move whose reduction is an explicit polynomial-sign condition
  analogous to A3a. Also: restate A3b as a property of the Rule-R loop (absorption is not
  coordinate-monotone; the loop, not a single absorption, is what is correct).

### Progress logged
- R1: A1/A3 closed-form marginals re-derived independently to 1e-15; A2 symbolic odds-squaring,
  S0/S1, B1/B2 orbit formula+limit all confirmed; Rule R terminates in <=n rounds (B strictly
  grows) and reduces maxbias when it stops below mb (absorption is NOT coord-monotone — 65
  new-riser events — but the re-check loop handles it); spec n=3 residual confirmed genuine; B3
  holds on all 189 independently-found n=3 residuals with ham(O*)/n=1/3 and is load-bearing
  (fails 23/2012 without residual hyp); 0 total failures of the combined construction in 8424
  trials. Remaining gap: Lemma B3 (residual => ham(O*)/n < mb) — OPEN.
