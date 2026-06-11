# Round 3 — Correction + clarification of the Avenue-A obstruction (Frankl-file entropy approach)

**Constant: `frankl` (Frankl's Union-Closed Sets Conjecture, entropy method).**
**Record (lower bound on the max element bias): 0.38271 (Liu, arXiv:2306.08824).
Target: 1/2 (the conjecture, OPEN). No bound is moved this round; the record stands.**

This is a **CORRECTION + CLARIFICATION** round. It does three things and nothing else:

1. **Retracts** a now-false numerical assertion that appeared in the round-2 narrative
   and in the round-2 certificate's check R2-7(ii) — the surrogate inequality **(L')**
   (`B_l(x) >= 0` for all `l > 0`) is **FALSE** in general, with an explicit, frozen,
   high-precision counterexample.
2. **Records the (L) ≠ (L') separation** as a small genuine clarifying result: the true
   lemma **(L)** (`P_{1+s} >= 0`) survives on the very family where the surrogate (L')
   fails.
3. **Downgrades the honesty framing of (L)** from "certified-numerically, unproven" to
   "unproven **AND** with eroding-margin evidence it may be **FALSE at scale**."

Everything that was PROVEN in rounds 1–2 — the unconditional integer-`t` core, the
additivity identity, the single-lemma reduction, the §8 verdict, and the record 0.38271
— is **UNCHANGED and explicitly re-affirmed** below. The obstruction conclusion (the
perturb-uniform Frankl-file approach cannot reach 1/2) **never depended on (L)/(L')** and
is therefore **not weakened**.

All numbers below are re-checked, from scratch, by
`research/frankl/certificate_round3.py` (re-runnable, network-free, PASS/FAIL per check,
nonzero exit on any failure; reuses the round-1 helpers; leaves
`certificate_round1.py` / `certificate_round2.py` intact). Last run: **ALL CHECKS PASS
(exit 0)**.

---

## 1. What is being corrected (and what is not)

Recall the round-2 reduction chain (writeup §§5–6):

- **(L)** (the *true* lemma the obstruction's non-integer-`t` extension reduces to):
  `(P_1 (*) P_s)(x) = P_{1+s}(x) >= 0` for all `s in [0,1)`, every union-closed `F`.
- **Pick reduction** `(L') => (L)`: using the Stieltjes/Pick representation
  `u^{1+s} = (sin(pi s)/pi) int_0^inf u^2/(u+l) l^{s-1} dl`, one has
  `P_{1+s}(x) = (sin(pi s)/pi) int_0^inf B_l(x) l^{s-1} dl` with
  `B_l(x) = sum_{y<=x} mu(y,x) Q(y)^2/(Q(y)+l)`. Since the integral kernel
  `(sin(pi s)/pi) l^{s-1}` is positive, **(L)** would follow from the pointwise surrogate
  **(L')**: `B_l(x) >= 0` for all `l > 0`, all `x`.

Round 2 stated (writeup §6.2/§6.3, §7, §9, and certificate check R2-7(ii)) that **(L')**
holds — "certified numerically with zero failures across ~57 families, margin bounded
away from zero." **That generalization is FALSE.** It passed only because the round-2
sweep capped the ground-set size at `n = 7` (≈57 families) on a coarse 10-point `l`-grid,
and never reached the regime where (L') breaks.

**Precisely what changes:** the assertion "(L') holds in general." **Precisely what does
NOT change:** the *implication* `(L') => (L)` (still a valid, correctly-derived
one-directional sufficient condition — its premise is simply false, so it is a dead route
to (L)); the unconditional integer-`t` core (§3 below); additivity (§4); the single-lemma
reduction (§5); and the §8 verdict.

Round 2's certificate check R2-7(ii) is **not** a false PASS in disguise: its assertion is
literally true on the `n<=7` sweep it actually runs. This round documents that it does
**not** generalize and supplies the explicit counterexample. We therefore leave
`certificate_round2.py` intact and do the correction here, in the round-3 certificate and
this writeup (per the build instructions: prefer leaving the round-2 file untouched, and
relabel rather than leave a false PASS — the relabel/retraction lives in §2 below and in
the round-3 certificate's R3-1/R3-2 checks).

---

## 2. (L') is FALSE — explicit frozen witness, high-precision

**Witness family `F*`.** An explicit, RNG-independent, frozen list of 52 integer bitmasks
on `n = 9` ground elements (`certificate_round3.py`, constant `WITNESS`):

```
0, 39, 114, 119, 150, 153, 159, 183, 191, 246, 247, 251, 255, 275, 289, 295,
307, 311, 371, 375, 407, 411, 412, 413, 414, 415, 439, 441, 443, 445, 447, 456,
468, 470, 471, 473, 475, 476, 477, 478, 479, 489, 495, 501, 502, 503, 505, 506,
507, 509, 510, 511
```

The certificate verifies (check R3-0) that `F*` is **genuinely union-closed** (closed under
bitwise OR, contains the empty set `0`, equals its own OR-closure) with `|F*| = 52`.

> **CAUTION on reproducibility (the single most important build note).** The round-3
> exploration attributed this witness to `rand_family(9, seed=1711)` "in the round-2
> certificate's RNG convention." That attribution is **WRONG**: round-2's `rand_family`
> uses `k = randint(2, 7)`, which for seed 1711 gives `|F| = 21` and `min B_l > 0`
> (NO counterexample). The `|F*| = 52` witness requires the **wider** generator count
> `k = randint(2, 12)`. To make the counterexample reproducible **forever** and immune to
> RNG-convention drift, the certificate **hard-codes the frozen mask list** and re-derives
> `min B_l < 0` directly from it, never from the RNG.

**The negativity (check R3-1, float64).** Over a dense `l`-grid near `l ≈ 0.126`, the
minimum of `B_l(x)` over `x in F*` is

> `min_x B_l(x) = -1.122032767565e-02` at `l = 0.126100`, achieved at `x = 511` (the top
> element `0b111111111`).

`cond(Z*) = 129.46` — modest — so the negativity is **not** an ill-conditioning artifact.

**The negativity (check R3-2, 60-digit mpmath).** An independent LU-solve at 60 decimal
digits (`mpmath`) at the same `l*` gives

> `min_x B_l(x) = -0.01122032767564579611612628`,

agreeing with the float64 value to `6.4e-17`. Both confirm `min B_l < -0.011 < 0`.

**Conclusion: (L') is FALSE.** A pointwise positivity of the resolvent integrand `B_l`
does not hold on union-closed families in general; the Pick surrogate (L') cannot serve as
a route to (L).

---

## 3. The (L) ≠ (L') separation (the clarifying result)

**(L) survives on the SAME witness (check R3-3).** On `F*`, sweeping `s in (0,1)` on a
3000-point grid,

> `min_s min_x P_{1+s}(x) = +3.698e-04 > 0`, with the minimum driven toward `s -> 1^-`.

So on a *single explicit family* the surrogate (L') fails (`-0.0112`) while the target (L)
holds (`+3.7e-4`). This is the explicit **(L) ≠ (L') separation**.

**Why (L) survives where (L') fails (mechanism, verified — check R3-3).** The negative mass
of `B_l` sits at **small `l`** (near `l ≈ 0.126`). In the Pick integral
`P_{1+s} = (sin(pi s)/pi) int_0^inf B_l l^{s-1} dl`, the weight `l^{s-1}` with `s` near 1 is
`l^{-(1-s)}`, which is *integrably small* near `l = 0` relative to where the positive mass
of `B_l` lives, so the negative contribution is **downweighted** and the integral stays
nonnegative. The certificate confirms this is not a coincidence of bookkeeping: the
log-spaced quadrature reproduces the **nonnegative** `P_{1+s}` from the **sign-indefinite**
`B_l` to integration tolerance (reusing the round-2 R2-7(i) representation check).

**What the separation rules out.** Every *black-box* positivity framework — total
positivity / sign-regularity of the Möbius kernel, complete-monotonicity-in-`l`,
Löwner/operator-monotone arguments, and Pick-as-stated — delivers exactly the **per-`l`**
positivity (L'). Since (L') is now an explicit false statement, **none of these frameworks
can close (L).** A proof of (L), if one exists, must be a native combinatorial argument
about the `s`-averaged (weight-integrated) Möbius sums of convex-monotone valuations on
join-semilattices — crucially using the `s`-averaging, not a pointwise/operator positivity.
This narrows the open conjecture to its true form and is the genuine (if small) advance of
this round.

---

## 4. (L): downgraded honesty — unproven AND eroding-margin evidence it may be false

Round 2 labelled (L) "certified-numerically-but-unproven." This round **downgrades** that to
**"unproven AND with eroding-margin evidence it may be FALSE at scale."** Two observations
force the downgrade:

- **The closely-related surrogate (L') *does* cross zero** at modest `n` (§2), having looked
  positive on all `n<=7` tests — exactly the pattern a quantity that fails only at larger
  scale produces.
- **The (L) margin is itself eroding (check R3-6).** Sweeping (L) past round-2's `n<=7`
  cutoff, the minimum of `P_{1+s}` over the sweep is **monotone-decreasing** in the maximum
  `n`:

  | max `n` | `min P_{1+s}` over sweep |
  |--------:|--------------------------|
  |     7   | `+4.17e-4`               |
  |     8   | `+3.19e-4`               |
  |     9   | `+1.88e-4`               |
  |    10   | `+1.88e-4`               |

  The margin shrinks and concentrates at `s -> 1^-`. It remains strictly positive on
  everything tested (so (L) is not disproven), but the trend is the wrong direction and
  mirrors how (L') looked positive until it crossed.

**Honest status of (L): a conjecture with a non-trivial chance of being FALSE at scale.**
Not a near-theorem.

**Onset of the (L') failure (check R3-5) — stated as OBSERVED, not as a hard fact.** In a
small deterministic sweep (wider-`k` convention, 80 seeds per `n`), there were **0** (L')
failures at `n = 7`, and failures **appeared by `n = 8`** (`2/80` at `n=8`, `5/79` at
`n=9`). Per the outline review, the **exact** onset integer is seed-set- and `l`-grid-
dependent and is **not** asserted as a clean "exactly `n=8`, zero at `n<=7`" fact; a
different sweep can show a failure at `n=7`. The **robust, qualitative** point is the only
one claimed: **round 2's `n<=7` sweep on a coarse `l`-grid simply did not reach the failure
regime**, which is why round 2 missed it.

---

## 5. Invariants preserved — the unconditional core is insulated from the (L') failure

This is the crux of the correction's *scoping*: the false node (L') is a **conjectural,
non-integer-`t` surrogate** and is explicitly **NOT** part of the held/verified result. The
proven core does not touch it. The round-3 certificate (check R3-4) demonstrates this
concretely **on the very `n=9` witness `F*` where (L') dies**:

- **Integer-`t` core (UNCONDITIONAL, PROVEN, round-2 §3):** `P_m = Z^{-1} Q^m` equals the
  brute-force law of `A_1 OR ... OR A_m` (`m` iid uniform copies) for `m = 2, 3, 4` on `F*`,
  to machine precision (`<= 1e-9`), and is a genuine distribution (`min P_m >= 0`,
  `sum = 1`). Hence `H[P_m] <= H[A]` on `F*` — checked for `m = 1,2,3,4` (`H[A] = log2 52 =
  5.7004`).
- **Additivity (PROVEN, exact, round-2 §4):** `P_{a+b} = P_a (*) P_b` on `F*` for five
  `(a,b)` pairs.
- **Smoothing operator (PROVEN, round-2 §4):** `M_F` is column-stochastic, nonnegative, and
  `M_F @ P_s = P_{1+s}` on `F*`.

These are all true on the family where (L') fails, demonstrating that the failure of the
non-integer-`t` surrogate **cannot disturb** the integer-`t` ceiling, the additivity
identity, or the single-lemma reduction. None of those ever invoked (L) or (L').

**Banner (certificate output, matches §6 of this writeup):** the unconditional integer-`t`
core is UNCHANGED; additivity UNCHANGED; the single-lemma reduction UNCHANGED; the §8
verdict (perturb-uniform approach cannot reach 1/2) UNCHANGED; record 0.38271 (Liu)
UNCHANGED. Only the conjectural non-integer-`t` surrogate (L') is corrected (now FALSE);
(L) remains conjectural with the eroding-margin caveat.

---

## 6. Corrected status and verdict

- **(T) PROVEN here, unconditionally (UNCHANGED from rounds 1–2):** the Frankl-file program
  (perturb uniform `A` on `F` into a `C` on `F` with `H[C] > H[A]`) is impossible
  (round-1 Theorem 1); Avenue-A's `P_m` is, at every integer `m`, a genuine distribution
  obeying `H[P_m] <= H[A]` on every family; additivity `P_{a+b} = P_a (*) P_b` and the
  single-lemma reduction (all-`t>=1` nonnegativity ⇔ lemma (L)) hold exactly; the Pick
  *implication* `(L') => (L)` is a valid one-directional reduction.
- **(L') — FALSE (NEW this round):** the pointwise resolvent positivity `B_l(x) >= 0` for
  all `l > 0` does **not** hold on union-closed families; explicit frozen witness
  (`|F*|=52`, `n=9`, `min B_l = -0.0112` at `l ≈ 0.126`, 60-dps confirmed,
  `cond(Z) ≈ 129`). The Pick surrogate is therefore a **dead route** to (L), and the entire
  class of per-`l`/per-minor/operator-positivity frameworks (TP, complete-monotonicity-in-
  `l`, Löwner, Pick-as-stated) is ruled out (each implies the false (L')).
- **(L) — conjectural, DOWNGRADED honesty (NEW this round):** `P_{1+s} >= 0`. Holds on
  everything tested (incl. the witness `F*`: `+3.7e-4`), but **unproven AND with
  eroding-margin evidence it may be FALSE at scale** (margin shrinks `+4.2e-4 -> +1.9e-4`
  as the swept `n` grows, concentrating at `s -> 1^-`). Hence the *all-real-`t>=1`* ceiling
  remains conditional on (L); the *integer-`t`* ceiling is unconditional.
- **(S) CITED, not proved here (UNCHANGED):** the published sharp barriers
  (0.38196601125, 0.382345533366703, 0.38271) cap the known two-sample variants below 1/2.
- **Bound status (UNCHANGED):** the record `0.38271` (Liu) **stands**. No improvement is
  claimed or available.

**The §8 verdict is UNCHANGED in substance.** The plain-language answer — *the Frankl-file
"perturb uniform `A` to raise its entropy" approach cannot reach 1/2* — rests entirely on
round-1 Theorem 1 (uniform maximizes entropy on its support) and the unconditional
integer-`t` core. It **never depended on (L) or (L')**. Correcting (L') to FALSE and
downgrading (L) to "may be false at scale" therefore **does not weaken the obstruction**:
if anything it sharpens it — for non-integer `t`, *if* (L) failed, `P_t` would be a signed
measure, which is *already* an obstruction (round-2 §7(ii): not even a probability
construction), so (L) failing would merely change the *reason* the `t = 1+epsilon` proposal
is barred, not rescue it.

---

## 7. Why this was worth a round (integrity)

A previously reviewer-verified numerical assertion (round-2 R2-7(ii) "B_l >= 0 on the
sweep") does **not** generalize. Recording an explicit, frozen, high-precision
counterexample, scoping the retraction precisely to the conjectural surrogate, and honestly
downgrading the confidence in (L) — while machine-checking that the proven core survives on
the very witness where (L') dies — **raises** the integrity of the verified artifact rather
than overstating it. It also records a genuine mathematical fact (the (L) ≠ (L')
separation) that narrows the open conjecture to its true form and rules out an entire class
of black-box proof strategies. No bound moves; the record 0.38271 (Liu) stands.

**Certificate:** `research/frankl/certificate_round3.py` — re-runnable, network-free,
PASS/FAIL per check, nonzero exit on failure; freezes the witness as explicit bitmasks
(RNG-independent); reproduces `min B_l < 0` in float64 and 60-dps mpmath; confirms (L) on
the same witness; machine-checks the integer-`t` core/additivity/`M_F` on the witness;
retains non-vacuity guards. Last run: **ALL CHECKS PASS (exit 0)**. Leaves
`certificate_round1.py` / `certificate_round2.py` intact (both still exit 0).

### References (see `research/frankl/literature/digests.md`)
- Liu, arXiv:2306.08824 (current record 0.38271).
- Gilmer, arXiv:2211.09055; Alweiss–Huang–Sellke, arXiv:2211.11504; Chase–Lovett; Sawin;
  Cambie, arXiv:2212.12500; survey arXiv:2306.12351.
- Cover & Thomas, *Elements of Information Theory*, Thm 2.6.4 (uniform maximizes entropy).
- Stanley, *Enumerative Combinatorics* Vol. 1, Ch. 3 (Möbius inversion on posets).
- Stieltjes/Pick representation of `u^a`, `a in (0,1)` (Bhatia, *Matrix Analysis*, Ch. V).
