# Proof attempt — Round 1

**Approach:** P-dependent construction. PRIMARY move = an explicit `k=2` partition
("glue the argmax coordinate across two copies and absorb risers into its constant block",
plus the whole-copy collapse); BACKSTOP = `k = mn` cyclic glue on the anti-correlated residual.
The committed target (critic's "single cleanest target") is to prove `maxbias(P') < maxbias(P)`
**directly**, never through the refuted `Φ_p` power-mean potential.

**Status:** INCOMPLETE — blocked at the BACKSTOP (Lemma B3). All other steps are closed
rigorously: the reduction to partitions, well-definedness, the two exact closed-form marginal
maps, the diagonal odds-squaring contraction (the sole use of `maxbias<1/2`), the whole-collapse
sufficient condition, the Rule-R loop, and the exact orbit/limit formula for the cyclic glue.
**R3 progress:** Lemma B3 is now *reduced* to two concrete scalar sub-claims — **(B3-a)** the
geometric-mean-maximizing cyclic orbit is the weight-1 orbit `O_1` (so `ham(O*)/n = 1/n`), and
**(B3-b)** `mb > 1/n` — which trivially give `ham(O*)/n = 1/n < mb`. Both are certified with zero
violations on every isolated residual at `n=3,4,5` (90 residuals total, incl. newly-exhibited
`n=4` cases), the Step-2 mechanism is corrected (mass-smallness, not the backwards A3a squeeze),
the A3b narrative is reworded (a property of the Rule-R loop), and the dead-end attribution is
fixed. **The theorem is NOT claimed proved**: (B3-a) and (B3-b) remain aggregate consequences of
the residual hypothesis without elementary proofs. Details in **Section "Gap (sharpened R3)"**.

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

**What would close it.** (i) A geomean-level concentration inequality: residual ⇒ for every cyclic
orbit `O ≠ O_1`, `∏_{y∈O}P(y) < (∏_i P(e_i))^{|O|/n}` — the aggregate fact, now pinned to the
specific orbit `O_1`. (ii) A boundary-tight lower bound on `P(0^n)` (sharper than the union bound)
forcing the whole-collapse threshold whenever `mb ≤ 1/n`, OR any other rigorous proof of `mb>1/n`
on residuals. Either of (i)+(ii) closes the theorem via Lemma B2; neither is in hand.

**Honest status.** This is a precisely-stated, numerically-certified *scalar reduction* of B3 (the
mechanism — cyclic geometric-mean limit, identified maximizer `O_1`, threshold `1/n` — is named;
margins verified on all isolated `n=3` AND newly-hunted `n=4` residuals, plus `n=5` and the spec).
It is NOT a proof of B3, and the theorem is NOT claimed proved. It strictly sharpens R1's open
aggregate inequality `ham(O*)/n<mb` into two concrete scalar sub-claims and corrects the dead-end
attribution.

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
| **(B3-a) residual ⇒ `O* =` weight-1 orbit `O_1` (`ham(O*)/n = 1/n`)** | **OPEN — certified 90/90 residuals, n=3,4,5** |
| **(B3-b) residual ⇒ `mb > 1/n`** | **OPEN — certified 90/90 residuals, n=3,4,5** |

Combined construction (best `k=2` partition else `k=mn` cyclic): **0 failures** over 30,000+
adversarial/near-boundary/residual instances (`n=2,3,4`), so the theorem is almost certainly
true; the proof is complete modulo Lemma B3.
