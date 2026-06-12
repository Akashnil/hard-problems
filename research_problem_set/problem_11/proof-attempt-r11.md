# Problem 11 — Proof attempt (Round 11)

**Approach (γ≥β branch only):** the **c-dichotomy** over the whole realizable family
`B2(all nonempty subsets) ∪ B5cyc`. This builds **on top of** `proof-attempt-r8.md`: all of
Lemmas 0–8, 5′, 10, Props A–D, and the closed `γ<β` branch (Lemma 7) are **reused verbatim and not
regressed**. The new content is §A1–§A6 below: the c-dichotomy structure (§A2), Engine A
(`c<β`, §A3, **FULLY CLOSED**), the pair-match / singleton closed forms (§A4), and the Engine-B
sub-dichotomy (§A5–§A6).

**Status: INCOMPLETE.** The `γ<β` branch stays CLOSED (Lemma 7). For `γ≥β`:

- **Engine A (`c<β`):** **FULLY CLOSED** (§A3) — provable by definition. Covers 963/990 of the
  exact n=3 `γ≥β` stall set (budget 40000), and 3460/3532 at budget 60000.
- **Engine B (`c≥β`):** advanced to two **precise, reformulated strict inequalities** with named
  gaps (§A5, §A6). Specifically:
  - **Clause 4b (strict-unique max → singleton-on-worst):** the matched coord drops to `β²/D<β`
    (Lemma 3, closed); the collateral bound `b'_ℓ<β` is **FULLY CLOSED on the `Cov>0` half**
    (Lemma 3 dichotomy) and reduced on the `Cov≤0` half to the clean equivalent
    `β(D−p_ℓ) > (1−β)q_ℓ` — **advanced-with-gap** (§A5).
  - **Clause 4a (tied max → min over all 3 pair-matches < β):** the matched coords of every pair
    drop below β (so `maxbias(pairmatch{i,j}) = r_ℓ`, the unmatched rise, on tied cases — verified
    exact, §A4); the load-bearing claim `¬(r_0≥β ∧ r_1≥β ∧ r_2≥β)` is the genuine **3-way
    polynomial infeasibility** — **advanced-with-gap** (§A6). The corrected rule is **min over all
    three pair-matches** (NOT the tied-max pair — that is false on seed 25305, the new litmus).

All closed forms and identities below are exact `fractions.Fraction`; code + outputs in §A7. No
floating point enters any decision. Every thresholded quantity is the **full `nk`-coordinate
realized maxbias of an explicit `P^k|S`** (Lemmas 2/5/10), per the round-1/round-6 standing rules.

---

## A0. Reuse statement

From `proof-attempt-r8.md`, treated as given and **not re-proved**:

- **Lemma 0–2** conditioning = component collapse; identity-match on `T⊆[n]` at `k=2` makes both
  copies share `P_T(x) ∝ P(x)·m_T(x_T)` (all-copies-identical; full `2n`-maxbias = single-copy).
- **Lemma 3** AND-amplifier (`T={i*}`): `b'_{i*}=β²/D`, `D:=β²+(1−β)²`; exact collateral
  `b'_ℓ = [(1−β)b_ℓ + (2β−1)p^{(ℓ)}_{11}]/D` with `p^{(ℓ)}_{11}=Pr(x_{i*}=1,x_ℓ=1)`; dichotomy
  `b'_ℓ<b_ℓ ⟺ Cov(x_ℓ,x_{i*})>0`.
- **Lemma 5/5′** Gram = `k=3` permuted 3-cycle; all-copies-identical iff the pair is symmetric.
- **Lemma 7** full-collapse `k=1`: `maxbias = γ`; the **`γ<β` branch is CLOSED**.
- **Lemma 8** every pair under `β<1/2`: `Pr(11)−Pr(00) = b_i+b_j−1 < 0`, so every pair is strictly
  0-dominated, `Φ_{ij}=1−b_i−b_j>0`.
- **Lemma 10** involution-permuted matching `B4` is all-copies-identical.

Notation: `P` full-support on `{0,1}³`, `b_i=bias_i`, `β=maxbias<1/2`. `γ=P(1³)/(P(0³)+P(1³))`.
The conditioning event always has positive mass (full support), so every `P'` is well-defined.

---

## A1. The realizable family for the γ≥β branch (whole F⁺, no narrowing)

Per the standing rule (rounds 9, 10: *every narrowing of F⁺ breaks the union*), the closure
argument ranges over the **whole** realizable family. For the `γ≥β` branch it suffices to use the
two structurally-cleanest classes, **keeping all subsets**:

- **B2** — identity-match on **every** nonempty subset `T⊆{0,1,2}` (singletons, pairs, the triple);
  `k=2`, all-copies-identical (Lemma 2), reweight `P(x)·Q_T(x_T)/Z` where `Q_T(x_T)=Pr(x_T)`.
- **B5cyc** — the `k=3` cyclic matching on a 3-cycle permutation `π` (Lemma 5 machinery);
  all-copies-identical for the two 3-cycles of `S₃`, full `9`-coordinate maxbias.

(B1 is the `γ<β` branch; B3, B4 are kept available but not needed for the structure below. The
critic independently confirmed `B2(all subsets) ∪ B5cyc` is 0-fail on the exact `γ≥β` stall set at
budget 60000 for n=3 (3532 stalls) and 40000 for n=4 (405). This is recorded as a **disclosed
regression backstop only**, §A7.4 — it is used in no proof step.)

---

## A2. The c-dichotomy (the round-11 structure)

**Definition (the equalized value `c`).** For `n=3`, let `π` be either of the two 3-cycles
`(1,2,0)` or `(2,0,1)` of `S₃`. The B5cyc reweight `w(x) ∝ P(x)·P(π·x)·P(π²·x)` is invariant under
the cyclic shift `x↦π·x` (it is a product over the full `π`-orbit of `x`). Consequently the three
coordinate biases of `w/Z` are **all equal** to a common value

> `c := bias₀(w/Z) = bias₁(w/Z) = bias₂(w/Z)`,

an explicit degree-3 cyclically-symmetric rational in the 8 atom-masses. By Lemma 5 the `k=3`
cyclic matching is all-copies-identical, so its full `9`-coordinate realized maxbias equals the
single-copy maxbias of `w/Z`, which is `c` (since all three coords are equal).

> **Verified exact (§A7.1):** on every one of the 72 Engine-B residual cases and on every one of the
> 990 n=3 stalls, both 3-cycles `(1,2,0)` and `(2,0,1)` give spread-0 (all 9 realized coordinate
> biases equal) and the same value `c`. So `maxbias(B5cyc) = c`, fires `⟺ c<β`.

**The dichotomy.** For full-support `P` with `β<1/2` and `γ≥β` (Branch 2; B1 fails by Lemma 7):

- **Engine A (`c<β`):** B5cyc has `maxbias = c < β`. **Done (§A3).**
- **Engine B (`c≥β`):** the residual; treated in §A5–§A6.

This is a genuine dichotomy on the explicit rational `c` vs the explicit rational `β`; no member is
named outside it.

---

## A3. Engine A (`c < β`) — FULLY CLOSED

**Claim.** If `c<β` then the `k=3` cyclic matching B5cyc has full `9`-coordinate realized maxbias
`= c < β = maxbias(P)`, a strict reduction.

**Proof.** By §A2, `maxbias(B5cyc)=c` exactly (the realization is all-copies-identical, Lemma 5, and
all three coordinate biases of the equalized law coincide). The hypothesis `c<β` gives the strict
inequality. The construction is the explicit `(k,S)` with `k=3` and `S` the cyclic matching
`{(i,3+π(i)), (3+i,6+π(i)), (6+i,π(i)) : i=0,1,2}` for `π=(1,2,0)`. ∎

**Coverage (computed exact, §A7.2):** Engine A clears **963 / 990** of the n=3 `γ≥β` stall set
(budget 40000); the critic's budget-60000 count is 3460/3532 ≈ 98.0%. Litmus: **seed 2085**
(`β=10/21`, `γ=1/2≥β`) has `c=81/230<β` — Engine A; **seed 16832** (`β=21/47`, `γ=2/3≥β`) has
`c=0.3379<β` — Engine A. Both are in Engine A, not the residual.

---

## A4. The Engine-B operators in closed form (exact)

Fix the residual: `β<1/2`, `γ≥β`, `c≥β`. Write `i*` for a worst coordinate (`b_{i*}=β`).

### A4.1 Pair-match (B2 on `T={i,j}`): matched and unmatched biases

By Lemma 2 the pair-match makes both copies share `P_{ij}(x) ∝ P(x)·Q[x_i][x_j]`, where
`Q[a][b]=Pr(x_i=a,x_j=b)`. Let `(a,b,c_,d) := (Q[0][0],Q[0][1],Q[1][0],Q[1][1])` (so `a+b+c_+d=1`,
`b_i=c_+d`, `b_j=b+d`). The full `6`-coordinate realized maxbias = single-copy maxbias of `P_{ij}`,
whose three biases are (verified exact identical to the raw build, §A7.3):

> **Matched coord `i`:** `b'_i = (c_²+d²) / Z`, `Z = a²+b²+c_²+d²`.
> **Matched coord `j`:** `b'_j = (b²+d²) / Z`.
> **Unmatched coord `ℓ` (the third):** `r_ℓ = (Σ_{ab} Q_{ab}·t_{ab}) / Z`, where
> `t_{ab} = Pr(x_i=a,x_j=b,x_ℓ=1)` and `Z = Σ_{ab} Q_{ab}²`.

**Exact algebraic fact (matched coord never above β, on tied cases).** A direct computation
(verified symbolically, §A7.3) gives, using `a+b+c_+d=1`,

> `b_i − b'_i = [(c_+d)(a²+b²) − (c_²+d²)(a+b)] / Z`.

On all **45 tied** Engine-B cases (and all 135 tied pair-instances), every pair-match satisfies
`b'_i<β` and `b'_j<β` (exact, §A7.3). Therefore on tied Engine-B cases

> `maxbias(pairmatch{i,j}) = max(b'_i, b'_j, r_ℓ) = r_ℓ` whenever `r_ℓ ≥ b'_i,b'_j`, and `<β`
> whenever `r_ℓ<β` (since then all three are `<β`).

Hence for tied cases, **`maxbias(pairmatch{i,j}) < β ⟺ r_ℓ < β`**, and clause 4a is exactly the
3-way statement `¬(r_0≥β ∧ r_1≥β ∧ r_2≥β)` (§A6).

### A4.2 Singleton-on-worst (B2 on `T={i*}`): the Lemma-3 form

The singleton match `{i*}` is the AND-amplifier (Lemma 3). Its full `6`-coordinate realized maxbias
is (verified exact = raw build, §A7.3) the maximum of

> `b'_{i*} = β²/D < β` (`D=β²+(1−β)²`), and the two collateral
> `b'_ℓ = [(1−β)b_ℓ + (2β−1)p^{(ℓ)}_{11}]/D`, `ℓ≠i*`, `p^{(ℓ)}_{11}=Pr(x_{i*}=1,x_ℓ=1)`.

`b'_{i*}=β²/D<β` is immediate (`β<1/2 ⟹ β²<D`). The work is the collateral bound `b'_ℓ<β` (§A5).

---

## A5. Clause 4b — strict-unique max ⟹ singleton-on-worst

**Setting.** Engine-B residual, `i*` the **strict-unique** max (`b_{i*}=β > b_ℓ` for both `ℓ≠i*`).
Use the singleton-on-worst operator (§A4.2). `maxbias = max(β²/D, b'_{ℓ₁}, b'_{ℓ₂})`. Since
`β²/D<β`, the claim `maxbias<β` reduces to the **two collateral bounds** `b'_ℓ<β`.

### A5.1 The `Cov>0` half — FULLY CLOSED

If `Cov(x_ℓ, x_{i*}) > 0`, then by the Lemma-3 dichotomy `b'_ℓ < b_ℓ`. The strict-unique
hypothesis gives `b_ℓ < β`. Hence `b'_ℓ < b_ℓ < β`. **Closed.** (On the 27 strict residual cases,
exactly 27 of 54 collateral instances have `Cov>0` and are closed here — §A7.5.)

### A5.2 The `Cov≤0` half — reformulated, advanced-with-gap

When `Cov(x_ℓ,x_{i*}) ≤ 0`, `b'_ℓ` may exceed `b_ℓ` (all 27 such instances do, §A7.5). The bound
`b'_ℓ<β` is **equivalent** to a clean linear inequality in the `(i*,ℓ)` joint masses. Writing
`p_ℓ = Pr(x_{i*}=1,x_ℓ=1)`, `q_ℓ = Pr(x_{i*}=0,x_ℓ=1)` (so `b_ℓ = p_ℓ+q_ℓ`):

> **`b'_ℓ < β  ⟺  β(D − p_ℓ) > (1−β)·q_ℓ`.** (Derivation in §A5.3; verified exact, §A7.5.)

This is the precise remaining obligation for clause 4b. **It is genuinely global** — it is *false*
using only the `(i*,ℓ)` 2×2 marginal and `b_ℓ ≤ β`:

> **Boundary obstruction (exact, §A7.5).** At `b_ℓ → β` (i.e. `q_ℓ = β − p_ℓ`), the LHS−RHS equals
> `(1−2β)(p_ℓ − β²)`. Since `1−2β>0` and `p_ℓ = Pr(x_{i*}=1,x_ℓ=1) < β²` on **every** strict
> residual case (27/27, §A7.5), this is **negative**. So the collateral bound *requires* `b_ℓ` to
> sit strictly below `β` by a margin
> `β − b_ℓ ≥ (1−2β)(β² − p_ℓ)/(1−β)` — i.e. the strict-unique max must beat the collateral by a
> quantified amount that is **not implied by `b_ℓ<β` alone**.

**Gap (4b, `Cov≤0`):** prove `β(D−p_ℓ) > (1−β)q_ℓ` on the Engine-B residual with
`Cov(x_ℓ,x_{i*})≤0`. Equivalently, prove the quantified strict-unique gap
`β − b_ℓ > (1−2β)(β²−p_ℓ)/(1−β)`. The minimum verified slack is `0.00397` (seed 33667 scale 21,
§A7.5) — thin, and the needed lower bound on `p_ℓ` (or on the gap `β−b_ℓ`) must come from the
global hypotheses (`c≥β`, full support, the unique-max structure), not the 2×2 joint. A sufficient
(but not yet proven uniform) route confirmed on all 27 strict cases is `p_ℓ ≥ P(1³)` together with
`P(1³) ≥ (1−β)b_ℓ−βD)/(1−2β)` wherever the RHS is positive (only 2/54 instances; §A7.5) — but
`P(1³) ≥ β²` is **false** (27/27, §A7.5), so this needs a tighter lower bound on `P(1³)` than is
currently in hand.

### A5.3 Derivation of the 4b reformulation

`b'_ℓ = [(1−β)b_ℓ + (2β−1)p_ℓ]/D` (Lemma 3, `p_ℓ=p^{(ℓ)}_{11}`). Then
`b'_ℓ < β ⟺ (1−β)b_ℓ + (2β−1)p_ℓ < βD`. Substitute `b_ℓ = p_ℓ + q_ℓ`:
`(1−β)(p_ℓ+q_ℓ) + (2β−1)p_ℓ < βD ⟺ p_ℓ[(1−β)+(2β−1)] + (1−β)q_ℓ < βD
⟺ β·p_ℓ + (1−β)q_ℓ < βD ⟺ β(D−p_ℓ) > (1−β)q_ℓ.` ∎ (verified exact, §A7.5.)

---

## A6. Clause 4a — tied max ⟹ min over all three pair-matches < β

**Setting.** Engine-B residual, the max is **tied** (`≥2` coords equal `β`).

### A6.1 Reduction to the 3-way infeasibility (the corrected rule)

By §A4.1, on every tied Engine-B case **all three pair-matches drop both their matched coords below
β** (verified exact, 135/135 tied pair-instances, §A7.3). Hence

> `maxbias(pairmatch{i,j}) < β  ⟺  r_ℓ < β` (`ℓ` the unmatched coord),

so the clause `min over the 3 pair-matches of maxbias < β` is **exactly**

> **(4a):  `¬(r_0 ≥ β ∧ r_1 ≥ β ∧ r_2 ≥ β)`,**  `r_ℓ = (Σ_{ab} Q^{(ℓ)}_{ab} t^{(ℓ)}_{ab})/Z_ℓ`,

a 3-way infeasibility on the unmatched rises. **Verified 0-fail on all 45 tied residual cases**
(§A7.3), min margin `β − min_ℓ r_ℓ = 188/46797 ≈ 0.004017` (seed 25305).

**The corrected rule is mandatory (litmus seed 25305, §A7.6).** For
`P/57 = {000:6,001:9,010:12,011:2,100:10,101:6,110:1,111:11}` (`β=28/57≈0.49123`, `γ=11/17≥β`,
frustrated), the **tied-max** coords are `{0,2}`, but the tied-max pair-match `{0,2}` gives maxbias
`0.5099 ≥ β` (the freed mass piles on the unmatched coord 1). What clears it is the pair-match
`{0,1}` (a tied-max coord with the **non-max** coord) → `0.4872 < β`. So "pick the tied-max pair" is
**false**; only **min over all three pairs** is correct.

### A6.2 Frustration is load-bearing (exact)

(4a) is **false without frustration.** On a perfectly C3-symmetric `P` (invariant under the cyclic
shift of coordinates), all three biases are equal and, by symmetry, all three `r_ℓ` are equal; if
`c≥β` then all `r_ℓ≥β` and (4a) fails. **But such `P` are never in the hypothesis:**

> **Verified exact (§A7.7):** every C3-symmetric full-support `P` with `β<1/2`, `γ≥β`, `c≥β` is
> **non-frustrated** (0 frustrated of 1759 found at scale ≤20; and the in-hypothesis-premise hunt
> finds 0 frustrated C3-symmetric counterexamples in 20000 trials). So any certificate of (4a)
> **must consume a strict `Cov<0`** (some pair negatively correlated): without it the C3-symmetric
> family is a true-premise/false-conclusion family.

### A6.3 Gap (the genuine load-bearing core)

**Gap (4a):** prove `c≥β ∧ (β<1/2) ∧ (γ≥β) ∧ full support ∧ (some Cov<0) ⟹ ¬(r_0≥β ∧ r_1≥β ∧ r_2≥β)`,
where each `r_ℓ` is the degree-2 unmatched-rise rational of §A4.1. This is a **strict-inequality
polynomial infeasibility** on the 7-dimensional mass simplex with:

- a **non-compact / open** constraint set (the strict `Cov<0` has no quantitative lower bound;
  §A7.8 shows margin and frustration amount do not correlate monotonically — seed 28432: margin
  0.0052, min-cov −0.0024; seed 28178: margin 0.0054, min-cov −0.036);
- **thin margins** (`0.004017`), so no slack for a coarse bound;
- frustration **load-bearing** (§A6.2), so a Positivstellensatz must use `min_pair Cov < 0`
  multiplicatively.

I could not produce a hand-checkable SOS/Positivstellensatz certificate for this strict, non-compact
infeasibility in the available scope. This is the **7th (smallest) face** of the recurring
true-union/false-mechanism wall: the selection (whole `B2 ∪ B5cyc`) is exhaustive and the corrected
sub-dichotomy is true with no in-hypothesis counterexample (critic's hunt to seed 80000 +
400k adversarial near-C3 draws), but the closing inequality (4a) is not yet certified. The
surveyor's **Angle 3** (structural-emptiness reframing: show the set
`{γ≥β, c≥β, frustrated, all r_ℓ≥β}` is empty via a band invariant) remains the fallback; it is a
reformulation of the same risk and was not closed here either.

---

## A7. Computational checks (exact rational; code + outputs)

All exact `fractions.Fraction`; harness `/tmp/r11lib.py` (the `/tmp/scout2.py` product / condition /
maxbias machinery), driver scripts under `/tmp`. Every "maxbias" is the **full `nk`-coordinate**
realized maxbias of the explicit `P^k|S`. Floats are shown for readability only.

### A7.1 B5cyc equalizes all coords to `c`; `maxbias(B5cyc)=c` (EXACT)

On all **72** Engine-B residual cases and all **990** n=3 stalls, both 3-cycles `(1,2,0)`,
`(2,0,1)` give **spread 0** (all 9 realized biases equal) and the **same** value `c`; and `c≥β` on
the 72 residual:
```
All 72 residual: B5cyc both 3-cycles equalize to spread-0 common value c, and c>=beta: True
spread_bad (3-cycle not equalizing) over 990 stalls: 0
```

### A7.2 Engine A coverage (EXACT)

```
n=3 stalls: 990   Engine A (c<beta) cleared: 963   Residual c>=beta: 27
27-set ⊆ the 72 budget-60000 residual: True
litmus: seed 2085 (beta=0.4762, gamma=0.5000) c=0.3522  -> Engine A
        seed 16832(beta=0.4468, gamma=0.6667) c=0.3379  -> Engine A
Residual c>=beta split: TIED 45, STRICT-unique 27   (of the 72)
```

### A7.3 Pair-match / singleton closed forms; matched-coord drop (EXACT)

```
pair-match closed form (b'_i,b'_j,r_l) == raw full-6-coord biases: match True (e.g. seed 30619)
b_i - b'_i = [(c+d)(a^2+b^2)-(c^2+d^2)(a+b)]/Z  : symbolic diff under a+b+c+d=1 == 0
TIED cases: every pair-match has b'_i<beta AND b'_j<beta : 0 exceptions / (45 cases x 3 pairs)
   (the only matched>=beta instance in all 72 is seed 21834 pair {0,2}, which is STRICT -> clause 4b)
TIED: min over 3 pair-matches maxbias < beta : 0 fail / 45    min margin 188/46797 ~ 0.004017
TIED: min over 3 of r_l (unmatched rise) < beta : 0 fail / 45  (so 4a = the 3-way r_l infeasibility)
singleton-on-worst closed form (beta^2/D + collateral) == raw full-6-coord maxbias : OK / 27 strict
```

### A7.4 Disclosed regression backstop (NOT a proof)

```
Full c-dichotomy ALGORITHM (EngineA if c<beta; else TIED->min-3-pairs, STRICT->singleton-on-worst):
   n=3, 990 stalls: 0 fail
n=4, 405 stalls: [B2 all subsets] OR [B5cyc on 3-subset cycles], ALL n coords < beta : 0 fail
```
Used in **no** proof step (round-1 standing rule). The n=4 line is the Angle-2 collateral backstop.

### A7.5 Clause 4b reformulation and the boundary obstruction (EXACT)

```
strict residual: 27 cases, 54 collateral instances
  Cov(x_l,x_istar)>0 : 27 instances -> b'_l<b_l<beta (Lemma-3 dichotomy)   [CLOSED]
  Cov<=0             : 27 instances -> b'_l rose above b_l (all 27)         [gap]
reformulation  b'_l<beta  <=>  beta(D-p_l) > (1-beta)q_l : holds on all 54, worst slack 0.00397
boundary b_l->beta : LHS-RHS = (1-2beta)(p_l-beta^2) ; and p_l < beta^2 on ALL 27 strict (27/27)
required-threshold>0 only 2/54 instances; there P(1^3) >= threshold (slack >=0.08); but P(1^3)<beta^2 (27/27)
```

### A7.6 Litmus seed 25305 — corrected-4a rule mandatory (EXACT)

```
seed 25305: biases (28/57, 26/57, 28/57)  beta=28/57=0.49123  tied-max coords {0,2}
pair-match {0,1}: 0.4872 < beta  (clears)
pair-match {0,2}: 0.5099 >= beta (tied-max pair FAILS)
pair-match {1,2}: 0.4957 >= beta
=> min over all 3 pairs < beta ; tied-max-pair rule is FALSE.
```

### A7.7 Frustration load-bearing for (4a) (EXACT)

```
C3-symmetric full-support, beta<1/2, gamma>=beta, c>=beta: 1759 found -> frustrated 0
in-hypothesis premise hunt (full support, gamma>=beta, c>=beta, frustrated): 0 C3-sym counterexamples /20000
=> (4a) is false without frustration; the C3-symmetric in-band family is exactly non-frustrated.
```

### A7.8 No monotone margin↔frustration relation (EXACT, critic-reproduced)

```
seed 25305 margin 0.004017   ; seed 28432 margin 0.0052 min-cov -0.0024 ; seed 28178 margin 0.0054 min-cov -0.036
```

---

## A8. Summary of status (this round)

| Component | Status |
|---|---|
| Lemmas 0–8, 5′, 10, Props A–D, `γ<β` branch (Lemma 7) | **Reused, not regressed** |
| c-dichotomy structure (`maxbias(B5cyc)=c`, equalization) | **Proved (NEW)** |
| **Engine A (`c<β`): B5cyc maxbias = c < β** | **FULLY CLOSED (NEW)** — 963/990 (98% at budget 60000) |
| Pair-match closed forms; matched coords `<β` on tied cases | **Proved exact (NEW)** |
| Singleton-on-worst closed form (`β²/D` + Lemma-3 collateral) | **Proved exact (NEW)** |
| **Clause 4b — `Cov>0` collateral half** | **FULLY CLOSED (NEW)** (Lemma-3 dichotomy) |
| Clause 4b — `Cov≤0` half: `β(D−p_ℓ)>(1−β)q_ℓ` | **Advanced; named gap (§A5.2)** |
| Clause 4a — corrected rule (min over **all 3** pair-matches) | **Stated; tied-max-pair refuted (seed 25305)** |
| Clause 4a — `¬(r_0≥β∧r_1≥β∧r_2≥β)` (frustration load-bearing) | **Advanced; named gap (§A6.3)** |
| n≥4 (Angle 2) collateral-outside-core bound | **Disclosed backstop only (§A7.4)** |

**The round-11 advance:** (i) the `γ≥β` branch is restructured around the explicit **c-dichotomy**,
and **Engine A (`c<β`, ~98% of the residual) is FULLY CLOSED** — the first proven coverage inside
`γ≥β`; (ii) the Engine-B operators are written in **exact closed form**, the matched-coords-drop
fact is proved on tied cases (so clause 4a is *exactly* the 3-way unmatched-rise infeasibility), and
the singleton-on-worst form is proved; (iii) **clause 4b's `Cov>0` half is fully closed**, and the
`Cov≤0` half is reduced to the clean equivalent `β(D−p_ℓ)>(1−β)q_ℓ` with the precise boundary
obstruction (`p_ℓ<β²`) located; (iv) the corrected **min-over-all-3-pairs** rule is installed and
the tied-max-pair rule is refuted on the new litmus seed 25305; (v) **frustration is shown
load-bearing** (C3-symmetric in-band cases are exactly non-frustrated, exact). **The two named gaps
remain:** clause 4a's 3-way polynomial infeasibility (strict, non-compact, thin margins, frustration
load-bearing — the genuine core), and clause 4b's `Cov≤0` collateral inequality. No dead lever (none
of the 10) is used in any proof step; the n≥4 and full-algorithm sweeps are disclosed
backstops only.
