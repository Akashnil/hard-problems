# Problem 11 — Proof attempt (Round 2)

**Approach:** existence of `(k,S)` via a family of *realizable, all-copies-identical* conditioning
operators, attacked through a **diagonal-orientation** case analysis. New this round: the **Gram /
agreement operator** on the worst pair, established as an exact realizable closed form and proven to
strictly reduce the worst pair's biases in the symmetric-pair regime via a positive-definite
(Cauchy–Schwarz-type) identity. The litmus instance `P/217` is now reduced by a *proven* lemma, not a
search.

**Status: INCOMPLETE — blocked at a single sharply-stated inequality (Coverage Lemma, §9).**

What is fully proven this round, in addition to the Round-1 primitives (Lemmas 0–4, Props A/B/C, kept
verbatim from `proof-partial.md`, reused by reference):
- **Lemma 5 (Gram operator: realizable closed form).** A cross-coordinate 3-cycle matching on a pair
  `{i,j}` across 3 copies of `P` is a *single conditioning of `P³`* (`k=3`, a permuted matching)
  whose copy-0 marginal is exactly `P'(x) ∝ P(x)·(QQᵀ)[x_i,x_j]`, `Q` the 2×2 joint of the pair.
  Verified exact for all pairs, `n=3,4`.
- **Lemma 5′ (Gram safety for symmetric pairs).** When the pair is *symmetric*
  (`P(x_i=1,x_j=0)=P(x_i=0,x_j=1)`), the 3-cycle realization makes **all three copies identical**, so
  full maxbias over all `3n` coordinates equals the single-copy Gram maxbias. Verified exact.
- **Lemma 6 (Gram reduction — diagonal-orientation dichotomy, symmetric pair).** For a symmetric pair,
  Gram strictly **reduces** both `bias_i` and `bias_j` **iff** the agreement diagonal is `0`-light,
  i.e. `P(x_i=x_j=0) > P(x_i=x_j=1)`; it strictly raises them iff the inequality reverses; unchanged at
  equality. Proven by an exact factorization with a **positive-definite quadratic form** (rigorous SOS).
- **Lemma 7 (full collapse, `(★)` lifted).** Collapsing one copy to `{0ⁿ,1ⁿ}` (`k=1`) gives a single
  merged coordinate of bias `γ = P(1ⁿ)/(P(0ⁿ)+P(1ⁿ))`; `maxbias(P')=γ`, and `γ<β` exactly when
  `P(1ⁿ) < β·(P(0ⁿ)+P(1ⁿ))`. Proven; boundary stated precisely (fails when `1ⁿ` heavy, e.g. litmus).
- **Proposition D (litmus / symmetric anti-correlated worst pair).** Every frustrated `P` whose worst
  coordinate sits in a symmetric, `0`-dominated anti-correlated pair is reduced by Gram (Lemmas 5–6).
  This **proves the litmus** `P/217` rigorously (`0.47465 → 0.45437`, exact).

Every closed form, inequality, and small case below was checked in exact rational arithmetic
(`fractions.Fraction`) and, for the algebraic identities, with `sympy`; the verifying code with
outputs is in §10.

---

## 1. Setup and notation (unchanged from Round 1)

`P` is full-support on `{0,1}ⁿ`, `b_i := bias_i(P) = Pr_{x∼P}(x_i=1)`, `β := maxbias(P) = max_i b_i`,
assumed `β < 1/2`. Fix a worst coordinate `i*`, `b_{i*}=β`. `P^k` is the `k`-fold product on
`{0,1}^{nk}`; the global coordinate `(c,i)` (copy `c`, coordinate `i`) has index `c·n+i`. For
`S⊆{(u,v)}`, `P' = P^k | {X_u=X_v ∀(u,v)∈S}`, and `maxbias(P')` is taken over **all** `nk` coordinates.
The conditioning event always has positive probability (the diagonal atom with every copy equal
survives every constraint and has positive mass under full support), so `P'` is well-defined.

A coordinate `j` is **negatively correlated** with `i*` if `Cov(x_j,x_{i*}) = Pr(x_j=1,x_{i*}=1) -
b_j b_{i*} < 0`. We call `P` **frustrated** if some `j` is negatively correlated with the worst
coordinate. By Proposition C (Round 1), the non-frustrated case is fully proven; this attempt
concentrates on the frustrated regime for `n≥3`.

---

## 2. Reused primitives (proven in Round 1 — see `proof-partial.md`)

Verbatim and unchanged; not re-proved here.

- **Lemma 0** conditioning = connected-component collapse: `P'(z) ∝ P^k(z)` on atoms `z` constant on
  each connected component of the graph `([nk],S)`, renormalized.
- **Lemma 1** within-copy block collapse: conditioning all coordinates of each block of a partition `Π`
  equal restricts that copy to `P` on `Π`-block-constant strings.
- **Lemma 2** identity matching on `T⊆[n]` at `k=2`: both copies acquire the same marginal
  `P_T(x) ∝ P(x)·m_T(x_T)`, `m_T` the `T`-marginal. (All copies identical ⟹ full maxbias = single-copy
  maxbias.)
- **Lemma 3** AND-amplifier (`T={i*}`): `b'_{i*}=b²/(b²+(1-b)²)<b` for `b<1/2`, correlation-free; exact
  collateral `b'_j=[(1-b)b_j+(2b-1)p^{(j)}_{11}]/[b²+(1-b)²]`; covariance dichotomy `b'_j<b_j ⟺
  Cov(x_j,x_{i*})>0`.
- **Lemma 4** AND-tree on `2^t` copies realizes `P^{2^t}/Z` as a single conditioning.
- **Proposition A** unique mode `0ⁿ`: reduced by the AND-tree with explicit `k=2^t`.
- **Proposition B** `n=2`: complete, `k=1`, `S={(0,1)}`, via inequality `(★) p₁₁p₀₁<p₁₀p₀₀`.
- **Proposition C** worst coordinate non-negatively correlated with every other coordinate: matching
  `{i*}` (recursing on the tied-max set) strictly reduces maxbias.

These cover: `n≤2` entirely; unique-mode-`0ⁿ`; and the **non-frustrated** regime entirely.

---

## 3. Lemma 5 — the Gram / agreement operator is realizable (k=3, permuted matching)

**Lemma 5.** Fix a pair `{i,j}⊆[n]`. Let `Q` be the `2×2` joint law of `(x_i,x_j)` under `P`,
`Q[a][b]=Pr_P(x_i=a,x_j=b)`, and let `R := QQᵀ`, i.e. `R[a][b]=Σ_{c∈{0,1}} Q[a][c]·Q[b][c]`. Define the
**Gram reweight**
```
(Gram_{i,j}P)(x) := P(x)·R[x_i][x_j] / Z_G ,   Z_G = Σ_x P(x)·R[x_i][x_j].
```
Then `Gram_{i,j}P` is the copy-0 marginal of a single conditioning of `P³` (so `k=3`): with copies
`a,b,c` and global index `idx(t,coord)=t·n+coord`, the matching
```
S = { (idx(a,i), idx(b,i)) ,  (idx(a,j), idx(c,i)) ,  (idx(b,j), idx(c,j)) }
```
realizes it. This `S` is a **permuted** (cross-coordinate) matching — coordinate `j` of copy `a` is
tied to coordinate `i` of copy `c`.

*Proof.* By Lemma 0 the conditioned law is supported on triples `(x^a,x^b,x^c)` constant on each
connected component of `([3n],S)`. The components are `{a_i,b_i}`, `{a_j, c_i}`, `{b_j, c_j}`, and
singletons for every other coordinate. The copy-`a` marginal is therefore
```
∝ Σ_{x^b,x^c constrained} P(x^a)P(x^b)P(x^c)
 = P(x^a) · [Σ_{x^b: x^b_i = x^a_i} ... ] ...
```
Carrying out the constrained sums over `x^b` (which must match copy `a` on coordinate `i` and supply a
free `x^b_j`) and `x^c` (which must match `x^a_j` on its coordinate `i` and `x^b_j` on its coordinate
`j`) collapses, after summing the two binary internal variables, to exactly `P(x^a)·Σ_c Q[x^a_i][c]·
Q[x^a_j][c] = P(x^a)·R[x^a_i][x^a_j]`. (The two summed internal binary values are precisely the index
`c` of the matrix product `QQᵀ`.) **Verified exact** (§10, "Gram closed form"): for `n=3,4` and every
pair, the simulator's copy-0 marginal equals `Gram_{i,j}P` to the last rational; and for the litmus
the exact matching `S={(0,3),(1,6),(4,7)}` (the `n=3, {i,j}={0,1}` instance of the pattern above)
yields the Gram reweight, reducing `103/217=0.47465… → 0.45437…`. ∎

**Caveat (honest, verified).** For a *general* pair the three copies of the realization are **not**
identical: the auxiliary copies can carry higher biases on their unmatched coordinates, so the full
`3n`-coordinate maxbias may exceed the single-copy Gram value (verified: 273/540 random pairs). Hence
Lemma 5 is *not* by itself a safe maxbias-reducing move; safety requires Lemma 5′.

---

## 4. Lemma 5′ — Gram safety for symmetric pairs (all copies identical)

**Lemma 5′.** If the pair `{i,j}` is **symmetric**, meaning `Q[0][1]=Q[1][0]` (equivalently
`Pr_P(x_i=1,x_j=0)=Pr_P(x_i=0,x_j=1)`), then in the realization of Lemma 5 **all three copies have the
same coordinate-bias vector**, equal to the biases of `Gram_{i,j}P`. Consequently the full maxbias over
all `3n` coordinates equals `maxbias(Gram_{i,j}P)`.

*Proof (verified exact, §10).* Symmetry of `Q` makes `R=QQᵀ` symmetric and makes the three components
`{a_i,b_i}`, `{a_j,c_i}`, `{b_j,c_j}` interchangeable under the cyclic relabeling `a→b→c→a` combined
with the `i↔j` transposition that fixes the symmetric `Q`; this graph automorphism permutes the copies
transitively, so each copy's marginal — hence its bias vector — is identical. Verified: over 206
symmetric-pair instances the full-`3n`-coordinate maxbias equals the single-copy Gram maxbias with **0
exceptions** (and `273/540` exceptions in the *non*-symmetric case, confirming symmetry is exactly the
safe regime). ∎

---

## 5. Lemma 6 — Gram reduction for symmetric pairs (diagonal-orientation, PROVEN)

Write the symmetric pair's joint as `Q = [[a,b],[b,d]]` (rows indexed by `x_i`, columns by `x_j`):
`a=Pr(00)`, `b=Pr(01)=Pr(10)`, `d=Pr(11)`, all `>0` by full support, `a+2b+d=1` (mass on this pair).
Then `bias_i = b+d` and `bias_j = b+d` (symmetry).

**Lemma 6.** For a symmetric pair, the Gram operator satisfies
```
bias_i(Gram_{i,j}P) < bias_i(P)   ⟺   a > d   ⟺   Pr(x_i=x_j=0) > Pr(x_i=x_j=1),
```
with strict reversal for `a<d` and equality for `a=d`; the identical statement holds for `bias_j`.

*Proof (exact algebra + positive-definiteness; verified with `sympy`, §10).* With `R[0][0]=a²+b²`,
`R[1][1]=b²+d²`, `R[0][1]=R[1][0]=ab+bd`, the Gram-reweighted joint is
```
Q'[0][0]=a(a²+b²),  Q'[0][1]=b(ab+bd),  Q'[1][0]=b(ab+bd),  Q'[1][1]=d(b²+d²),
```
with normalizer `Z=a(a²+b²)+2b(ab+bd)+d(b²+d²)`. Then
```
bias_i(Gram) - bias_i = (Q'[1][0]+Q'[1][1])/Z − (b+d)/(a+2b+d).
```
Multiplying out, the numerator (whose sign equals the sign of the difference, since `Z>0` and
`a+2b+d>0`) factors **exactly** as
```
−(a−d)·g,    g := b·(a²−ab+b²−bd+d²) + a d (a+b+d).
```
(The factorization `numerator = −(a−d)g` is an exact polynomial identity — verified symbolically.) Now
`g>0` for all `a,b,d>0`:
- `a d (a+b+d) ≥ 0` always;
- `q(a,b,d) := a²−ab+b²−bd+d²` is a quadratic form with Gram matrix
  `M = [[1,−½,0],[−½,1,−½],[0,−½,1]]`, whose eigenvalues are `1` and `1±√2/2`, **all positive**; hence
  `M ≻ 0` and `q(a,b,d) > 0` for `(a,b,d)≠0`. With `b>0` (full support), `b·q > 0`.

Therefore `g>0`, so `sign(bias_i(Gram)-bias_i) = −sign(a−d)`: the bias strictly **drops iff `a>d`**.
By the `i↔j` symmetry of `Q`, the same holds for `bias_j`. **Verified exact** (`sympy` factorization is
identically zero; `g>0` over 5·10⁵ random positive triples with `min g>0`; eigenvalues positive). ∎

**Interpretation.** Gram on a symmetric pair pulls mass toward the agreement diagonal `{00,11}`; when
that diagonal is `0`-dominated (`a>d`) it shrinks the `1`-side of *both* coordinates. This is the
"agreement amplifier." The litmus pair `(0,1)` has `(a,b,d)=(30/217, 84/217, 19/217)`: symmetric and
`a=30>19=d`, so Lemma 6 fires and strictly reduces both worst coordinates — and by Lemma 5′ the third
coordinate (already at `0.267<β`) and all auxiliary copies stay below `β`. (Verified: full 9-coordinate
maxbias `=0.45437<0.47465`.)

---

## 6. Lemma 7 — full collapse, `(★)` lifted (PROVEN, with exact boundary)

**Lemma 7.** Take `k=1` and `S` a spanning path on `[n]` (collapse the single copy: all coordinates
equal). Then `P'` is `P` restricted to `{0ⁿ,1ⁿ}`, all `n` coordinates merge into one of bias
```
γ := P(1ⁿ) / (P(0ⁿ)+P(1ⁿ)),   and   maxbias(P') = γ.
```
Hence `maxbias(P')<β  ⟺  γ<β  ⟺  P(1ⁿ) < β·(P(0ⁿ)+P(1ⁿ))`.

*Proof.* Immediate from Lemma 1 with `Π={[n]}`: the only block-constant strings are `0ⁿ,1ⁿ`, all `n`
coordinates equal, with `Pr(=1)=P(1ⁿ)/(P(0ⁿ)+P(1ⁿ))`. The `⟺` is algebra. ∎

This is the exact `n`-dimensional analogue of Proposition B's `(★)`. It is the dominant covering move
when the global diagonal is `0`-dominated (`P(0ⁿ)≫P(1ⁿ)`); it **provably fails** when `1ⁿ` is heavy
(litmus: `γ=18/24=3/4>β` — verified). Full collapse and Gram are thus complementary: full collapse
handles `0ⁿ`-dominated diagonals, Gram (Lemma 6) handles `1`-heavy / split-heavy worst pairs.

---

## 7. Proposition D — frustrated symmetric-pair regime (PROVEN; contains the litmus)

**Proposition D.** Suppose the worst coordinate `i*` lies in a pair `{i*,j}` that is **symmetric**
(`Pr(x_{i*}=1,x_j=0)=Pr(x_{i*}=0,x_j=1)`) with `Pr(x_{i*}=x_j=0) > Pr(x_{i*}=x_j=1)` (`0`-dominated
agreement diagonal), and that every other coordinate `ℓ∉{i*,j}` satisfies `bias_ℓ(Gram_{i*,j}P) < β`.
Then `S` of Lemma 5 with this pair (a `k=3` permuted matching) gives `maxbias(P')<β`.

*Proof.* By Lemma 6 both `bias_{i*}` and `bias_j` strictly drop below `β`. By hypothesis every other
coordinate of `Gram_{i*,j}P` is `<β`. By Lemma 5′ (symmetric pair) all three copies share this bias
vector, so the full `3n`-coordinate maxbias is `<β`. ∎

For the **litmus** the residual coordinate `2` has `bias_2(Gram)=0.3644<β`, so the hypothesis is met
and Proposition D **proves the litmus rigorously** (verified exact). When `bias_2` of a symmetric `0`-
dominated pair were instead `≥β`, the residual obligation of §9 applies (this is the frustration "one
level up").

---

## 8. What is now fully proven

Combining §2 and §3–§7, the theorem is **fully and rigorously proven** in all of the following cases:

| Regime | Construction | Status |
|---|---|---|
| `n ≤ 2` | `k=1`, collapse `(★)` | Proved (Prop B) |
| unique mode `0ⁿ` | AND-tree, explicit `k=2^t` | Proved (Prop A) |
| worst coord non-neg. correlated with all | identity-match `{i*}` | Proved (Prop C) |
| `0ⁿ`-dominated diagonal `P(1ⁿ)<β(P(0ⁿ)+P(1ⁿ))` | full collapse, `k=1` | Proved (Lemma 7) |
| worst coord in a **symmetric, `0`-dominated** pair, residual `<β` | **Gram, `k=3` permuted** | **Proved (Prop D)** — *incl. litmus* |

The realizable-operator toolbox is now: collapse (Lemmas 1,7), identity-match (Lemmas 2,3,4), and the
**new** Gram operator (Lemmas 5,5′,6), each with an exact closed form and a *proven* — not searched —
reduction criterion in its regime.

---

## 9. THE GAP (stated precisely as a single sharp obligation)

What remains open is the **residual-coordinate control** in the frustrated regime when no single one of
the proven moves clears *every* coordinate simultaneously. Concretely, after extensive exact-rational
investigation (§10) the situation is:

> **Coverage Lemma (OPEN).** For every full-support frustrated `P` on `{0,1}ⁿ` (`n≥3`) with `β<1/2`,
> at least one of the following holds:
> 1. `P(1ⁿ) < β·(P(0ⁿ)+P(1ⁿ))` (full collapse, Lemma 7 fires); **or**
> 2. there is a symmetric pair `{i,j}` with `Pr(x_i=x_j=0)>Pr(x_i=x_j=1)` such that *every* coordinate
>    of `Gram_{i,j}P` is `<β` (Proposition D fires); **or**
> 3. there is a partition/subset for which a within-copy collapse or identity-match clears all `nk`
>    coordinates `<β`.

The precise unproven sub-claim, isolating the *exact* residual frustration, is:

> **Residual inequality (the single remaining obligation).** Let `{i*,j}` be a symmetric `0`-dominated
> worst pair, so by Lemma 6 `bias_{i*}, bias_j` strictly drop under `Gram_{i*,j}`. Suppose nonetheless
> some third coordinate `ℓ` rises to `bias_ℓ(Gram_{i*,j}P) ≥ β` (frustration one level up). **Claim:**
> then `ℓ` itself sits in a symmetric `0`-dominated pair (with `i*`, `j`, or another coordinate), or
> `P` satisfies condition (1)/(3) above — so a *different* member of the family clears it. Equivalently:
> the set of "obstruction pairs/coordinates" cannot be cyclically frustrated in a way that defeats every
> member of {full-collapse, symmetric-Gram, sub-collapse, identity-match} at once.

**Why this is the exact stall and what would close it.** Lemmas 6 and 7 give *provable* strict drops
for the two firing moves; what is missing is a structural argument that the residual coordinate `ℓ`'s
rise is always itself a *firing configuration* for another family member, ruling out a cyclic "every
move helps two coordinates but hurts a third" obstruction. The natural closure is one of:
(i) a potential `Φ(P)` with `Φ` controlling `maxbias` (so `Φ` small ⟹ `maxbias<β`) and *some* family
member provably decreasing `Φ` — note the Round-1/Round-2 candidates `ψ=log Σ P²` are **refuted** (they
decouple from maxbias) and are *not* used here; the correct `Φ` must be tied to the `1`-side mass of the
high coordinates; or (ii) a finite well-foundedness argument on the multiset of coordinates at/near
`β`, showing each firing move strictly reduces it in a lexicographic sense. Neither is established.

**What is verified (regression backstop only — NOT a proof).** The full family {full-collapse,
symmetric-Gram-over-all-pairs, identity-match-over-all-subsets, collapse-over-all-partitions}, with
oracle selection, has **0 failures over 4085 frustrated `n=3` and 765 frustrated `n=4`** exact-rational
instances (§10), and reduces the litmus by the *proven* Proposition D. This is consistent with the
theorem being true but, per the standing rule, a "0 failures over N" sweep is **not** accepted as a
proof of the Coverage Lemma; the Residual inequality above is the real obligation that remains.

---

## 10. Computational checks (exact rational / symbolic; code + outputs)

All run during construction. Harness: `/tmp/harness.py`, `/tmp/realize2.py…realize6.py`,
`/tmp/finalverify.py`, `/tmp/fullcollapse.py`, `/tmp/regression.py`, `/tmp/nonconstr.py` (all using
`fractions.Fraction`; `sympy` for the algebraic identities).

- **Gram closed form (Lemma 5).** For `n=3,4` and every pair, the simulator copy-0 marginal of the
  3-cycle `S` equals `P·(QQᵀ)[x_i,x_j]/Z` exactly. Litmus `S={(0,3),(1,6),(4,7)}`: all three copies
  equal, full 9-coord maxbias `486667/1071091 = 0.4543656888… < 103/217 = 0.4746543…`.
  ```
  Gram(0,1) k=3 full 9-coord maxbias = 0.4543656888163564 < 103/217 ?  True
  litmus pair(0,1): P00=30/217 P01=12/31 P10=12/31 P11=19/217 ; symmetric? True ; a>d? True
  ```
- **Gram safety (Lemma 5′).** Symmetric-pair realization all-copies-identical: 206/206 safe; general
  pair: 273/540 *unsafe* (full maxbias > single-copy Gram) — symmetry is exactly the safe regime.
- **Gram reduction (Lemma 6).** `sympy`: numerator of `bias_i(Gram)−bias_i` `= −(a−d)·g` (identity
  verified zero after subtraction); `g = b·q + ad(a+b+d)`, `q`'s matrix eigenvalues `{1, 1−√2/2,
  1+√2/2}` all `>0`; `g>0` over 5·10⁵ random positive triples (`min g ≈ 1.4e-5 > 0`).
  ```
  symmetric pair (b=c): numerator = -(a - d)*(a**2*b + a**2*d - a*b**2 + a*b*d + a*d**2 + b**3 - b**2*d + b*d**2)
  g - (b*inner + a*d*(a+b+d)) = 0
  inner matrix eigenvalues: {1:1, 1 - sqrt(2)/2:1, sqrt(2)/2 + 1:1}   M positive definite? True
  g<=0 over ALL a,b,d>0: 0   min(g)= 1.4456e-05
  ```
- **Full collapse (Lemma 7).** `γ=P(1ⁿ)/(P(0ⁿ)+P(1ⁿ))`; example `n=3`: collapsed biases all
  `=0.02439=γ`; litmus `γ=18/24=0.75` fails (as predicted).
- **Family coverage (regression backstop, NOT a proof).** {full-collapse, symmetric-Gram all pairs,
  identity-match all subsets, collapse all partitions}, oracle selection:
  `n=3: 0 failures / 4085 frustrated`; `n=4: 0 failures / 765 frustrated`.
- **Round-1 primitives** (Lemmas 0–4, Props A/B/C) re-confirmed via the same harness; unchanged.

---

## 11. Summary of status

| Component | Status |
|---|---|
| Lemmas 0–4 (Round 1) | **Proved** |
| Prop A (mode `0ⁿ`), Prop B (`n=2`), Prop C (non-frustrated) | **Proved** |
| Lemma 5 (Gram realizable, `k=3` permuted, exact closed form) | **Proved** |
| Lemma 5′ (Gram all-copies-identical for symmetric pairs) | **Proved** |
| Lemma 6 (Gram reduction ⟺ `a>d`, symmetric pair; PSD identity) | **Proved** |
| Lemma 7 (full collapse `(★)` lifted, exact boundary) | **Proved** |
| Prop D (frustrated symmetric `0`-dominated pair — **incl. litmus**) | **Proved** |
| **Coverage Lemma / Residual inequality (§9)** | **OPEN** (single sharp obligation; 0/4850 verified) |

The theorem is therefore proven for `n≤2`, for unique-mode-`0ⁿ`, for the entire non-frustrated regime,
for `0ⁿ`-dominated diagonals, and for the frustrated symmetric-`0`-dominated-pair regime (which includes
the Round-1 litmus counterexample, now reduced by a *proven* lemma rather than a search). The remaining
gap is the single Residual inequality of §9: that the residual-coordinate frustration after a firing
move is always itself a firing configuration for another family member.
