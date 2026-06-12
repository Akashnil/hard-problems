# Progress — problem_11

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
