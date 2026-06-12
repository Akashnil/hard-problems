# Progress — problem_11

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
