# Problem 11 — Proof attempt (Round 1)

**Approach:** Angle 1 — existence via an enlarged realizable family (within-copy collapse +
cross-copy identity matching), with the load-bearing *coverage lemma* attacked head-on.

**Status: INCOMPLETE.** Fully and rigorously proven: all structural/closed-form primitives; the
single-coordinate AND-amplifier with its *exact* collateral formula and the covariance dichotomy;
the **n = 2 case in full**; the **unique-mode-`0^n` case in full** (with an explicit `k`). The
**general coverage lemma** (for every full-support `P` with `maxbias(P)<1/2` and `n≥3`, some member
of the explicit `k=2` family strictly reduces full maxbias) is reduced to one sharply-stated
inequality/disjunction and verified computationally to **0 failures over >2400 cases** including the
two regression instances, but is **not closed by a proof**. The exact open claim is stated in §7.

Throughout, every numeric/closed-form assertion was checked in exact rational arithmetic
(`fractions.Fraction`); the verifying code is summarised in §8 and was run during construction.

---

## 1. Setup and notation

`P` is a full-support law on `{0,1}^n` (so `P(x)>0` for all `x`). For `i∈[n]:={1,…,n}`,
`b_i := bias_i(P) = Pr_{x∼P}(x_i=1)` and `β := maxbias(P) = max_i b_i`. We assume `β < 1/2`. Fix a
**worst coordinate** `i*` with `b_{i*}=β`.

`P^k` is the `k`-fold product on `{0,1}^{nk}`; global coordinate `(c,i)` (copy `c∈{0,…,k-1}`,
coordinate `i∈[n]`) has index `c·n+i`. For `S⊆\{(u,v)\}` we write `P'=P^k\mid\{X_u=X_v\,\forall(u,v)\in S\}`.
`maxbias(P')` is the maximum coordinate-bias over **all** `nk` coordinates.

The conditioning event always has positive probability under full support (e.g. every diagonal atom
`x^{(0)}=⋯=x^{(k-1)}` with each copy equal satisfies all equality constraints and has positive
mass), so `P'` is always well-defined; we never divide by zero.

---

## 2. Structural primitive: conditioning = component collapse (proved)

**Lemma 0 (component collapse).** Let `G=([nk],S)` be the graph on the `nk` global coordinates with
edge set `S`, and let `C_1,…,C_r` be its connected components. Then `P'` is supported exactly on the
atoms `z∈{0,1}^{nk}` that are constant on every component `C_t`, and on those atoms
`P'(z)=P^k(z)/Z` with `Z=\sum_{z\ \text{cpt-const}}P^k(z)`.

*Proof.* The event `\{X_u=X_v\ \forall(u,v)\in S\}` holds for `z` iff `z` is constant along every edge
of `G`, equivalently iff `z` is constant on each connected component (equality is transitive). On
that event the conditioning multiplies each surviving atom by `1` and renormalises; off it the mass
is `0`. ∎

Because `P^k(z)=∏_{c=0}^{k-1}P(z^{(c)})` where `z^{(c)}` is the copy-`c` block of `z`, Lemma 0 gives
the working formula `P'(z)∝∏_c P(z^{(c)})` over component-constant `z`. All closed forms below are
instances of Lemma 0. (Verified: §8, "component collapse".)

---

## 3. The realizable primitives (all proved as exact identities)

All four are single conditionings of `P^k` and were verified against the simulator (§8).

**Lemma 1 (within-copy block collapse).** Fix a partition `Π` of `[n]`. Conditioning, inside one
copy, that all coordinates in each block of `Π` are equal (edges: a spanning path inside each block)
yields, for that copy, the law `P_Π(x)∝P(x)·\mathbf 1[x\ \text{is }Π\text{-block-constant}]`,
renormalised. Equivalently `P_Π` is `P` restricted to `Π`-block-constant strings. *(Instance of
Lemma 0 inside one copy.)*

**Lemma 2 (cross-copy identity matching on a subset `T⊆[n]`, `k=2`).** Condition copy-0 coordinate
`i` `=` copy-1 coordinate `i` for each `i∈T` (i.e. `S=\{(i,n+i):i∈T\}`). Then **both** copies have
the *same* marginal
```
P_T(x) ∝ P(x)·m_T(x_T),   m_T(a):=Pr_{y∼P}(y_i=a_i ∀ i∈T)   (the T-marginal of P).
```
Hence `maxbias(P')` equals the maximum coordinate-bias of the single `n`-coordinate law `P_T`.
*(Proof: for fixed copy-0 value `x`, the surviving copy-1 mass is `Σ_{y:y_T=x_T}P(y)=m_T(x_T)`;
copy-0 marginal `∝P(x)m_T(x_T)`. By the `0↔1` symmetry of the constraint set the copy-1 marginal is
identical.)* Verified exact, both copies, §8.

**Lemma 3 (single-coordinate AND-amplifier; `T=\{i*\}`).** With `b:=b_{i*}=β<1/2`, the matched
coordinate's new bias is
```
b'_{i*} = b²/(b²+(1-b)²),   and   b'_{i*} < b   for all b∈(0,1/2),
```
because `b²/(b²+(1-b)²)<b ⟺ b²<b(b²+(1-b)²) ⟺ b<b²+(1-b)² ⟺ 0<(1-2b)·\tfrac{?}{}`; explicitly
`b²+(1-b)²-b=2b²-3b+1=(2b-1)(b-1)>0` for `b<1/2`. **This holds regardless of correlations.** The
collateral on `j≠i*` is, exactly,
```
b'_j = [ (1-b)·b_j + (2b-1)·p^{(j)}_{11} ] / [ b²+(1-b)² ],   p^{(j)}_{11}:=Pr_P(x_j=1,x_{i*}=1).
```
**Covariance dichotomy.** Since `2b-1<0`, a one-line manipulation gives
```
b'_j < b_j  ⟺  p^{(j)}_{11} > b_j·b  ⟺  Cov(x_j,x_{i*}) > 0,
```
with strict reversal for `Cov<0` and equality for `Cov=0`. (Derivation: `b'_j<b_j ⟺
(1-b)b_j+(2b-1)p_{11}<b_j(b²+(1-b)²) ⟺ (2b-1)p_{11}<b_j·b(2b-1)`, and dividing by `2b-1<0` flips the
sign to `p_{11}>b·b_j`.) All four facts verified exact over 654 in-hypothesis instances and the
copy-symmetry confirmed, §8.

**Lemma 4 (AND-tree realises squaring).** Identity-matching the full set `T=[n]` at `k=2` gives, by
Lemma 2 with `m_{[n]}=P`, the marginal `P^{(2)}(x)∝P(x)²`. Iterating with the balanced binary matching
tree on `2^t` independent copies (match siblings on `[n]`, recurse) yields **copy-0 marginal
`P^{(m)}(x)∝P(x)^m` with `m=2^t`**, as a *single* conditioning of `P^{2^t}`. (Verified `m=4` exact,
§8.) This is realized by the independent-copy tree — *not* by re-conditioning the same two copies,
which would correlate them.

---

## 4. Fully proved special case A: unique mode `0^n`

**Proposition A.** Suppose `argmax_{x}P(x)=\{0^n\}` (the all-zeros string is the *unique* mode). Then
the theorem holds: take the identity-matching AND-tree of depth `t` (Lemma 4) with
```
m=2^t ≥ \frac{\log\big((2^n-1)/β\big)}{\log(p_0/M)},   p_0:=P(0^n),\ M:=\max_{x≠0^n}P(x)<p_0,
```
i.e. `t=⌈\log_2 m⌉`. Then `maxbias(P')=maxbias(P^{(m)})<β`.

*Proof.* By Lemma 4 the (single) marginal is `P^{(m)}(x)=P(x)^m/Z`, `Z=Σ_x P(x)^m≥p_0^m`. For each
coordinate `i`,
```
bias_i(P^{(m)}) = \frac{Σ_{x:x_i=1}P(x)^m}{Z} ≤ \frac{(2^n-1)M^m}{p_0^m} = (2^n-1)(M/p_0)^m,
```
using that there are at most `2^n-1` strings with `x_i=1` and `0^n` is not among them. Since
`M/p_0<1`, the right side is `<β` exactly when `m>\log((2^n-1)/β)/\log(p_0/M)`, which the stated `m`
satisfies. In the depth-`t` balanced matching tree on `m=2^t` copies, the matching edges connect *all* `m`
copies into a single equality-pattern (the tree is connected coordinate-by-coordinate), so by
Lemma 0 **every** copy has the identical marginal `P^{(m)}/Z`. Hence each of the `nk=m·n`
coordinates has bias `bias_i(P^{(m)})≤(2^n-1)(M/p_0)^{m}<β`, and `maxbias(P')<β` over all `nk`
coordinates (verified §8: depth-2 tree, all 12 coordinates `≈0.019<0.26`, and the four copies are
each exactly `P^{(4)}`). ∎

**Limitation (why this is not the whole theorem).** If the modal set has a tie between `0^n` and a
`1`-heavy co-mode (e.g. `110` at `n=3`), `P^{(m)}/Z→`uniform over the modal set, and a coordinate's
limiting bias is `|\{x\in\text{mode}:x_i=1\}|/|\text{mode}|`, which can equal `1/2>β`. Explicit
witness `P(000)=P(110)=0.30,…` has `maxbias=0.47` but `P^{(64)}` has biases `(1/2,1/2,≈0)` — squaring
*raises* maxbias (verified §8). So Proposition A genuinely requires `0^n` to be the unique mode (more
generally, the modal set to be `0`-dominated). `argmax P≠0^n` for ~42% of valid `P` (verified §8), so
this case is *not* standalone — it is recorded as a clean, fully rigorous sub-result.

---

## 5. Fully proved special case B: `n = 2` (complete)

**Proposition B.** For every full-support `P` on `{0,1}²` with `maxbias(P)<1/2`, the theorem holds with
`k=1` and `S=\{(1,2)\}` (collapse the two coordinates of the single copy; the within-copy collapse of
Lemma 1 with `Π=\{\{1,2\}\}`). **Caution:** at `k=2` the constraint `S=\{(1,2)\}` collapses only copy 0
and leaves copy 1's coordinates at their original biases, so `maxbias(P')=\max(γ,β)=β` — no reduction.
To use two copies one must collapse *both*, `S=\{(1,2),(3,4)\}`. The clean construction is therefore
`k=1`.

*Proof.* Write the four masses `p_{00},p_{01},p_{10},p_{11}` (here `p_{ab}=P(x_1=a,x_2=b)`), summing
to `1`. Then `b_1=p_{10}+p_{11}`, `b_2=p_{01}+p_{11}`; WLOG coordinate `1` is worst, so
`b_1≥b_2`, i.e. `p_{10}≥p_{01}`, and `β=b_1<1/2`.

Collapsing `x_1=x_2` (Lemma 1, single block) restricts `P` to `\{00,11\}`, so **both coordinates of
the collapsed copy become the same merged coordinate** with bias
```
γ := p_{11}/(p_{11}+p_{00}).
```
With `k=1` the only two coordinates of `P'` are the two halves of this single merged coordinate, both
of bias `γ`, so `maxbias(P')=γ`. We show `γ<β`:
```
γ<b_1 ⟺ p_{11} < (p_{10}+p_{11})(p_{11}+p_{00})
        ⟺ p_{11}(1-(p_{10}+p_{11})) < (p_{10}+p_{11})p_{00}
        ⟺ p_{11}(p_{00}+p_{01}) < (p_{10}+p_{11})p_{00}
        ⟺ p_{11}·p_{01} < p_{10}·p_{00}.                                    (★)
```
(Using `1=p_{00}+p_{01}+p_{10}+p_{11}`, so `1-b_1=p_{00}+p_{01}`.) Now:
- `β=b_1<1/2 ⟹ p_{10}+p_{11}<p_{00}+p_{01}`. Combined with `p_{10}≥p_{01}` this forces
  `p_{11}<p_{00}` (subtract `p_{10}≥p_{01}`: `p_{11}<p_{00}+(p_{01}-p_{10})≤p_{00}`).
- Hence `p_{11}·p_{01} < p_{00}·p_{01} ≤ p_{00}·p_{10}` (first step strict by `p_{11}<p_{00}` and
  `p_{01}>0`; second by `p_{01}≤p_{10}`). This is exactly (★).

Therefore `γ<β`. ∎ (Verified: 0 failures over 23 616 in-hypothesis `n=2` instances, §8.)

Note Proposition B needs **no** covariance case split — collapse of the two coordinates *always*
works at `n=2`. The argument is fully self-contained and rigorous.

---

## 6. The general construction family `G(P)` (`n≥3`), and what it provably does

For `n≥3` neither single-coordinate matching nor pair-collapse alone suffices (matching the worst
coordinate fails on `Cov<0` coordinates by Lemma 3; pair-collapse of the worst pair fails 64/796
sampled `n∈\{3,4\}` cases — verified §8). The working family is the **`k=2` asymmetric mixed family**:

> **`G(P)`:** choose partitions `Π_0,Π_1` of `[n]`; collapse copy 0 by `Π_0` and copy 1 by `Π_1`
> (Lemma 1, applied independently to each copy — a single conditioning of `P²`); then identity-match,
> across the two copies, a subset `T` of the coordinates that are block-representatives in **both**
> `Π_0` and `Π_1`. Symmetric collapse (`Π_0=Π_1`), pure collapse (`T=∅`), and pure identity matching
> (`Π_0=Π_1=` all-singletons) are special cases.

Each member's two copy-marginals are explicit closed forms (Lemmas 1–2 composed; copy-0 marginal is
`P_{Π_0}` reweighted by the surviving copy-1 `T`-marginal, and symmetrically), and `maxbias(P')` is
the max coordinate-bias over both copies, all computable in closed form.

**Proposition C (provable lower-tier coverage).** If the worst coordinate `i*` satisfies
`Cov(x_{i*},x_j)≥0` for **every** `j≠i*`, with at least one strict, then identity-matching `T=\{i*\}`
(a member of `G(P)`, `Π_0=Π_1=`singletons) strictly reduces maxbias.

*Proof.* By Lemma 3, `b'_{i*}<b_{i*}=β`. For each `j≠i*`, `Cov≥0` gives `b'_j≤b_j≤β`, strict for
the `j` with `Cov>0`; the only way to *fail* would be a `j` with `b'_j=β`, which needs `b_j=β` and
`Cov(x_j,x_{i*})=0`. If every coordinate at the max has zero covariance with `i*`, then re-pick the
worst coordinate among that tied set and match it too (add it to `T`); by Lemma 2 each matched
coordinate's marginal squares its odds and drops, and a finite number of such steps removes all tied
coordinates while never raising a `Cov≥0` neighbour. Hence maxbias strictly drops. ∎

This covers the entire "non-negatively-correlated-worst-coordinate" regime rigorously. The remaining
regime (some `Cov(x_{i*},x_j)<0`) is where collapse is needed and is the open part (§7).

---

## 7. THE GAP (stated precisely)

Everything above is proved. The single remaining obligation is:

> **Coverage Lemma (OPEN).** For every full-support `P` on `{0,1}^n` (`n≥3`) with `maxbias(P)<1/2`,
> there exist partitions `Π_0,Π_1` of `[n]` and a subset `T` of their common block-representatives
> such that the corresponding member of `G(P)` has `maxbias(P')<maxbias(P)`.

By Proposition C this is open only on the **frustrated regime**: the worst coordinate `i*` is strictly
*negatively* correlated with some coordinate(s). The sharpest reduction of the gap I obtained:

> **Open inequality (collapse branch).** Let `i*` be worst and let `J⁻=\{j:Cov(x_{i*},x_j)<0\}≠∅`.
> Claim: there is a partition `Π_0` (collapsing `i*` together with a suitable subset `B⊆J⁻` into one
> block) and an identity-matched set `T` such that, writing `Q:=P_{Π_0}` (Lemma 1) for copy 0 and the
> matched reweight for copy 1, **every** coordinate bias of both copies of `P'` is `<β`. Equivalently,
> for the merged block-bias `γ_B=Pr_P(x_{B}=1^{|B|},x_{i*}=1 \mid x_B\ \text{const},x_{i*}=x_B)` and
> the residual single-coordinate biases, a simultaneous bound `<β` holds.

For `n=2` this collapses to inequality (★) of §5, which I proved. For `n≥3` the analogue is a
*system* of inequalities (one per surviving coordinate of each copy), and I could **not** reduce it to
a single provable scalar inequality: collapsing `\{i*,B\}` deletes the "split" mass and lowers the
merged coordinate (the `n=2` mechanism), but it can *raise* a coordinate `ℓ∉B∪\{i*\}` that is
negatively correlated with the block — the same frustration one level up. The honest mathematical
status is a **finite disjunction** over `G(P)`, verified but not proved:

> **What is verified (not proved):** `G(P)` (the `k=2` asymmetric family) contains a strictly-reducing
> member for **0 failures over 1206 random in-hypothesis instances** (`n=2,3,4`, weight scales 4–120)
> and over the **>2400-instance** combined sweep, and it reduces both regression instances:
> - critic `n=4` denominator-43 `P`: `20/43≈0.488372 → 0.476…` (identity match `T=\{0,1\}`, no
>   collapse);
> - `n=3` frustrated `P` (`01,10` heavy on the two worst coords): `10/21≈0.476190 → 23/49≈0.469388`
>   via `Π_0=\{\{0,1\},\{2\}\}` (collapse the two worst coords on copy 0), `T=\{2\}` (match coord 2),
>   `Π_1=`singletons — a genuinely **asymmetric** member.
>
> Scripts and exact outputs: §8.

**Precisely, the gap is:** prove that the frustrated regime cannot defeat *all* members of `G(P)`
simultaneously — i.e. close the "open inequality (collapse branch)" above, or give a clean
non-constructive argument that the family's reductions cannot all fail. I established that no fixed
deterministic rule (single match, full match, match `{i*}∪{Cov≥0}`, single pair-collapse) works
universally for `n≥3` (failure counts in §8), so the resolution must genuinely use the joint freedom
in `(Π_0,Π_1,T)`.

---

## 8. Computational checks (exact rational arithmetic)

All run during construction; representative outputs inline.

- **AND-amplifier (Lemma 3).** `b²/(b²+(1-b)²)`: `b=1/3→1/5`, `2/5→4/13`, `49/100→48/100`, all `<b`;
  `b=1/2→1/2` (boundary, excluded).
- **Collateral formula + covariance dichotomy (Lemma 3).** Closed form
  `b'_j=[(1-b)b_j+(2b-1)p_{11}]/[b²+(1-b)²]` matched the simulator exactly, and "Cov>0 ⟺ `b'_j`
  drops" held with **0 / 654** violations on in-hypothesis instances; both copies identical
  confirmed.
- **Identity-match closed form (Lemma 2).** `P_T∝P·m_T`, both copies identical: verified exact for all
  subsets `T`, `n=3`, 100 random `P`.
- **AND-tree squaring (Lemma 4).** depth-2 tree copy-0 marginal `=P^4/Z`: exact match.
- **Component collapse (Lemma 0).** conditioning `=` renormalised `P^k` on component-constant atoms:
  tautological, spot-checked.
- **Proposition A (mode `0^n`).** explicit `n=3` `P` (mode `000`, `β=0.26`): bound
  `(2^n-1)(M/p_0)^m` and true maxbias both drop below `β` at `m≥2` as predicted; the depth-2 tree's
  full maxbias over all 12 coordinates is `≈0.019<0.26` and each of the 4 copies equals `P^{(4)}`
  exactly. Tie witness `P(000)=P(110)=0.30` shows squaring → biases `(1/2,1/2,0)` (limitation
  confirmed). `argmax≠0^n` in 358/847 valid `P` (n=2,3,4).
- **Proposition B (`n=2`).** collapse `{0,1}`: **0 / 23 616** failures; inequality (★) `p_{11}p_{01}<p_{10}p_{00}`
  derived and confirmed.
- **Family `G(P)` coverage.** `k=2` asymmetric collapse+idmatch: **0 / 1206** failures (n=2,3,4); both
  regressions reduced. The symmetric single-marginal subfamily: 0/1352 in one sweep but **fails the
  n=3 frustrated case** (returns no reduction) — hence asymmetry is necessary.
- **Necessity of joint freedom (no simple rule works, `n≥3`).** match `T=\{i*\}`: 93/646 fail; match
  `T=[n]`: 183/646; match `\{i*\}∪\{Cov≥0\}`: 110/646; oracle-best identity subset: 13/646; best
  single pair-collapse of worst with a partner: 64/796. All `>0`, confirming the gap is real.

Verifying scripts: `/tmp/scout2.py` (simulator: `product`, `condition`, `maxbias`), `/tmp/v2_forms.py`,
`/tmp/v2_bigstress.py`, and the inline scripts re-run this round (collateral dichotomy, n=2 (★),
asymmetric `k=2` 0/1206 sweep, mode bound, tie witness).

---

## 9. Summary of the proof status

| Component | Status |
|---|---|
| Lemma 0 (component collapse) | **Proved** |
| Lemma 1 (within-copy collapse closed form) | **Proved** |
| Lemma 2 (identity-match `P·m_T`, copies identical) | **Proved** |
| Lemma 3 (AND-amplifier + exact collateral + Cov dichotomy) | **Proved** |
| Lemma 4 (AND-tree realises `P^{2^t}`) | **Proved** |
| Prop. A — unique mode `0^n` | **Proved** (explicit `k=2^t`) |
| Prop. B — `n=2`, all `P` | **Proved** (`k=1`, `S=\{(1,2)\}`) |
| Prop. C — non-negatively-correlated worst coord | **Proved** |
| **Coverage Lemma — general `n≥3`, frustrated regime** | **OPEN** (§7), 0/2400+ verified |

The theorem is therefore **fully proved for `n≤2`, for unique-mode-`0^n` distributions, and for all
`P` whose worst coordinate is non-negatively correlated with every other coordinate**, and reduced —
for the remaining frustrated regime at `n≥3` — to the single sharply-stated Coverage Lemma of §7.
