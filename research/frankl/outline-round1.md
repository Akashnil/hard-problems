# Round-1 outline — Frankl's union-closed conjecture (entropy approach)

## frankl
Spec review: required  (the recommended deliverable is an impossibility/obstruction writeup; its
load-bearing claim — that NO perturbation of uniform A can force H[C] > H[A] — must be stated as a
theorem with the right quantifiers, and the reviewer must confirm we are not "claiming a
contradiction by misusing the false hypothesis," which is exactly the run_state's forbidden move.)

Target to beat: 0.38271 = current table value (Liu, arXiv:2306.08824), moving the LOWER bound.
The conjecture target is 1/2 (delta = +0.117), OPEN.

---

### Independent sanity-check of the explorer's claims (done this round, re-runnable)

I re-derived the three load-bearing facts on concrete OR-closed families before relying on them:

- **H[C] <= H[A] is unconditional.** On every union-closed F I built (n=5,7, low-bias and
  high-bias), with A,B iid uniform and C = A OR B: C never escaped F, and H[C] <= H[A] held with
  margin (e.g. low-bias n=7 family: H[A]=3.16993, H[C]=2.53853). CONFIRMED.
- **Avenue A (Q_t = Q^t Mobius fractional union) lowers entropy.** For every t > 1 on every family,
  bias rises but H[P_t] strictly drops: t=1.05 -> dH=-0.0028, t=1.1 -> dH=-0.011, t=2 -> dH=-0.63.
  CONFIRMED (matches explorer's dH<0 finding).
- **Ceiling constants.** 1-1/phi = (3-sqrt5)/2 = 0.38196601125; Cambie sharp atom b2 = 0.32945
  (root of h(x)(2-h(x)) - h(2x-x^2)). Both reproduced. CONFIRMED.
- **One caveat on the explorer's "P_t is a signed measure for non-integer t" claim:** on the small
  non-distributive families I tested (e.g. the 7-element non-distributive OR-closed lattice
  {∅,{1},{2},{1,2},{1,3},{2,3},{1,2,3}}), P_1.1 stayed nonnegative. So "signed measure" is
  family-dependent, NOT universal. The obstruction does NOT need it — dH<0 already kills Avenue A
  even when P_t is a bona fide distribution. The writeup should phrase signedness as "can fail to be
  nonnegative on some non-distributive lattices" (a secondary defect), and rest the impossibility on
  max-entropy + dH<0, which are airtight.

Verdict: the explorer's strategic conclusion is sound. No realistic single-round improvement on
0.38271 exists via Avenue A/B or any "perturb uniform A" scheme; the honest deliverable is the
obstruction writeup.

---

### Recommended deliverable: (1) the rigorous OBSTRUCTION / IMPOSSIBILITY writeup.

Reason in one line: the goal's explicit fallback; every "improve 0.38271" angle below is either
provably capped below 1/2 by published sharp barriers or is a multi-round research program with no
within-round payoff, so honesty + a clean theorem is the maximal verifiable progress this round.

Angle 1 (top pick): Impossibility theorem for the Frankl-file program + ceiling survey + certificate
  Moves: neither bound numerically; delivers a *proven obstruction* (run_state's stated fallback).
  Skeleton:
    1. **Setup (cited/standard).** F finite, OR-closed, F != {∅}. A,B iid uniform on F. C = A OR B.
       State H[A] = log2|F|.
    2. **Lemma 1 (Support).** C is supported on F. — by OR-closure of F (a OR b in F for a,b in F).
       Trivial; prove in two lines.
    3. **Theorem 1 (Unconditional max-entropy ceiling — THE core claim).**
       For ANY random variable X supported on F, H[X] <= log2|F| = H[A], with equality iff X is
       uniform. Hence for ANY C supported on F (in particular C = A OR B, or any perturbation of A
       that stays on F): H[C] <= H[A], *independent of any hypothesis on the biases*.
       — by Gibbs'/Jensen's inequality (uniform maximizes Shannon entropy on a finite support).
       PROVE RIGOROUSLY (3-4 lines). This is the formal refutation of the Frankl file's directive.
    4. **Corollary (why the Frankl file is a category error).** The bias hypothesis max-bias < 1/2
       constrains the *coordinatewise conditional-entropy lower bound* sum_i E[h(p_i q_i)] on H[C];
       it does NOT and cannot raise the *actual* H[C] above H[A]. Gilmer's contradiction is
       "lower-bound-on-H[C] exceeds H[A]," never "H[C] itself exceeds H[A]." State both inequalities
       side by side so the inversion in the Frankl file is unambiguous.
       — by inspecting the direction of data-processing in Gilmer's chain-rule expansion (cited
       arXiv:2211.09055; restate the one chain-rule line).
    5. **Proposition A (Avenue A fails concretely).** Define Q(y)=sum_{x<=y in F} P(x), Q_t = Q^t,
       P_t by Mobius inversion (P_t = Z^{-1} Q^t on the lattice F). Then for integer t, P_t = law of
       OR of t iid uniforms; for t -> 1+, dH/dt < 0 (entropy strictly decreases) while every bias
       weakly increases. So Avenue A moves entropy the WRONG way and cannot give H[P_t] > H[A].
       — supported by the re-runnable certificate (below); the analytic dH/dt|_{t=1+} < 0 sign is the
       hard step (see Hard step).
    6. **Proposition B (Avenue B collapses).** With B concentrated on ∅ (mass 1-eps at 0^n),
       C = A OR B -> A in distribution as eps -> 0, so H[C] -> H[A]^- and bias(C) -> bias(A); there
       is no regime H[C] > H[A]. Additionally cite Ellis-Ivan-Leader 2023: the smallest-set
       intuition behind B provably fails (min frequency of the smallest set can be (1+o(1))log k/(2k)
       -> 0). — by continuity of H and the EIL construction (cited).
    7. **Ceiling survey (cited, exact statements).** Record the proven barriers of the *broader*
       entropy method so the writeup is self-contained:
         - iid OR method: tight at c = (3-sqrt5)/2 = 0.38196601125 (Alweiss-Huang-Sellke 2211.11504;
           Chase-Lovett approximate-union-closed sharp example).
         - Sawin dependent two-sample linear combination: EXACTLY c = 0.382345533366703, SHARP
           (Cambie 2212.12500 Subsec 2.3; sharp 2-atom distribution P(p=1)=a~0.0789, P(p=b)=1-a,
           b~0.32945 root of h(x)(2-h(x))-h(2x-x^2)).
         - Liu conditionally-iid coupling: c = 0.38271, the current record (2306.08824).
       State explicitly that all are < 1/2 and that Cambie's own paper says "another core method will
       be needed for the full resolution."
    8. **Conclusion.** The Frankl-file program (perturb uniform A to force H[C] > H[A]) is impossible
       by Theorem 1; the broader coordinatewise two-sample entropy method is capped well below 1/2 by
       the cited sharp barriers. Honest status: 0.38271 stands; 1/2 needs a different object.
  Hard step: **the analytic sign dH/dt|_{t=1+} < 0 for Avenue A in full generality** (Prop A, step 5).
    Mechanism: at t=1 P_t is uniform = the entropy maximum on F, so the first-order term in t-1 is a
    directional derivative of H *at its global max along a feasible (sum-1) direction*; the leading
    behavior is governed by the curvature (negative-definite Hessian -1/(ln2) sum dP^2/P of Shannon
    entropy), giving dH <= 0 with equality only if the perturbation direction is null. One must show
    the Q^t direction dP/dt|_{t=1} = Z^{-1}(Q ln Q) is NOT entropy-null (it is not, since it strictly
    changes biases), hence dH/dt|_{t=1+} < 0 strictly. This is the only step needing a real proof;
    the numerics already show it holds on every tested family.
  Check (computational certificate, must be re-runnable, no network):
    - Build several OR-closed F (random closures + the explicit non-distributive 7-element lattice).
    - Assert C = A OR B never leaves F and H[C] <= H[A] (with margin) on each.
    - Compute P_t = Z^{-1} Q^t for t in {1.05,1.1,1.3,2.0}; assert dH = H[P_t]-H[A] < 0 and
      max-bias(P_t) >= max-bias(A) (Avenue A wrong-direction certificate).
    - Avenue B: sweep eps -> 0 for B = (1-eps)·δ_∅ + eps·uniform; assert H[C] increases monotonically
      to H[A]^- and never exceeds it.
    - Recompute the three ceiling constants (1-1/phi; Cambie b2 root; print Liu 0.38271) to 1e-9.
    - Script lives at research/frankl/certs/obstruction_cert.py; prints PASS/FAIL per assertion.

---

### Improvement angles considered and why each is NOT recommended this round

Angle 2: Richer coupling beyond Liu (more auxiliary structure than conditional-iid).
  Moves: lower bound, hoping for > 0.38271. Skeleton would be: generalize Liu's auxiliary-variable
  conditioning to a 2- or 3-parameter family, set up the finite-dim optimization, certify the optimum
  via its KKT/dual. Hard step: proving the new optimization's value strictly exceeds 0.38271 AND that
  it is still a valid lower bound (the coupling must keep both marginals uniform on F and C on F).
  Why not now: Liu already optimized the natural conditional-iid class; any strict gain is a genuine
  research advance with no guarantee of being > 0.38271, and certifying a NEW analytic optimum
  rigorously in one build round is unrealistic. Cambie's sharp barrier (0.3823455 for the Sawin form)
  shows how thin the remaining slack is. Speculative, multi-round, likely sub-1/2 even if it works.

Angle 3: The |F OR F| > |F|^{c(eps)} expansion route (Cambie survey 2306.12351).
  Moves: lower bound. Skeleton: prove a polynomial expansion lower bound on the OR-product set when
  all biases < 1/2-eps, then convert to a bias bound. Hard step: the expansion exponent c(eps) and
  its conversion are conjectural and themselves believed to fall short of 1/2. Not within-round
  certifiable; belongs to a different (set-counting, not entropy) toolkit than the mandated approach.

Angle 4: Direct attack on 1/2 (the conjecture).
  Excluded. delta=+0.117 above record; no entropy variant has come within 0.11 of 1/2; run_state
  flags any "reached 1/2" as almost certainly a bug. Do not attempt.

---

Ranking: **Angle 1 (obstruction writeup) is the recommendation** — it is the only deliverable that is
both rigorous and completable in one round, it is the goal's stated honest fallback, and it converts
this round's verified negative results into a clean, reviewable artifact (theorem + cited ceilings +
re-runnable certificate). Fall back to Angle 2 ONLY in a later round and ONLY if a specific new
coupling is identified with a concrete reason to exceed 0.38271; do not start it speculatively now.
Angles 3 and 4 are out of scope / out of reach. Do NOT log any bound improvement this round — none is
honestly available.
