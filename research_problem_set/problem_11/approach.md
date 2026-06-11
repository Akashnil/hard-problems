# Problem 11 — Approach record

## Angle tried (Round 1)
**Angle 1:** existence via an enlarged realizable family — within-copy block collapse (Lemma 1) +
cross-copy identity matching on a subset (Lemma 2), composed at `k=2` (asymmetric: collapse copy 0 by
`Π_0`, copy 1 by `Π_1`, match a subset `T` of common block-representatives). Plus the AND-tree
realization of squaring (Lemma 4) for the mode route.

## What was established (fully rigorous)
- **Lemma 0** conditioning = component collapse (`P'∝∏_c P(copy_c)` on component-constant atoms).
- **Lemma 1** within-copy collapse closed form (restrict to block-constant strings).
- **Lemma 2** identity matching `T`: both copies get `P_T(x)∝P(x)·m_T(x_T)`; maxbias = max coord bias
  of one `n`-coordinate law.
- **Lemma 3** AND-amplifier `b→b²/(b²+(1-b)²)<b` for `b<1/2` (correlation-free), with the **exact**
  collateral formula `b'_j=[(1-b)b_j+(2b-1)p_{11}]/[b²+(1-b)²]` and the **covariance dichotomy**
  `b'_j<b_j ⟺ Cov(x_j,x_{i*})>0`.
- **Lemma 4** AND-tree on `2^t` copies realizes `P^{2^t}/Z` as a single conditioning.
- **Proposition A** unique mode `0^n`: explicit `k=2^t` with `m=2^t≥log((2^n−1)/β)/log(p_0/M)` gives
  `maxbias(P')<β`. Tie to a `1`-heavy co-mode breaks it (genuine limitation).
- **Proposition B** `n=2` complete: `k=2`, `S={(0,1)}` (collapse the two coords) always works; reduces
  to the proved inequality `p_{11}p_{01}<p_{10}p_{00}` (★), which follows from `β<1/2 ⟹ p_{11}<p_{00}`
  and `p_{01}≤p_{10}`.
- **Proposition C** worst coord non-negatively correlated with all others ⟹ matching `{i*}` (plus
  matching tied-max coords) strictly reduces. Covers the entire `Cov≥0` regime.

## What blocks completion (the exact gap)
**Coverage Lemma (general `n≥3`, frustrated regime).** When the worst coordinate `i*` is strictly
negatively correlated with some coordinate(s), matching alone can raise those coordinates (Lemma 3),
and collapse must be used; but for `n≥3` collapsing `{i*}∪B` can raise a coordinate outside the block
(frustration one level up). The needed claim is a **system** of inequalities over the surviving
coordinates of both copies; I could not reduce it to a single provable scalar inequality (the `n=2`
case reduces to (★); `n≥3` does not). Verified to **0 failures over 1206 + >2400 combined** random
in-hypothesis instances and both regression cases, but **not proved**.

Proved-insufficient fixed rules (so the resolution must use joint `(Π_0,Π_1,T)` freedom):
match `{i*}` (93/646 fail), match `[n]` (183/646), match `{i*}∪{Cov≥0}` (110/646), oracle-best
identity subset (13/646), best single pair-collapse (64/796). Symmetric single-marginal subfamily:
0/1352 but **fails the n=3 frustrated case** — asymmetry is necessary.

## Conjecture (labelled, NOT proved)
**Conjecture (coverage).** For every full-support `P` with `maxbias<1/2`, the `k=2` asymmetric family
`G(P)` contains a member with `maxbias(P')<maxbias(P)`. Strongest evidence: 0/2400+ exact-rational
trials, both regressions reduced, and a proof for `n≤2`, mode-`0^n`, and `Cov≥0`-worst-coord cases.

## Files
- `research_problem_set/problem_11/proof-partial.md` — full proof of all the above + sharp gap.
- Verifying scripts: `/tmp/scout2.py`, `/tmp/v2_*.py`, and inline round-1 scripts (collateral
  dichotomy, n=2 (★), asymmetric k=2 sweep, mode bound, tie witness).

## Next-round target
Close the Coverage Lemma for `n≥3` frustrated `P`. Most promising: a non-constructive "the reductions
cannot all fail" argument, or an induction on `n` peeling the worst coordinate via the proven `n=2`
collapse mechanism inside a chosen block while controlling the residual via Lemma 3's exact formulas.
