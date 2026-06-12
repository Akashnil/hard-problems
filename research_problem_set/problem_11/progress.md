# Progress — problem_11

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
