# Problem 11 — Proof attempt (Round 8)

**Approach:** Restructure the proof around the **γ-dichotomy** (`γ := P(1ⁿ)/(P(0ⁿ)+P(1ⁿ))`),
and add a new proven structural lemma (Lemma 10) repairing the realizable family.

- **Branch γ < β (NEWLY STATED AS A CLEAN BRANCH, fully closed):** by the already-proven Lemma 7,
  B1 full-collapse gives full realized maxbias `= γ`, so `γ < β` ⟹ `maxbias(P') = γ < β`. This is a
  proper closure of the theorem for the entire `γ < β` regime — empirically ~95% of all frustrated
  `n=3` stalls, including the R7 over-count witness seed 770 (`γ = 1/8 < β = 20/41`).
- **NEW Lemma 10 (involution-permuted matchings are all-copies-identical):** for an **involution**
  `π = π⁻¹` and `S = {(i, n+π(i)) : i}` on `P²`, **both** copies share the law `P(x)·P(π·x)/Z`, so
  the full `2n`-coordinate realized maxbias equals the single-copy maxbias of `P(x)·P(π·x)`. This adds
  a load-bearing operator (call it **B4**) to the realizable family `F → F⁺`, fixing a genuine
  non-exhaustiveness defect (`n=3` seed 16832, where every member of the old `F` stalls and only an
  involution-permuted matching reduces full maxbias). It supplies the **right object** (full realized
  maxbias, not a single-copy fiction), routing around the R6 single-copy trap.

**Status: INCOMPLETE — the `γ ≥ β` branch remains OPEN.** Stated honestly: the `γ < β` branch is
fully closed by Lemma 7, and Lemma 10 + B4 are fully proven and exact-verified. The hard residual is
the `γ ≥ β` regime (the `1ⁿ`-heavy minority, ~5% of frustrated `n=3` stalls). No member-selection
closure is claimed there: every named singleton/pair/subset rule is numerically refuted (survey
probes 3–5), and the Angle-2 `min Φ`-increase lever is refuted on the exact `γ≥β` stall set
(approach-critic R8) — it joins the dead-lever list. The empirical fact that the enlarged family
`F⁺ = F ∪ {B4}` clears 0/20000 `γ≥β` stalls at each of three scales is recorded **as a disclosed
regression backstop only — NOT a proof of any coverage/closure lemma**.

This attempt builds **on top of** `proof-attempt-r5.md`: Lemmas 0–8, Props A–D, and the litmus
discharges (A/B/C) are reused verbatim and **not regressed**. The new content is §3.5 (the
γ-dichotomy restructuring), §4′ (Lemma 10 + B4), and the honest restatement of the open gap in §10′.

All closed forms, identities, and small cases below were checked in exact rational arithmetic
(`fractions.Fraction`); code + outputs in §11′. No floating point is used in any verification.

---

## 1. Setup and notation

`P` is full-support on `{0,1}ⁿ`. `b_i := bias_i(P) = Pr_{x∼P}(x_i=1)`, `β := maxbias(P) = max_i b_i`,
assumed `β < 1/2`. Fix a worst coordinate `i*`, `b_{i*}=β`. `P^k` is the `k`-fold product on
`{0,1}^{nk}`; the global coordinate `(c,i)` (copy `c`, coordinate `i`) has index `c·n+i`. For
`S⊆{(u,v)}`, `P' = P^k | {X_u=X_v ∀(u,v)∈S}`, and `maxbias(P')` is taken over **all** `nk`
coordinates. The conditioning event always has positive probability (the all-copies-equal diagonal
atom survives every constraint and has positive mass under full support), so `P'` is well-defined.

`Cov(x_j,x_{i*}) = Pr(x_j=1,x_{i*}=1) − b_j b_{i*}`. `P` is **frustrated** if some `j≠i*` has
`Cov(x_j,x_{i*})<0`. By Proposition C (Round 1) the non-frustrated case is proven; this attempt
concentrates on the frustrated regime for `n≥3`.

For a pair `{i,j}` write its `2×2` joint `Q[a][b]=Pr(x_i=a,x_j=b)`. The pair is **symmetric** if
`Q[0][1]=Q[1][0]`; **0-dominated** if `Q[0][0]>Q[1][1]` (i.e. `Φ_{ij}:=Pr(00)−Pr(11)>0`).

The **diagonal ratio** is `γ := P(1ⁿ)/(P(0ⁿ)+P(1ⁿ))`; under full support `P(0ⁿ),P(1ⁿ)>0` so `γ` is
well-defined and `0<γ<1`.

---

## 2. Reused primitives (proven & independently verified in Rounds 1–2, 5 — treated as given)

Reproduced from `proof-partial.md` / `proof-attempt-r2.md` / `proof-attempt-r5.md`; **not** re-proved
here, and **not regressed**.

- **Lemma 0** conditioning = connected-component collapse: `P'(z) ∝ P^k(z)` on atoms constant on each
  connected component of `([nk],S)`, renormalized.
- **Lemma 1** within-copy block collapse.
- **Lemma 2** identity matching on `T⊆[n]` at `k=2`: both copies acquire `P_T(x) ∝ P(x)·m_T(x_T)`,
  `m_T` the `T`-marginal; **all copies identical**, so full `2n`-maxbias = single-copy maxbias.
- **Lemma 3** AND-amplifier (`T={i*}`): `b'_{i*}=β²/D<β` (`D:=β²+(1−β)²`); exact collateral
  `b'_j=[(1−β)b_j+(2β−1)p^{(j)}_{11}]/D`; covariance dichotomy `b'_j<b_j ⟺ Cov(x_j,x_{i*})>0`.
- **Lemma 4** AND-tree on `2^t` copies realizes `P^{2^t}/Z`.
- **Proposition A** unique mode `0ⁿ`: reduced by the AND-tree, explicit `k=2^t`.
- **Proposition B** `n=2`: complete, `k=1`, `S={(0,1)}`, via `(★) p₁₁p₀₁<p₁₀p₀₀`.
- **Proposition C** worst coord non-negatively correlated with all others: match `{i*}` reduces.
- **Lemma 5 / 5′** Gram operator `Gram_{i,j}P(x) ∝ P(x)·R[x_i][x_j]`, `R=QQᵀ`, realizable as a
  `k=3` permuted 3-cycle matching; all copies identical (full `3n`-maxbias = single-copy) **iff** the
  pair is symmetric.
- **Lemma 6** symmetric pair `Q=[[a,b],[b,d]]`: `bias_i(Gram)<bias_i ⟺ a>d`, via the exact
  factorization `numerator = −(a−d)·g` with `g>0`.
- **Lemma 7** full collapse `k=1` (spanning path on one copy): `maxbias(P')=γ`; reduces `⟺ γ<β`.
- **Lemma 8** for every pair `{i,j}` under `β<1/2`: `Pr(11)−Pr(00)=b_i+b_j−1<0`, hence every pair
  is strictly 0-dominated, `Φ_{ij}=1−b_i−b_j>0`; the all-1-dominated stall is logically impossible.
- **Proposition D** symmetric, 0-dominated worst pair with residual `<β` reduced by Gram (round-1
  litmus `P/217`).

These cover: `n≤2` entirely; unique-mode-`0ⁿ`; the non-frustrated regime; and the
symmetric-0-dominated-pair-with-low-residual regime.

---

## 3. Lemma 8 (reused) and its consequences

Lemma 8 (`Pr(11)−Pr(00)=b_i+b_j−1`, so `β<1/2` ⟹ every pair strictly 0-dominated, `Φ_{ij}=1−b_i−b_j>0`)
is reused verbatim from `proof-attempt-r5.md` §3. Its three consequences (C1 the all-1-dominated stall
is impossible; C2 Lemma 6 fires unconditionally on every symmetric pair; C3 `Φ` is a uniformly
positive, maxbias-implying potential) stand. These are used below only as background structure; the
round-8 advance does not depend on a contradiction built from `Φ`.

---

## 3.5 The γ-dichotomy (the round-8 restructuring)

The proof is now organized around the single, exhaustive dichotomy on the diagonal ratio `γ`:

> **Dichotomy.** For full-support `P` with `β<1/2`, either `γ < β` or `γ ≥ β`.
>
> - **Branch 1 (`γ < β`): CLOSED.** By Lemma 7 (proven, round 2), the `k=1` full-collapse B1
>   (spanning path on a single copy, `S={(1,2),(2,3),…,(n−1,n)}`) yields
>   `maxbias(P') = γ`. Since `γ < β`, we have `maxbias(P') = γ < β = maxbias(P)`. **Done.**
> - **Branch 2 (`γ ≥ β`): OPEN** (the `1ⁿ`-heavy minority); treated as the residual in §10′.

**Branch 1 is genuinely exhaustive within `γ<β`** — there is no sub-case to check. `γ` is
well-defined for every full-support `P` (`P(0ⁿ),P(1ⁿ)>0`), the collapse atom `{0ⁿ,1ⁿ}` on the single
copy has positive mass, and Lemma 7's identity `maxbias(B1) = γ` is an exact closed form (re-verified
exact this round, §11′). This is **not** a sweep used as a proof: it is the direct content of a proven
lemma. The only role of computation here is to confirm the realized full `n`-coordinate maxbias of
the explicit conditioning equals `γ` (it does, 0 mismatch — §11′), and to report the empirical size
of the branch.

**Coverage of Branch 1 (reported, not used as proof).** Over exact `n=3` sweeps (20000 seeds, scales
8/12/16), the frustrated `β<1/2` instances split as `γ<β : γ≥β = 1687:106, 653:32, 1805:98`
respectively — i.e. **Branch 1 closes 94.1% / 95.3% / 94.9%** of all frustrated stalls by Lemma 7
alone. **Seed 770** (the R7 over-count witness, biases `(20/41, 18/41, 8/41)`, `β=20/41<1/2`) has
`γ = 1/8 < β` and is in Branch 1: B1 full-collapse gives `maxbias = 1/8 < β` (verified exact, §11′).

The remaining work is entirely in Branch 2 (`γ≥β`), which §4′–§10′ narrow precisely.

---

## 4. The reduction family F⁺ (vertex-transitive, all-copies-identical)

Per the standing rule we use only conditionings whose realization makes all `k` copies share the same
bias vector, so full `nk`-maxbias equals the single-copy maxbias of the operator (verified per
operator). The named family, now **augmented with B4**:

- **B1 (full-collapse, Lemma 7):** `k=1`, spanning path. `maxbias = γ`. Fires `⟺ γ<β`.
- **B2 (identity-match on a subset `T⊆[n]`, Lemmas 2/3):** `k=2`, copies identical. Reweight
  `P·m_T/Z`. Special cases: `T={i*}` (AND-amplifier), `T=T₀` (tied-max set), `T={i,j}` (pair-match).
- **B3 (symmetric-Gram, Lemmas 5/5′/6):** `k=3` permuted 3-cycle on a **symmetric** pair `{i,j}`.
  By Lemma 8 (C2) it always reduces that pair's two biases; safe (all copies identical) by Lemma 5′.
- **B4 (involution-permuted matching, NEW — Lemma 10 below):** `k=2`, `S={(i,n+π(i))}` for an
  involution `π=π⁻¹`. All copies identical; reweight `P(x)·P(π·x)/Z`. For `n=3` the nontrivial
  involutions are the three transpositions `(0,2,1),(1,0,2),(2,1,0)` (the last being the reverse
  permutation).
- **B5 (cyclic `k=3`):** the verified `k=3` cyclic realization for **non-involution** permutations
  (3-cycles), which are NOT copy-identical at `k=2` (see Lemma 10's caveat); realized as the
  Lemma-5-style permuted 3-cycle, full `3n`-maxbias.

`F⁺ := {B1, B2, B3, B4, B5}`. By Lemmas 0–2/5/10 each member's realization is a single conditioning of
`P^k` with all copies identical (verified). The closure question for Branch 2 is whether *some* member
of `F⁺` reduces full maxbias — and §10′ states this honestly as OPEN.

---

## 4′. Lemma 10 (NEW) — involution-permuted matchings are all-copies-identical

This is the round-8 structural lemma. It supplies operator **B4** and repairs a genuine
non-exhaustiveness defect in the old family `F = {B1,B2,B3}`.

**Setup.** Fix a permutation `π` of `[n]={0,…,n−1}` and consider `P²` on `{0,1}^{2n}` with global
coordinates `(0,i)` (copy 0) and `(1,i)` (copy 1), `0≤i<n`. Let
```
S = { ((0,i), (1, π(i))) : 0 ≤ i < n }.
```
This is a perfect matching between the two copies that connects copy-0 coordinate `i` to copy-1
coordinate `π(i)`. Define `P' := P² | {X_u = X_v ∀(u,v)∈S}`, the conditioning that forces
`x^{(0)}_i = x^{(1)}_{π(i)}` for all `i`.

**Lemma 10.** Let `π` be an **involution**, `π = π⁻¹`. Then:

1. **(Copy-0 law)** The marginal of copy 0 under `P'` is
   ```
   P'_{copy 0}(x) = P(x)·P(π·x) / Z,   where  (π·x)_j := x_{π(j)},   Z = Σ_x P(x)·P(π·x).
   ```
2. **(Copy-1 law)** The marginal of copy 1 under `P'` is the *same* law: `P'_{copy 1}(y) = P(y)·P(π·y)/Z`.
3. **(All-copies-identical)** Hence the two copies have identical bias vectors, and the full
   `2n`-coordinate realized maxbias of `P'` equals the single-copy maxbias of the law `P(x)·P(π·x)/Z`.

**Proof.**

*Step 1 — the constraint is a bijection on atoms.* The matching `S` connects each copy-0 coordinate
to exactly one copy-1 coordinate and vice versa (`π` is a permutation, so `i↦π(i)` is a bijection
`[n]→[n]`). By Lemma 0, conditioning collapses each connected component of the constraint graph
`([2n],S)` to a single value. Each component here is a single edge `{(0,i),(1,π(i))}`, so the surviving
atoms are exactly those `(x,y)∈{0,1}^n×{0,1}^n` with `x_i = y_{π(i)}` for all `i`. Given the copy-0
half `x`, the copy-1 half `y` is **fully determined**: `y_{π(i)} = x_i` for all `i`. Writing `j=π(i)`
(so `i=π⁻¹(j)`), this says `y_j = x_{π⁻¹(j)}` for all `j`, i.e. `y = π⁻¹·x` where `(σ·z)_j := z_{σ(j)}`.

Thus the surviving atoms are in bijection with `{0,1}^n` via `x ↦ (x, π⁻¹·x)`, and by Lemma 0
```
P'(x, y) ∝ P²(x,y) · 1[y=π⁻¹·x] = P(x)·P(y)·1[y=π⁻¹·x],
```
so the (unnormalized) law on the copy-0 half is `x ↦ P(x)·P(π⁻¹·x)`.

*Step 2 — involution collapses π⁻¹ to π.* Since `π` is an involution, `π⁻¹=π`, so `π⁻¹·x = π·x` where
`(π·x)_j = x_{π(j)}`. Hence
```
P'_{copy 0}(x) = P(x)·P(π·x) / Z,    Z = Σ_x P(x)·P(π·x),
```
proving claim 1. (Without the involution hypothesis the law would be `P(x)·P(π⁻¹·x)`; the symmetry
needed for claim 2 below would then fail.)

*Step 3 — the two copies have the same law (this is where π=π⁻¹ is load-bearing).* The law of copy 1
is obtained by marginalizing `P'(x,y)` over `x`. For a fixed copy-1 value `y`, the unique surviving
`x` is the one with `x_i = y_{π(i)}` for all `i`, i.e. `x = π·y` (since `(π·y)_i = y_{π(i)}`). Hence
```
P'_{copy 1}(y) ∝ P(π·y)·P(y) = P(y)·P(π·y),
```
the **same** unnormalized function of its argument as the copy-0 law. (Both equal `w(z):=P(z)·P(π·z)`
evaluated at the copy's own value.) Crucially, `w` is **symmetric under π**: `w(π·z) = P(π·z)·P(π·π·z)
= P(π·z)·P(z) = w(z)`, using `π·π = id` (the involution property). This symmetry is exactly what makes
the copy-0 marginal and copy-1 marginal coincide as *functions*, not merely up to the relabeling `π`.

*Step 4 — identical bias vectors and full maxbias.* By Steps 2–3, both copies of `P'` have the same
law `w(z)/Z`. Therefore for each coordinate `i`, the bias of global coordinate `(0,i)` equals the bias
of `(1,i)` (both `= Pr_{z∼w/Z}(z_i=1)`). The set of `2n` realized biases is exactly the multiset
`{bias_i(w/Z) : i} ∪ {bias_i(w/Z) : i}`, so
```
maxbias(P') = max over all 2n coords = max_i bias_i(w/Z) = maxbias( P(x)·P(π·x)/Z ),
```
the single-copy maxbias of the closed-form law. This proves claim 3. ∎

**Caveat (non-involutions are NOT covered, by design).** For a non-involution `π` (e.g. a 3-cycle on
`n=3`), `π⁻¹≠π`, the copy-0 law is `P(x)·P(π⁻¹·x)` and the copy-1 law is `P(y)·P(π·y)` — these are
*different* functions (one uses `π⁻¹`, the other `π`), so the copies are **not** identical and full
`2n`-maxbias can exceed the single-copy value. Verified exact: on seed 16832 the 3-cycles `(1,2,0)`
and `(2,0,1)` give `copies_identical = False` (§11′). For non-involution permutations the correct
vertex-transitive realization is the **`k=3` cyclic matching** B5 (Lemma 5-style), with full
`3n`-maxbias — the builder must use B5, never apply Lemma 10's `k=2` form to a 3-cycle. (This matches
the round-6 standing rule: a `k=2` permuted matching is all-copies-identical only when it is genuinely
copy-symmetric, which for the full `n`-coordinate matching means `π=π⁻¹`.)

**Why B4 is load-bearing (the seed-16832 defect).** The old family `F={B1,B2,B3}` is **non-exhaustive
even on `γ≥β`**: at scale 16, seed 16832 (weights
`{000:1,001:15,010:12,011:1,100:8,101:3,110:5,111:2}`, `β=21/47≈0.4468`, `γ=2/3≥β`) stalls every
member of `F` — every singleton/pair/triple identity-match has full maxbias `≥β`; `B1 = γ = 2/3 > β`;
and there is **no symmetric pair**, so B3 cannot fire. It is reduced **only** by B4: the involution
revperm `π=(2,1,0)` gives full `2n`-realized maxbias `= 79/204 ≈ 0.3873 < β` (all six coordinate biases
`{0.338, 0.387, 0.338, 0.338, 0.387, 0.338}` lie below `β`; full `2n` = single-copy closed form,
verified exact §11′). So **B4 is required** in the family; this is exactly the non-exhaustiveness
defect Lemma 10 repairs.

---

## 5. Proven coverage (the closed regimes)

| Regime | Construction | Status |
|---|---|---|
| `n ≤ 2` | `k=1` collapse `(★)` | Proved (Prop B) |
| unique mode `0ⁿ` | AND-tree, explicit `k=2^t` | Proved (Prop A) |
| non-frustrated (`Cov(i*,·)≥0`) | identity-match `{i*}` | Proved (Prop C) |
| **`γ < β`** (Branch 1, the `1ⁿ`-light majority, ~95% of frustrated `n=3`) | **full collapse B1, `k=1`** | **Proved (Lemma 7); restructured as Branch 1** |
| `Cov(x_j,x_{i*})>0` for all `j` clears match-`{i*}` | AND-amplifier | Proved (Lemma 3) |
| symmetric pair `{i*,j}`, residual coords `<β` after Gram | Gram `k=3` permuted | Proved (Prop D; C2 makes firing unconditional) |

**The residual** to which the theorem is not yet reduced is exactly Branch 2:

> **(R) The `γ≥β` stall residual.** `P` is full-support, frustrated, `n≥3`, `β<1/2`, **`γ≥β`** (so B1
> fails), and *no single named member of `F⁺` has been proven to fire* — because the firing member is
> currently selected by an oracle over `2ⁿ−1` subsets and the permutation set, with no proven
> selection rule.

By Lemma 8, on `(R)` every pair is 0-dominated; by C2 every symmetric pair admits a pair-reducing
Gram step. So `(R)` is not obstructed at the pair level; it is obstructed solely by the
third-coordinate rise and the un-routed member selection. This is the open core, stated in §10′.

---

## 6. The litmus witnesses, discharged (reused from r5 §8, not regressed)

Each litmus is discharged by a *named* operator with an exact verified reduction (verbatim from
`proof-attempt-r5.md` §8):

- **Litmus A** (seed 135209, biases all `8/17`, all pairs symmetric & 0-dominated, `γ=1/2≥β`, tied-set
  match fails) — Branch 2. Cleared by the **`k=3` cyclic matching** B5
  `S={(0,3),(3,7),(1,5),(5,6),(2,4),(4,8)}`: full 9-coord maxbias `746/1987 ≈ 0.37544 < 8/17`. Exact.
- **Litmus B** (seed 789, `β=28/59`, **no symmetric pair**, `γ=9/17>β`) — Branch 2. Cleared by the
  identity-match B2 on `T={1}`: full maxbias `789/1745 ≈ 0.45215 < 28/59`. Exact (re-verified §11′).
- **Litmus C** (seed 8191, `β=18/41`, **no symmetric pair**, `γ≥β`, tied-set match fails) — Branch 2.
  Cleared by the identity-match B2 on `T={0,2}`: full maxbias `≈ 0.42495 < 18/41`. Exact (re-verified
  §11′).

All three are Branch-2 (`γ≥β`) instances cleared by named operators — they are within the residual
`(R)` but discharged individually; the open gap is the *general* `γ≥β` closure, not these witnesses.

---

## 10′. THE GAP (stated precisely; what is proven, what is open)

**Proven this round (new):**
- **Branch 1 (`γ<β`) is closed** by Lemma 7, stated as the first branch of an exhaustive dichotomy.
  This is a genuine closure of the theorem for the entire `γ<β` regime (~95% of frustrated `n=3`
  stalls), including seed 770.
- **Lemma 10** (involution-permuted matchings are all-copies-identical; copy-0 = copy-1 law
  `P(x)·P(π·x)/Z`; full `2n`-maxbias = single-copy maxbias). Adds operator **B4**, repairing the
  seed-16832 non-exhaustiveness defect with the **right object** (full realized maxbias).

**Reused (proven earlier, not regressed):** Lemmas 0–8, Props A–D, the litmus discharges.

**Open (the residual `(R)` = Branch 2, `γ≥β`).**

> **`γ≥β` Closure (OPEN).** Let `P` be full-support, frustrated, `n≥3`, `β<1/2`, with `γ≥β`. Then
> there exists a member of `F⁺ = {B1,B2,B3,B4,B5}` whose single-copy (= full, by vertex-transitivity /
> Lemmas 2/5/10) maxbias is `< β`.

**Why it is not closed, precisely (and which levers are dead).**

- **No named single-member selection exists.** The clean dichotomy the R7 critic hoped for —
  "`γ≥β` ⟹ singleton-match on the diagonal-heavy coordinate `i*`" — is numerically **false**: the
  AND-amplifier match `{i*}` clears only `54/106, 70/97, 72/98` of `γ≥β` stalls across scales, and
  `27/97` of them have `match{i*} ≥ β` (survey probes 3, 5). No named pair rule closes it either:
  most-negative-cov pair `11/20`, two-non-worst `8/20`, two-smallest-bias `7/20`, triple `7/20`
  (survey probe 4). This is the 4th recurrence of the **"true union, false mechanism"** wall, now
  relocated into Branch 2. **Do not propose a single named member as the `γ≥β` closure.**
- **The `min Φ`-increase lever is refuted (dead lever #7).** The Angle-2 plan — "SOME involution
  strictly increases `min_{ij}Φ_{ij}`, and the only common fixed point of all involution-reweights is
  a point mass" — was gated pre-build by the approach-critic on the **exact `γ≥β` stall set** and is
  **numerically false**: it fails on `2/97` (scale 12), `5/106` (scale 8), `3/98` (scale 16) genuine
  in-hypothesis `γ≥β` stalls. On those (e.g. seed 1219, biases `(25/51, 8/17, 25/51)`, `β=25/51<1/2`,
  `γ=10/19≥β`) **every** involution-reweight gives `min Φ ≤ baseline` and `maxbias ≥ 0.50`, and the
  clearing move is `match{1}` — a **non-involution** identity-match. So `min Φ` (= `1 − sum of the two
  largest biases`) joins ψ, separable `Σf(b_i)`, Φ-magnitude pair-selection, `Σb_i`, tied-core
  averaging, and single-copy iterated `M_argmax` on the dead-lever list. **Do not use `min Φ`-increase
  or any involution-orbit fixed-point argument.**

**Disclosed regression backstop (NOT a proof).** The enlarged family `F⁺ = F ∪ {B4}` has an **empty
stall set** on the `γ≥β` residual: 0/20000 frustrated `β<1/2` `n=3` seeds at each of scales 8, 12, 16
(survey + my own exact re-run, §11′). In particular the unique scale-16 old-`F` stall (seed 16832) is
cleared by B4. **This is recorded as a disclosed regression backstop only.** It is the "true union"
half of the wall; the *routing mechanism* (which member of `F⁺` fires) is still an unproven oracle.
**It is used in NO proof step**, exactly as the standing rule requires.

**What would suffice (the minimal missing content).** A non-constructive existence over `F⁺` proving
SOME member reduces full maxbias on every `γ≥β` instance, via a potential that is (a) maxbias-implying
and (b) provably moved by some family member — where the potential is **not** a separable sum, `Σb_i`,
Φ-magnitude, or `min Φ` (all refuted), and the mover is **not** restricted to involutions (the
clearing move on the refuting seeds was a non-involution match). The most concrete untested route
(suggested by the approach-critic for future rounds, **not built here**): a `γ≥β`-specific lower bound
on the singleton-match collateral via the Lemma-3 formula
`b'_ℓ = [(1−β)b_ℓ + (2β−1)p^{(ℓ)}_{11}]/D` — `γ≥β` lower-bounds the `11`-corner mass `p^{(ℓ)}_{11}` —
**paired with a routed fallback** to a specific other member with a proved inequality. Until such a
routed bound exists, Branch 2 stays open.

---

## 11′. Computational checks (exact rational; code + outputs)

All run during construction; exact `fractions.Fraction`; harness `/tmp/r8lib.py` (reuses the
`/tmp/scout2.py` product/condition/maxbias machinery). No floating point in any decision; floats shown
only for human readability. Sweeps ≤20000 seeds per the operational constraint, chunked.

### 11′.1 Lemma 10 — involution matchings all-copies-identical, full `2n` = single-copy (EXACT)

For each seed in `{16832, 770, 8356, 9350, 12663, 16580, 6639, 1219, 1523, 12599}` and each of the
four involutions on `n=3` (`(0,1,2),(0,2,1),(1,0,2),(2,1,0)`), the realized full `2n`-coordinate
maxbias of `P²|S` (`S={(i,3+π(i))}`) equals the single-copy maxbias of the closed form `P(x)·P(π·x)/Z`,
and both copies have identical bias vectors:
```
all involutions all-copies-identical AND full2n==closedform: True
```
The closed-form direction `z` (defined by `z_{π(i)}=x_i`) equals `π·x` (`(π·x)_j=x_{π(j)}`) for every
`x`, for every involution and every tested seed:
```
seed 16832 perm (0,2,1) z==pi.x for all x: True   (and (2,1,0),(1,0,2),(0,1,2): True)
seed  8356 perm (0,2,1) z==pi.x for all x: True   (and (2,1,0),(1,0,2),(0,1,2): True)
```
Non-involutions (3-cycles) are NOT copy-identical (so Lemma 10 correctly does not apply; use B5):
```
3-cycle (1,2,0) copies_identical= False
3-cycle (2,0,1) copies_identical= False
```

### 11′.2 Branch 1 (`γ<β`) — B1 realized maxbias = γ, seed 770 (EXACT)

```
seed 770 biases ['20/41','18/41','8/41'] beta=20/41 (0.48780)
gamma=1/8 (0.12500)  gamma<beta? True
B1 realized full collapse maxbias = 1/8 (0.12500)  == gamma? True
```
Lemma 7's identity `maxbias(B1)=γ` confirmed; seed 770 is in Branch 1 and cleared by B1.

### 11′.3 Seed 16832 — old family F stalls; B4 rescues (EXACT)

```
seed 16832 beta = 21/47 (0.44681)  biases [0.38298, 0.42553, 0.44681]
gamma = 2/3 (0.66667)  >= beta? True
family_reduces (B1 + all matches + symmetric-Gram): None   (every member stalls)
involution (2,1,0) closed-form maxbias 0.38725 < beta? True
involution (0,2,1) closed-form maxbias 0.43478 < beta? True
involution (1,0,2) closed-form maxbias 0.51876 < beta? False
seed 16832 revperm FULL 2n maxbias = 79/204 (0.38725) < beta? True
  per-coord 6 biases: [0.33824, 0.38725, 0.33824, 0.33824, 0.38725, 0.33824]
```
Full `2n`-realized maxbias `79/204` equals the single-copy closed form, all six biases `<β`. B4 is
load-bearing.

### 11′.4 γ-dichotomy coverage and the F⁺ backstop (DISCLOSED BACKSTOP, NOT A PROOF)

Exact `n=3` sweep, scale 12, `N=8000`:
```
frustrated 685  gamma<beta 653  gamma>=beta 32
F-stall (within gamma>=beta) 0   F+stall 0   []
gamma<beta fraction of frustrated: 0.953
```
Exact `n=3` sweep, scale 16, `N=20000`:
```
frustrated 1903  gamma<beta 1805  gamma>=beta 98
F-stalls (old family fails, gamma>=beta): 1  [(16832, 21/47)]
F+ stall (with B4 involution matchings): 0
```
So Branch 1 (`γ<β`) covers ~95% of frustrated stalls (the content of Lemma 7), and the enlarged family
`F⁺ = F ∪ {B4}` has **empty stall** over the `γ≥β` residual on these sweeps. **Used in NO proof step.**

### 11′.5 Litmus B / C named-operator discharges, re-verified (EXACT)

```
seed 789 match (1,)  maxbias 0.45215  beta 0.47458  reduces? True
seed 8191 match (0,2) maxbias 0.42495 beta 0.43902  reduces? True
seed 135209 biases [8/17, 8/17, 8/17]  beta 8/17     (Litmus A; cleared by B5, r5 §8)
```

---

## 12′. Summary of status

| Component | Status |
|---|---|
| Lemmas 0–8, Props A/B/C/D (rounds 1–2, 5) | **Proved** (reused, not regressed) |
| γ-dichotomy restructuring (exhaustive on `γ<β` vs `γ≥β`) | **NEW** |
| **Branch 1 (`γ<β`): full-collapse B1, `maxbias = γ < β`** | **Proved (Lemma 7); stated as Branch 1, ~95% of frustrated** |
| **Lemma 10 (involution matchings all-copies-identical; copy law `P(x)P(π·x)/Z`; full 2n = single-copy)** | **Proved (NEW), exact-verified** |
| **B4 added to family `F → F⁺`; repairs seed-16832 non-exhaustiveness** | **Proved (NEW)** |
| Litmus A (B5 k=3 cyclic), B (match{1}), C (match{0,2}) | **Discharged by named operators (reused)** |
| **`γ≥β` Closure (Branch 2, §10′)** | **OPEN** — no named selection; `min Φ`-increase refuted (dead lever #7); F⁺ 0/20000 backstop only |

**The round-8 advance:** (i) the proof is restructured around the exhaustive γ-dichotomy, with
**Branch 1 (`γ<β`) fully closed** by Lemma 7 — a clean, large, named branch covering ~95% of
frustrated `n=3` stalls and the R7 witness seed 770; and (ii) **Lemma 10** is newly proven, adding the
load-bearing operator **B4** (involution-permuted matchings, all-copies-identical, full `2n`-maxbias =
single-copy closed form `P(x)·P(π·x)/Z`) and repairing the seed-16832 non-exhaustiveness defect with
the right object. **Branch 2 (`γ≥β`) remains OPEN** and is stated honestly: every named member
selection is refuted (probes 3–5), the `min Φ`-increase lever is refuted on the exact `γ≥β` stall set
(dead lever #7), and the empirical 0/20000 `F⁺` clearance is a disclosed regression backstop used in no
proof step.
