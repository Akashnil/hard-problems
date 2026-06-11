# Proof review — Round 1 (Frankl obstruction analysis)

**Verdict: APPROVE**
**Verification level: verified** (this is an obstruction/impossibility analysis, NOT a bound
improvement; the record 0.38271 stands and the writeup claims no improvement).

This round's deliverable is the run_state's explicit honest fallback: a rigorous impossibility
theorem for the Frankl-file "perturb uniform A to force H[C] > H[A]" program, plus an honest
ceiling survey and a re-runnable certificate. I reproduced the certificate and independently
re-derived every load-bearing step. The analysis is correct and rigorous.

## Goal Progress
- Eval: reviewer-verified milestone lines (run_state Metric — adversarial verification by
  proof-reviewer; count of `^- R[0-9]` milestone lines in `research/frankl/current.md`).
- Previous: 0 (no `## Progress log` / milestone lines existed before this round)
- Current: 1 (one verified-milestone line logged this round)
- Direction: IMPROVED

## New value vs table value
- New value: NONE claimed. The deliverable is an obstruction analysis, not a bound.
- Table/record value: 0.38271 (Liu, arXiv:2306.08824) — stands, correctly cited as
  cited-not-proven. The writeup explicitly states no improvement is claimed or available.

## Milestone logged
Logged (yes). Appended to `research/frankl/current.md` `## Progress log`:
`- R1: VERIFIED obstruction — Theorem 1 (H[C] <= H[A] for any supp(C) ⊆ F, hypothesis-free,
Gibbs/KL) re-derived from scratch; Avenue A H''(1)=-1/ln2·Σ(dP/dt)²/Pᵢ<0 confirmed (closed
form == finite-diff, -2.1518 on nondistributive lattice); Avenue B collapse C→A confirmed;
certificate reproduced (exit 0) and shown non-vacuous (perturbing core checks → exit 1).`
Rationale: a verified feasibility/impossibility result on the mandated bold line is a real
advance per the role brief, and it closes the round's question (the program is provably dead).

---

## What I verified independently

### 1. Theorem 1 (max-entropy ceiling) — CORRECT, hypothesis-free, quantifiers right
I re-derived the Gibbs/KL identity from scratch on a test distribution:
`D(X||u) = Σ P(s) log2(P(s)/(1/m)) = -H[X] + log2 m`, verified numerically to 1e-12, with
`D >= 0 ⟹ H[X] <= log2 m` and equality iff uniform. The writeup's chain
`H[C] <= log2|supp(C)| <= log2|F| = H[A]` correctly uses only `supp(C) ⊆ F` (Lemma 1, OR-closure),
not `supp(C) = F` (outline-review Issue 3 satisfied). Equality to H[A] correctly requires both
full support AND uniformity. The theorem is genuinely independent of any bias hypothesis — no
use of the false `Pr(A_i=1) < 1/2` premise enters. Correct.

### 2. Proposition A (Avenue A) — CORRECT corrected derivative analysis
Independently on the explicit non-distributive 7-element lattice:
- `P_1 = Z^{-1}Q` is uniform (1/7 each) — confirmed.
- Mobius interpretation validated: `P_t = Z^{-1}Q^t` for integer t = 2, 3 equals the exact
  distribution of the OR of t iid uniform samples (I rebuilt the OR-of-t distribution by brute
  force; `np.allclose` true). So the construction is the file's "fractional union", correctly.
- `dP/dt = Z^{-1}(Q ln Q)` sums to 0 (feasible) and is nonzero (‖·‖∞ = 0.330). Non-nullity is
  justified the right way (Q ln Q ≠ 0 ⟺ Q(y) ∈ {0,1}; Q>0 always since y≤y, Q=1 only at the
  top), not via "it changes biases" (outline-review Issue 2 satisfied; certificate confirms
  exactly one Q=1).
- First-order `dH/dt|_{t=1} = 0` exactly (`~7e-16`), as it must be at the entropy maximizer.
- Second-order `H''(1) = -(1/ln2) Σ (dP/dt)²/Pᵢ`: I recomputed both the closed form (-2.1518)
  and an independent central finite difference of the true entropy of `Z^{-1}Q^t` (-2.15181);
  they agree. The d2P/dt2 gradient term correctly drops out (ln P + 1 constant at uniform,
  Σ d2P/dt2 = 0). Strictly negative since Pᵢ>0 and dP/dt≠0. Taylor conclusion `H[P_t] < H[A]`
  for t>1 follows. Correct (outline-review Issue 1 — the off-by-one-order error — is fixed).
- Signed-measure caveat is correctly scoped: the impossibility rests on dH/dt<0 where P_t≥0
  (near t=1), with signedness flagged as a secondary, family-dependent defect, never the
  impossibility (outline-review Issue 3). Correct.

### 3. Avenue B collapse — CORRECT
`B = (1-eps)δ_∅ + eps·Unif(F)`, C = A OR B stays in F (Lemma 1), so H[C] ≤ H[A] for every eps
by Theorem 1; as eps→0, C→A and H[C]→H[A]⁻ monotonically. Certificate confirms monotone
increase to H[A] from below on two families; no regime H[C]>H[A]. The Ellis-Ivan-Leader
smallest-set obstruction is correctly cited as additional motivation-killer. Correct.

### 4. Category-error diagnosis — ACCURATE, no illegitimate contradiction
The diagnosis is correct and matches the Gilmer setup in the Frankl file: the bias hypothesis
inflates the chain-rule *lower bound* `H[C] >= Σ E[h(p_i q_i)]` above H[A], producing the
contradiction against the true `H[C] <= H[A]`; it never raises the *actual* H[C]. The writeup
keeps the two inequalities side by side and explicitly derives NO contradiction from the false
premise — it shows the premise is irrelevant to `H[C] <= H[A]`. This respects run_state's NEVER
rule (no reasoning from a false premise to a contradiction). The file's "trivial calculation
H[C]<H[A] does not mean failure" is correctly identified as backwards. Correct.

### 5. Cited ceilings — cited correctly, kept distinct from the self-proven theorem
- iid OR tight (3-sqrt5)/2 = 0.38196601125: reproduced; identity with 1-1/phi checked to 1e-15.
- Cambie/Sawin-form exact 0.382345533366703: I independently bisected the root b2 of
  h(x)(2-h(x)) - h(2x-x²) and got 0.329455, matching the cited sharp 2-atom value.
- Liu 0.38271 record: confirmed against arXiv:2306.08824 (J. Liu, "Improving the Lower Bound
  ... via Conditionally IID Coupling"), correctly the current record, marked cited-not-proven.
- Ordering 0.3819660 < 0.3823455 < 0.38271 < 0.5 checked. The writeup keeps (T) the self-proven
  impossibility distinct from (S) the cited barriers and does NOT overclaim "the entropy method
  cannot reach 1/2 (proven)" (outline-review Issue 5 guard satisfied).

### 6. Certificate — reproduced, exit 0, non-vacuous
`python3 certificate_round1.py` → ALL CHECKS PASS, exit 0 (reproduced).
Non-vacuity tested by perturbation:
- Flipping the H''(1)<0 check to H''(1)>0 → 4 FAILs, exit 1.
- Flipping the (a) check to demand H[C]>=H[A] (false) → 16 FAILs, exit 1.
The script genuinely exercises each claim and exits nonzero on failure.

## Caveats (non-blocking)
- No bound was improved; none is available. This is correct and honest per the goal's fallback.
- The certificate uses small/finite families (n ≤ 7) and a fixed set of t-values for the
  numerical Avenue-A checks; Theorem 1 itself is a clean analytic proof (Gibbs) that needs no
  enumeration, so the finite scope is illustrative, not load-bearing. The analytic spine is
  sound. Hence "verified" rather than minimal.

## Conclusion
The impossibility analysis is rigorous and correct, the certificate reproduces and is
non-vacuous, the false hypothesis is never misused, and the record 0.38271 is correctly cited
and not claimed improved. APPROVE.
