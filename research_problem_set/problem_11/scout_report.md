# Scout Report — problem_11

## Problem: research_problem_set/problem_11
Classification: **novel / standalone** (uses standard boolean-analysis vocabulary, but the exact
statement is not a named theorem in the literature; no prior art found).

### Goal (restated precisely)
Let `P` be a **full-support** probability distribution on `{0,1}^n`. Define
`bias_i(P) = Pr_{x~P}(x_i = 1)` and `maxbias(P) = max_i bias_i(P)`. **Hypothesis:** `maxbias(P) < 1/2`.
Let `P^k` be the product of `k` independent copies of `P` (a distribution on `{0,1}^{nk}`, coords
`1..nk`). 

**Claim (existence / construction):** For every such `P` there exist an integer `k >= 1` and a set
of index pairs `S ⊆ {(u,v) : 1<=u,v<=nk}` such that, defining `P'` as `P^k` conditioned on the
event `{X_u = X_v for all (u,v) in S}`, we have `maxbias(P') < maxbias(P)` (strict).

Type of result: **existence + explicit construction**. We must exhibit `k` and `S` and prove strict
reduction. The problem asks to *prove the theorem is true*, not disprove it.

### Key structure (all numerically verified)

**1. Equality-`S` = forcing a partition to be constant.** Any pair set `S` induces an equivalence
relation on the `nk` coordinates (connected components of the graph with edges `S`). Conditioning on
`X_u = X_v ∀(u,v)∈S` is exactly conditioning `P^k` on "every component is constant." So the design
space is: choose `k`, then choose a **partition of the `nk` coordinates** (groups may mix coordinates
*and* copies), and condition each group to a common value. This reframing is the cleanest way to think
about `S`.

**2. The base mechanism (odds-squaring), n=1.** For `P = Bernoulli(p)`, `p<1/2`, take `k=2` and
`S={(1,2)}` (equate the two iid bits). Then
`bias(P') = p^2/(p^2+(1-p)^2)`. In odds `o = p/(1-p)`, this maps `o -> o^2`. Since `p<1/2 ⇒ o<1 ⇒
o^2 < o`, bias strictly drops. Verified for `p∈{.1,.2,.3,.4,.45,.49,.499}`: always `f(p) < p`.

**3. Multivariate: the cross-copy same-coordinate move.** Take `k=2`; equate coordinate `i` across the
two copies: `S = {(i, i+n)}`. The two copies are independent, so the closed form for the resulting
marginals (both copies identical by symmetry; verified against brute force to 1e-9) is, with
`p_i = bias_i`, `q_i = 1-p_i`, `Z = p_i^2 + q_i^2`:
```
bias_i(P')  = p_i^2 / Z                                       (< p_i, always)
bias_j(P')  = [ P(X_j=1,X_i=1)·p_i + P(X_j=1,X_i=0)·q_i ] / Z   (j ≠ i)
```
The diagonal term `bias_i` always drops. **But** `bias_j` for a *correlated* coordinate `j` can RISE:
if `X_j` is negatively correlated with `X_i`, the mass `P(X_j=1,X_i=0)` is reweighted by the larger
factor `q_i > p_i`, pushing `bias_j` up — possibly above the old `maxbias`. This is the central
obstruction.

**4. What FAILS (do not propose as the universal construction):**
   - **"Equate every coordinate across both copies" (P'(x) ∝ P(x)^2 per copy, i.e. force the two
     whole copies equal).** FAILS: raises max bias on anti-correlated `P`. ~37% of random `n=2`
     trials are counterexamples. Example: `P(00)=.109,P(01)=.449,P(10)=.428,P(11)=.014`,
     `max .463 -> .508`.
   - **"Equate only the argmax coordinate across two copies" (single move).** FAILS ~9% of the time
     (the diagonal drops but a negatively-correlated coordinate rises above the old max). Verified.
   - **"Best single cross-copy same-coord move over all i."** Still FAILS ~5% of the time, on
     XOR-like / strongly anti-correlated `P` (e.g. `P(00)=.256,P(01)=.369,P(10)=.372,P(11)=.003`,
     biases `[.375,.372]`: no single coordinate-equate beats `.375`).
   - **"Force all coordinates of one copy equal" (support {0^n,1^n}, bias = P(1^n)/(P(0^n)+P(1^n))).**
     FAILS ~1.7% of the time — `maxbias<1/2` does NOT imply `P(1^n)<P(0^n)`. Found 699/~60000 random
     samples with `maxbias<1/2` yet `P(1^n) >= P(0^n)`, so the "all-equal, large k" limit need not go
     to 0.

**5. What WINS on the hard cases.** For the XOR-like example above, exhaustive search found `k=2`,
`S = {(0,1),(0,2),(0,3)}` (all four coords of both copies in one group ⇒ force the whole 4-tuple
constant) drops max bias to `≈0.00014 = P(11)^2/(P(00)^2+P(11)^2)`. Mechanism: forcing many
coordinates equal concentrates mass on the *rare* all-equal patterns; for an anti-correlated `P` the
all-ones pattern is the rarest, killing every bias.

**6. Existence always holds (strong numerical evidence the theorem is TRUE).** Exhaustive search over
`k<=3` and `|S|<=3` (i.e. all partitions reachable with up to 3 equality constraints):
   - `n=2`: 3000/3000 random `P` had a reducing `S`.
   - `n∈{2,3}`: 747/747 random `P` (incl. heavy-tailed weight sampling to stress corners) had a
     reducing `S`. Zero failures.
No counterexample to the theorem was found. **Triage = none: proceed (theorem appears true).**

### Triage
**None — proceed.** The statement is well-posed (full support guarantees all conditioning events have
positive probability; `maxbias<1/2` is the key hypothesis). No counterexample found in extensive
search; the theorem is almost certainly true. Not equivalent to any famous open problem; no exact
prior-art match (it is self-contained boolean analysis). The hypothesis `maxbias < 1/2` is *used*: it
is exactly what makes every per-coordinate odds `< 1`.

### Hard step
**The one claim a proof must establish:** that *some* equality-partition reduces the global max
**without any coordinate's bias being pushed above the old `maxbias`**. The base odds-squaring
mechanism handles the target coordinate trivially; the entire difficulty is **controlling the
"risers"** — coordinates negatively/weakly correlated with the equated one whose bias can increase.
A correct proof must either (a) exhibit a partition where a global potential strictly decreases, or
(b) argue by extremality/compactness that the worst-case `P` over the closed feasible set still admits
a reducing `S`. Naming the precise mechanism that simultaneously drops the max and bounds all risers
below `maxbias` is the crux the approach-surveyor must address.

### Angles to try (ranked)

**Angle 1 — Potential / monotone-functional on the simplex (most promising).**
Mechanism: define a potential (candidate: `Φ(P) = max_i bias_i`, or a smoothed soft-max, or the
log-odds `max_i log(p_i/(1-p_i))`) and show that *some* equality-partition strictly decreases it.
Key lemma: for the argmax coordinate `i*`, there is a choice of partition (possibly grouping `i*`
across copies *together with* the coordinates that would otherwise rise) whose resulting biases are
all `< maxbias`. Why it might work: the closed-form marginal map in structure-point 3 is explicit and
quadratic in `P`; one can analyze the sign of `bias_j(P') - maxbias`. The hypothesis `o_{i*} < 1`
(odds-squaring contraction on the diagonal) is the lever.

**Angle 2 — Two complementary moves + a dichotomy (concrete, constructive).**
Mechanism: prove that *at least one* of these always works: (i) cross-copy same-coordinate equate
(structure pt. 3) when the argmax coordinate has no strong negative-correlation riser; (ii) a "force a
constant block" partition (structure pt. 5) when correlations are adversarial. Key lemma: a clean
dichotomy on the correlation pattern of the argmax coordinate deciding which move to use. Hard step:
showing the two cases exhaust all `P` with `maxbias<1/2` and that in case (ii) the resulting bias
`P(1^|block|...)/(...)` is `< maxbias` — needs the right block and possibly `k>2`.
Why it might work: numerics show these two mechanisms cover all observed cases.

**Angle 3 — Reduce to the single-coordinate (n=1) statement via marginalization.**
Mechanism: the marginal of any single coordinate `i` under `P` is `Bernoulli(bias_i)` with `bias_i<1/2`.
Try to construct `S` acting only "within the argmax coordinate's copies" so that, projected to that
coordinate, it reproduces the proven `o->o^2` drop, and prove the *other* coordinates' biases are
governed by a convex combination that cannot exceed the argmax. Key lemma: the riser bound
`bias_j(P') <= max(bias_j, bias_i)`-type inequality (FALSE as stated per pt. 3, so this needs the
correct corrected inequality). Hard step: finding the true riser bound. Lower priority — the naive
version is already numerically refuted, but a corrected version may be the cleanest route.

**Angle 4 — Extremal / compactness existence (non-constructive fallback).**
Mechanism: the set `{P : maxbias(P) <= 1/2 - ε}` is compact; for each `P` define
`g(P) = min over (k,S) of maxbias(P')`. If one shows `g(P) < maxbias(P)` fails only on a set that is
empty by a limiting argument, existence follows. Hard step: proving `g` is well-behaved and the
infimum is attained strictly below. Weakest, because the problem explicitly asks to "detail the
construction of k and S" — a non-constructive proof may not satisfy the deliverable.

### Computational levers available to later rounds
- The closed-form marginal map (structure pt. 3) is exact and cheap — use it to test any proposed
  riser bound symbolically for `n=2,3`.
- Brute-force partition search (`product`/`cond` helpers, verified in this round) confirms or refutes
  any "single universal construction" claim in seconds for `n<=3`, `k<=3`.
- To stress-test a candidate proof: sample anti-correlated/XOR-like `P` (mass on `01`,`10`) — these
  are the adversarial cases where naive moves fail.

### Dead ends (do not retry)
- `P(x)^2` "equate-both-whole-copies" construction — raises max bias (counterexamples found).
- "Equate the argmax coordinate across two copies" as a *universal* single move — fails ~9%.
- "Best single cross-copy same-coord move" as universal — fails ~5% (XOR-like P).
- "Force one whole copy constant / all-equal large-k" as universal — fails when `P(1^n) >= P(0^n)`,
  which is compatible with `maxbias<1/2`.

### Literature digests saved
None — classified novel/standalone; no matching prior art. Search returned only loosely related
boolean-analysis work (p-biased Fourier analysis, noise/bias amplification of nonlocal boxes, subcube
conditioning for distribution testing), none stating this theorem.
