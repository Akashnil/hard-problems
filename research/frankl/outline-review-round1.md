# Outline review — Round 1 (Frankl obstruction writeup)

**Verdict: CHANGES REQUESTED**

The chosen angle (Angle 1: rigorous obstruction/impossibility writeup + ceiling survey +
re-runnable certificate) is the correct, honest, and completable deliverable for this round.
It cannot and does not claim to beat 0.38271 — it is the goal's explicit fallback, and it is
certifiable. I independently re-ran the outliner's scripts and re-derived the load-bearing
facts; the strategic conclusion is sound. But the **hard step is stated with an
order-of-derivative error** that, if copied verbatim, would produce a wrong derivation. Fix
the items below while building; none requires re-outlining.

---

## What I verified (all PASS)

- `frankl_check2.py` / `frankl_check3.py` reproduce: C stays in F, H[C] <= H[A] with margin;
  Avenue A raises bias but dH < 0 for all t>1; 1-1/phi = 0.38196601125; Cambie b2 root ~0.32945.
- Constant ordering: 0.3819660 < 0.3823455 < 0.38271. Correct.
- P_t stays nonnegative for t near 1 across 300 random families (min ~0.063 at t in {1.01,1.05}),
  so the local dH/dt argument concerns a genuine distribution.

## Issue 1 (load-bearing — MUST FIX) — the hard step's stated mechanism is off by one derivative order

The outline (step 5 / Hard step) says: *"the first-order term in t-1 is a directional
derivative of H at its global max along a feasible direction; the leading behavior is governed
by the curvature (negative-definite Hessian)."* This conflates two orders and is internally
inconsistent (a "first-order term" cannot be "governed by curvature"). I computed it explicitly
on the non-distributive 7-element lattice:

- dP/dt|_{t=1} = Z^{-1}(Q ln Q), with **sum(dP/dt) = 0** (feasible), and dP/dt =/= 0.
- **dH/dt|_{t=1} = -1/ln2 * sum (dP/dt)(ln P + 1) = 0 EXACTLY** (because P is uniform so ln P is
  constant and sum(dP/dt)=0). The first-order term vanishes — as it must at the global max.
- The sign is therefore **second order**: H''(1) = -1/ln2 * sum (dP/dt)^2 / P_i  +
  [grad term that vanishes because sum(d2P/dt2)=0]. Computed H''(1) = -2.15180, matching the
  numerical second difference to 5 digits.
- Hence dH/dt|_{t=1+} = H''(1)(t-1) + O((t-1)^2) < 0 for t slightly above 1, because H''(1) < 0
  and dP/dt =/= 0.

**Action:** Restate the hard step correctly: (i) first-order directional derivative is zero
(uniform is the max); (ii) the leading nonzero term is the second-order one, H''(1), equal to
the Hessian quadratic form -1/ln2 * sum (dP/dt_i)^2 / P_i evaluated on the feasible non-null
direction dP/dt, which is strictly negative; (iii) the d2P/dt2 contribution drops out because
the gradient of H at uniform is the constant vector and sum(d2P/dt2)=0. As written, the outline
would have the builder claim a nonzero first-order term — a real error.

## Issue 2 (MUST STATE) — non-nullity of dP/dt needs the right justification

The outline justifies non-nullity by "it strictly changes biases." That is the wrong handle for
the Hessian argument — what is needed is dP/dt =/= 0 as a vector. The clean statement:
dP/dt = Z^{-1}(Q ln Q) = 0 iff Q ln Q = 0 iff Q(y) in {0,1} for all y. Since Q(y) > 0 always
(y <= y) and Q(y) = 1 only at the top element, dP/dt =/= 0 whenever |F| >= 2. State it this way;
it is two lines and fully rigorous. (Restricting to the feasible subspace sum d = 0, the Hessian
is still strictly negative-definite, so "non-null" = "nonzero" suffices.)

## Issue 3 (quantifier scope on Theorem 1 / Lemma 1) — make the support claim do exactly its job

Theorem 1 (Gibbs: uniform maximizes entropy on finite support) is correct and is the spine of
the impossibility. But be precise about scope:

- The theorem gives H[X] <= log2|supp(X)|. To conclude H[C] <= H[A] = log2|F| you need
  supp(C) ⊆ F (Lemma 1), not supp(C) = F. State the bound as
  H[C] <= log2|supp(C)| <= log2|F| = H[A]. Equality with H[A] requires both supp(C)=F and C
  uniform. This is the airtight, hypothesis-free core — keep it exactly this general.
- For **Avenue B** confirm supp(C) ⊆ F: C = A OR B with A,B supported on F and F OR-closed, so
  every realized a OR b is in F. Fine. For **Avenue A** with non-integer t, P_t can be a *signed*
  measure on some non-distributive lattices; then "H[P_t]" is not Shannon entropy and Theorem 1
  simply does not apply to it. The outline correctly rests the Avenue-A obstruction on dH/dt < 0
  (valid where P_t >= 0, which holds near t=1 — verified). Make explicit that the dH/dt argument
  is the obstruction for Avenue A and that signedness is only a secondary defect, never invoked
  as the impossibility. The run_state caveat ("signed measure is family-dependent, not
  universal") is honest and should be carried into the writeup verbatim.

## Issue 4 (the forbidden move — handled correctly, keep it sharp)

Step 4 (Corollary) correctly diagnoses the Frankl file's category error: the bias hypothesis
inflates the *lower bound* sum_i E[h(p_i q_i)] on H[C]; it never raises the *actual* H[C] above
H[A]. The outline does NOT derive any contradiction from the false hypothesis — it shows the
hypothesis is irrelevant to H[C] <= H[A]. This respects run_state's NEVER rule. Keep the two
inequalities side by side (true: H[C] <= H[A]; Gilmer's: H[C] >= sum E[h(p_i q_i)]) so the
inversion is unambiguous. No circularity. Good.

## Issue 5 (ceilings — used correctly, one honesty guard)

The three constants are stated accurately and as < 1/2: iid OR tight at (3-sqrt5)/2 = 0.3819660
(Chase-Lovett sharp example), Sawin two-sample exact 0.382345533... (Cambie, sharp 2-atom),
Liu 0.38271 (current record). The outline does NOT overstate: it scopes the impossibility to
"perturb uniform A to force H[C] > H[A]" (proven impossible, unconditional) and separately
reports the *broader* two-sample coordinatewise method as "capped by published sharp barriers."
**Guard to enforce in the writeup:** distinguish "this specific Frankl-file program is impossible"
(a theorem you prove) from "the entire entropy method is bounded below 1/2" (NOT proven — it is a
survey of others' sharpness results plus Cambie's own remark that a new core method is needed).
Do not let the conclusion blur into "the entropy method cannot reach 1/2 (proven)" — that
overclaims. Phrase it as: the mandated perturbation program is provably impossible; the known
sharp barriers (0.382...) bound the published two-sample variants, and no entropy variant has
come within 0.11 of 1/2. That is the honest line.

## Certificate (approve, with two additions)

The planned `research/frankl/certs/obstruction_cert.py` covers the right assertions. Add:
1. A direct check that **first-order dH/dt|_{t=1} ~ 0** and **H''(1) < 0** (second difference)
   on each family — this is the certificate for the corrected hard step (Issue 1), and prevents
   the builder from silently reverting to the wrong first-order story.
2. Assert dP/dt = Z^{-1}(Q ln Q) is nonzero and sums to 0 on each family (Issue 2).
Keep it network-free and PASS/FAIL per assertion as planned.

---

## Bottom line

Approve the angle and the certificate plan; the deliverable is the right honest fallback and is
fully certifiable. Before the writeup is accepted, the builder must (1) correct the hard step to
second order (Issue 1), (2) justify non-nullity via Q ln Q =/= 0 (Issue 2), (3) state the support
bound as H[C] <= log2|supp(C)| <= log2|F| and scope Avenue A's obstruction to dH/dt with the
signed-measure caveat (Issue 3), and (4) keep the "specific program impossible" vs "method
bounded (cited, not self-proven)" distinction explicit (Issue 5). No bound improvement is to be
logged this round — none is honestly available.
