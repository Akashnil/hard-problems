# Round-2 outline (REVISED after CHANGES REQUESTED) — closing Avenue A globally + plain-language verdict (Frankl entropy approach)

## frankl
Spec review: required  (the deliverable rests on a NEW load-bearing structural theorem —
"P_t = Z^{-1}Q^t is a genuine probability distribution for every real t >= 1 on every
union-closed family." The TARGET is true and stress-tested clean by both the explorer and the
reviewer; but the proof MECHANISM is the open risk and the round-1 reviewer already flagged the
first proposed mechanism as FALSE. The revised hard step (averaging-into-the-cone) is non-obvious
and must be proven family-independently incl. non-distributive lattices, so review remains
required. The reviewer must also re-confirm we derive NO contradiction from the false bias
hypothesis, and that the deliverable never presents an unproven Theorem 2 as proven.)

Target to beat: 0.38271 = current record (Liu, arXiv:2306.08824), the LOWER bound.
No bound improvement is claimed or available this round. The deliverable upgrades the round-1
OBSTRUCTION (the run_state's honest fallback) from local to GLOBAL, and answers the user's
actual question in plain language. Round-1 logged 1 verified milestone; this round logs the
global-dichotomy upgrade as the next verified milestone (still no numeric bound moved — correct
and honest, the entropy "perturb uniform A" program is provably dead).

---

### REVISION NOTE (what the review changed)

The outline-review (CHANGES REQUESTED) confirmed: (a) the TARGET (Theorem 2: P_t >= 0 for all
real t >= 1, every union-closed family) is almost certainly true — ~37,500 families, zero
failures, t=1 cutoff comfortable (largest signed t<1 was 0.847, nothing signed in (0.9,1.0)); and
(b) the integer-anchor identity and the join-convolution additivity P_{a+b} = P_a (*) P_b hold
exactly. So the TARGET stays as the goal. BUT the previously-proposed mechanism — "P_t = P_1 (*)
P_{t-1} where the fractional remainder P_{t-1} is itself nonnegative because Q^{frac} is a
sub-idempotent join CDF" — is FALSE: the fractional remainder P_s for s in (0,1) is exactly the
SIGNED branch (P_0.3.min() = -0.0231 on the non-distributive lattice; I re-confirmed this round).
That false sub-mechanism is DELETED. It is replaced by the genuine mechanism: join-convolution
with the uniform measure P_1 is a SMOOTHING/AVERAGING operator that maps the specific signed
remainder P_{t-1} into the nonnegative cone — the "averaging-into-the-cone" lemma, which is the
real (and honestly hard) load-bearing claim.

---

### What I re-derived this round before ranking angles (re-runnable, done now)

I tested the structure directly on the concrete non-distributive family
F = {∅,1,2,12,13,23,123} (the canonical case where the Mobius function alternates):

- **P_1 = uniform** (1/7 on each element) — boundary of the cone, all mass nonneg.
- **Fractional remainder is genuinely SIGNED.** P_0.3.min() = -0.0231 — NOT nonnegative.
  This is precisely why the round-1 "nonnegative remainder" mechanism fails.
- **Convolution additivity holds exactly.** P_t = P_1 (*) P_{t-1} (np.allclose True) for
  t = 1.3, 1.7, 2.4, where (mu (*) nu)(z) = sum_{x|y=z} mu(x) nu(y) is join-convolution.
- **Convolving the signed remainder with uniform LIFTS it into the cone.** P_1 (*) P_0.3 has
  min = +0.0797 (= P_1.3.min()): a signed measure convolved with uniform comes out nonnegative.
  So the nonnegativity of P_t for t >= 1 is REAL but comes from the SMOOTHING action of P_1, not
  from the remainder being nonneg.
- **The averaging operator is explicit and column-stochastic.** M[z,y] = (1/m) #{x in F : x|y = z}
  (join-convolution with uniform = left-multiply by M). M's columns sum to 1; M maps the simplex
  to itself. The hard lemma is NOT "M maps every signed vector to nonneg" (false in general) —
  it is "M maps the SPECIFIC signed remainder P_s (s in [0,1)) to a nonneg vector." That
  specificity is the crux.

Verdict: the round-2 objective is achievable as a clean GLOBAL theorem; the entropy conclusion is
a one-line corollary of Theorem 1 the instant P_t >= 0. The ONLY hard part is the
averaging-into-the-cone lemma, now correctly identified.

---

## Angle 1 (top pick): Global dichotomy via the averaging-into-the-cone lemma (P_t >= 0 for t >= 1)

Moves: neither numeric bound. Upgrades the Avenue-A obstruction from LOCAL (dH/dt|_1=0,
H''(1)<0, small-n) to a GLOBAL, family-independent, hypothesis-free closure. Aims strictly past
the round-1 deliverable (which left exactly this caveat open), not past 0.38271 (no entropy
"perturb uniform A" scheme can move that — proven round 1).

Skeleton:
  1. **Setup (round-1, cited).** F union-closed, F != {∅}, encoded OR-closed in {0,1}^n. A uniform
     on F. Domination order x <= y = bitwise. Q(y) = Pr(A <= y) = (1/|F|)#{x in F : x <= y} is the
     CDF of A under <=. Zeta matrix Z[i,j]=1[F[j] <= F[i]]; Mobius inversion P = Z^{-1}Q.
     P_t := Z^{-1}Q^t (entrywise power), P_t(x) = sum_{y <= x} mu(y,x) Q(y)^t. — standard.
  2. **Integer anchor (cited, round-1, re-verified by reviewer for m=2,3,4).** For integer t = m,
     P_m is exactly the law of A_1 OR ... OR A_m (m iid uniform copies), because Pr(max <= y) =
     Q(y)^m and Mobius inversion recovers the pmf. Hence P_m is a genuine distribution on F.
  3. **Additivity / join-convolution identity (verified exactly this round and by reviewer).**
     Because Q^{a+b} = Q^a · Q^b entrywise, Mobius inversion turns the entrywise product of
     domination-CDFs into the join-convolution of the inverted measures:
     P_{a+b} = P_a (*) P_b, where (mu (*) nu)(z) = sum_{x | y = z} mu(x) nu(y). — algebraic
     identity, confirmed for (a,b) = (1,0.5),(1.2,0.8),(0.7,0.3),(2,1.5),(1,1) by reviewer and
     (1.3),(1.7),(2.4) by me this round.
  4. **Theorem 2 (THE new global claim — nonnegativity for all real t >= 1).** For every
     union-closed F and every real t >= 1, P_t = Z^{-1}Q^t is a nonnegative measure summing to 1
     (a genuine probability distribution on F). — proven via the averaging lemma in the Hard step.
  5. **Theorem 1 applies globally (one-line corollary).** Since P_t (t >= 1) is a distribution
     supported on F, Theorem 1 (round 1: H[X] <= log2|supp(X)| <= log2|F| = H[A], Gibbs/KL,
     hypothesis-free) gives **H[P_t] <= H[A] for ALL real t >= 1, every family, unconditionally** —
     with equality iff P_t = uniform iff t = 1. No derivative, no curvature, no small-n.
  6. **Global Avenue-A dichotomy (the deliverable statement).** For every real t and every
     union-closed F, exactly one holds: (i) t >= 1 => P_t is a genuine distribution on F and
     H[P_t] <= H[A] (Theorem 1); or (ii) t < 1 => P_t may be a SIGNED measure (then "H[P_t]" is
     undefined and Avenue A is not even a probabilistic construction; this branch is the WRONG
     direction anyway — t<1 lowers the bias, away from the conjecture's >= 1/2). Either way the
     file's t = 1+epsilon proposal lands in branch (i): a bona fide distribution with H <= H[A].
     **Avenue A is closed globally, no leaning on Taylor + n<=7 numerics.** The round-1
     H''(1) < 0 calculation is retained only as a corollary/consistency check (local shadow of
     the global H[P_t] <= H[A], equality at t=1).
  7. **Consolidation / plain-language verdict (part (2) of the objective).** Direct answer to the
     user: "Can Frankl's conjecture be solved via the Frankl-file approach?" — NO, now for a fully
     global reason. Three sentences in plain language: (a) the file asks to perturb the uniform
     distribution to push entropy UP, but uniform is the unique entropy maximizer on the family, so
     every in-family perturbation pushes entropy DOWN — H[C] <= H[A] always; (b) the file's own
     Avenue A (fractional unions) is, for t >= 1, a genuine distribution that therefore obeys
     H[P_t] <= H[A] for every family with no exceptions, and for t < 1 isn't a distribution at all;
     Avenue B collapses C -> A; (c) the broader two-sample entropy method is separately capped near
     0.382 by published sharp barriers (cited, not proved here), so 1/2 needs a genuinely different
     object. Keep (T) self-proven DISTINCT from (S) cited (round-1 guard).

Hard step: **Theorem 2 — P_t = Z^{-1}Q^t >= 0 for every real t >= 1 on every union-closed F.**
  Mechanism (corrected; this is now the genuine load-bearing argument):
  - Write t = 1 + s with s = t - 1 >= 0. By the additivity identity (step 3),
    **P_t = P_1 (*) P_{t-1}**, i.e. P_t = M_F · P_{t-1}, where M_F is the join-convolution-with-
    uniform operator M_F[z,y] = (1/|F|) #{x in F : x | y = z} (column-stochastic; maps simplex to
    simplex). [For s >= 1 induct: P_t = P_{floor(t)} (*) P_{t-floor(t)}; floor(t)>=1 is a genuine
    distribution by the integer anchor + integer convolution, so WLOG reduce to s in [0,1).]
  - The remainder P_{t-1} = P_s with s in [0,1) is in general a SIGNED measure (verified:
    P_0.3.min() = -0.0231). So nonnegativity of P_t is NOT inherited from the remainder. The
    load-bearing claim is the **averaging-into-the-cone lemma:** M_F maps the SPECIFIC signed
    measure P_s (s in [0,1)) to a nonnegative vector — equivalently, for every x in F,
    sum_{y} M_F[x,y] P_s(y) >= 0.
  - Why it should hold (the mechanism, one line): M_F = E_{w~uniform}[ shift-by-join-w ], so
    (M_F P_s)(x) = E_w[ P_s restricted/pushed forward along join with w ]. P_s is the Mobius
    inversion of the CDF-power Q^s; the join-smoothing exactly cancels the negative Mobius
    alternations of P_s because each negative coefficient mu(y,x)Q(y)^s at a "deep" element gets
    averaged against the strictly larger total CDF mass Q(x) >= Q(y) sitting above it. Formally:
    (M_F P_s)(x) = sum_{w in F} (1/|F|) P_s({y : y | w = x}); the inner sum is a *down-closed-style*
    aggregate of P_s that telescopes back to a nonnegative CDF-difference Q(x)^s - (lower terms),
    and the s in [0,1) concavity of u |-> u^s makes that difference nonneg (where s>1 it would not
    matter because those t are covered by the integer anchor). The cleanest concrete target for the
    builder: prove **(M_F P_s)(x) = sum over the order-filter generated structure that equals a
    nonnegative combination of CDF increments**, using submodularity of the join and concavity of
    u^s for s in [0,1). This is the identity to nail.
  - Why t >= 1 is exactly the cutoff (not t > 0): a true max-infinite-divisible distribution would
    give P_t >= 0 for all t > 0; here the signed t < 1 branch (largest signed t = 0.847; nonempty,
    1619/2395 families) shows Q is NOT generally max-inf-divisible, so classical Balkema-Resnick /
    max-inf-div characterizations do NOT apply as a black box. The cutoff arises because exactly
    ONE factor of P_1 (one full smoothing pass) is what lifts the signed remainder into the cone:
    t >= 1 guarantees at least one such pass; t < 1 has none.

  DO NOT use the deleted route: "the fractional remainder P_{t-1} is itself nonnegative because
  Q^{frac} is a sub-idempotent join CDF" — this is FALSE (the remainder is signed) and must not
  appear in the proof.

Check (re-runnable certificate, extends certificate_round1.py, no network):
  - Confirm the additivity identity: assert P_t == joinconv(P_1, P_{t-1}) (np.allclose) across
    many families and t, and assert P_t == joinconv(P_{floor t}, P_{t - floor t}).
  - Confirm the averaging lemma's CONTENT empirically: exhibit families where P_s (s in [0,1)) is
    signed (min < 0) yet M_F · P_s >= 0 — this is the phenomenon the analytic lemma must explain.
  - Confirm the SHARP cutoff: over >= 8000 random OR-closed families assert P_t >= 0 for a grid of
    t >= 1 (incl. 1+1e-4 ... 50) with ZERO failures, AND exhibit families signed for some t < 1
    (non-vacuity of branch (ii); largest observed signed t ~0.847).
  - For each nonneg P_t assert H[P_t] <= H[A] with margin (Theorem 1 corollary), margin -> 0 as
    t -> 1+ (consistency with H''(1) < 0).
  - Integer anchor: rebuild P_m by brute-force OR of m iid uniform samples for m=2,3,4 and assert
    P_m == Z^{-1}Q^m (np.allclose).
  - GUARDRAIL (keep explicit): the certificate is ILLUSTRATIVE. The universally-quantified
    Theorem 2 (all real t >= 1, all F, incl. non-distributive) CANNOT be settled by finite
    enumeration; the builder owes the analytic averaging-into-the-cone proof, not just the script.
    Non-vacuity: perturbing the t>=1 assertion to t>=0.5 must produce FAILs / exit 1.

---

## Angle 2 (declared fallback): monotone non-increasing entropy via Schur-concavity / majorization

Moves: same target (global closure of Avenue A), via a mechanism that SIDESTEPS proving
nonnegativity for ALL t. Honest caveat up front: this angle still ASSUMES P_t >= 0 on its
interval — it does NOT by itself close the signed t < 1 branch — and carries its own
family-independence burden (the majorization must be shown on non-distributive lattices too).

Skeleton:
  1. Restrict to the regime where P_t is a distribution (t >= 1, or any interval where P_t >= 0).
     [This assumption is the honest cost: Angle 2 is conditional on nonnegativity in its interval.]
  2. Show t |-> H[P_t] is monotone NON-INCREASING on [1, infinity), strict for t>1 — by showing
     dH/dt = -(1/ln2) sum_i (dP_i/dt)(ln P_i + 1) <= 0 for ALL t >= 1, using that P_t is a
     distribution, dP/dt = Z^{-1}(Q^t ln Q) sums to 0, and t=1 is the entropy max (uniform).
  3. Conclude H[P_t] <= H[P_1] = H[A] for all t >= 1, globally.
Hard step: dH/dt <= 0 for ALL t >= 1 (not just the t=1 second-order shadow). Mechanism: H is
  Schur-concave; if the curve t |-> P_t is majorization-MONOTONE away from the uniform max (the
  join-of-t-samples operation concentrates mass on larger sets, a monotone mixing), then H
  decreases. Sub-mechanism: P_t = P_{t-1} (*) P_1 shows each unit step is a join-convolution that
  can only spread mass UP the order = a majorization step lowering H (Schur-concavity).
Check: assert H[P_t] monotone decreasing on a fine t-grid in [1,T] for many families; assert
  dH/dt <= 0 at sampled t; verify P_t majorizes P_{t'} for t > t' on the order (Lorenz/sorted
  partial sums). GUARDRAIL: this is conditional on P_t >= 0 in the interval — state that.
Why second: it still needs P_t >= 0 (does NOT resolve the signed branch), and "majorization lowers
  entropy family-independently on non-distributive lattices" is itself nontrivial (the reviewer
  flagged it is not obviously easier than Angle 1's lemma). It is the safer fallback because
  monotonicity on [1,inf) is weaker than full nonnegativity and may yield to Schur-concavity; but
  Angle 1 is strictly cleaner if the averaging lemma goes through.

---

## Angle 3 (escape hatch — CONDITIONAL deliverable, only if both above stall)

Moves: partial / conditional global closure — the HONEST floor if neither the averaging lemma
(Angle 1) nor the family-independent majorization (Angle 2) can be proven within budget.

Deliverable: state the global upgrade CONDITIONALLY and label it as such, never as proven:
  "For every union-closed family on which P_t >= 0 (numerically verified for ALL ~37,500+ tested
  families and every tested t >= 1, conjectured in general but NOT proven here), Theorem 1 gives
  H[P_t] <= H[A]; thus Avenue A is closed on every such family, and the t=1+epsilon construction in
  the Frankl file lands in this regime. The remaining gap is purely the universally-quantified
  nonnegativity Theorem 2, which is supported by overwhelming numerics but lacks an analytic proof."
Plus the integer-anchor unconditional core: for integer m >= 1, P_m IS a genuine distribution
  (proven, OR-of-m-samples), so H[P_m] <= H[A] holds UNCONDITIONALLY at every integer t — a
  genuine (if partial) global statement requiring no conjecture.
Hard step: none beyond honesty — the point of Angle 3 is to deliver a TRUE conditional/partial
  statement rather than overclaim. The integer-t core is fully proven; the all-real-t extension is
  flagged conditional.
Check: certificate as in Angle 1, but the writeup must clearly mark the all-t nonnegativity as
  CERTIFIED-BUT-UNPROVEN (conjectural), and the integer-t closure as proven. The proof-reviewer
  must see no unproven Theorem 2 dressed as proven.
Why third: it concedes the global theorem to a conjecture; use ONLY if Angles 1 and 2 both stall.
  It still strictly upgrades round 1 (integer-t global closure + the explicit conditional global
  statement + the plain-language verdict) and remains honest.

---

## Ranking

**Angle 1 first.** The TARGET is settled in shape by ~37,500 families (0 failures for t >= 1,
comfortable t=1 cutoff, signed only for t < 1). The entire round-1 caveat is replaced by "P_t is a
distribution => H[P_t] <= H[A], globally." The only real work is the corrected hard step — the
averaging-into-the-cone lemma (P_t = P_1 (*) P_{t-1}; join-convolution with uniform P_1 lifts the
SPECIFIC signed remainder into the nonneg cone) — whose mechanism is now concrete: submodularity
of join + concavity of u^s for s in [0,1), with t >= 1 supplying exactly one smoothing pass. The
FALSE "nonnegative remainder" route is deleted.

**Fall back to Angle 2** if the builder cannot push the averaging lemma past non-distributive
lattices: prove the WEAKER sufficient statement that H[P_t] is monotone non-increasing on
[1, infinity) via Schur-concavity / majorization, restricting to the nonneg regime and treating the
signed branch as "entropy undefined, construction void." Honestly note it still assumes P_t >= 0
on the interval and has its own family-independence burden.

**Angle 3 is the escape hatch.** If BOTH the averaging lemma and the family-independent
majorization stall, deliver the CONDITIONAL global upgrade (all-t nonnegativity certified-but-
unproven, integer-t closure proven) clearly labelled as conditional — NEVER present an unproven
Theorem 2 as proven. This is the honest floor and still strictly upgrades round 1.

Do NOT attempt to move 0.38271 — no "perturb uniform A" entropy scheme can (proven round 1). The
round-2 win is the GLOBAL obstruction + the plain-language verdict, the run_state's honest fallback
made airtight (Angle 1/2) or honestly conditional (Angle 3).
