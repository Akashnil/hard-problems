# Spec — problem_11 (CORRECTED, post-RETHINK)

Spec review: required

## 0. What changed vs. the refuted Angle 1

The previous #1 angle (full-cycle "symmetrize" gadget) was refuted: a single fixed-form
gadget is provably NOT uniform (full-cycle k=n glue overshoots ~0.6% of n=3 cases near the
1/2 boundary; verified here, 23/3753). The critic's redirect ("k=2 collapses the whole
problem") is ALSO too optimistic: **k=2 is genuinely insufficient** — there exist valid P for
which NO k=2 partition (full design space) reduces maxbias. Verified counterexample (n=3):

```
P = [0.0352, 0.3315, 0.4299, 0.00033, 0.0545, 0.1069, 0.00028, 0.0415]  (order 000..111)
biases = [0.2031, 0.4720, 0.4801], maxbias = 0.4801, P(111)>=P(000).
best over ALL 203 k=2 partitions: maxbias stays 0.4801 (no reduction).
best k=3 cyclic glue: maxbias -> 0.3347 (reduction).
```

So the deliverable is a **P-dependent construction** (fully legitimate: the theorem is
existential, "there exist k and S"). It is built from ONE uniform *mechanism* — a monotone
potential that is strictly decreasable by a free-choice move — not a case tree. k is chosen
as a function of P (almost always k=2; a measure-tiny anti-correlated residual needs k=3).

All numbers below are from exact brute-force over copies (union-find on the pair graph,
itertools.product over the k copies); closed forms cross-checked to 1e-9.

---

## 1. Construction of k and S (P-dependent, from an explicit family)

Coordinate layout: copy `c` (0-indexed), coordinate `i`, maps to global index `c*n + i`.
Conditioning on `S` = force each connected component of the graph `([nk], S)` constant.

**Primary move (k=2, free partition choice).** Among all set-partitions of the `2n`
coordinates of two i.i.d. copies, choose the partition `Π*` minimizing the **mean-odds
potential** (Sec. 2). Let `S` chain each block of `Π*`. For all but a measure-tiny set of P
this already gives `maxbias(P') < maxbias(P)` (empirically ~99.76% of valid P at n=3).

**Backstop move (k=3 cyclic glue), used only when no k=2 partition reduces maxbias.**
Take `k = n` copies and the full-cycle permutation `σ(i) = (i+1) mod n`; glue
`(c, i) ~ (c+1 mod k, σ(i))` for all c, i. Equivalently: force each copy to be a cyclic
shift of copy 0. This concentrates mass on cyclic-shift orbits (Sec. 3) and was verified to
fix **every** k=2-failure found (47 such cases across two independent searches; result
always the orbit density, e.g. exactly 1/3 for n=3).

The construction is "search the family, take the minimizer" — existence is what the theorem
asks for. The single mechanism unifying both moves is the **monotone mean-odds potential**:
the primary move is "the k=2 partition that drives the potential down," the backstop is "the
k=3 glue that drives it down when k=2 cannot lower the max."

---

## 2. The potential and the central lemma to discharge

Work in **odds coordinates**: for a distribution Q on `{0,1}^m`, let `o_j(Q) = b_j/(1-b_j)`
where `b_j = Pr_Q(X_j=1)`. The hypothesis `maxbias(P) < 1/2` is used in EXACTLY one place:
it says every original odds `o_i(P) < 1`.

Define, for a parameter `p >= 1`, the **mean-odds potential**

```
        Φ_p(Q) = ( 1/m · Σ_{j=1}^{m} o_j(Q)^p )^{1/p}        (power mean of the odds).
```

Φ_1 = arithmetic mean of odds; Φ_∞ = max odds = the maxbias in odds form (strictly
increasing in maxbias, so `Φ_∞` decreasing ⟺ maxbias decreasing).

**CENTRAL LEMMA (the one obligation).**
> Let P be full-support on `{0,1}^n` with `maxbias(P) < 1/2`. Then there is a k=2 partition
> Π of the 2n coordinates such that the conditioned distribution P' satisfies, for p ∈ {1,2},
> `Φ_p(P') < Φ_p(P)` strictly.   [Φ_p(P) computed on the n marginals of P; Φ_p(P') on the 2n
> marginals of P', which include both copies.]

**Measured failure rate of the lemma: 0.** Best-k2 strictly decreases Φ_1 and Φ_2 in
**0 / 51,200** valid stressed instances (n=2: 20000 each p; n=3: 5000 each p; n=4: 1200, p=2),
sampling uniform + low-α Dirichlet + heavy-tailed (anti-correlated) + near-boundary P.
For comparison Φ_∞ (= maxbias directly) fails ~0.24% at k=2 — those are exactly the cases
that the k=3 backstop resolves. So the potential is genuinely monotone-decreasable at k=2;
maxbias itself is not, and that gap is the whole reason the backstop exists.

**Why the proof needs the bridge from Φ to maxbias.** Φ_p decreasing does not by itself lower
the max. Two rigorous routes, in order of preference:

- **Route A (recommended, finite-p + escalation).** Prove the Central Lemma for a fixed
  large-but-finite p (numerics: p up to 4 still 0-failure at n=3; p=8 starts to fail ~0.07%).
  For p large, `Φ_p` is within a factor `m^{1/p}` of the max, so a strict multiplicative drop
  in `Φ_p` forces the max strictly below `maxbias(P)` once `p > log(2n)/log(1/(1-gap))` — make
  this quantitative using the odds-squaring gap of Sec. 4. Where even this leaves a residual
  (P with max-odds nearly equal across coordinates AND anti-correlated), invoke the k=3
  backstop, whose output is the orbit density (Sec. 3), provably `< 1/2`.

- **Route B (cleanest if it closes).** Strengthen the Central Lemma to `p = ∞` *with k allowed
  to be 2 or 3*: "there is a k∈{2,3} partition with maxbias(P') < maxbias(P)." This is the
  combined construction; measured failure rate 0 (Sec. 5). It avoids the Φ-to-max bridge
  entirely but requires proving the k=3 orbit bound (Sec. 3) in the residual k=2-fails case.

---

## 3. The k=3 backstop: exact orbit-density mechanism (proven formula)

For the full-cycle glue (k=n, σ = +1 shift), let `Sx = (x_{σ^{-1}(1)},...)` be the cyclic
coordinate shift. The feasible configurations are exactly the orbit tuples
`(x, Sx, S²x, …, S^{n-1}x)`, with weight `w(x) = Π_{c=0}^{n-1} P(S^c x)`. By the cyclic
relabeling symmetry every marginal equals the SAME value, and (verified exactly to 1e-9):

```
        b* = ( Σ_x w(x) · ham(x)/n ) / ( Σ_x w(x) ),
```

a `w`-weighted average of the normalized Hamming weights `ham(x)/n`. **Mechanism for why this
beats maxbias on the hard (anti-correlated) cases:** when P is anti-correlated (the regime
where k=2 fails, which forces `P(1^n) >= P(0^n)` to be possible), the product weight
`w(x) = Π_c P(S^c x)` is maximized by patterns that are *invariant-ish and low-weight*; the
mass concentrates on the orbit of a low-Hamming-weight pattern (for n=3 the weight-1 orbit
{100,010,001}), giving `b* ≈ ham/n < 1/2`. Verified: every k2-failure collapsed to b* ≈ 1/3.

**Obligation in Route B:** show that whenever no k=2 partition reduces maxbias, the dominant
orbit of the k=3 (more generally k=n) glue has representative Hamming weight `< n/2`, so
`b* < 1/2 <= ... `. Heuristic: k=2 failure ⟺ strong anti-correlation ⟺ joint mass sits on
low-weight patterns ⟺ dominant orbit is low-weight. The proof-builder must turn this chain
into an inequality (candidate: the k=2-fail condition implies `Σ_{ham(x)<n/2} w(x) >
Σ_{ham(x)>=n/2} w(x)` for the cyclic-product weights).

---

## 4. The genuine crux inequality (odds-squaring beats the riser), made precise

This is the single inequality every viable route shares. For the **same-coordinate k=2 cross
glue on coordinate i** (`S={(i, i+n)}`), the closed form (verified vs brute force, Sec. 5
harness `glue_marginals`) with `p_i=bias_i, q_i=1-p_i, Z=p_i²+q_i²` is:

```
 diagonal:  o_i  ↦  o_i²            (since bias_i ↦ p_i²/Z;  o_i<1 ⇒ strict decrease o_i-o_i²=o_i(1-o_i)>0)
 riser j:   bias_j(P') = [P(X_j=1,X_i=1)·p_i + P(X_j=1,X_i=0)·q_i]/Z   (a CONDITIONAL, no 1/2 cap)
```

The diagonal contracts by the multiplicative gain `o_i < 1` (the ONLY use of maxbias<1/2).
The riser j can rise (when j is anti-correlated with i, the `q_i > p_i` factor reweights the
`X_i=0` mass up). **The crux is that for the mean-odds potential Φ_p, the diagonal drop
`o_i^p - o_i^{2p}` plus the freedom to choose which coordinates to group dominates the sum of
riser increases.** Concretely, the proof-builder must show: for the best k=2 partition the
total change `Σ_j (o_j(P')^p − o_j(P)^p) < 0`. The free coordinate/partition choice is what
makes this hold — a SINGLE forced coordinate fails (measured: best single same-coord glue
fails Φ_1 14/25068 at n=3), but minimizing over partitions never failed (0/51200).

**Mechanism sketch for the partition freedom:** if forcing coordinate i alone overshoots
because of one anti-correlated riser j, the partition is free to ALSO group j with its own
cross-copy mate (driving `o_j ↦ o_j²` on the diagonal too) or to place i,j in the same block
(forcing them jointly constant, which kills the conditional reweighting). The minimizer over
the 2n-coordinate partition lattice always finds a configuration whose net Φ_p change is
negative. Making "always finds" into a constructive existence proof is the load-bearing work;
the power-mean (p=2) is recommended because `o_j(P')^2` is a quadratic form in the joint
masses and the net change is an explicitly signable polynomial.

---

## 5. Numerical verification (failure rates; all by exact brute force)

Harness: `glue_marginals` (closed form, matched to brute force, 5/5 exact); `cond_marginals_general`
(union-find + product over k copies); `all_k_partitions_search` (Bell-number enumeration of full
partitions). Sampling modes: uniform, Dirichlet(α=0.3), heavy-tailed `u^4` (anti-correlated),
boundary-targeted; only instances with maxbias<1/2 counted.

| claim tested | n | trials (valid) | failures | rate |
|---|---|---|---|---|
| **Central Lemma**: best-k2 decreases Φ_1 | 2 | 20000 | **0** | 0.000% |
| **Central Lemma**: best-k2 decreases Φ_2 | 2,3,4 | 20000+5000+1200 | **0** | 0.000% |
| Φ_4 best-k2 decrease | 3 | 1500 | 0 | 0.000% |
| Φ_8 best-k2 decrease (degrades→max) | 3 | 1500 | 1 | 0.067% |
| best-k2 decreases maxbias (=Φ_∞) | 3 | 2500 | 6 | 0.240% |
| **Route B**: best-k2-partition OR k≤3 cyclic-perm reduces maxbias | 2,3 | 4000+2500 | **0** | 0.000% |
| every no-k2-fix case fixed by full k=3 | 3 | 47 collected | **0** | 0.000% |

Adversarial / critic cases handled:
- **P=(0.10,0.41,0.41,0.08), biases (0.49,0.49):** best k=2 partition `S={(0,1),(0,2),(0,3)}`
  → maxbias 0.49 → **0.390** (reduces). (The refuted full-cycle gadget RAISED it to 0.4949;
  the free k=2 partition choice fixes it.)
- **P(1^n) >= P(0^n) anti-correlated cases (n=3):** these are exactly where some need k=3;
  e.g. b=[0.2031,0.472,0.480] no-k2-fix → k=3 cyclic glue → 0.335. All 47 collected such
  cases reduced under the backstop.
- **Near-boundary (maxbias→1/2):** covered by the combined construction (0 failures);
  the fixed full-cycle gadget fails here (0.6%), which is why the construction is P-dependent.

**Bottom line failure rate of the proposed construction (combined k≤3, Route B): 0** across
all 6,500+ stressed instances; central potential lemma (k=2, Φ_p): **0 / 51,200**.

---

## 6. What the proof-builder must deliver

1. Prove the **Central Lemma** (Sec. 2): best-k2 partition strictly decreases Φ_p (target
   p=2; the net Φ_2 change is a signable polynomial in the joint masses — Sec. 4 crux).
2. Bridge to maxbias by **Route A** (finite-p approximation of the max + the odds-squaring
   multiplicative gap to make the drop beat the `(2n)^{1/p}` slack) OR **Route B** (prove the
   k=3 orbit-density bound `b* < 1/2` in the k2-fails/anti-correlated residual, Sec. 3).
3. Edge cases to cover explicitly: full support (all conditioning events have positive prob —
   given); n=1 (reduces to plain odds-squaring o↦o², strict since o<1); ties at the max
   (handled — the move lowers a max-attaining coordinate and the potential is symmetric in
   coordinates); biases all equal (the (0.49,0.49) case shows the free partition still works).

Recommended order: attempt Route B first (it matches the theorem's `p=∞` target directly and
its two ingredients — Central Lemma intuition for k=2 + orbit bound for k=3 — are both
0-failure verified). Fall back to Route A's quantitative Φ_p argument if the k=3 orbit-density
inequality resists.

## 7. Reusable code

The verified harness lives at `/tmp/harness.py` (functions `glue_marginals`,
`cond_marginals_general`, `all_k_partitions_search`, `biases`, `maxbias`, `odds_sum`). The
proof-builder can re-run any candidate inequality symbolically/numerically in seconds for
n≤3, k≤3.
