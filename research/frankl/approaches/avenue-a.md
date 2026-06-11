# Approach: Avenue A — fractional unions P_t = Z^{-1} Q^t (Frankl-file entropy method)

## What this is
The Frankl-file's Avenue A: perturb the uniform law `A` on a union-closed family `F` into
the "fractional union" `P_t = Z^{-1} Q^t` (`Q` = domination-CDF, `Z` = zeta matrix), hoping
some `t = 1 + epsilon` gives `H[P_t] > H[A]` and a contradiction with "max bias < 1/2".

## Round 1 (verified)
LOCAL obstruction: `P_1` = uniform is the entropy maximizer; `dH/dt|_1 = 0` (feasibility),
`H''(1) = -(1/ln2) Σ (dP/dt)²/P_i < 0`. So `H[P_t] < H[A]` for `t` slightly above 1 wherever
`P_t >= 0` near `t = 1`. Valid only locally + small-n; signedness handled as a caveat.

## Round 2 (this round)
GLOBAL upgrade via Theorem 1 (H[X] <= log2|supp X|): *the instant `P_t` is a genuine
distribution, `H[P_t] <= H[A]` globally, family-independently, no derivatives.* Reduced the
"`P_t` distribution?" question to nonnegativity, and established:
- **PROVEN, unconditional:** integer-`t` anchor (`P_m` = law of OR of `m` iid uniform,
  Prop 3.1); additivity `P_{a+b} = P_a (*) P_b` via `Z(mu(*)nu) = (Zmu)(Znu)` (Prop 4.1);
  the **single-lemma reduction** — all-real-`t>=1` nonnegativity ⇔ lemma (L)
  `(P_1 (*) P_s)(x) >= 0`, `s in [0,1)` (Prop 5.1, with the `t->t+1` step being
  nonneg-convolution-of-nonnegatives for free).
- **PROVEN reduction, not closed:** lemma (L) reduces, via the Pick/Stieltjes
  representation `u^{1+s} = (sin πs/π)∫ u²/(u+l) l^{s-1} dl`, to the exponent-free
  inequality (L') `B_l(x) = Σ_{y<=x} mu(y,x) Q(y)²/(Q(y)+l) >= 0` for all `l>0`.
- **CONJECTURE (certified-numerically-but-UNPROVEN):** (L)/(L') on every union-closed
  family (incl. non-distributive). ~57 families, dense `s`/`l` grids, 0 failures, margins
  `+1.6e-3` (L) / `+2.7e-5` (L'); but finite enumeration cannot settle the for-all claim.

Result: global `H[P_t] <= H[A]` is UNCONDITIONAL at integer `t`, CONDITIONAL (on (L)) at
non-integer `t>=1`. No numeric bound moved; record 0.38271 (Liu) stands. Certificate:
`certificate_round2.py` (exit 0, non-vacuous). Full writeup: `obstruction-round2.md`.

## What would push it further
1. **Close (L').** Prove `B_l(x) = Σ_{y<=x} mu(y,x) Q(y)²/(Q(y)+l) >= 0` for all `l>0`,
   family-independently. Partial-fraction form: `B_l(x) = P_1(x) + l² Σ_{y<=x} mu(y,x)/(Q(y)+l)`
   for non-bottom `x`; the residual resolvent sum is sign-indefinite and needs a structural
   (submodularity-of-join / interval-Mobius) argument. No black-box theorem applies (the
   `t>=1` vs `t>0` cutoff shows `Q` is NOT max-infinitely-divisible). Closing this turns the
   whole global ceiling unconditional.
2. **Or prove (L) directly** as a smoothing statement: `(P_1(*)P_s)(x) = (1/|F|)Σ_a G_a(x)`,
   `G_a(x) = Σ_{a<=x'<=x} mu(x',x) Q(x')^s`; the `a=x` term is `Q^s(x) > 0`, other terms can
   be negative — need the average over `a` to be nonneg. NOT term-by-term (`M_F` sends ~76%
   of random signed vectors negative); the specificity of `P_s` is essential.
3. **Note:** even if closed, this moves NO numeric bound — it only makes the Avenue-A
   obstruction fully unconditional. Reaching 1/2 needs a different object (entropy two-sample
   method is capped near 0.382 by Chase-Lovett / Sawin / Liu — cited, not us).
