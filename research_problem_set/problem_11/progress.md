# Progress — problem_11

- R6 (builder, pending critic verification): BUILT the approved orbit-aggregate `(†)` angle and
  discharged the approach-critic's CHANGES-REQUESTED obligation. Theorem still NOT proved; the gap
  (★)/(B3-a′) is UNCHANGED and OPEN, but is now MAPPED PRECISELY by three RIGOROUS new facts
  (certificate `b3_round6.py`, all reproduced): (R6-T1, PROVED) the `(†) SLACK_O > BIASGAP` framing
  is a TAUTOLOGY — `SLACK_O − BIASGAP = log(∏P(e_i)/∏_s P(S^s y))` exactly (the `bias_i` cancel by
  the R5-2 incidence collapse; verified |err|<7e-15), so `(†)` carries ZERO information beyond the
  bare product inequality (B3-a′), and "cap BIASGAP from above" is not a strategy (the critic's
  warning, now formal). (R6-T2, PROVED via explicit full-support certificate) N7 (all-single-glues-
  fail, the source of the `(UB)` caps) does NOT imply (B3-a′): `P3=[.26314,.22514,.06373,.12761,
  .01397,.03575,.19734,.07332]` is full-support, mb=0.462<1/2, satisfies N7, yet ∏_s P(weight-2)
  =9e-4 > 2e-4=∏P(e_i); it is k=2-reducible (whole-collapse→0.072), so correctly not a residual.
  This RIGOROUSLY KILLS the (UB)-from-N7-only route (exactly the critic's objection). (R6-T3, PROVED
  via explicit full-support n=4 certificate) the cleanest two-constraint candidate {N7, whole-
  collapse-failure (WC)} holds on all 89 residuals and is conjecturally sufficient at n=3 (no
  counterexample in >1e7 trials + SA, worst margin >0.13), but is PROVABLY INSUFFICIENT at n≥4:
  explicit full-support P on {0,1}^4 (mb=0.4898<1/2) satisfies N7 ∧ (WC) yet violates (B3-a′)
  (margin -1.87) and is k2-reducible (best 0.4375) by a partial absorb-block. => NO FIXED FINITE
  conjunction of k=2 move-failures is uniformly sufficient; the minimal sufficient set GROWS with n.
  EXACT GAP (restated, with margins): prove ∏_s P(S^s y) < ∏_i P(e_i) for every full-support
  residual and ham(y)≠1; 0 viol on 89 isolated + 60 fresh near-mb=1/2 residuals, min rel margin
  0.167 (n=3)/0.866 (n=4), critic SA true-residual margin ≈0.094 at mb≈0.4997. Missing: a derivation
  that consumes the residual hypothesis GLOBALLY (the A3a per-block disjunction over the whole Bell
  lattice), not any bounded family of caps. Files: proof.md (§"Hard step (expanded, R6)", Gap, table,
  banner), b3_round6.py (new certificate; b3_round5.py untouched). NOT a proof.

- R6 (critic-verified): CONFIRMED all three R6 structural advances by INDEPENDENT re-derivation
  (my own conditioning/orbit/glue/slow-Bell-lattice code, not b3lib/harness); theorem still NOT
  proved, no overclaim, gap (★)/(B3-a′) UNCHANGED and OPEN. (R6-T1, PROVED) the identity
  SLACK_O − BIASGAP = log(∏P(e_i)/∏_s P(S^s y)) reproduced independently to |err|=7.1e-15 on all
  89 residual orbits (bias_i cancel by R5-2 incidence, verified symbolically) => (†) SLACK_O>BIASGAP
  IS (B3-a′) verbatim, carries zero information; the v2 angle's hard step ("cap BIASGAP from above,
  SLACK dominates") is therefore CIRCULAR -- it bounds one side of an identity by the other. T1 does
  NOT touch the (★)->(B3-a′)->(B3-a)->theorem reduction chain (sound, unaffected); it only kills the
  (†)-decomposition tactic. (R6-T2, PROVED via explicit full-support certificate) P3=[.26314,.22514,
  .06373,.12761,.01397,.03575,.19734,.07332] independently confirmed full-support (minP=0.0140),
  mb=0.462<1/2, satisfies N7, VIOLATES (B3-a′) (∏_s P(wt-2 orbit) > ∏P(e_i)), and is k=2-reducible
  to 0.072 by my own slow Bell-lattice search (so correctly NOT a residual) => N7-alone (the (UB)
  source) is rigorously insufficient. (R6-T3, PROVED via explicit full-support n=4 certificate)
  re-ran the n=4 search with my own conditioning code (seed 9090): full-support P (minP=0.0023,
  mb=0.4898<1/2) satisfies N7∧WC, violates (B3-a′), k=2-reducible to 0.4375 (own slow Bell-lattice)
  => {N7,WC} insufficient at n=4 (PROVED); the broader "no FIXED finite k=2-failure set is uniformly
  sufficient / minimal sufficient conjunction grows with n" is a sound STRUCTURAL inference from the
  n=3-suffices(conjectural)/n=4-fails(proved) data point, correctly labeled as the obstruction map,
  not a proved universal lemma. INDEPENDENTLY re-verified: (UB) holds 95/95 and binding 95/95 on
  realized n=3 riser pairs; all 89 .pkl residuals satisfy N7∧WC; sampled .pkl entries (8/8 n=3) are
  GENUINE residuals (no k=2 reduction via own slow Bell-lattice); B3-a' holds on all residuals
  (worst dedup rel margin 0.835 n=3 / 0.9998 n=4). FRESH critic counterexample hunt: 80 NEW genuine
  slow-Bell-lattice residuals up to mb=0.4969, 0 violations of (B3-a′), worst rel margin 0.872 --
  beat the builder's near-mb=1/2 search, still no counterexample (B3-a′ remains true and open).
  b3_round5.py reproduced EXACTLY (★ min rel margin 0.167/0.866/0.976). CHANGES REQUESTED (milestone:
  T1/T2/T3 verified; the multi-round (†)/finite-reduction strategy is now PROVED a dead end for
  closing (★) -- a global residual argument is required).

- R5 (builder, pending critic verification): BUILT Angle 1 (orbit-AVERAGE reduction of B3-a′).
  Theorem still NOT proved. The (B3-a) half is reduced to a SINGLE clean scalar gap (★), and the
  marginals are PROVED insufficient to close it. New PROVED lemmas (all verified, general where
  stated): (R5-1) monotone-support bound P(z)≤min_{i∈supp}bias_i≤GM_supp(bias_i), and P(z)≤q_i for
  i∉supp (general, 0/159000); (R5-2) cyclic incidence — each coord is 1 in exactly w of the n shifts
  of a weight-w pattern (combinatorial, n=3..6); (R5-3, NEW) shift-product cap ∏_s P(S^s y) ≤
  ∏_i bias_i (and sharper ∏_i bias_i^{w/n} q_i^{(n-w)/n}) — PROVED from R5-1+R5-2+AM-GM, GENERAL
  (0/159000); (R5-4) orbit AM-GM ∏_s P(S^s y) ≤ P̄_O^n, SAFE direction (78/78,315/315,7/7). Top-level
  chain CLOSED to one gap: ∏_s P(S^s y) =[R4-1] (∏_O P)^{n/d} ≤[R5-4] P̄_O^n <[★, OPEN] G(O_1)^n =
  ∏_i P(e_i) = (B3-a′). The OPEN gap is now the SINGLE inequality (★) P̄_O < G(O_1) for orbit weight
  ≠1 (P̄_O = orbit-average mass, G(O_1)=(∏_i P(e_i))^{1/n}); certified 0 viol on 90 isolated + 40
  fresh n=3 residuals, min rel margin 0.167 (n=3), 0.866 (n=4), 0.976 (n=5). CONFIRMED the surveyor's
  M_w/d route is BROKEN (M_1/d≥G(O_1) 100%, M_w/d≥P̄_O 100% — intermediate strictly stronger than ★,
  false). KEY NEW RIGOROUS NEGATIVE RESULT: R5-3 proves the MARGINALS bias_i CANNOT close (★)/(B3-a′)
  — any per-element bound aggregates (via cyclic incidence) to a product of per-coord factors, capped
  at ∏bias_i ≥ ∏P(e_i)=G(O_1)^n (overshoots by ∏bias_i/P(e_i), up to 25:1/coord); and (★) fails ~55%
  on GENERAL mb<1/2 P, so the JOINT residual hypothesis is load-bearing and not expressible via
  marginals. This pins what a closing argument must use (joint k=2-failure mass constraints, not
  marginals, not layer mass M_w). Also verified bracketing facts: P̄_O<AM_i(e_i) (stronger than ★ via
  AM≥GM, but only equals ★ when d=n; 0 viol), P̄_O<max_i(e_i) (0 viol), singletons P(0^n),P(1^n)<G(O1)
  (0 viol). Files: proof.md (§"Hard step (expanded, R5)"), b3_round5.py (new certificate). NOT a proof.

- R4 (builder, pending critic verification): BUILT Angle 1. Theorem still NOT proved; two EXACT
  reformulations + one strict reduction added, all numerically certified 0 violations on the 90
  SLOW-verified residuals (b3_round4.py). (1) (B3-a) rewritten EXACTLY as the shift-product
  inequality via PROVED combinatorial identity G(O)=(∏_{s=0}^{n-1}P(S^s y))^{1/n}: for ham(y)≠1,
  ∏_s P(S^s y) < ∏_i P(e_i) [B3-a']. Folds singletons 0^n,1^n into one statement (no separate
  smallness sub-arg). Certified 130/130 n=3, 756/756 n=4, 27/27 n=5. STILL OPEN: per-pattern
  P(y)<G(O_1) fails 3/26; the log-supermodular bound P(y)P(0^n)^{w-1}≤∏_supp P(e_i) (0 viol on all
  residuals) goes the WRONG way after multiplying over shifts. (2) (B3-b) mb>1/n rewritten EXACTLY
  as E[ham]>1 via PROVED decomposition E[ham]-1=Σ_{ham≥2}P(x)(ham-1)-P(0^n). (3) PROVED riser bound
  bias_j'≤p_j q_i/(p_i²+q_i²) (direction re-verified, 0/382). (4) PROVED conditional chain: combine
  whole-collapse-failure P(1^n)≥√(mb/(1-mb))P(0^n) (A3a, direction re-verified 90/90) with the
  decomposition => n·mb≥E[ham]≥1+[(n-1)√(mb/(1-mb))-1]P(0^n), so mb>1/((n-1)²+1) ⇒ E[ham]>1 ⇒ mb>1/n
  [B3-b'']. This RETIRES the round-3 boundary-degeneracy obstruction (union bound P(0^n)≥1-n·mb → 0
  at mb=1/n is replaced by the no-degeneracy whole-collapse bound) and reduces (B3-b) to the strictly
  weaker mb>1/((n-1)²+1) (1/5 vs 1/3 at n=3). STILL OPEN: even the weaker bound needs the residual
  CONJUNCTION — single-glue alone fails 44/889 over E[ham]≤1; single-glue+whole-collapse+all
  permutation-glues cover all 850 E[ham]≤1 candidates (0 uncovered). SLOW-test contrapositive: 917
  full-support P with E[ham]≤1, 0 residuals (worst 0.44·mb) — boundary NOT tight, bound TRUE w/ margin
  but no closed multi-move chain yet. Per approach-critic: did NOT cite the fast-test "1.0000001"
  figure (fast_is_residual_k2 false-positive near boundary); all R4 residual claims use slow is_residual.
  Files: proof.md (updated, §"Hard step (expanded, R4)"), b3_round4.py (new certificate). NOT a proof.

- R3: BUILT Angle 1 (mass-concentration close of B3). PROGRESS, theorem still not proved. Lemma B3
  SHARPENED into two certified scalar sub-claims: (B3-a) on a residual the geomean-maximizing cyclic
  orbit is the weight-1 orbit O_1={e_1,...,e_n} (so ham(O*)/n=1/n), and (B3-b) mb>1/n. Trivially
  (B3-a)&(B3-b) => ham(O*)/n=1/n<mb = Lemma B3. Both certified with ZERO violations on EVERY isolated
  residual: n=3 26/26, n=4 63/63 (n=4 residuals now EXHIBITED via targeted hunt biasing weight-1 mass
  + tiny P(0^n) — refutes prior "0 n=4 residuals"; O* is weight-1 on ALL of them, refuting the R2-critic
  worry that an interior weight-2 orbit ham/n=0.5>=mb could be O*), n=5 1/1, spec residual incl. Margins
  mb-1/n>=0.039, runner-up/winner orbit geomean <=0.0011 (mass-concentration extreme, not borderline).
  CORRECTIONS: (i) A3b reworded as a property of the Rule-R loop (absorption NOT coord-monotone), per
  R1 critic. (ii) Step-2 mechanism re-derived: the survey's A3a "both-sides squeeze" is BACKWARDS
  (whole-collapse failure gives P(1^n)/P(0^n)>=sqrt(mb/(1-mb)), the OPPOSITE direction); the real content
  is P(0^n),P(1^n) tiny in ABSOLUTE value (<=6e-3 vs G(O_1) in [0.07,0.32]) so singletons lose the geomean.
  (iii) DEAD-END RE-ATTRIBUTION: the "orbit-vs-complement fails" dead end is the IRRELEVANT singleton pair
  (0^n,1^n) [G(0^n)>=G(1^n) fails 21/26]; the RELEVANT weight-1>weight-2 comparison HOLDS 26/26. STILL OPEN:
  (B3-a) is a geomean-level (not per-pattern: per-pattern suff cond fails 3/26 at n=3) aggregate fact; (B3-b)
  whole-collapse reduces all mb<=1/n cases (3103/3103 n=3, 370/370 n=4) but union bound P(0^n)>=1-n*mb degrades
  to 0 at mb=1/n so no boundary-tight proof. Files: proof.md (updated), b3lib.py, fast_residual.py,
  b3_certificate.py, res_n{3,4,5}.pkl. NOT a proof of the theorem.

- R1: VERIFIED independently — S0 (S<->partition-constant), S1 (positive prob via 0^n), A1 & A3
  closed-form marginals (re-derived to 1e-15), A2 symbolic odds-squaring o->o^2 (sole use of
  mb<1/2), A3a/A3b block contraction, B1 cyclic equal-marginals+orbit formula, B2 geomean limit.
  Rule R terminates in <=n rounds (B strictly grows; 0 growth violations/30000) and reduces
  maxbias when it stops below mb. CAVEAT: absorption is NOT coordinate-monotone (65 new-riser
  events) — the Rule-R re-check loop, not a single absorption, is what is correct (A3b should be
  restated). Spec n=3 residual P=[.0352,.3315,.4299,.00033,.0545,.1069,.00028,.0415] confirmed a
  GENUINE residual (full Bell-lattice k=2 search = identity, no reduction); cyclic b*=0.3347 at
  k=3 reduces. B3 verified on 189 independently-found n=3 residuals (ham(O*)/n = 1/3 always,
  mb in [0.373,0.493]); residual hypothesis is load-bearing (B3 conclusion fails 23/2012 for
  general mb<1/2 P). 0 total failures of the combined construction in 8424 trials. GAP: Lemma B3
  (residual => tie-avg ham(O*)/n < mb) remains OPEN — aggregate weighted fact, not termwise;
  orbit-vs-complement rearrangement false on residual. Could neither close nor refute it.

- R3 (critic-verified): INDEPENDENTLY confirmed the B3 reduction is LOGICALLY SOUND and non-circular —
  (B3-a)[O*=O_1, UNIQUE: runner-up/winner geomean <=0.0011 so tie-averaging is moot] & (B3-b)[mb>1/n]
  => ham(O*)/n=1/n<mb = Lemma B3, and B2 then gives a finite k=mn with b*<mb (re-derived b* from orbit
  weights = brute force, b*->1/3<mb for spec). Re-implemented residual test + B3 checks from scratch:
  reproduced 26/26 (n=3), 63/63 (n=4), 1/1 (n=5) zero violations; independently re-verified all 26 n=3
  and 8 sampled n=4 .pkl entries are GENUINE residuals via full Bell-lattice k=2 search (n=4 residuals
  real, refuting R2 worry). Fresh adversarial hunt: 4.4M trials surfaced 4371 NEW n=3 residuals, 0
  violations of B3-a/B3-b (min mb=0.3459>1/3). A1/A3 closed forms and A2 symbolic factorization re-checked.
  Confirmed Step-2 (P(0^n),P(1^n) small, NOT backwards A3a) and A3a-direction correction (whole-collapse
  failure => P(1^n)/P(0^n)>=sqrt(mb/(1-mb)), 26/26 & 63/63). NOTE prose "P(0^n),P(1^n)<=6e-3" is loose:
  n=3 residuals reach P(1^n)=0.053, P(0^n)=0.020 (still << G(O_1) in [0.107,0.33], qualitative point holds).
  (B3-a),(B3-b) GENUINELY OPEN (no hidden proof, no overclaim); theorem NOT proved.

- R4 (critic-verified): CONFIRMED the round-4 advances; theorem still NOT proved, no overclaim. Independently RE-DERIVED all four new claims from scratch: R4-1 orbit-geomean=shift-product G(O)=(∏_s P(S^s y))^{1/n} [PROVED: n shifts hit each of d orbit elts n/d times, exact ✓]; R4-2 riser bound bias_j'≤p_j q_i/Z [PROVED via a_1 p+a_0 q=p_j q+a_1(p_i-q_i), p_i<q_i ⇒ direction is an UPPER bound, 0 viol]; R4-3 decomposition E[ham]-1=Σ_{ham≥2}P(ham-1)-P(0^n) [PROVED exact ✓]; R4-4 A3a whole-collapse-fail P(1^n)≥√(mb/(1-mb))P(0^n) [direction re-derived: residual ⇒ NOT reduced ⇒ A1/A0≥√, 90/90 ✓]. Conditional chain n·mb≥E[ham]≥1+[(n-1)√(mb/(1-mb))-1]P(0^n) verified PROVED algebra; the implication mb>1/((n-1)²+1)⇒mb>1/n is sound & NON-circular (1/((n-1)²+1)<1/n strictly for n≥3, so B3-b'' is genuinely WEAKER yet implies B3-b — the residual A3a bound supplies the gap; bracket>0⇔mb>1/((n-1)²+1) verified symbolically). b3_round4.py reproduced EXACTLY (n=3 26/26 all 7 lines, n=4 63/63, n=5 1/1). .pkl residuals re-confirmed GENUINE via slow Bell-lattice (sampled 11/90). FRESH critic hunt (slow test, prescreened): 289 NEW n=3 residuals, 0 violations of B3-a'/B3-b''/B3-b, min mb=0.3714. No "1.0000001" fast-test figure cited. STILL OPEN: B3-a' (∏_s P(S^s y)<∏_i P(e_i) for ham(y)≠1) and B3-b'' (mb>1/((n-1)²+1)) — both genuine aggregate residual-conjunction facts, no elementary proof. Verdict CHANGES REQUESTED (milestone).

- R5 (critic-verified): CONFIRMED the round-5 advances; theorem still NOT proved, no overclaim. INDEPENDENTLY re-derived every new R5 claim with my OWN code (rebuilt patterns/biases/shifts/orbits, not b3lib): R5-1 monotone-support P(z)<=min_supp bias_i<=GM_supp (0/159000, +min<=GM step 0/159000); R5-2 cyclic incidence (n=3..7); R5-3 shift-product cap prod_s P<=prod bias_i [direction CORRECT] (0/159000, per-shift log bound P(y)<=GM_supp 0/44000); R5-4 orbit AM-GM prod_s P<=Pbar^n [SAFE direction product<=mean^d, NOT the reversed log-supermodular] verified on GENERAL P 0/36000 + rel-tol 0/160000; R4-1 identity re-confirmed exact (1e-19). REDUCTION (B3-a')<==(star) is SUFFICIENT and NON-CIRCULAR: 0/160000 genuine sufficiency counterexamples (Pbar<G but prod_s P>=prod P(e_i)) under relative tolerance; (star) is sufficient but not necessary (5065 cases B3-a' holds while star fails) -- a legitimate strict strengthening, not a backwards/weaker variant. (star) is DISTINCT from the dead per-pattern bound (per-pattern P(z)<G fails 3 orbits at n=3, star holds 0 -- averaging repairs the failures). NEGATIVE result VERIFIED: prod bias_i>=prod P(e_i) always (0/6000; bias_i>=P(e_i) 0/24000) so marginal cap overshoots, and (star) fails on majority of general mb<1/2 P (I measured 85% vs builder's ~55% -- regime-dependent, strengthens the claim); does NOT undermine the reduction. b3_round5.py reproduced EXACTLY (min rel margin star 0.167/0.866/0.976 n=3/4/5). FRESH slow Bell-lattice hunt: 50 NEW n=3 residuals (disjoint from .pkl), 0 violations of star/B3-a'/R5-3/R5-4, min mb=0.360. Sampled .pkl residuals re-confirmed GENUINE via my own slow search (5/5 n=3, 5/5 n=4). NOTE: a first abs-tol sufficiency test showed 123 false positives on ~1e-22 degenerate masses -- artifacts, 0 under rel-tol. STILL OPEN: (star) [joint residual fact, marginals proved insufficient] and (B3-b'') [deprioritized, natural chains circular]. Either + B2 closes the theorem. CHANGES REQUESTED (milestone).
