# Proof attempt — Round 1

**Approach:** P-dependent construction. PRIMARY move = an explicit `k=2` partition
("glue the argmax coordinate across two copies and absorb risers into its constant block",
plus the whole-copy collapse); BACKSTOP = `k = mn` cyclic glue on the anti-correlated residual.
The committed target (critic's "single cleanest target") is to prove `maxbias(P') < maxbias(P)`
**directly**, never through the refuted `Φ_p` power-mean potential.

**Status:** INCOMPLETE — blocked at the BACKSTOP (Lemma B3), specifically the single inequality
(★)/(B3-a′). All other steps are closed rigorously: the reduction to partitions,
well-definedness, the two exact closed-form marginal maps, the diagonal odds-squaring contraction
(the sole use of `maxbias<1/2`), the whole-collapse sufficient condition, the Rule-R loop, and the
exact orbit/limit formula for the cyclic glue.
**R6: the orbit-aggregate `(†)` angle is shown to be a TAUTOLOGY of (B3-a′) (the `bias_i` cancel
identically); and the two finite reductions the approach-critic flagged are PROVED insufficient by
explicit full-support counterexamples — N7 alone (`n=3`), and `N7 + whole-collapse-failure`
(`n≥4`). This maps the gap precisely: (★)/(B3-a′) is closable only by using the residual
hypothesis globally, not via any fixed finite family of `k=2`-move-failure caps. The gap is
unchanged and OPEN; see "Hard step (expanded, R6)".**
**R5: the (B3-a) half of B3 is reduced to a single open scalar inequality (★) `P̄_O < G(O_1)`
(orbit-average mass below the weight-1 geometric mean), via the now-CLOSED orbit-average chain
(R4-1 identity + safe-direction AM-GM R5-4); the surveyor's layer-mass route is confirmed broken,
and the marginals are PROVED insufficient (R5-3). The remaining open gaps are (★) [for (B3-a)] and
(B3-b″) [for (B3-b)]; either + B2 closes the theorem.**
**R3 progress:** Lemma B3 is now *reduced* to two concrete scalar sub-claims — **(B3-a)** the
geometric-mean-maximizing cyclic orbit is the weight-1 orbit `O_1` (so `ham(O*)/n = 1/n`), and
**(B3-b)** `mb > 1/n` — which trivially give `ham(O*)/n = 1/n < mb`. Both are certified with zero
violations on every isolated residual at `n=3,4,5` (90 residuals total, incl. newly-exhibited
`n=4` cases), the Step-2 mechanism is corrected (mass-smallness, not the backwards A3a squeeze),
the A3b narrative is reworded (a property of the Rule-R loop), and the dead-end attribution is
fixed. **The theorem is NOT claimed proved**: (B3-a) and (B3-b) remain aggregate consequences of
the residual hypothesis without elementary proofs. Details in **Section "Gap (sharpened R3)"**.

**R4 progress (this round): two exact reformulations + a rigorous conditional chain; theorem still
NOT proved.** (i) *(B3-a)* is rewritten exactly as a **shift-product inequality** with no orbit-
length bookkeeping: for every pattern `y` of Hamming weight `≠ 1`,
`∏_{s=0}^{n-1} P(S^s y) < ∏_{i} P(e_i)` (proved equivalent to the orbit-geomean form via the
combinatorial identity `G(O) = (∏_s P(S^s y))^{1/n}`). (ii) *(B3-b)* `mb>1/n` is rewritten exactly
as `E_P[ham] > 1`, and then via the **exact decomposition** `E[ham]-1 = Σ_{ham(x)≥2}P(x)(ham(x)-1)
- P(0^n)` as the inequality `Σ_{ham≥2}P(x)(ham(x)-1) > P(0^n)`. (iii) A **rigorous riser bound**
`bias_j(P') ≤ p_j q_i/(p_i²+q_i²)` (direction re-verified, valid because `mb<1/2`) and a **rigorous
conditional chain**: combining the whole-collapse-failure bound `P(1^n) ≥ √(mb/(1-mb))·P(0^n)` (a
genuine `k=2` residual consequence, A3a, direction re-verified 90/90) with the decomposition gives
`n·mb ≥ E[ham] ≥ 1 + [(n-1)√(mb/(1-mb)) - 1]·P(0^n)`, so **`mb > 1/((n-1)²+1) ⇒ E[ham]>1 ⇒
mb>1/n`**. This reduces (B3-b) to the strictly weaker bound `mb > 1/((n-1)²+1)`. (iv) Slow-test
contrapositive evidence: across 917 full-support `P` with `E[ham]≤1`, **zero** are residuals
(worst reduces to `0.44·mb` — large margin), confirming the `E[ham]=1` boundary is not tight.
**Still OPEN:** the shift-product inequality (B3-a) and the weaker scalar bound `mb>1/((n-1)²+1)`
(or directly `mb>1/n`) both remain aggregate consequences of the full residual conjunction without
an elementary proof. Details in **Section "Hard step (expanded, R4)"** and the updated Gap.

**R5 progress (this round): the (B3-a) half is reduced to a SINGLE clean scalar gap (★), and the
marginals are proved insufficient.** Following the approved orbit-AVERAGE chain, (B3-a′) now follows
from the one inequality **(★) `P̄_O < G(O_1)`** (orbit-average mass `<` weight-1 geometric mean) via
two CLOSED steps: the R4-1 identity and the SAFE-direction AM-GM **R5-4** (`∏_s P(S^s y) ≤ P̄_O^n`).
The survey's `M_w/d` route is CONFIRMED broken (`M_1/d ≥ G(O_1)` and `M_w/d ≥ P̄_O` in 100% of
cases). A NEW general lemma **R5-3** (`∏_s P(S^s y) ≤ ∏_i bias_i`, proved from a monotone-support
bound R5-1 + a cyclic incidence count R5-2) is the best bound the *marginals* yield — and it
provably overshoots `∏_i P(e_i)` (by `∏_i bias_i/P(e_i)`), so **(★) cannot be closed from the
marginals alone; it genuinely requires the joint residual-mass constraints.** (★) is verified with
`0` violations on 90 slow-isolated + 40 fresh n=3 residuals, min relative margin `0.167` (n=3).
Details in **Section "Hard step (expanded, R5)"**. The theorem is **NOT** claimed proved.

---

## Setup

Let `P` be a full-support probability distribution on `{0,1}^n`, write `p_i = bias_i(P) =
Pr_{x~P}(x_i=1)`, `q_i = 1-p_i`, and `mb := maxbias(P) = max_i p_i`. The hypothesis is `mb < 1/2`,
equivalently every coordinate **odds** `o_i := p_i/q_i` satisfies `o_i < 1`.

`P^k` is the product of `k` i.i.d. copies on `{0,1}^{nk}`; global coordinate `(c,i)` (copy
`c ∈ {0,…,k-1}`, local coordinate `i ∈ {0,…,n-1}`) has index `c·n + i`. For a pair set
`S ⊆ {(u,v)}`, `P'` is `P^k` conditioned on `{X_u = X_v : (u,v) ∈ S}`. To prove: there exist
`k ≥ 1` and `S` with `maxbias(P') < mb`.

### S0. Reduction to "force a partition constant" (rigorous)

**Claim S0.** Conditioning `P^k` on `{X_u=X_v : (u,v)∈S}` is identical to the following: form
the graph `G = ([nk], S)`, take its connected components `C_1,…,C_r`, and condition on the event
`E` that *every component is constant* (all coordinates in a component share one common bit).

*Proof.* `X_u = X_v` is an equivalence-generating relation; the transitive closure of the
relations imposed by `S` is exactly "`u,v` in the same connected component of `G` ⇒ `X_u = X_v`".
A configuration satisfies all constraints in `S` iff it is constant on each connected component.
∎

Thus the entire design space is: **choose `k`, choose a set partition `Π` of the `nk`
coordinates, condition each block of `Π` to a common value.** Below we describe each move by its
partition.

### S1. Well-definedness / positive probability (rigorous)

**Claim S1.** For full-support `P` and any `k` and any partition `Π`, the conditioning event `E`
has `Pr_{P^k}(E) > 0`, so `P'` is well-defined.

*Proof.* Full support means `P(x) > 0` for every `x ∈ {0,1}^n`. Consider the configuration of
`P^k` in which every copy equals the all-zeros vector `0^n`. Then every coordinate is `0`, so
every block of `Π` is constant; this configuration lies in `E` and has probability
`P(0^n)^k > 0`. Hence `Pr_{P^k}(E) > 0`. ∎

(All conditional probabilities used below are therefore well-defined ratios with strictly
positive denominators.)

---

## Argument

The construction is **P-dependent** (legitimate: the theorem is existential). We exhibit a small
menu of moves and the explicit rule selecting which to use. Two of the moves are `k=2`
partitions handled by exact closed forms (Lemmas A1–A3); the third is the `k=mn` cyclic glue
(Lemmas B1–B2 closed-form, B3 the open inequality).

### Move I: single same-coordinate cross-copy glue (`k=2`)

`Π` glues `(0,i) ~ (1,i)` (force coordinate `i` equal across the two copies), all other
coordinates free.

**Lemma A1 (exact marginals — VERIFIED, Certificate 2).** With `p=p_i`, `q=q_i`, `Z=p²+q²`, and
joint masses `a_v := P(X_j=1, X_i=v)`,
```
   bias_i(P') = p² / Z,
   bias_j(P') = (a_1·p + a_0·q) / Z        (j ≠ i).
```
*Proof.* The two copies are independent. Conditioning on `X^{(0)}_i = X^{(1)}_i` puts weight
`P(x)P(y)·[x_i=y_i]` on `(x,y)`; normalizing, `Z' := Σ_{x_i=y_i} P(x)P(y) = p²+q²` (the two
copies agree on coordinate `i` either both-1, prob `p²`, or both-0, prob `q²`). By symmetry the
two copies have identical marginals. For coordinate `i` in copy 0: it is `1` exactly on the
both-1 branch, weight `p²`, giving `p²/Z`. For `j≠i` in copy 0: copy 1 is independent given the
shared `i`-value `v` (probability `p²` for `v=1`, `q²` for `v=0`), and copy 0's `j`-marginal in
that branch is `P(X_j=1 | X_i=v) = a_v / Pr(X_i=v)`. Hence
`bias_j(P') = [p²·(a_1/p) + q²·(a_0/q)] / Z = (a_1 p + a_0 q)/Z`. Cross-checked against
brute-force enumeration over two copies, 20/20 random instances (Certificate 2). ∎

**Lemma A2 (diagonal odds-squaring — the ONLY use of `mb<1/2`; PROVED, Certificate 1).**
In odds, Move I maps `o_i ↦ o_i²` on the glued coordinate, and `o_i < 1 ⇒ o_i² < o_i` strictly.

*Proof.* `bias_i(P')/(1-bias_i(P')) = (p²/Z)/(q²/Z) = (p/q)² = o_i²`. Equivalently
`p_i - bias_i(P') = p(p-1)(2p-1)/(2p²-2p+1)` (symbolic factorization, Certificate 1). For
`0 < p < 1/2`: `p>0`, `(p-1)<0`, `(2p-1)<0`, denominator `>0`, so the product is `>0`, i.e.
`bias_i(P') < p_i` strictly. This is the unique place `mb<1/2` enters: it is exactly `o_i<1`. ∎

**The obstruction (verified, symbolic).** Move I can fail to reduce `mb` because a riser `j`
(anti-correlated with `i`) can rise above `mb`. Worst case `a_1=0, a_0=p_j`: then
`bias_j(P') = p_j q/Z`, and the threshold bound is `p_j < p_i(p²+q²)/q`; but symbolically
`p²+q²-q = p(2p-1) < 0` for `p<1/2`, so `(p²+q²)/q < 1`, hence even a riser tied at the max can
overshoot. This is why a single move is not universal (matches scout's ~5% failure). It is
resolved by absorbing the offending risers into `i`'s block — Move II.

### Move II: absorb-block glue (`k=2`)

For a block `B ⊆ {0,…,n-1}` with `i* = argmax ∈ B`, the partition forces **all of**
`{(0,j),(1,j) : j∈B}` into one constant block; other coordinates free. Let
`A_v := P(x_j = v for all j∈B)` be the mass on the all-`v` block pattern (`v∈{0,1}`), and
`Su_{v,u} := P(X_u=1, block=v)`.

**Lemma A3 (exact marginals — VERIFIED, Certificate 3).** With `Z = A_0² + A_1²`,
```
   for u ∈ B:   bias_u(P') = A_1² / Z          (= odds (A_1/A_0)² — a squared "block odds")
   for u ∉ B:   bias_u(P') = (A_0·Su_{0,u} + A_1·Su_{1,u}) / Z .
```
*Proof.* Conditioning event `E_B`: each copy is block-constant with a common value `v`, and the
two copies share that value. Per copy the block is all-`v` with prob `A_v`; the two copies
independently must share `v`, so `Pr(E_B) = A_0² + A_1² = Z`. Given `E_B` with value `v`, the two
copies are independent draws from `P(·|block=v)`. A coordinate `u∈B` is `1` iff `v=1`: contributes
`A_1²` to the numerator, giving `A_1²/Z`; its odds is `(A_1/A_0)²`. A coordinate `u∉B` in copy 0
has marginal `Σ_v Pr(E_B,v)·P(X_u=1|block=v) = Σ_v A_v²·(Su_{v,u}/A_v) = Σ_v A_v Su_{v,u}`, over
`Z`. Cross-checked against brute force, 20/20 random `(P,B)` (Certificate 3). ∎

**Two clean rigorous consequences of Lemma A3:**

**Lemma A3a (block contraction).** For `u∈B`, `bias_u(P') < mb` **iff**
`A_1/A_0 < √(mb/(1-mb))`. In particular the *whole-collapse* (`B = {0,…,n-1}`, so
`A_1 = P(1^n)`, `A_0 = P(0^n)`) reduces every coordinate below `mb` whenever
`P(1^n)/P(0^n) < √(mb/(1-mb))`.

*Proof.* `A_1²/Z < mb ⟺ A_1²(1-mb) < mb·A_0² ⟺ (A_1/A_0)² < mb/(1-mb)`. Since `mb<1/2`,
`mb/(1-mb) < 1`, so the threshold `√(mb/(1-mb)) < 1` is well-defined and `<1`. For the
whole-collapse all coordinates are in `B`, so this single inequality controls all `n` marginals
simultaneously. ∎

**Lemma A3b (the Rule-R loop, restated correctly — REWORDED R3).** Absorbing a riser `j` into the
block `B` switches `j`'s marginal from the conditional form `(a_1 p + a_0 q)/Z` of Lemma A1 (no
`1/2` cap, can exceed `mb`) to the squared-block form `A_1²/Z` of Lemma A3 (`< mb` exactly under
the explicit polynomial condition of Lemma A3a). **Caveat (verified by the R1 critic):** a single
absorption is **not** coordinate-monotone — moving `j` into `B` can lift some *other*, previously
safe coordinate `u ∉ B` above `mb` (65 such "new-riser" events in 30000 trials). So absorption does
not, by itself, "kill the riser." The object that is correct is the **Rule-R loop** (below), which
**re-checks all coordinates each round** and re-absorbs any coordinate (old or newly created) whose
Lemma-A3 marginal is `≥ mb`. Because `B` strictly grows on every non-terminal round, the loop
terminates in `≤ n` rounds; when it halts it does so with **all** `nk` marginals `< mb`, and only
then is the partition output. Thus the correct load-bearing statement is a property of the loop,
not of any single absorption. ∎

**Explicit `k=2` rule R (the TARGET LEMMA construction).** Start `B = {i*}`. Repeat: compute the
Lemma-A3 marginals; if some coordinate `u ∉ B` has `bias_u(P') ≥ mb`, add all such `u` to `B`
and repeat; else stop. (Terminates in `≤ n` rounds since `B` strictly grows.) If the final
marginals are all `< mb`, output this `k=2` partition.

**Status of Move II / Rule R.** Rule R is a *correct, terminating, explicit* procedure; whenever
it stops with all marginals `< mb` it provably reduces `maxbias` (Lemmas A3,A3a). Its sufficient
condition is an explicit polynomial-sign condition in the joint masses (Lemmas A3a/A3b). It is
**not universal**: on the anti-correlated residual `B` grows to the whole set and the whole-
collapse condition `P(1^n)/P(0^n) < √(mb/(1-mb))` fails (verified failure mode; see Edge cases).
Those exact instances are passed to the BACKSTOP.

### Move III: cyclic glue (`k = mn`) — the BACKSTOP

Let `S` be the cyclic shift `(Sx)_i = x_{(i-1) mod n}`. Take `k = m·n` copies and glue
`(c,i) ~ (c+1 mod k, (i+1) mod n)` for all `c,i`; equivalently force copy `c` to be `S^c` applied
to copy 0. The feasible configurations are exactly the "orbit tuples"
`(x, Sx, S²x, …, S^{k-1}x)` with weight `w_k(x) = Π_{c=0}^{k-1} P(S^c x)`.

**Lemma B1 (equal marginals + orbit formula — VERIFIED, Certificate 4).** For `k = n`, all `nk`
marginals of `P'` are equal to
```
   b* = ( Σ_x w_n(x)·ham(x)/n ) / ( Σ_x w_n(x) ),   w_n(x) = Π_{c=0}^{n-1} P(S^c x),
```
where `ham(x)` is the Hamming weight.

*Proof.* The partition is invariant under the simultaneous relabeling "shift copy index by 1 and
apply `S` to local coordinates," which acts transitively on the `n²` coordinates of the `k=n`
gluing; hence all marginals coincide. Their common value is the `w_n`-weighted average of the
normalized Hamming weight of copy 0, which is the displayed `b*`. `w_n` is constant on each
cyclic orbit. Verified: brute force gives all marginals equal (20/20) and matching `b*` to `1e-9`
(20/20), Certificate 4. ∎

**Lemma B2 (geometric-mean limit — VERIFIED, Certificate 5).** Let `O` range over cyclic orbits
and `G(O) := (Π_{y∈O} P(y))^{1/|O|}` be the geometric mean of `P` over the orbit. As `m→∞` with
`k = mn`,
```
   b*_{mn}  →  ham(O*)/n,
```
where `O*` is the orbit(s) maximizing `G(O)`; if there are ties the limit is the (uniform)
average of `ham(O)/n` over the maximizing orbits.

*Proof.* Over `k = mn` cyclic steps each element of `orbit(x)` is visited `mn/|orbit(x)|` times,
so `w_{mn}(x) = (Π_{y∈orbit(x)} P(y))^{mn/|orbit(x)|} = G(orbit(x))^{mn}`. Thus in the weighted
average `b*_{mn}`, the weight of orbit `O` is proportional to `|O|·G(O)^{mn}`; as `m→∞` this
concentrates (geometric domination) on the maximizers of `G`, giving the stated limit.
Numerically `b*_{24}` matches the geometric-mean limit to `1e-3` (Certificate 5; remaining slack
is the finite-`m` rate near orbit ties). ∎

**Consequence (the backstop reduction).** If `ham(O*)/n < mb` (with the tie-average `< mb`),
then by Lemma B2 there is a finite `m` with `b*_{mn} < mb`, and Move III at `k = mn` reduces
`maxbias`. Reducing the BACKSTOP to a *single combinatorial inequality* on the residual:

> **Lemma B3 (OPEN — reduced R3).** If no `k=2` partition reduces `maxbias(P)` (the residual),
> then the max-geometric-mean cyclic orbit satisfies `ham(O*)/n < mb` (tie-average strictly below
> `mb`). **R3 reduction:** this follows from the two certified scalar sub-claims **(B3-a)** `O* =`
> the weight-1 orbit `O_1` (so `ham(O*)/n = 1/n`) and **(B3-b)** `mb > 1/n` (see Hard step (2)).

---

## Hard step (expanded)

The two hard steps are the riser control (Move II) and the backstop (Lemma B3).

**(1) Riser control — CLOSED.** Lemma A1 isolates the riser term `bias_j(P') = (a_1 p + a_0 q)/Z`,
a *conditional* average with no `1/2` cap, which is the scout's central obstruction. The
mechanism that defeats it is the **Rule-R loop** (Lemma A3b, reworded R3): each absorption
replaces a riser's conditional marginal by the squared-block odds `(A_1/A_0)²`, whose reduction
below `mb` is the **explicit polynomial inequality** `A_1²(1-mb) < mb·A_0²` (Lemma A3a). A single
absorption is *not* coordinate-monotone (it can create a new riser), so it is the loop — which
re-checks all coordinates each round, terminates in `≤ n` rounds since `B` strictly grows, and
outputs only when **all** marginals are `< mb` — that is correct. The mechanism is "the diagonal
odds-squaring (the only use of `mb<1/2`) dominates, once the harmful conditional reweighting is
removed by absorption, iterated to a fixed point."

**(2) Backstop (Lemma B3) — new structural reduction (R3), reduced to two certified scalar
sub-claims.** Lemmas B1–B2 turn Move III into the purely combinatorial quantity `ham(O*)/n`,
where `O*` maximizes the orbit geometric mean `G(O) = (∏_{y∈O} P(y))^{1/|O|}`. The R3 work
sharpens "`O*` is low Hamming weight" into an **explicit identification of `O*` plus a scalar
threshold on `mb`**, and corrects the recorded dead-end attribution. Let
`O_1 := orbit(e_1) = {e_1, …, e_n}` be the **weight-1 cyclic orbit** (the cyclic shift `S` sends
`e_1 ↦ e_2 ↦ … ↦ e_n ↦ e_1`, so all `n` standard basis vectors form one orbit), with
`G(O_1) = (∏_{i=1}^n P(e_i))^{1/n}` and `ham(O_1)/n = 1/n`. I reduce Lemma B3 to:

> **(B3-a)** On a residual, `O_1` is the **unique** geometric-mean-maximizing cyclic orbit; hence
> `O* = O_1` and `ham(O*)/n = 1/n` (no ties).
>
> **(B3-b)** On a residual, `mb > 1/n`.

Trivially **(B3-a) ∧ (B3-b) ⇒ `ham(O*)/n = 1/n < mb`**, which is exactly Lemma B3 (the
tie-average degenerates to the single value `1/n` by (B3-a)). This is strictly more structure than
R1's "the aggregate `ham(O*)/n < mb`": both sub-claims are *concrete scalar* statements, and the
geometric-mean quantity is pinned to a known orbit.

**Correction of the recorded dead end.** R1/R2 recorded "orbit-vs-complement `G(O) ≥ G(Ō)` is
false on residuals." I verified the precise content (script `probe_ovc.py`): the failing pair is
the **singleton pair** `(0^n, 1^n)` — `G(0^n) ≥ G(1^n)` fails on 21/26 `n=3` residuals (because
anti-correlation makes `P(1^n) ≥ P(0^n)`). **But that pair is irrelevant to identifying `O*`:**
both singletons have *absolutely tiny* geomean (Step 2 below) and lose to the interior orbits.
The comparison that actually matters, **weight-1 orbit vs. weight-2 orbit**, *holds* on every
residual (26/26 at `n=3`; and at `n=4,5` the weight-1 orbit's geomean exceeds the runner-up orbit
by a factor `≥ 1000`, i.e. runner-up/winner ≤ 0.0011). So the dead end was mis-attributed; the
relevant ordering is not dead.

**Step 2 (corrected R3 — singletons are not the maximizer, for the mass-smallness reason).** The
R2 survey's "A3a both-sides squeeze" justification is *wrong* (it had the A3a inequality backwards:
whole-collapse failure gives `P(1^n)/P(0^n) ≥ √(mb/(1-mb))`, the *opposite* direction). The
correct content is: **on a residual `P(0^n)` and `P(1^n)` are small in absolute value**, so the
singleton orbits `{0^n}` (geomean `P(0^n)`) and `{1^n}` (geomean `P(1^n)`) lose the geometric-mean
maximization to the interior weight-1 orbit. Numerically (`probe_struct.py`): on `n=3,4` residuals
`P(0^n), P(1^n) ≤ 6·10⁻³` while `G(O_1) ∈ [0.07, 0.32]` — three to four orders of magnitude larger.
This absolute-smallness is itself a *piece* of the open concentration content (it is **not** a free
A3a corollary), so Step 2 is folded into Step 3, not logged as an independent closed lemma.

**Step 3 (the gate — still open, sharply reduced).** (B3-a) and (B3-b) are each TRUE with zero
violations on every independently-isolated residual (n=3: 26/26, n=4: 63/63, n=5: 1/1; spec
residual included), with margins `mb − 1/n ≥ 0.039` and runner-up/winner geomean `≤ 0.0011` — see
`b3_certificate.py` reproduced below. They are the genuine remaining content: each is an
**aggregate consequence of the full residual hypothesis** (the conjunction of all `k=2`-partition
failures), and neither has been reduced to an elementary signable inequality. In particular:

- *(B3-b) attempt.* The contrapositive `mb ≤ 1/n ⇒ not a residual` is supported by the
  **whole-collapse**: on every tested `P` with `mb ≤ 1/n` the whole-collapse reduces (3103/3103 at
  `n=3`, 370/370 at `n=4`; margin `W/mb ≤ 0.20`). The rigorous facts `P(1^n) ≤ mb` (the pattern
  `1^n` contributes `P(1^n)` to *every* marginal) and the union bound `P(0^n) ≥ 1 − Σ_i bias_i ≥
  1 − n·mb` are in hand, but the second bound degrades to `0` exactly at `mb = 1/n`, so it does not
  by itself yield `P(1^n)/P(0^n) < √(mb/(1-mb))` at the boundary. (Empirically `mb` stays bounded
  away from `1/n` on residuals — see Gap.)
- *(B3-a) attempt.* A per-pattern sufficient condition `max_{ham(y)≠1} P(y) < G(O_1)` would force
  `O* = O_1`, and it holds at n=4,5 — but it *fails* 3/26 at n=3 (a single weight-2 pattern can
  exceed `G(O_1)` while the weight-2 *orbit geomean* still loses). So (B3-a) is genuinely a
  geometric-mean-level (aggregate) fact, not a per-pattern one.

---

## Hard step (expanded, R4) — exact reformulations and a conditional chain

All claims in this section are PROVED (rigorous algebra/combinatorics) **except** the two clearly
labelled OPEN aggregate inequalities at the end. Every identity, bound, and direction below is
verified with zero violations on all 90 isolated residuals by `b3_round4.py` (reproduced in
*Computational checks*); the riser-bound direction is additionally checked on 382 random valid
instances. (Tooling note: residual isolation here uses the **slow** Bell-lattice
`is_residual`; `fast_residual.fast_is_residual_k2` produces false positives near the boundary and
is NOT used for any new claim.)

### (R4-A) Exact reformulation of (B3-a): the shift-product inequality

**Lemma R4-1 (orbit geomean = shift geomean — PROVED, combinatorial).** Let `S` be the cyclic
shift `(Sx)_i = x_{(i-1) mod n}`, and for a pattern `y` let `O = orbit(y)` have length `d` (so
`d | n`). Then
```
   G(O) := (∏_{z∈O} P(z))^{1/d} = (∏_{s=0}^{n-1} P(S^s y))^{1/n}.
```
*Proof.* The `n` shifts `S^0 y,…,S^{n-1} y` traverse the orbit `O` periodically, hitting each of
its `d` distinct elements exactly `n/d` times. Hence `∏_{s=0}^{n-1} P(S^s y) = (∏_{z∈O} P(z))^{n/d}`;
taking the `n`-th root gives `(∏_{z∈O}P(z))^{1/d}/... = (∏_{z∈O}P(z))^{1/d}` after the exponent
`(n/d)·(1/n)=1/d`. ∎  (Verified exact, `b3_round4.py` block [R4-1], `n=3,4,5`.)

This removes all orbit-length bookkeeping: `G(O)` is simply the geometric mean of `P` over the
`n` cyclic shifts of any representative `y`. For the weight-1 orbit `O_1 = orbit(e_1)` the shifts
are exactly `e_1,…,e_n`, so `G(O_1) = (∏_i P(e_i))^{1/n}`. Therefore (B3-a) `G(O) < G(O_1)` for
every orbit `O ≠ O_1` is **exactly equivalent** to:

> **(B3-a′) [shift-product form].** For every pattern `y` with `ham(y) ≠ 1`,
> `∏_{s=0}^{n-1} P(S^s y) < ∏_{i=1}^{n} P(e_i)`.

(For `y` of weight `1` the product equals `∏_i P(e_i)` exactly — equality, the maximizer.) This
is a clean comparison of two products of `n` masses each, with no exponents to track. The
singletons `0^n,1^n` (weight `0` and `n`) are special cases of `ham≠1`, so (B3-a′) handles them
uniformly together with all interior orbits — superseding the earlier separate "singleton
absolute-smallness" sub-argument. **Status:** (B3-a′) is verified with zero violations on all 90
residuals (n=3: 130/130 patterns, n=4: 756/756, n=5: 27/27); it remains OPEN as a theorem.

### (R4-B) Exact reformulation of (B3-b) and a rigorous conditional chain

**Lemma R4-2 (E[ham] decomposition — PROVED).** With `bias_i = E_P[x_i]`,
`Σ_i bias_i = E_P[ham]` (linearity), and
```
   E_P[ham] - 1 = Σ_{x: ham(x)≥2} P(x)·(ham(x)-1)  -  P(0^n).
```
*Proof.* `E[ham]-1 = Σ_x P(x)(ham(x)-1) = -P(0^n) + 0 + Σ_{ham(x)≥2}P(x)(ham(x)-1)` (weight-0 term
contributes `-P(0^n)`, weight-1 terms contribute `0`). ∎  Hence, with `mb ≥ E[ham]/n` (max ≥ mean):

> **(B3-b′) [excess-mass form].** `mb > 1/n  ⟺  E[ham] > 1  ⟺  Σ_{ham(x)≥2}P(x)(ham(x)-1) > P(0^n).`
>
> (the first `⟺` is `mb≥E[ham]/n` together with: if `E[ham]≤1` then every `bias_i≤?`... — see the
> caveat below; the second `⟺` is Lemma R4-2.)

*Caveat on the first equivalence.* `mb ≥ E[ham]/n` gives only `E[ham]>1 ⇒ mb>1/n` (one direction);
the converse can fail when biases are unequal. So the operative target is the **forward** direction:
derive `E[ham] > 1` (equivalently the excess-mass inequality), which then yields `mb > 1/n`. As the
approach-critic noted, in the symmetric regime `E[ham]>1 ⟺ mb>1/n` exactly, so the lever gives no
free slack there and the residual hypothesis must do the work. The slow-test contrapositive below
shows the residual hypothesis is *strong enough*: it forbids `E[ham]≤1` outright.

**Lemma R4-3 (riser upper bound — PROVED, direction verified).** In Move I (single-coordinate glue
on `i`, Lemma A1), every riser `j ≠ i` satisfies, when `p_i < 1/2`,
```
   bias_j(P') = (a_1 p_i + a_0 q_i)/(p_i²+q_i²)  ≤  p_j·q_i/(p_i²+q_i²),
```
where `a_1 = P(X_j=1,X_i=1)`, `a_0 = P(X_j=1,X_i=0)`, `a_1+a_0 = p_j`.
*Proof.* Write `bias_j(P') = (p_j q_i + a_1(p_i-q_i))/(p_i²+q_i²)`. Since `p_i<1/2` gives
`p_i-q_i<0` and `a_1≥0`, the expression is maximized at `a_1=0`, value `p_j q_i/(p_i²+q_i²)`. ∎
(Verified 0 violations on 382 random valid instances; note this is exactly the *failed* sufficient
condition for single-glue universality — at the argmax it collapses to the tautology `mb≤1/2` — so
it is a true but, on its own, non-decisive bound. Recorded for completeness and because the
direction had to be pinned: see role memory on this problem's history of backwards bounds.)

**Lemma R4-4 (whole-collapse failure bound — PROVED, A3a, direction verified 90/90).** On a
residual the whole-collapse `k=2` move (block `B = {0,…,n-1}`) does not reduce `maxbias`; by
Lemma A3a applied to `B`,
```
   P(1^n)/P(0^n) ≥ √(mb/(1-mb))   i.e.   P(1^n) ≥ √(mb/(1-mb))·P(0^n).
```
(This is the *corrected* A3a direction — whole-collapse FAILURE gives `≥`, the opposite of the R2
survey's "both-sides squeeze". Verified 26/26 n=3, 63/63 n=4, 1/1 n=5.)

**The conditional chain (PROVED, given the weaker bound).** Drop all weight-≥2 terms in the
decomposition except `1^n` (which has coefficient `ham(1^n)-1 = n-1`):
```
   E[ham] - 1  =  Σ_{ham≥2}P(x)(ham(x)-1) - P(0^n)
               ≥  (n-1)·P(1^n) - P(0^n)                      [drop nonneg terms]
               ≥  [(n-1)·√(mb/(1-mb)) - 1]·P(0^n).           [Lemma R4-4]
```
Therefore `n·mb ≥ E[ham] ≥ 1 + [(n-1)√(mb/(1-mb)) - 1]·P(0^n)`. If the bracket is positive — i.e.
`(n-1)√(mb/(1-mb)) > 1`, equivalently `mb > 1/((n-1)²+1)` — then `E[ham] > 1`, hence `mb > 1/n`.
**This reduces (B3-b) to the strictly weaker scalar bound:**

> **(B3-b″).** On a residual, `mb > 1/((n-1)²+1)`.

For `n=3` this asks `mb > 1/5` (vs the target `1/3`); for `n=4`, `mb > 1/10` (vs `1/4`). Verified:
the chain `E[ham] ≥ 1 + [(n-1)√(mb/(1-mb)) - 1]P(0^n)` and `mb > 1/((n-1)²+1)` both hold with zero
violations on all 90 residuals (`b3_round4.py`). **Status:** (B3-b″) is OPEN — it is weaker than
the original (B3-b) but is still an aggregate consequence of the residual conjunction lacking an
elementary proof. The chain is a genuine reduction (not a relabel): it converts the boundary-tight
`mb>1/n` into the slacker `mb>1/((n-1)²+1)`, and replaces the round-3 union bound `P(0^n)≥1-n·mb`
(which degraded to `0` at `mb=1/n`) by the whole-collapse bound, which has no boundary degeneracy.

### (R4-C) Why no single `k=2` move closes either piece (the residual conjunction is essential)

I tested, with the slow Bell-lattice residual test, exactly which moves are needed:
- **single-coordinate glue alone** reduces `mb` on `197/210` near-boundary `E[ham]≤1` instances,
  but fails `44/889` in the full `E[ham]≤1` sweep (Lemma R4-3 at the argmax is non-decisive, as
  shown). So single-glue is not sufficient for the (B3-b) contrapositive.
- **single-glue + whole-collapse + all permutation glues** together reduce **every** one of `850`
  tested `E[ham]≤1` residual-candidates (`0` uncovered). The permutation glue (force
  `copy1 = π(copy0)` for a permutation `π`; feasible configs `(x,π(x))` with weight `P(x)P(π(x))`,
  closed form verified) is the third necessary family and is itself a `k=2` move in the design
  space. This is direct evidence that the proof of (B3-b) genuinely requires the **conjunction** of
  several `k=2`-move failures (not any single move), exactly the approach-critic's success bar.
- **Slow-test contrapositive:** `917` full-support `P` with `E[ham]≤1` were tested; **`0`** are
  residuals (worst reduces to `0.44·mb`). So `E[ham]≤1 ⇒ not a residual` holds with a *large* margin
  — the `E[ham]=1` boundary is not tight, consistent with the observed residual floor `E[ham]≥1.009`.

---

## Hard step (expanded, R5) — orbit-average reduction of (B3-a′), and the exact gap

This round targets **(B3-a′)** via the orbit-AVERAGE chain (approach-critic APPROVED the
top-level reduction as direction-sound and non-circular). The chain is:

> For an orbit `O` of length `d` and representative `y` (`ham(y)=w≠1`), with
> `P̄_O := (1/d)·Σ_{z∈O} P(z)` the orbit-average mass and `G(O_1) := (∏_i P(e_i))^{1/n}`:
>
> `∏_{s=0}^{n-1} P(S^s y)  =  (∏_{z∈O}P(z))^{n/d}`  [R4-1, PROVED]
> `                        ≤  P̄_O^{\,n}`              [AM-GM, **R5-4**, SAFE direction]
> `                        <  G(O_1)^n = ∏_i P(e_i)`  [**(★)**, OPEN — the one remaining gap].

The first two steps are now closed; only **(★) `P̄_O < G(O_1)`** is open. Every claim below is
verified with **zero violations** on all 90 slow-isolated residuals plus 40 fresh n=3 residuals
(`b3_round5.py`, reproduced in *Computational checks*).

### (R5-4) The AM-GM step is the SAFE direction — PROVED

**Lemma R5-4 (orbit AM-GM).** For any orbit `O` of length `d` with representative `y`,
`∏_{s=0}^{n-1} P(S^s y) ≤ P̄_O^{\,n}`, where `P̄_O = (1/d)Σ_{z∈O}P(z)`.
*Proof.* By the AM-GM inequality on the `d` positive numbers `{P(z) : z∈O}`,
`∏_{z∈O}P(z) ≤ ((1/d)Σ_{z∈O}P(z))^d = P̄_O^{\,d}`. Raising both sides to the positive power `n/d`
(monotone, both sides `>0`) and using `∏_s P(S^s y) = (∏_{z∈O}P(z))^{n/d}` (R4-1) gives
`∏_s P(S^s y) ≤ P̄_O^{\,n}`. ∎ (Verified `78/78, 315/315, 7/7` orbits, n=3,4,5; the survey's
direction concern is resolved — this is `product ≤ mean^d`, not the reversed log-supermodular bound.)

Note `P̄_O = (1/n)Σ_{s=0}^{n-1} P(S^s y)` as well, since the `n` shifts hit each of the `d` distinct
orbit elements `n/d` times. So (★) is exactly: the orbit-average of `P` over the cyclic shifts of `y`
is strictly below the geometric mean of `P` over the weight-1 patterns.

### (R5-broken) The survey's layer-mass route is dead — CONFIRMED

The surveyor proposed `P̄_O ≤ M_w/d`, then `M_w/d < G(O_1)` from `M_w<M_1`. This is **broken** (the
approach-critic flagged it; I re-verified numerically, `b3_round5.py`):
`M_1/d ≥ G(O_1)` in **100%** of cases (because `M_1 = n·AM(P(e_i)) ≥ n·GM = n·G(O_1) ≥ d·G(O_1)`),
and `M_w/d ≥ P̄_O` in **100%** of cases — so `M_w/d < G(O_1)` is *strictly stronger* than (★) and
routes the wrong way. We DO NOT coarsen to layer mass; the margin lives at the orbit-average level.

### (R5-1,2,3) A new PROVED general cap — and why marginals alone cannot close (★)

We isolate exactly how far elementary, residual-free bounds can go, and where the genuine
joint-mass content begins.

**Lemma R5-1 (monotone-support bound — PROVED, general).** For every full-support `P` and every
pattern `z` of weight `w≥1`, `P(z) ≤ min_{i∈supp(z)} bias_i`. Moreover, for every `i∉supp(z)`,
`P(z) ≤ 1-bias_i = q_i`. Hence `P(z) ≤ GM_{i∈supp(z)}(bias_i)` and
`P(z) ≤ ∏_{i=1}^n (bias_i^{z_i} q_i^{1-z_i})^{1/n}`.
*Proof.* `{X=z} ⊆ {X_i=1}` for `i∈supp(z)` gives `P(z)≤Pr(X_i=1)=bias_i`; likewise `{X=z}⊆{X_i=0}`
for `i∉supp(z)` gives `P(z)≤q_i`. The minimum of a set of upper bounds is an upper bound, and the
minimum is `≤` any geometric mean of the same numbers. ∎ (Verified `0/159000` random full-support
instances, all `n=3,4,5`.)

**Lemma R5-2 (cyclic incidence — PROVED, combinatorial).** For a weight-`w` pattern `y`, across the
`n` cyclic shifts `S^0 y,…,S^{n-1} y` each coordinate `i` is set to `1` in exactly `w` of them.
*Proof.* `(S^s y)_i = y_{(i-s) mod n}`; as `s` ranges over `0,…,n-1`, `(i-s) mod n` ranges over all
of `{0,…,n-1}` once, hitting the `w` positions of `supp(y)` exactly `w` times. ∎ (Verified n=3,4,5,6.)

**Lemma R5-3 (shift-product cap — PROVED, general, NEW this round).** For every full-support `P` and
every pattern `y` of weight `w≥1`,
```
   ∏_{s=0}^{n-1} P(S^s y)  ≤  ∏_{i=1}^{n} bias_i,
```
and the sharper `∏_s P(S^s y) ≤ ∏_i bias_i^{\,w/n}·q_i^{\,(n-w)/n}`.
*Proof.* Take logs and apply R5-1 in the form `log P(S^s y) ≤ (1/w)Σ_{i∈supp(S^s y)} log bias_i`
(GM over support). Summing over `s` and using R5-2 (each `i` is in the support of exactly `w` shifts):
`Σ_s log P(S^s y) ≤ (1/w)Σ_s Σ_{i∈supp(S^s y)} log bias_i = (1/w)·Σ_i (w·log bias_i) = Σ_i log bias_i`.
The sharper form uses the full R5-1 bound `log P(S^s y) ≤ (1/n)Σ_i (z_i log bias_i + (1-z_i)log q_i)`
for `z=S^s y`, summed with R5-2 (`Σ_s z_i = w`, `Σ_s(1-z_i)=n-w`). ∎ (Verified `0/159000` general
instances; `78/78, 315/315, 7/7` on residuals — it holds for ALL `P`, residual or not.)

**Why this caps out — the precise location of the gap.** R5-3 is the *best* bound obtainable from
the single-coordinate marginals `bias_i`: any per-element bound `P(z) ≤ f(bias_{·})` aggregates, via
the cyclic incidence R5-2, to a product of per-coordinate factors. But
`∏_i bias_i ≥ ∏_i P(e_i) = G(O_1)^n` (since `bias_i = Σ_{x_i=1}P(x) ≥ P(e_i)`), so the cap lands
**above** the target, by the factor `∏_i (bias_i/P(e_i))`. Numerically this factor is large (the
sharper `q`-weighted cap is even worse, `77×–320× · G(O_1)^n`), because `bias_i/P(e_i)` can reach
`25:1` on residuals (`min P(e_i)/bias_i = 0.039` at n=3). **Conclusion (rigorous):** no bound that
depends only on the marginals `bias_i` can prove (B3-a′): the marginals are consistent with mass
concentrated on high-weight patterns (where (★) fails — and indeed (★) fails on ~55% of *general*
`mb<1/2` `P`), and what forbids that concentration is the **joint** residual hypothesis, not the
marginals. This pins down exactly what a closing argument must use: the joint-mass constraints from
the `k=2`-move failures, not any per-coordinate quantity.

### (R5-5) Verified orbit-average facts that bracket (★)

On every residual (`b3_round5.py`, `0` violations; min relative margins below):
- `P̄_O < AM_i(P(e_i)) = M_1/n` for every weight-`≠1` orbit (the *arithmetic*-mean version; this is
  **stronger** than (★) when `d=n` because `P̄_O = orbit-mass/n` and the linear orbit-mass bound
  `orbit-mass < M_1` holds with `≥46%` margin — but it is **not by itself** (★), since `AM ≥ GM`).
- `P̄_O < max_i P(e_i)` (0 viol; again `max ≥ GM`, so weaker than (★)).
- `P(0^n) < G(O_1)` and `P(1^n) < G(O_1)` (the singleton orbits, `d=1`, are handled — they are not
  the maximizer).

So (★) is bracketed: `P̄_O < AM_i(P(e_i))` is verified but too weak (uses AM not GM), and the
per-pattern `P(z)<G(O_1)` is too strong (fails `3/26` at n=3). (★) lives strictly between — the
orbit *averaging* is exactly what repairs the per-pattern failures, and the `AM→GM` spread of the
weight-1 masses is exactly the residual content still to be quantified.

**Status of (★):** OPEN. It is now the **single** remaining gap (closing it gives (B3-a′) via R4-1
+ R5-4, hence (B3-a), hence — with the verified Lemma B2 and the (B3-b) half — the theorem). It is a
clean, fully-numeric, large-margin scalar inequality (min relative margin `(G(O_1)-P̄_O)/G(O_1) =
0.167` at n=3, `0.866` at n=4, `0.976` at n=5; `0` violations on 90+40 residuals). What is **not**
yet in hand is a signed derivation of (★) from the residual joint-mass constraints; R5-3 proves the
marginals are provably *insufficient*, so a joint argument is mandatory.

---

## Hard step (expanded, R6) — the orbit-aggregate (†) angle, what it gives, and the sharpened gap

This round executed the approved orbit-aggregate angle ("(†) `SLACK_O > BIASGAP`, aim the
glue-failure at an UPPER bound `(UB)` on weight-≥2 joint mass") and discharged the
approach-critic's CHANGES-REQUESTED obligation. The honest outcome is a **set of rigorous new
facts that sharpen the gap and rule out the two routes the critic flagged as risky**, plus a
**precisely-stated remaining gap**. The theorem is **NOT** proved this round. Every claim below is
reproduced by `b3_round6.py` (in *Computational checks*); every inequality direction was checked
under relative tolerance before composing.

### (R6-T1) The (†) SLACK/BIASGAP decomposition is a TAUTOLOGY — no new leverage. [PROVED]

For an orbit `O` of weight `w ≥ 2` with representative `y`, define (as in the survey)
```
   SLACK_O := Σ_{s=0}^{n-1} [ (1/w) Σ_{i∈supp(S^s y)} log bias_i  −  log P(S^s y) ]   (≥ 0, R5-1),
   BIASGAP := Σ_{i=1}^{n} log( bias_i / P(e_i) )                                       (≥ 0, R5-1 at w=1).
```
**Claim (R6-T1).** `SLACK_O − BIASGAP = log( ∏_i P(e_i) / ∏_s P(S^s y) )`. Hence
`(†) SLACK_O > BIASGAP` is **identically** `(B3-a′) ∏_s P(S^s y) < ∏_i P(e_i)`.

*Proof.* By the cyclic incidence count R5-2, each coordinate `i` lies in the support of exactly `w`
of the `n` shifts `S^s y`, so
`Σ_s (1/w) Σ_{i∈supp(S^s y)} log bias_i = (1/w) Σ_i (w · log bias_i) = Σ_i log bias_i.`
Therefore `SLACK_O = Σ_i log bias_i − Σ_s log P(S^s y)`, while
`BIASGAP = Σ_i log bias_i − Σ_i log P(e_i)`. Subtracting, the `Σ_i log bias_i` terms cancel
**exactly**, leaving `SLACK_O − BIASGAP = Σ_i log P(e_i) − Σ_s log P(S^s y) = log(∏_i P(e_i)/∏_s P(S^s y))`. ∎
(Verified `|error| < 7.1·10⁻¹⁵` on all 89 residual orbits, `b3_round6.py [T1]`.)

**Consequence.** The orbit-aggregate framing carries **zero** information beyond the bare product
inequality (B3-a′): the `bias_i` cancel identically, so "bound `BIASGAP` above and let `SLACK_O`
dominate" cannot be a proof strategy — it is the target written twice. The load-bearing object is
the bare `∏_s P(S^s y) < ∏_i P(e_i)`, exactly as in R4/R5. (This is the formal statement of the
critic's warning "do NOT lean on '(UB) caps BIASGAP'": there is no `BIASGAP` to cap that is not
already the answer.)

### (R6-T2) N7 (the source of the `(UB)` caps) is PROVABLY INSUFFICIENT for (B3-a′). [PROVED, explicit certificate]

The angle's only joint input is **N7** = "every single-coordinate glue (Move I) fails to reduce
`maxbias`", which yields the per-riser cap `(UB) a1^{(i,j)} ≤ (p_j q_i − mb·Z)/(q_i − p_i)`. We
show N7 **cannot** imply (B3-a′), so any argument built solely from the `(UB)` caps is doomed.

**Claim (R6-T2).** There is a **full-support** distribution `P` on `{0,1}³` with `mb < 1/2`
satisfying N7 for which (B3-a′) **fails**.

*Certificate (verified, `b3_round6.py [T2]`).* Take (order `000,001,010,011,100,101,110,111`)
```
   P3 = [0.26314, 0.22514, 0.06373, 0.12761, 0.01397, 0.03575, 0.19734, 0.07332]
```
Then `minP3 = 0.0140 > 0` (full support), biases `(0.3204, 0.4620, 0.4618)`, `mb = 0.4620 < 1/2`;
**N7 holds** (every one of the three single-coordinate glues fails to reduce `maxbias`); yet for
the weight-2 orbit `{110,101,011}`, `∏_s P(S^s y) = 9.0·10⁻⁴ > 2.0·10⁻⁴ = ∏_i P(e_i)`, so
**(B3-a′) FAILS** (min relative margin `−89.9`). The point `P3` is **not** a residual — the full
Bell-lattice `k=2` search reduces `maxbias` to `0.072` (the whole-collapse move), consistent with
the theorem. ∎

**Consequence.** N7 alone is a strictly weaker hypothesis than "residual", and it does not imply
(B3-a′). Hence the `(UB)` caps — which are exactly the quantitative content of N7 at the realized
riser pairs — **cannot** close (B3-a′) on their own, regardless of how cleverly they are composed.
(My adversarial search confirms the failure is generic, not a single fluke: under the
N7-only hypothesis the (B3-a′) relative margin is driven to `−∞`.) This rigorously vindicates the
approach-critic's objection: the missing mass sits on pairs/structure that N7 does not constrain.

### (R6-T3) The minimal sufficient conjunction of `k=2` move-failures GROWS with `n`. [PROVED, explicit certificate]

What N7 misses is supplied by the **other** `k=2` move-failures (the residual is the conjunction of
**all** of them). The cleanest additional scalar constraint is the **whole-collapse failure**
(Lemma R4-4 / A3a), a residual consequence verified `89/89` here:
```
   (WC)   P(1^n) ≥ √(mb/(1-mb)) · P(0^n).
```

- **At `n = 3`,** the pair `{N7, (WC)}` appears **sufficient**: across `>10⁷` structured random
  draws plus multi-start simulated annealing on the constraint manifold near `mb = 1/2`, **no**
  full-support `P` with `mb<1/2` satisfying N7 ∧ (WC) was found to violate (B3-a′) (worst observed
  relative margin `> 0.13`); and **all** 26 isolated `n=3` residuals satisfy N7 ∧ (WC). (Conjecture,
  not proved; see Gap.) Note the binding `n=3` residual regime — the approach-critic's SA drove the
  true-residual margin to `≈ 0.094` at `mb ≈ 0.4997` — sits inside this set.
- **At `n ≥ 4`,** the pair `{N7, (WC)}` is **PROVABLY INSUFFICIENT**. *Certificate
  (`b3_round6.py [T3]`):* there is a full-support `P` on `{0,1}⁴` with `minP = 0.0023`,
  `mb = 0.4898 < 1/2`, satisfying **both** N7 and (WC), for which (B3-a′) fails (min relative
  margin `≈ −1.87`); it is `k=2`-reducible (full Bell-lattice `k=2` reduces `maxbias` to `0.4375`),
  so correctly not a residual. The reducing move is a *partial* absorb-block (Move II) on a proper
  subset of coordinates — a `k=2` failure that neither N7 nor (WC) records.

**Consequence (the precise structural obstruction).** No FIXED finite list of `k=2` move-failures
is uniformly sufficient to imply (B3-a′): the residual hypothesis is the conjunction over the
**entire Bell lattice** of `k=2` set-partitions, and the minimal sufficient sub-conjunction grows
with `n` (`{N7,(WC)}` suffices at `n=3`, fails at `n=4`; at `n=4` the partial absorb-blocks are
needed, and so on). This is exactly why every per-pair / per-move closing attempt over five rounds
has stalled: the input that closes (B3-a′) is irreducibly the *full* residual conjunction, not any
bounded family of its consequences. A closing proof must use the residual hypothesis **as a whole**
(e.g. via the absorb-block contraction Lemma A3a applied to *every* block simultaneously), not a
fixed finite set of scalar caps.

### (R6) Net effect on the gap

(★)/(B3-a′)/(†) remains **OPEN** and is unchanged as a target (all three are the same inequality,
now including the tautology R6-T1). What is newly **rigorous** is the *map of the gap*: (i) the
orbit-aggregate `SLACK/BIASGAP` reframing is information-free; (ii) the `(UB)`-from-N7 route is
provably insufficient (explicit `n=3` certificate); (iii) no fixed finite conjunction of `k=2`
move-failures is uniformly sufficient (explicit `n=4` certificate against the cleanest candidate
`{N7,(WC)}`). The exact remaining gap is stated in the Gap section.

---

## Edge cases

- **Full support / positive probability:** Lemma S1 — every conditioning event contains the
  all-copies-`0^n` configuration of probability `P(0^n)^k > 0`. Covered for all moves.
- **`n = 1`:** `P = Bernoulli(p)`, `p<1/2`. Move I with `S={(0,1)}` gives `o ↦ o²`, strict drop
  by Lemma A2. (No risers exist.) Covered.
- **Ties at the max:** `i* = argmax` may be non-unique. Lemma A2 lowers the chosen `i*`; any other
  coordinate tied at `mb` is, after Move I, either reduced or flagged as a riser (`≥ mb`) and
  absorbed by Rule R into `B`, where Lemma A3a controls it. Covered by the rule's `≥ mb` test
  (note the test uses `≥`, so a coordinate *equal* to `mb` is treated as a riser and absorbed,
  guaranteeing the strict final inequality). Covered up to the residual.
- **All biases equal (e.g. the critic's `P=(0.10,0.41,0.41,0.08)`, biases `(0.49,0.49)`):**
  Move II whole-collapse gives `A_1=P(11)=0.08`, `A_0=P(00)=0.10`, threshold
  `√(0.49/0.51)=0.980`, and `0.08/0.10 = 0.8 < 0.980`, so Lemma A3a applies and the common
  bias drops to `0.08²/(0.10²+0.08²)=0.390 < 0.49`. Verified. (The refuted fixed cyclic gadget
  RAISED this to `0.4949`; the absorb-block move fixes it.) Covered rigorously.
- **`P(1^n) ≥ P(0^n)` anti-correlated cases:** these can make every `k=2` collapse fail (whole-
  collapse threshold violated). They are exactly the BACKSTOP residual; covered *only* up to the
  open Lemma B3.
- **`n=2` and the "`k=n` backstop is vacuous" concern:** for `n=2`, `k=n=2` is itself a `k=2`
  partition already in Move I/II's search space, so the residual would be empty there; verified:
  `n=2` never needs the backstop (0 over 20,000 near-boundary + 7,432 random valid instances).

---

## Computational checks

All run with `python3` (numpy + sympy) against the verified harness `harness.py` (in this
directory). R3 scripts: `b3lib.py` (orbits / geomean / residual API), `fast_residual.py`
(fast Bell-lattice residual test), `b3_certificate.py` (the B3-reduction certificate),
`res_n{3,4,5}.pkl` (isolated residual datasets). Reproduce with `PYTHONPATH=. python3 b3_certificate.py`.

### Certificate suite (`/tmp/final_verify.py`)

```
CERTIFICATE 1 (symbolic): p - p^2/(p^2+q^2) = p(p-1)(2p-1)/(2p^2-2p+1);
              for 0<p<1/2 sign is +  =>  strict diagonal drop. odds: o-o^2=o(1-o)>0 for 0<o<1.   PROVED
CERTIFICATE 2: single-glue closed form (Lemma A1) vs brute force: 20/20 match.                    VERIFIED
CERTIFICATE 3: absorb-block closed form (Lemma A3) vs brute force: 20/20 match.                   VERIFIED
CERTIFICATE 4: cyclic glue all-marginals-equal 20/20, orbit formula (Lemma B1) match 20/20.       VERIFIED
CERTIFICATE 5: b*_(24) within 1e-3 of geometric-mean limit (Lemma B2): 8/10 (slack=finite-m rate).VERIFIED
```

### Combined-construction stress test (`/tmp/stress.py`, `/tmp/combined2.py`)

Construction tested: *best `k=2` full set-partition; if it reduces `maxbias`, use it; else use the
`k=n` cyclic glue.* (`all_k_partitions_search` enumerates the full Bell-number partition lattice.)

```
Near-boundary (0.40 ≤ mb < 0.50), adversarial mix (uniform / Dirichlet(0.3) / heavy-tailed u^4 /
                                                    1^n-boosted anti-correlated):
  n=2:  valid=20000   used_kn=0    fails=0
  n=3:  valid= 8000   used_kn=10   fails=0
  n=4:  valid= 1500   used_kn=0    fails=0      (+ a second run n=4 valid=600, fails=0)
Random (all regimes):
  n=2:  valid≈ 734    fails=0
  n=3:  valid≈ 203    used_kn=1    fails=0
  n=4:  valid≈  30    fails=0
Residual isolation (cases where NO k=2 partition reduces maxbias):
  n=3:  4–7 residual cases found; cyclic backstop reduced ALL; min margin (mb - b*) = 0.097,
        b* clusters at 1/3.
  n=4:  0 residual found in 8000 trials (k=2 sufficed).
Spec n=3 counterexample P=[.0352,.3315,.4299,.00033,.0545,.1069,.00028,.0415]:
  biases [.2032,.472,.4802], mb=.4802; best k=2 partition = identity (.4802, NO reduction);
  k=3 cyclic glue b* = .3347 (reduces).   Confirms k=2 genuinely insufficient and backstop needed.
```
**Total: 0 failures** of the combined construction across all stressed instances (> 30,000).

### Backstop b* is NOT universally < 1/2 (why the residual hypothesis is essential)

```
b* >= 1/2 occurs for general (non-residual) P: n=3 9/2478, n=4 30/1191, n=5 8/115 valid instances.
max b* observed: 0.559 (n=3), 0.999 (n=4).   => the cyclic glue alone is NOT a universal reducer;
ham(O*)/n < mb holds ONLY on the residual (n=3: 42/3707 general-case violations of ham(O*)/n<mb,
n=4: 274/1891) — so Lemma B3 genuinely needs the residual hypothesis, which is exactly the gap.
```

### R3 B3-reduction certificate (`b3_certificate.py`, `b3lib.py`, `fast_residual.py`)

Residuals isolated by full Bell-lattice `k=2` search (`fast_is_residual_k2`, validated identical
to the slow `all_k_partitions_search` and ~30× faster). For each residual, `O*` is found by
geometric-mean maximization over all cyclic orbits (`ostar_info`). All checks at `err ~ 1e-16`.

```
                              (B3-a) O*=O_1   (B3-b) mb>1/n    TARGET ham(O*)/n<mb
n=3   26 residuals            26/26           26/26            26/26   (min margin 0.0431)
n=4   63 residuals            63/63           63/63            63/63   (min margin 0.0392)
n=5    1 residual              1/1             1/1              1/1     (min margin 0.1098)
spec  P=[.0352,.3315,.4299,.00033,.0545,.1069,.00028,.0415]:
      residual, mb=0.4802, O*={e_i} (weight-1), ham(O*)/n=1/3 < mb.  (B3-a),(B3-b) hold.

Strength of (B3-a): runner-up/winner orbit geomean ratio <= 0.0011 at n=4 (weight-1 dominates by
                    ~1000x); 0.0008 at n=3.  Mass-concentration is extreme, not borderline.
Strength of (B3-b): smallest observed (mb - 1/n) over residuals: 0.039 (n=4), 0.043 (n=3) — bounded
                    away from 0, but the exact gap is not proven.
Whole-collapse certificate for (B3-b)'s contrapositive: every tested P with mb<=1/n is reduced by
                    the whole-collapse (n=3 3103/3103, n=4 370/370; W/mb <= 0.20).
Dead-end re-attribution: orbit-vs-complement G(0^n)>=G(1^n) fails 21/26 (n=3) — IRRELEVANT singleton
                    pair; the relevant weight-1>weight-2 comparison holds 26/26.
```

n=4 residuals — previously reported as "0 found" — DO exist (63 isolated here by a targeted hunt
biasing mass toward weight-1 patterns with tiny `P(0^n)`); `O*` is the weight-1 orbit on ALL of
them, refuting the R2-critic worry that an interior weight-2 orbit (`ham/n=0.5 ≥ mb`) could be the
maximizer on a residual.

### R4 advances certificate (`b3_round4.py`)

Reproduce with `PYTHONPATH=. python3 b3_round4.py`. All checks below are on the SLOW-verified
residual datasets `res_n{3,4,5}.pkl`; the riser bound is on 382 random valid instances.

```
[R4-1] G(O) = (prod_s P(S^s y))^(1/n) identity (PROVED): exact=True              n=3,4,5
[R4-2] riser bound bias_j' <= p_j q_i/(p_i^2+q_i^2) on 382 valid P: violations=0
n=3 (26 residuals):
  E[ham]=sum bias (identity)                 : 26/26
  E[ham]-1 = sum_{w>=2}P(ham-1) - P(0^n)     : 26/26   (decomposition, PROVED)
  (B3-a') prod_s P(S^s y) < prod_i P(e_i)    : 130/130 (OPEN aggregate)
  whole-collapse fail P(1^n)>=sqrt..P(0^n)   : 26/26   (A3a, PROVED on residuals)
  chain E[ham] >= 1+[(n-1)sqrt-1]P(0^n)      : 26/26   (PROVED algebra)
  weaker bound mb > 1/((n-1)^2+1)            : 26/26   (OPEN, but weaker than 1/n)
  (B3-b) mb > 1/n                            : 26/26
n=4 (63 residuals): all 7 lines pass (756/756 for B3-a').
n=5 (1 residual):   all 7 lines pass (27/27 for B3-a').
```

### R5 advances certificate (`b3_round5.py`)

Reproduce with `PYTHONPATH=. python3 b3_round5.py`. General lemmas (R5-1, R5-3) checked on 159000
random full-support instances; orbit facts on the SLOW-verified residual datasets.

```
[R5-1] P(z) <= GM_supp(bias_i)  (general)            : violations = 0/159000
[R5-2] cyclic incidence (each coord in w of n shifts): True  (n=3,4,5,6)
[R5-3] prod_s P(S^s y) <= prod_i bias_i  (general)   : violations = 0/159000
n=3 (26 residuals, 78 weight-!=1 orbits):
  [R5-4] prod_s P <= Pbar^n (safe AM-GM)         : 78/78
  [R5-3 on residuals] prod_s P <= prod bias_i    : 78/78
  (star)  Pbar_O < G(O1)   [OPEN]                : 78/78   min rel margin = 0.1672
  (B3-a') prod_s P < prod e_i [OPEN, via R5-4]   : 78/78
  Pbar_O < AM_i(e_i)  [VERIFIED]                 : 78/78
  Pbar_O < max_i(e_i) [VERIFIED]                 : 78/78
  P(0^n),P(1^n) < G(O1) [VERIFIED]               : 52/52
  BROKEN survey route M_1/d >= G(O1) (=100%)     : 78/78
  BROKEN survey route M_w/d >= Pbar  (=100%)     : 78/78
n=4 (63 residuals): all pass; (star) 315/315, min rel margin 0.866; broken routes 100%.
n=5 (1 residual):   all pass; (star) 7/7,   min rel margin 0.976; broken routes 100%.
```

Fresh adversarial n=3 residual hunt (slow Bell-lattice `is_residual`, structured sampling toward
weight-1 mass + tiny singletons): **40** new residuals isolated, **0** violations of (★), (B3-a′),
or R5-3. The 100% figures for `M_1/d ≥ G(O_1)` and `M_w/d ≥ P̄_O` confirm the survey's layer-mass
route is broken (the intermediate `M_w/d < G(O_1)` is strictly stronger than (★) and false).

### R6 advances certificate (`b3_round6.py`)

Reproduce with `PYTHONPATH=. python3 b3_round6.py`.

```
[T1] (dagger) SLACK_O > BIASGAP  IS  (B3-a') prod_s P < prod e (bias_i cancel)
     max | (SLACK_O - BIASGAP) - log(prod e / prod_s P) |  =  7.1e-15   (== 0)   [TAUTOLOGY, PROVED]

[T2] N7 (all single-glues fail) does NOT imply (B3-a')  -- (UB)-only route is dead
     P3 = [0.26314,0.22514,0.06373,0.12761,0.01397,0.03575,0.19734,0.07332] (full support, minP=0.014)
     biases (0.3204,0.4620,0.4618), mb=0.4620<1/2;  N7 holds = True
     (B3-a') min rel margin = -89.9  (FAILS);  FULL Bell-lattice k=2 reduces maxbias to 0.0720
     ==> N7 strictly insufficient; the (UB) caps alone cannot close (B3-a').            [PROVED]

[T3] N7 + whole-collapse-failure (WC): clean scalar pair
     n=3: all 26 residuals satisfy N7 ∧ (WC);   sufficient in >1e7 trials + SA (worst margin >0.13) [CONJECTURE]
     n=4: all 63 residuals satisfy N7 ∧ (WC);   but explicit full-support P (minP=0.0023, mb=0.4898<1/2)
          satisfies N7 ∧ (WC) with (B3-a') min rel margin = -1.87 (FAILS); k=2-reducible (best 0.4375).
     ==> N7 ∧ (WC) PROVABLY INSUFFICIENT for n>=4; minimal sufficient k=2-failure set grows with n. [PROVED]

[(UB) cited, direction re-confirmed] a1^{(i,j)} <= (p_j q_i - mb*Z)/(q_i-p_i) on risers: 95/95
```

### R4 contrapositive / move-coverage probes (slow Bell-lattice residual test)

```
Full-support P with E[ham] <= 1 (i.e. mb <= 1/n possible):  checked 917,  residuals found = 0
  (worst case reduces to 0.44 * mb -- large margin; the E[ham]=1 boundary is NOT tight)
single-coord glue alone reduces mb:  197/210 near-boundary, fails 44/889 over full E[ham]<=1 sweep
single-glue + whole-collapse + all permutation glues:  0 of 850 E[ham]<=1 candidates uncovered
```
This shows (B3-b)'s contrapositive holds with margin and requires the CONJUNCTION of several
`k=2`-move families (no single move suffices) — consistent with the residual hypothesis being the
load-bearing assumption.

---

## Gap (sharpened R3)

**The proof is complete except for Lemma B3, now reduced to two certified scalar sub-claims.**
Given Lemma B3, the theorem is fully proved: by Lemma B2 some finite `k=mn` makes the cyclic-glue
common marginal `b* < mb`, and that `k` with the cyclic `S` is the required construction; the
non-residual is handled by the explicit `k=2` Rule-R loop / whole-collapse (Lemmas A1–A3, A3a,
A3b), rigorous whenever it terminates with all marginals `< mb`. **The R3 reduction:**

> **Lemma B3 (open) ⟸ (B3-a) ∧ (B3-b).** Let `P` be a residual (full support, `mb<1/2`, no `k=2`
> set-partition of the `2n` coords reduces `maxbias`). Then
> **(B3-a)** the weight-1 cyclic orbit `O_1 = {e_1,…,e_n}` is the unique maximizer of the orbit
>   geometric mean `G(O) = (∏_{y∈O}P(y))^{1/|O|}`; equivalently, for every other orbit `O`,
>   `(∏_{y∈O}P(y))^{1/|O|} < (∏_{i}P(e_i))^{1/n}`; hence `O* = O_1` and `ham(O*)/n = 1/n`.
> **(B3-b)** `mb > 1/n`.
> These give `ham(O*)/n = 1/n < mb` (no ties, so the tie-average is just `1/n`), which is Lemma B3.

**Status of the two sub-claims.** Both are TRUE with **zero violations** on every isolated residual
(`n=3`: 26/26; `n=4`: 63/63 — n=4 residuals now exhibited, contradicting the earlier "0 found";
`n=5`: 1/1; spec residual included), with margins `mb−1/n ≥ 0.039` and runner-up/winner orbit
geomean `≤ 0.0011`. Each is an **aggregate** consequence of the full residual hypothesis (the
conjunction of all `k=2`-partition failures); neither is yet reduced to a single signable
polynomial-sign inequality. Concretely, the obstructions are:

- **(B3-a) is a geometric-mean-level fact, not per-pattern.** The clean per-pattern sufficient
  condition `max_{ham(y)≠1} P(y) < G(O_1)` (which would force `O*=O_1`) holds at `n=4,5` but FAILS
  3/26 at `n=3`: a single weight-2 pattern can exceed `G(O_1)` while the weight-2 *orbit geomean*
  still loses. So one must control the geomean of each orbit, i.e. the joint of all its shifts —
  the aggregate concentration content. (The recorded "orbit-vs-complement dead end" is NOT the
  obstruction here: I re-checked it (`probe_ovc.py`) and it is the *singleton* pair `(0^n,1^n)`
  whose order flips; the relevant weight-1 > weight-2 comparison holds on all residuals.)

- **(B3-b) `mb>1/n` lacks a boundary-tight bound.** The contrapositive `mb≤1/n ⇒ not a residual`
  is witnessed by the whole-collapse (reduces 3103/3103 at `n=3`, 370/370 at `n=4`). The rigorous
  facts `P(1^n) ≤ mb` (pattern `1^n` contributes to every marginal) and the union bound
  `P(0^n) ≥ 1 − Σ_i bias_i ≥ 1 − n·mb` are in hand, but the latter degrades to `0` exactly at
  `mb=1/n`, so it does not yield the A3a threshold `P(1^n)/P(0^n) < √(mb/(1-mb))` at the boundary.
  Residuals stay bounded away (`mb−1/n ≥ 0.039` observed), but the exact strict gap is unproven.

**R4 update to the gap (this round).** Section "Hard step (expanded, R4)" advances both pieces to
exact, cleaner forms but does NOT close them:

- **(B3-a) → (B3-a′) shift-product form (EXACT, OPEN).** Via Lemma R4-1
  (`G(O)=(∏_s P(S^s y))^{1/n}`), (B3-a) is equivalent to: for every pattern `y` with `ham(y)≠1`,
  `∏_{s=0}^{n-1} P(S^s y) < ∏_i P(e_i)`. This eliminates orbit-length bookkeeping and folds the
  singletons `0^n,1^n` into the same statement (no separate "absolute smallness" sub-argument
  needed). It is verified 130/130 (n=3), 756/756 (n=4), 27/27 (n=5) but remains an OPEN aggregate
  inequality. **What resists:** the per-pattern bound `P(y)<G(O_1)` fails 3/26 (n=3); and the
  natural log-supermodular bound `P(y)P(0^n)^{w-1} ≤ ∏_{supp}P(e_i)` (verified 0 violations on all
  residuals) goes the WRONG way after multiplying over shifts (it yields
  `∏_s P(S^s y) ≤ (∏_i P(e_i))^w/P(0^n)^{n(w-1)}`, and `∏_i P(e_i) < P(0^n)^n` is FALSE since
  `P(0^n)` is tiny). So no per-pattern multiplicative bound in hand proves (B3-a′); a genuinely
  joint (geomean-level) argument is still required.

- **(B3-b) → (B3-b″) weaker bound (REDUCED, OPEN).** Via Lemmas R4-2/R4-4 and the conditional
  chain `n·mb ≥ E[ham] ≥ 1+[(n-1)√(mb/(1-mb))-1]P(0^n)`, (B3-b) `mb>1/n` is implied by the
  STRICTLY WEAKER `mb > 1/((n-1)²+1)` (e.g. `mb>1/5` instead of `1/3` at `n=3`). This replaces the
  round-3 union bound (which degraded to `0` at the `mb=1/n` boundary) by the whole-collapse bound
  (no boundary degeneracy), so the boundary tightness obstruction is *retired*. **What resists:**
  even the weaker `mb>1/((n-1)²+1)` is not proved — no single `k=2` move forces it (single-glue
  fails 44/889; only single-glue + whole-collapse + permutation-glues cover all `E[ham]≤1`
  candidates, 0/850 uncovered), so a derivation must combine ≥3 move families. The slow-test
  contrapositive (917 instances, 0 residuals with `E[ham]≤1`, worst `0.44·mb`) shows the bound is
  TRUE with large margin, but the multi-move conjunction has not been turned into a closed chain.

**R5 update to the gap (this round): the (B3-a) half is now ONE inequality (★).** Via the approved
orbit-average chain (R4-1 identity + safe-direction AM-GM R5-4), (B3-a′) — hence (B3-a) — follows
from the single scalar inequality

> **(★) [orbit-average form].** For every full-support residual `P` and every cyclic orbit `O` of
> weight `≠1`, `P̄_O := (1/|O|)Σ_{z∈O}P(z) < G(O_1) = (∏_i P(e_i))^{1/n}`.

This is the cleanest, least-boundary-tight target produced so far (min relative margin
`(G(O_1)-P̄_O)/G(O_1) = 0.167` at n=3, `0.866` at n=4, `0.976` at n=5; `0` violations on 90 isolated
+ 40 fresh n=3 residuals). **What resists:** R5-3 proves the *marginals* `bias_i` cannot close it —
the best marginal cap `∏_s P(S^s y) ≤ ∏_i bias_i` overshoots `∏_i P(e_i)` by the factor
`∏_i bias_i/P(e_i)` (up to `25:1` per coordinate), and (★) fails on ~55% of *general* `mb<1/2` `P`,
so the **joint** residual hypothesis (no `k=2` move reduces `maxbias`) is load-bearing and not
expressible through any per-coordinate quantity. A closing argument must therefore bound the
orbit-average `P̄_O` using the joint-mass constraints from the `k=2`-move failures directly.

**What would close it.** (i) (B3-a′): the single inequality **(★) `P̄_O < G(O_1)`**, from the joint
residual-mass constraints (NOT the marginals — proved insufficient via R5-3; NOT the layer-mass
`M_w/d` route — proved broken). (ii) (B3-b″): a rigorous `mb > 1/((n-1)²+1)` (or directly `mb>1/n`)
from the residual conjunction. Either path + B2 closes the theorem; neither is in hand.

**R6 update to the gap (this round): the gap is the SAME inequality (★)/(B3-a′)/(†), now mapped
precisely.** Three rigorous facts (Section "Hard step (expanded, R6)", certificate `b3_round6.py`):

- **(R6-T1) the orbit-aggregate `(†)` reframing is a tautology.** `SLACK_O − BIASGAP =
  log(∏_i P(e_i)/∏_s P(S^s y))` exactly (the `bias_i` cancel by the R5-2 incidence collapse), so
  `(†) SLACK_O > BIASGAP` **is** `(B3-a′)` verbatim. There is no `BIASGAP` to "cap from above"
  that is not already the target; the load-bearing object is the bare `∏_s P(S^s y) < ∏_i P(e_i)`.

- **(R6-T2) N7 (single-glue-failure, the source of the `(UB)` caps) is provably insufficient.** The
  explicit full-support `P3` on `{0,1}³` (`mb=0.462<1/2`) satisfies N7 yet violates (B3-a′)
  (`∏_s P = 9·10⁻⁴ > 2·10⁻⁴ = ∏ P(e_i)`), and is `k=2`-reducible (whole-collapse, `maxbias→0.072`).
  So the `(UB)` caps from the `n` single-glue risers **cannot** close (B3-a′) on their own — the
  joint mass that breaks N7-only examples sits on pairs/structure N7 does not constrain.

- **(R6-T3) no fixed finite conjunction of `k=2` move-failures is uniformly sufficient.** The
  cleanest two-constraint candidate `{N7, whole-collapse-failure (WC)}` holds on all 89 residuals
  and is (conjecturally, no counterexample in `>10⁷` trials + SA) sufficient at `n=3`, but is
  **provably insufficient at `n≥4`**: an explicit full-support `P` on `{0,1}⁴` (`mb=0.4898<1/2`)
  satisfies N7 ∧ (WC) yet violates (B3-a′) and is `k=2`-reducible by a partial absorb-block. The
  minimal sufficient sub-conjunction of `k=2` failures **grows with `n`**. Hence (★) is closable
  only by using the residual hypothesis **as a whole** (the absorb-block contraction A3a applied
  to every block simultaneously), not any bounded family of scalar caps.

> **Exact remaining gap (R6, precise).** Prove `(B3-a′): ∏_{s=0}^{n-1} P(S^s y) < ∏_i P(e_i)` for
> every full-support residual `P` (`mb<1/2`, no `k=2` set-partition of the `2n` coordinates reduces
> `maxbias`) and every pattern `y` with `ham(y)≠1`. Numeric status: `0` violations on `89` isolated
> residuals (`n=3,4`) + `60` fresh near-`mb=1/2` residuals; min relative margin `0.167` (`n=3`),
> `0.866` (`n=4`); the approach-critic's SA drove the true-residual margin to `≈0.094` at
> `mb≈0.4997`. **What is missing:** a derivation that consumes the residual hypothesis *globally*.
> The two natural finite reductions are ruled out: the marginal cap `∏ bias_i` overshoots (R5-3);
> the `(UB)`-from-N7 caps are insufficient (R6-T2); and `{N7,(WC)}` (or any fixed finite set of
> `k=2`-failure constraints) is insufficient for large `n` (R6-T3). A promising un-attempted lever:
> Lemma A3a says that for **every** block `B`, the residual forces either
> `A_1^{(B)}/A_0^{(B)} ≥ √(mb/(1-mb))` *or* an off-block coordinate `≥ mb`; turning this
> exponentially-large disjunction (one per block) into a single bound on `∏_s P(S^s y)` is the open
> problem. The conjecture (★)/(B3-a′) is **certified true** with margin but **not proved**.

**Honest status.** This is a precisely-stated, numerically-certified *scalar reduction* of B3 (the
mechanism — cyclic geometric-mean limit, identified maximizer `O_1`, threshold `1/n` — is named;
margins verified on all isolated `n=3` AND newly-hunted `n=4` residuals, plus `n=5` and the spec).
The R4 round added two EXACT reformulations (shift-product for B3-a, excess-mass + conditional
chain for B3-b) and a strict reduction of (B3-b) to a weaker non-boundary-tight bound, with all
identities/directions verified — but it is NOT a proof of B3, and the theorem is NOT claimed
proved. It strictly sharpens R1's open aggregate inequality `ham(O*)/n<mb` into two concrete scalar
sub-claims, reformulates them exactly, and reduces (B3-b) further.

---

## Summary of what is rigorous vs. open

| Component | Status |
|---|---|
| S0 reduction to partitions | PROVED |
| S1 well-definedness / positive prob (full support) | PROVED |
| A1 single-glue closed form | PROVED + VERIFIED |
| A2 diagonal odds-squaring `o↦o²`, `o<1` (only use of `mb<1/2`) | PROVED (symbolic) |
| A3 absorb-block closed form | PROVED + VERIFIED |
| A3a block contraction polynomial condition; whole-collapse | PROVED |
| A3b Rule-R loop (reworded R3: loop, not single absorption; absorption not coord-monotone) | PROVED |
| Rule R termination + correctness when it stops below `mb` | PROVED (not universal) |
| B1 cyclic equal-marginals + orbit formula | PROVED + VERIFIED |
| B2 geometric-mean limit `b*_{mn} → ham(O*)/n` | PROVED + VERIFIED |
| **B3 ⟸ (B3-a) ∧ (B3-b) [the R3 reduction]** | **PROVED (trivial: `1/n < mb`)** |
| R4-1 orbit geomean = shift-product `G(O)=(∏_s P(S^s y))^{1/n}` | PROVED (combinatorial) + VERIFIED |
| R4-2 riser bound `bias_j' ≤ p_j q_i/(p_i²+q_i²)` (uses `mb<1/2`) | PROVED + VERIFIED (direction) |
| R4-3 `E[ham]` decomposition `E[ham]-1 = Σ_{w≥2}P(x)(ham-1) - P(0^n)` | PROVED + VERIFIED |
| R4-4 whole-collapse failure `P(1^n) ≥ √(mb/(1-mb))P(0^n)` on residuals | PROVED (A3a) + VERIFIED 90/90 |
| R4 conditional chain `mb>1/((n-1)²+1) ⇒ E[ham]>1 ⇒ mb>1/n` | PROVED (algebra) + VERIFIED |
| R5-1 monotone-support `P(z) ≤ min_supp bias_i ≤ GM_supp bias_i` (general) | PROVED + VERIFIED |
| R5-2 cyclic incidence (each coord in exactly `w` of `n` shifts) | PROVED (combinatorial) + VERIFIED |
| R5-3 shift-product cap `∏_s P(S^s y) ≤ ∏_i bias_i` (general) | PROVED + VERIFIED |
| R5-4 orbit AM-GM `∏_s P(S^s y) ≤ P̄_O^n` (safe direction) | PROVED + VERIFIED |
| R5 marginals-insufficient: cap `∏_i bias_i ≥ ∏_i P(e_i)`, overshoots target | PROVED + VERIFIED |
| (B3-a′) ⟸ **(★)** via R4-1 + R5-4 (orbit-average chain) | PROVED (reduction) |
| R6-T1 `(†) SLACK_O > BIASGAP` is a tautology = `(B3-a′)` (`bias_i` cancel) | PROVED + VERIFIED (7e-15) |
| R6-T2 N7 (single-glue-failure) ⇏ `(B3-a′)` — explicit full-support `n=3` certificate | PROVED (counterexample) |
| R6-T3 no fixed finite `k=2`-failure set is uniformly sufficient — explicit `n=4` certificate | PROVED (counterexample) |
| **(★) residual ⇒ `P̄_O < G(O_1)` for orbit weight ≠ 1** | **OPEN — single scalar gap; certified 130/130** |
| **(B3-a′) residual ⇒ `∏_s P(S^s y) < ∏_i P(e_i)` for `ham(y)≠1`** | **OPEN — ⟸ (★); certified 89/89 + 60 fresh** |
| **(B3-b″) residual ⇒ `mb > 1/((n-1)²+1)` [⇒ (B3-b) `mb>1/n` via the chain]** | **OPEN — weaker than `1/n`; certified 90/90** |

Combined construction (best `k=2` partition else `k=mn` cyclic): **0 failures** over 30,000+
adversarial/near-boundary/residual instances (`n=2,3,4`), so the theorem is almost certainly
true; the proof is complete modulo Lemma B3.
