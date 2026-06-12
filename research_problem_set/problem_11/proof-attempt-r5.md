# Problem 11 — Proof attempt (Round 5)

**Approach:** Angle 2 — non-constructive existence on the bounded symmetric residual. The proven
engines (full-collapse, identity-match, symmetric-Gram) confine every frustrated `n≥3` instance to
a structurally characterized residual; on that residual we attempt a *counting incompatibility on the
stall set* (if no family member reduces full maxbias then `β≥1/2`, contradicting the hypothesis).

**Status: INCOMPLETE — blocked at the third-coordinate bridge (the stall-set counting closure).**
What is *newly and fully proven this round* is the necessary half of the incompatibility, in a clean
closed form that strictly strengthens the critic's "all-1-dominated stall is empty" requirement:

- **Lemma 8 (NEW, fully proven, one line).** Under `β<1/2`, **every** pair `{i,j}` (symmetric or not)
  satisfies `Pr(x_i=0,x_j=0) > Pr(x_i=1,x_j=1)`, i.e. the agreement-diagonal potential
  `Φ_{ij} := Pr(x_i=x_j=0) − Pr(x_i=x_j=1) > 0` on every pair. This is *not* an empirical fact and
  needs no sweep: it is the exact identity `Pr(11)−Pr(00)=b_i+b_j−1` together with `b_i,b_j<1/2`.
  Consequently the "all symmetric pairs 1-dominated" stall premise is **logically impossible**, not
  merely empty; and for *every* symmetric pair Lemma 6's firing condition `a>d` holds automatically.

This discharges the legitimate, mechanism-backed core the critic isolated (the marginal counting
inequality). What it does **not** discharge is the SUFFICIENT half — the third-coordinate bridge —
which remains the genuine open core after four rounds. §10 states that gap with surgical precision,
records the new structural evidence about it, and explicitly discharges the three named litmus
witnesses (A/B/C). §9 of the round-2 attempt is hereby corrected per the critic (the "Residual
inequality" was mislabeled as the single obligation; the real obligation is the stall-set bridge,
and Lemma 8 removes the all-1-dominated half of it).

All closed forms, inequalities, and small cases below were checked in exact rational arithmetic
(`fractions.Fraction`) and, for algebraic identities, with `sympy`; code + outputs in §11.

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

For a pair `{i,j}` write its `2×2` joint `Q[a][b]=Pr(x_i=a,x_j=b)` (within-pair mass `=1`). The pair
is **symmetric** if `Q[0][1]=Q[1][0]`. The pair is **0-dominated** if `Q[0][0]>Q[1][1]`
(equivalently `Φ_{ij}>0`).

---

## 2. Reused primitives (proven & independently verified in Rounds 1–2 — treated as given)

Verbatim from `proof-partial.md` / `proof-attempt-r2.md`; **not** re-proved.

- **Lemma 0** conditioning = connected-component collapse: `P'(z) ∝ P^k(z)` on atoms constant on each
  connected component of `([nk],S)`, renormalized.
- **Lemma 1** within-copy block collapse.
- **Lemma 2** identity matching on `T⊆[n]` at `k=2`: both copies acquire `P_T(x) ∝ P(x)·m_T(x_T)`,
  `m_T` the `T`-marginal; **all copies identical**, so full `2n`-maxbias = single-copy maxbias.
- **Lemma 3** AND-amplifier (`T={i*}`): `b'_{i*}=β²/D<β` (`D:=β²+(1−β)²`), correlation-free; exact
  collateral `b'_j=[(1−β)b_j+(2β−1)p^{(j)}_{11}]/D` with `p^{(j)}_{11}=Pr(x_j=1,x_{i*}=1)`; covariance
  dichotomy `b'_j<b_j ⟺ Cov(x_j,x_{i*})>0`. (Collateral formula re-verified exact this round, §11.)
- **Lemma 4** AND-tree on `2^t` copies realizes `P^{2^t}/Z`.
- **Proposition A** unique mode `0ⁿ`: reduced by the AND-tree, explicit `k=2^t`.
- **Proposition B** `n=2`: complete, `k=1`, `S={(0,1)}`, via `(★) p₁₁p₀₁<p₁₀p₀₀`.
- **Proposition C** worst coord non-negatively correlated with all others: match `{i*}` (recursing on
  the tied-max set) reduces maxbias. (Covers the non-frustrated regime.)
- **Lemma 5 / 5′** Gram operator `Gram_{i,j}P(x) ∝ P(x)·R[x_i][x_j]`, `R=QQᵀ`, is realizable as a
  `k=3` permuted 3-cycle matching; for a **symmetric** pair all three copies are identical, so full
  `3n`-maxbias = single-copy Gram maxbias.
- **Lemma 6** symmetric pair `Q=[[a,b],[b,d]]`: `bias_i(Gram)<bias_i ⟺ a>d`, via the exact
  factorization `numerator = −(a−d)·g` with `g>0` (PSD quadratic form, eigenvalues `1,1±√2/2`).
- **Lemma 7** full collapse `k=1`: `maxbias(P')=γ:=P(1ⁿ)/(P(0ⁿ)+P(1ⁿ))`; reduces `⟺ γ<β`.
- **Proposition D** worst coord in a symmetric, 0-dominated pair with residual `<β` reduced by Gram
  (includes the round-1 litmus `P/217`).

These cover: `n≤2` entirely; unique-mode-`0ⁿ`; the non-frustrated regime; `0ⁿ`-dominated diagonals
(`γ<β`); and the symmetric-0-dominated-pair-with-low-residual regime.

---

## 3. Lemma 8 (NEW) — every pair is strictly 0-dominated under `β<1/2`

This is the round-5 result. It is short, exact, and replaces the critic's empirical "all-1-dominated
stall premise is empty (0/110k)" with a *logical impossibility* requiring no sweep.

**Lemma 8.** Let `P` be any distribution on `{0,1}ⁿ` with `b_i<1/2` for all `i` (in particular any `P`
with `maxbias(P)=β<1/2`). Then for **every** pair `{i,j}`,
```
Pr(x_i=1, x_j=1) − Pr(x_i=0, x_j=0) = b_i + b_j − 1 < 0,
```
i.e. `Pr(x_i=0,x_j=0) > Pr(x_i=1,x_j=1)`, equivalently the agreement-diagonal potential
`Φ_{ij} := Pr(x_i=x_j=0) − Pr(x_i=x_j=1) = (1 − b_i − b_j) > 0`.

*Proof.* Let the pair joint be `Q[a][b]=Pr(x_i=a,x_j=b)`, with `Q[0][0]+Q[0][1]+Q[1][0]+Q[1][1]=1`.
The marginals are `b_i = Q[1][0]+Q[1][1]` and `b_j = Q[0][1]+Q[1][1]`. Hence
```
b_i + b_j − 1 = (Q[1][0]+Q[1][1]) + (Q[0][1]+Q[1][1]) − (Q[0][0]+Q[0][1]+Q[1][0]+Q[1][1])
             = 2Q[1][1] + Q[0][1] + Q[1][0] − Q[0][0] − Q[0][1] − Q[1][0] − Q[1][1]
             = Q[1][1] − Q[0][0]
             = Pr(x_i=1,x_j=1) − Pr(x_i=0,x_j=0).
```
This is an exact identity (no full support needed). Since `b_i<1/2` and `b_j<1/2`, we have
`b_i+b_j<1`, so `Pr(11)−Pr(00) = b_i+b_j−1 < 0`, i.e. `Pr(00)>Pr(11)` and `Φ_{ij}=1−b_i−b_j>0`. ∎

*(Algebraic identity verified with `sympy`; the strict 0-domination of every pair verified exact on
20 000 frustrated `n=3` instances and on Litmus A/B/C — §11.)*

**Three consequences that reshape the residual:**

1. **(C1) The all-1-dominated stall premise is impossible, not merely empty.** Angle 2's hard step
   was scoped (in the survey, and re-affirmed by the critic) around the configuration "γ≥β AND every
   symmetric pair 1-dominated (`d≥a`)". Lemma 8 shows *every* pair — symmetric or not — has `a>d`
   strictly. So "some symmetric pair is 1-dominated" never occurs under `β<1/2`. The 0/110k the critic
   measured is a theorem: the set is empty by Lemma 8, with no recourse to the sweep.

2. **(C2) Lemma 6 always fires on any symmetric pair.** For a symmetric pair `Q=[[a,b],[b,d]]`,
   Lemma 8 gives `a>d`, which is *exactly* Lemma 6's firing condition. So on **every** symmetric pair
   the Gram operator strictly reduces both of that pair's biases. The pair-level reduction is never the
   obstruction; only the third coordinate (and the safety of the auxiliary copies for *non*-symmetric
   pairs) can be.

3. **(C3) Φ is a genuine maxbias-linked potential and is uniformly positive.** `Φ_{ij}=1−b_i−b_j`
   directly encodes both biases: `b_i,b_j<1/2 ⟺ Φ_{ij}>0` is not just a correlate of low maxbias, it
   is the marginal sum. This is the maxbias-IMPLYING potential the critic required (and it is none of
   the forbidden ψ=log ΣP² / sum-odds / Lᵖ-odds). It is the right object; the open problem is *moving*
   it on the third coordinate, not finding it.

---

## 4. The reduction family (vertex-transitive, all-copies-identical)

Per the standing rule we use only conditionings whose realization makes all `k` copies share the
same bias vector, so full `nk`-maxbias equals the single-copy maxbias of the operator (verified per
operator on `/tmp/scout2.py`). The named family `F`:

- **B1 (full-collapse, Lemma 7):** `k=1`, spanning path. Fires `⟺ γ<β`. NAMED, checkable.
- **B2 (identity-match on a subset `T⊆[n]`, Lemmas 2/3):** `k=2`, copies identical. Reweight
  `P·m_T/Z`. The collateral biases are the closed form of Lemma 3 (generalized to `T`). Special cases:
  `T={i*}` (AND-amplifier), `T=T₀` (tied-max set), `T={i,j}` (pair-match).
- **B3 (symmetric-Gram, Lemmas 5/5′/6):** `k=3` permuted 3-cycle on a **symmetric** pair `{i,j}`. By
  Lemma 8 (C2) it always reduces that pair's two biases. Safe (all copies identical) by Lemma 5′.
- **B4/B5 (permuted/cyclic matchings, `k≤3`):** `k=2` reverse-permutation `π=(n−1,…,0)` and `k=3`
  cyclic; both realizable closed forms, kept vertex-transitive.

By Lemma 0–2/5 each member's realization is a single conditioning of `P^k` with all copies identical
(verified). The closure question is whether *some* member of `F` reduces full maxbias.

---

## 5. Proven coverage outside the residual

Combining §2–§4, the theorem is **fully proven** in each regime below (unchanged from round 2 except
that C2 now makes the symmetric-pair branch unconditional at the pair level):

| Regime | Construction | Status |
|---|---|---|
| `n ≤ 2` | `k=1` collapse `(★)` | Proved (Prop B) |
| unique mode `0ⁿ` | AND-tree, explicit `k=2^t` | Proved (Prop A) |
| non-frustrated (`Cov(i*,·)≥0`) | identity-match `{i*}` | Proved (Prop C) |
| `γ<β` (`0ⁿ`-dominated diagonal) | full collapse `k=1` | Proved (Lemma 7) |
| `Cov(x_j,x_{i*})>0` for all `j` clears match-`{i*}` | AND-amplifier | Proved (Lemma 3) |
| symmetric pair `{i*,j}`, residual coords `<β` after Gram | Gram `k=3` permuted | Proved (Prop D; C2 makes firing unconditional) |

The **residual** to which the theorem is not yet reduced is exactly:

> **(R) The stall residual.** `P` is frustrated, `β<1/2`, `γ≥β` (B1 fails), and *no single named
> member of `F` drives all `n` single-copy biases below `β`* — because whenever a move reduces the
> targeted coordinate(s), a **third coordinate** rises to `≥β`.

By Lemma 8, on `(R)` every pair (symmetric or not) is 0-dominated; and by (C2) every symmetric pair
admits a strictly-pair-reducing Gram step. So `(R)` is *not* obstructed at the pair level. It is
obstructed solely by the third-coordinate rise. This is the load-bearing bridge, treated next.

---

## 6. The intended Angle-2 closure and where it stands

The non-constructive plan is: **assume `(R)` (the stall) and derive `β≥1/2`**, contradicting the
hypothesis, hence `(R)` is empty and some member of `F` reduces. Lemma 8 supplies the *necessary*
half of this contradiction cleanly:

> **Established (necessary half).** On the stall set, every pair satisfies `Φ_{ij}=1−b_i−b_j>0`
> (Lemma 8). Therefore the configuration the survey/critic feared — "`γ≥β` together with a
> 1-dominated symmetric pair" — cannot arise; the would-be contradiction class is empty by a closed
> identity, with no sweep. In particular there is **no** P with `β<1/2` on which the all-1-dominated
> mechanism would even need to be invoked.

What this does **not** yet give is the *sufficient* half:

> **Open (sufficient half = the bridge).** That the third coordinate's rise, after a pair-reducing
> move, is itself caught by another member of `F`. Concretely: `Φ_{ij}>0` (hence Lemma 6 reduces the
> pair `{i,j}`) does **not** by itself imply full maxbias drops, because Gram on `{i,j}` can push a
> third coordinate `ℓ` to `bias_ℓ≥β` (verified failures: seeds 8356, 9350 — §7), and there is no
> *named* (non-oracle) rule selecting which member of `F` catches `ℓ`.

So Angle 2 is advanced to: *the contradiction's premise-class is provably empty at the pairwise/
counting level (Lemma 8), but the descent from "every pair has Φ>0" to "full maxbias strictly drops"
is not closed.* The gap is stated exactly in §10.

---

## 7. The third-coordinate obstruction, examined exactly (honest, not waved at)

Per the constraint "do not stop at the all-1-dominated stall," here is the exact behaviour on the
hardest residual instances (full `n=3`, `β<1/2`, frustrated, `γ≥β`, match-`{i*}` and match-`T₀`
both fail). These are the cases where the bridge genuinely bites.

- **Seed 8356** (`β=23/48`, all biases tied at `β`). All three pairs symmetric and (by Lemma 8)
  0-dominated, so Lemma 6 reduces each targeted pair — yet **Gram on every pair fails on full maxbias**
  because the third coordinate rises: pair `(0,1)→0.5001`, `(0,2)→0.4810`, `(1,2)→0.4833`, all `≥β`.
  The instance is nonetheless cleared by the identity-match `B2` on `T={0,2}` → `0.4697<β`. *Verified
  exact (§11).* This is a clean witness that "`Φ>0` on a pair ⟹ full-maxbias reducer" is **false**.
- **Seed 9350** (`β=21/43`, tied). Same picture: Gram on all three pairs fails (third coord rises to
  `0.4966`, `0.4985`, `0.4995`); cleared by `B2` on `T={0,1}` → `0.4879<β`. *Verified exact.*
- **Seed 15246** (`β=11/24`): has a symmetric pair `(1,2)` that is 0-dominated; Gram on `(1,2)` gives
  full maxbias `0.4288<β` — here the bridge *succeeds* (third coordinate stays low). *Verified exact.*

**Structural evidence about the offender (recorded, NOT asserted as a theorem):** over the 20 000-seed
exact sweep, in the cases where match-`{i*}` fails, the rising offender `j` sits in a *symmetric* pair
with `i*` in **28/29** instances; the lone exception is the non-symmetric residual (Litmus-C type).
This is *empirical-with-exception* — exactly the F3 shape the critic forbade asserting as a closed
form. It is recorded as a conjecture (approach.md), not used in any proof step.

**What clears the residual empirically (the oracle, recorded as the gap, not as proof):** the union
`F = {B1, all subset-matches B2, symmetric-Gram B3, B4/B5}` has **0 stall over 20 000 frustrated
`n=3` seeds** (§11). But the *clearing* member is selected by an oracle: in the five named-family
stalls (seeds 8191, 8356, 9350, 12663, 16580) the clearing move is a **pair identity-match `T={i,j}`**,
and the winning pair is **not** characterized by any tested named criterion (it is *not* the
most-negative-covariance pair: seed 9350 clears on `(0,1)`, cov `−0.099`, while the most-negative pair
`(0,2)`, cov `−0.122`, *fails*; seed 8191 clears on `(0,2)`, cov `−0.064`, while `(1,2)`, cov `−0.109`,
fails). So the closure is a genuine un-routed oracle over `2ⁿ−1` subsets. **Per the standing rule this
is forbidden as a proof step**; it is the precise content of the open gap (§10).

---

## 8. The three named litmus witnesses, discharged explicitly

Per the critic's obligation, each litmus is discharged by a *named* operator with an exact verified
reduction (not by oracle search):

- **Litmus A** (seed 135209, `P·51`, all biases `8/17`, all three pairs symmetric & 0-dominated,
  `γ=1/2≥β`, tied-set match fails). Symmetric-tied residual. Cleared by the **`k=3` cyclic matching**
  `S={(0,3),(3,7),(1,5),(5,6),(2,4),(4,8)}`: full 9-coord maxbias `746/1987 ≈ 0.37544 < 8/17`.
  *Verified exact (§11).* (The `k=2` reverse-perm does **not** clear it — gives `0.4842`; the `k=3`
  cyclic is essential here.)
- **Litmus B** (seed 789, `P·59`, `β=28/59`, **no symmetric pair**, `γ=9/17>β`). Cleared by the
  identity-match `B2` on `T={1}`: full maxbias `789/1745 ≈ 0.45215 < 28/59`. *Verified exact.* (This
  is a non-symmetric residual cleared by a named single-coordinate match — Lemma 8 still gives every
  pair 0-dominated, but no Gram is available because no pair is symmetric.)
- **Litmus C** (seed 8191, `P·41`, `β=18/41`, **no symmetric pair**, `γ≥β`, tied-set match fails).
  The lone non-symmetric residual in the critic's 300k sweep. Cleared by the identity-match `B2` on
  `T={0,2}`: full maxbias `≈ 0.42495 < 18/41`. *Verified exact.* It is NOT covered by any closed-form
  F3 (F3 is false here, as the critic noted); it is discharged as a named instance.

All three confirm Lemma 8 (every pair 0-dominated). A and the round-1 litmus `P/217` are
symmetric-pair instances closed by proven lemmas (Prop D / k=3 cyclic); B and C are non-symmetric
instances closed by a named identity-match. **None of the three is in the open gap**; they are all
discharged here by named operators.

---

## 9. Correction of round-2 §9 framing (per the critic)

Round-2 §9 named a "Residual inequality" — "after Gram raises a third coordinate `ℓ`, `ℓ` itself sits
in a symmetric 0-dominated pair" — as *the single remaining obligation*. Two corrections:

1. The "0-dominated" qualifier is now **automatic** for every pair by Lemma 8; it is not a hypothesis
   to be discovered. So the round-2 statement collapses to "the risen `ℓ` sits in a *symmetric* pair
   that catches it." This is **empirical-with-exception (28/29)** — a false universal in general (the
   non-symmetric residual exists), so it cannot be the closed-form obligation, exactly the F3 trap.
2. The true obligation is the **stall-set counting closure / third-coordinate bridge** of §10: that the
   residual `(R)` is empty, via a descent that need not name which operator fires. The round-2 framing
   is hereby demoted to a refuted sub-claim.

---

## 10. THE GAP (stated precisely; what is proven, what is assumed, the minimal missing lemma)

**Proven this round (and reused):** all of §2 (round 1–2 primitives), §3 (Lemma 8 — every pair
strictly 0-dominated; the all-1-dominated stall is impossible), §4 (the realizable family `F`), §5
(coverage outside `(R)`), §8 (the three litmus witnesses, by named operators). In particular the
*necessary* half of the Angle-2 contradiction is closed in closed form (no sweep).

**Assumed nowhere.** No oracle, no F3, no uniform contraction bound, no 1-dominated premise is used in
any proof step above. The empirical sweeps in §7 are diagnostics labeled as such.

**The minimal missing lemma (the open core).**

> **Bridge Lemma (OPEN).** Let `P` be full-support, frustrated, `n≥3`, `β<1/2`, with `γ≥β` (so B1
> fails). Then `(R)` is empty: there exists a member of the named family `F = {B1, B2 (identity-match
> on some subset `T`), B3 (symmetric-Gram on some symmetric pair), B4/B5 (k≤3 permuted/cyclic
> matchings)}` whose single-copy (= full, by vertex-transitivity) maxbias is `< β`.

Equivalently, in the contrapositive Angle-2 form that would close it:

> **Stall-set incompatibility (OPEN).** If no member of `F` reduces full maxbias, then `β ≥ 1/2`.

**Why it is not closed, precisely.** Lemma 8 gives `Φ_{ij}=1−b_i−b_j>0` on *every* pair, and Lemma 6
turns this into a strict reduction of the *two* biases of any *symmetric* pair under Gram. The descent
that is missing is from the pairwise potential `Φ` to **full** maxbias: a single Gram (or match) step
reduces its targeted coordinate(s) but can raise a third coordinate `ℓ` to `≥β` (seeds 8356, 9350,
§7). To close the bridge one needs **one** of:

- **(a) A named routing of the third coordinate.** A *closed-form* rule (a predicate on the `2ⁿ`
  atom-masses) naming a member of `F` that reduces full maxbias, with a proof it always fires. The
  obstruction: the clearing move on the §7 stalls is a *pair* identity-match `T={i,j}`, and no tested
  named criterion (most-negative covariance, lightest `Q[1][1]`, tied-set, offender-pairing) selects
  the winning pair — it is currently an oracle over the `2ⁿ−1` subsets, which the standing rule
  forbids as proof. **This is the recurring "true union, false mechanism" wall (4th round).**
- **(b) A well-founded / lexicographic descent on a maxbias-implying potential.** Lemma 8 makes
  `Φ_{ij}=1−b_i−b_j` the right object (it implies `b_i,b_j<1/2`, and is not a forbidden potential).
  The missing piece is a member of `F` that provably *increases* `min_{ij}Φ_{ij}` (equivalently
  decreases `max_{ij}(b_i+b_j)`, hence the two largest biases jointly) without ever raising the third
  pair's sum above `1`. Iterating the tied-set match is *not* such a descent (it diverges in 67/7420 —
  survey F5); no other `F`-member has been shown to be a monotone descent on `Φ`. This is the exact
  unproven inequality.

**What would suffice (minimal form).** A lemma of the shape: *for any frustrated `P` with `β<1/2` and
`γ≥β`, there is a pair `{i,j}` such that the identity-match `B2` on `T={i,j}` (or the symmetric-Gram
B3 when `{i,j}` is symmetric) sends* **every** *coordinate bias below `β`* — with a **named** choice
of `{i,j}` and a proof using the Lemma-3 collateral formula (for B2) or Lemmas 5′/6 (for B3) bounding
the third coordinate's rise by `Φ`/`β`. The collateral formula
`b'_ℓ=[(1−β)b_ℓ+(2β−1)p^{(ℓ)}_{11}]/D` (Lemma 3, here for pair-match `T={i,j}` with the pair-marginal
in place of the singleton) gives every third coordinate's post-move bias in closed form; the missing
step is a *uniform* bound showing some named pair makes all three `<β` simultaneously. The diagnostics
(§7, §11) confirm such a pair always exists (0 stall / 20 000) but do **not** name it — that naming +
its inequality is the entire remaining content.

---

## 11. Computational checks (exact rational / symbolic; code + outputs)

All run during construction; exact `fractions.Fraction`, `sympy` for identities; harness `/tmp/r5lib.py`,
simulator `/tmp/scout2.py`. Sweeps kept ≤20 000 seeds per the operational constraint.

- **Lemma 8 algebraic identity (`sympy`).** `Pr(11)−Pr(00) = b_i+b_j−1` verified identically:
  `Pr11-Pr00 = b01+b10+2*b11-1` and `bi+bj-1 = b01+b10+2*b11-1`; `equal? True`.
- **Lemma 8 strict 0-domination, exact sweep.** Over `N=20 000` frustrated `n=3` seeds, *every* pair
  has `Pr(00)>Pr(11)`: `every pair Pr(11)>=Pr(00): cnt=5615 violations(beta<1/2)=0` (the 5615 are the
  cases where the *opposite* (1-dominated) holds — all have `β≥1/2`, confirming the implication). On
  the three litmus witnesses every pair is 0-dominated (output in §8 checks).
- **All-1-dominated stall is impossible (C1), exact.** Premise "(`γ≥β`) ∧ (has symmetric pair) ∧ (all
  symmetric pairs 1-dominated)" : `count=972, violations (β<1/2)=0` — i.e. it only ever occurs with
  `β≥1/2`, matching Lemma 8 (and strengthening the critic's 0/110k to a theorem).
- **Lemma 3 collateral formula, re-verified.** `collateral formula mismatches: 0` over 3000 seeds.
- **Third-coordinate failures of Gram (§7), exact.** Seed 8356: Gram on `(0,1)→0.5001`, `(0,2)→0.4810`,
  `(1,2)→0.4833` (all `≥β=0.4792`); cleared by match `T={0,2}→0.4697`. Seed 9350: Gram on all pairs
  `→0.4966/0.4985/0.4995≥β`; cleared by match `T={0,1}→0.4879`. Seed 15246: Gram on symmetric pair
  `(1,2)→0.4288<β=0.4583` (bridge succeeds). All exact.
- **Named litmus discharges, exact.** Litmus A `k=3` cyclic → `746/1987≈0.37544<8/17`; Litmus B
  match`{1}`→`0.45215<28/59`; Litmus C match`{0,2}`→`0.42495<18/41`.
- **Family coverage (regression backstop, NOT a proof).** `F = {B1, all subset-matches, symmetric-Gram
  on Φ>0 pairs, B4/B5}` : `stall = 0 / 20 000` frustrated `n=3`. With only the NAMED moves (B1,
  match-`{i*}`, match-`T₀`, symmetric-Gram) the stall is `5/20 000` (seeds 8191, 8356, 9350, 12663,
  16580) — each cleared by a *pair* identity-match selected by no tested named criterion (the oracle =
  the gap). Per the standing rule this 0-stall sweep is a backstop only, never a proof.

---

## 12. Summary of status

| Component | Status |
|---|---|
| Lemmas 0–7, Props A/B/C/D (rounds 1–2) | **Proved** (reused, independently verified) |
| **Lemma 8 (every pair strictly 0-dominated; `Pr(11)−Pr(00)=b_i+b_j−1`)** | **Proved (NEW)** |
| C1: all-1-dominated stall impossible (necessary half of Angle-2 contradiction) | **Proved (NEW)** |
| C2: Lemma 6 fires on *every* symmetric pair (pair-level reduction unconditional) | **Proved (NEW)** |
| Litmus A (k=3 cyclic), B (match{1}), C (match{0,2}) | **Discharged by named operators** |
| Coverage outside `(R)` (n≤2, mode-0ⁿ, non-frustrated, γ<β, sym-pair-low-residual) | **Proved** |
| **Bridge Lemma / stall-set incompatibility (§10)** | **OPEN** — the third-coordinate bridge; sufficient half of Angle-2; 0/20 000 backstop only |

The theorem is proven on every regime except the stall residual `(R)`. The round-5 advance is Lemma 8,
which (i) closes the *necessary* half of the Angle-2 contradiction in closed form, removing the
all-1-dominated half of the obstruction entirely; (ii) makes `Φ_{ij}=1−b_i−b_j` the verified
maxbias-implying potential the critic asked for; and (iii) reduces the open problem to a single
sharply-stated **Bridge Lemma**: the descent from "`Φ_{ij}>0` on every pair" to "full maxbias strictly
drops," i.e. naming a member of `F` (currently an un-routed pair-match oracle) that catches the third
coordinate. That bridge — the sufficient half — remains open.
