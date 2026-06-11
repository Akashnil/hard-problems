# Proof review — Round 2 (Frankl, global Avenue-A obstruction upgrade)

**Verdict: APPROVE**
**Verification level: verified** (the unconditional core; the conjectural lemma (L)/(L) is
honestly labelled as such and is NOT part of the verified claim).

**Bound status: record 0.38271 (Liu, arXiv:2306.08824) UNCHANGED. No improvement claimed
or available; this is the goal's explicit honest fallback, upgraded from local to global.**

## What was reviewed
- `research/frankl/obstruction-round2.md` (writeup)
- `research/frankl/certificate_round2.py` (reuses `certificate_round1.py` helpers)
- `outline-round2.md` + `outline-review-round2.md` (approved spec; this is the Angle-3
  conditional deliverable, which the spec explicitly authorizes as the honest floor)
- `obstruction-round1.md`, `/home/agentuser/repo/Frankl`, `/tmp/memory/run_state.md`

## Reproduction
- `certificate_round2.py` runs to **exit 0, ALL CHECKS PASS** (R2-1..R2-7, R2-NV).
- `certificate_round1.py` still exits 0 (round-1 checks not broken; the helper-strip import
  was verified to load helpers without re-running round-1's driver — no stdout on import).
- **Non-vacuity confirmed independently (I perturbed core claims):**
  - Additivity with AND instead of OR convolution → `np.allclose` FALSE (correct fails).
  - Integer anchor m=3 compared to Q^2 (wrong power) → FALSE.
  - Reduced lemma B_l with Q^1 numerator (wrong exponent) → 7 negative events on the
    non-distributive lattice (correct Q^2 → 0). The built-in R2-NV (t>=0.5 → signed) also
    fires. The certificate genuinely tests its inequalities.

## Independent re-derivation of the load-bearing PROVEN steps
- **(a) Integer anchor (Prop 3.1).** `Pr(A_1∨…∨A_m ≤ y) = Q(y)^m`, and "pmf ↦ domination-CDF"
  is `Z·`, invertible by Möbius inversion, so the OR-of-m law is `Z^{-1}Q^m = P_m`. Being the
  law of an explicit F-valued r.v., P_m ≥ 0, sums to 1. Certificate confirms m=2,3,4 vs
  brute-force. UNCONDITIONAL, correct.
- **(b) Additivity (Prop 4.1).** I independently verified the lattice fact
  `x∨y ≤ z ⇔ x≤z ∧ y≤z` on the non-distributive family (holds), which gives
  `Z(μ(*)ν)=(Zμ)(Zν)`; with `Q^{a+b}=Q^a Q^b` and Z invertible, `P_{a+b}=P_a(*)P_b`. Exact.
- **(c) Single-lemma reduction (Prop 5.1).** The ⇐ induction rests only on: join-convolution
  of two nonnegative sum-1 measures is nonnegative sum-1 (true termwise, μ(x)ν(y)≥0). I
  reproduced `P_{2+s}=P_1(*)P_{1+s}` matching `P_t(2+s)`, min +0.0094, given `P_{1+s}≥0`.
  The reduction "all-real-t≥1 nonnegativity ⇔ (L)" is logically valid. PROVEN modulo (L).
- **(d) Pick/resolvent reduction (6.2).** I independently verified
  `u^{1+s}=(sin(πs)/π)∫₀^∞ u²/(u+l) l^{s-1} dl` for several (u,s) (the apparent s=0.85
  mismatch was pure quadrature truncation; widening the window converges to 1e-3). I also
  verified the B_l integral identity reproduces `P_{1+s}` on the non-distributive lattice,
  and the partial-fraction boundary form `B_l = P_1 − l·Z^{-1}(1) + l²·Z^{-1}(1/(Q+l))` with
  `Z^{-1}(1)=e_bottom` (so for non-bottom x the constant/linear terms vanish, matching the
  writeup). The implication (L')⇒(L) is valid (`sin(πs)/π>0`, `l^{s-1}>0`). PROVEN reduction.

## Honesty / hard-constraint audit
- **Conditional labelling is honest.** Lemma (L)/(L') is consistently called a CONJECTURE,
  certified-numerically-but-UNPROVEN (writeup §6.3, §9; certificate banner and the R2-7 NOTE
  "not proven analytically — open gap"). It is NEVER dressed as a theorem. The §1 status box
  separates "PROVEN unconditionally" from "CERTIFIED NUMERICALLY BUT NOT PROVEN."
- **Global ceiling correctly stated:** UNCONDITIONAL at every integer t (Prop 3.1+Thm 1);
  CONDITIONAL on (L) for non-integer t≥1. Stated this way in §2 Corollary, §7(i), §9.
- **No contradiction from the false bias hypothesis.** Every load-bearing step is explicitly
  hypothesis-free. §8.3 correctly diagnoses the file's "exploit the false hypothesis" as a
  category error and states "We derive nothing from the false premise (and must not)."
- **(T) vs (S) kept distinct.** (T) self-proven impossibility of the perturb-uniform program;
  (S) cited published barriers (0.38196601125, 0.382345533366703, 0.38271). Not blurred.
- **Liu record verified independently** via WebFetch of arXiv:2306.08824: Jingbo Liu, ~0.38271,
  "under numerically verified hypotheses." Record UNCHANGED; no bound improvement claimed.

## Goal Progress
- Eval: count of milestone lines `^- R[0-9]+:` in `research/frankl/current.md` (the run_state
  Metric is reviewer-gated verification of genuine advances; tracked as Progress-log lines).
- Previous: 1
- Current: 2
- Direction: IMPROVED

## Milestone logged
Yes. Round 1 left the Avenue-A obstruction LOCAL (Taylor at t=1, small-n). This round
makes it GLOBAL and family-independent at every integer t UNCONDITIONALLY, with a rigorous
reduction of the all-real-t≥1 case to a single clean inequality (L), itself reduced via Pick
to the exponent-free (L'). That is genuine, independently re-derived groundwork on the
mandated approach — a real advance even though no numeric bound moved (correct: no
perturb-uniform scheme can move 0.38271). Logged:
`- R2: VERIFIED global upgrade — integer anchor P_m = law(OR of m iid uniform) ⇒ H[P_m] ≤ H[A]
on every family at every integer t (unconditional); additivity P_{a+b}=P_a(*)P_b and the
single-lemma reduction (all-t≥1 nonneg ⇔ (L)) re-derived from scratch; Pick reduction of (L)
to exponent-free B_l≥0 verified; lemma (L)/(L') honestly CONJECTURAL (certified numerically,
unproven). Record 0.38271 (Liu) stands.`

## Why APPROVE rather than CHANGES REQUESTED
This is not a claimed bound improvement; per run_state the rigorous obstruction is the
honest fallback and an Angle-3 conditional deliverable is explicitly authorized. The
unconditional core re-derives correctly and the conditional part is labelled honestly and
not overclaimed. The single open gap (lemma (L)/(L') family-independent proof) is openly
disclosed, not hidden. Nothing here poisons the ledger: the record is untouched.
