## research_problem_set/problem_11
Spec review: required

### Orientation (what the survey verified numerically before ranking)

The conditioning event "X_u = X_v for all (u,v) in S" is exactly: form the graph with edge set S on
the nk coordinates, take its connected components, and force each component constant. So the design
space is { choose k, choose a partition of the nk coords (groups may mix coordinates AND copies),
condition every group constant }.

Core obstruction (re-confirmed, and now pinned to a mechanism): gluing coordinate i toward its
minority value reweights a coordinate j by the factor on the value it co-occurs with. The resulting
bias_j is a CONDITIONAL probability P(X_j=1 | X_i = forced-value)-type quantity, and conditional
probabilities have NO 1/2 upper bound. The hypothesis maxbias<1/2 controls only the MARGINALS, never
the conditionals — that is precisely why every "riser" can blow past the old max.

What the survey TESTED and the results (all by exact brute force over copies; n in {2,3}; random +
anti-correlated/XOR-like P; only valid instances with maxbias<1/2 counted):
- "equate each coordinate across k copies (n separate groups)" is ALGEBRAICALLY IDENTICAL to "force
  all k copies equal" = P(x)^k (agreeing on every coordinate <=> identical). Both fail ~5%; the limit
  concentrates on the modal element, whose 1-bits give bias 1.
- "best single same-coordinate cross-copy pair" fails ~5% (matches scout).
- "force the all-equal block {0^n,1^n} then odds-square via k copies": bias = P(1^n)^k/(P(0^n)^k+P(1^n)^k);
  wins iff P(1^n)<P(0^n); fails otherwise (matches scout dead-end #4).
- DICHOTOMY "single-pair OR (P(1^n)<P(0^n))": covers 40000/40000 for n=2 but FAILS 10/20000 for n=3
  (the block {0^n,1^n} is the wrong block when intermediate-weight patterns carry the mass).
- NEW family found: CROSS-COORDINATE / PERMUTATION gluing — glue coordinate i of copy c to coordinate
  sigma(i) of copy c+1. The hardest scout-style case (mb .4031) was rescued ONLY by the cyclic-shift
  glue [[(0,1),(1,2),(2,0)],[(0,2),(1,0),(2,1)],[(0,0),(1,1),(2,2)]] at k=3, dropping mb to .334.
- CYCLIC-PERM-GLUE over k in {2,3}, all sigma: fails only 2/20000; over k<=5 the 2 stubborn cases
  (mb .49, .499 — near the 1/2 boundary) still fail. Rich but NOT uniform.
- FULL-CYCLE SYMMETRIZE (sigma = full n-cycle, k=n): forces ALL coordinate marginals EQUAL (by the
  cyclic relabeling symmetry); fails only 4/3000, growing k cuts that to 3/3000. The common value is a
  reweighted average (NOT the plain mean), which can sit just above maxbias — the only failure mode.
- EXISTENCE confirmed: every stubborn case admits a winner under a general (mixed group-size,
  P-dependent) k=3 partition. No counterexample to the theorem in any test. The theorem is TRUE.

Conclusion forcing the ranking: there is NO fixed-form gadget that is uniform. A correct proof must
either (i) be structural/limiting (prove SOME partition in a rich parametric family works, via a
potential or extremal/compactness argument), or (ii) allow a P-dependent partition justified by a
case-free invariant. The user wants ONE elegant uniform construction; the closest to that is the
symmetrization family, which needs a small extra argument to handle the equalized-but-still-high case.

---

Angle 1 (top pick) — Symmetrize-then-contract via a cyclic / averaging glue, with a potential argument.
  Proves: the full theorem. Construction (uniform in form, k chosen as a function of P):
    Use k copies arranged in a directed cycle and a permutation sigma of {1..n}; glue (c,i)~(c+1 mod k, sigma(i)).
    The simplest instance: sigma = full n-cycle, k = n, which makes every coordinate's marginal EQUAL
    (the partition is invariant under the simultaneous "shift copy index / apply sigma to coords"
    relabeling, so all nk coordinates are in symmetric position => one common bias value b*).
  Skeleton:
    1. The symmetrizing glue equalizes all marginals to a single value b* — by the relabeling symmetry
       of the partition (every coordinate lies in a structurally identical orbit).
    2. Write b* explicitly: b* = E_{x^(0),...,x^(k-1) ~ P, constrained}[ X^(0)_1 ] = (sum over constrained
       tuples of P-product weighted by the coordinate) / Z. This is a ratio of degree-k polynomials in P.
    3. Show b* < maxbias(P). Two regimes:
       (a) biases not all equal: symmetrization replaces the max by an average-like quantity strictly
           below the max — needs the reweighting to not overshoot (the load-bearing inequality).
       (b) biases all (near) equal / regime (a) overshoots: fall back to ALSO contracting — combine the
           cyclic glue with an additional odds-squaring layer (take k a larger multiple, or compose the
           symmetrize map with the n=1 odds-squaring on the equalized coordinate), driving b* strictly down.
  Hard step: b* < maxbias(P) for the chosen (k, sigma) — because the symmetrized value is a weighted
    average of conditional one-coordinate biases whose weights are the constrained P-product mass; the
    mechanism that must be proven is that this reweighted average is dominated by maxbias UNLESS all
    coordinates are already symmetric, in which case the SAME glue with one extra cyclic layer applies an
    o -> (contraction)<o map (the n=1 lever o<1 from maxbias<1/2) to the common coordinate. The proof
    needs a monotone potential Phi (candidate: log of the largest coordinate odds, or the soft-max of
    biases) shown to strictly decrease under the symmetrize-and-contract step.
  Check: (i) derive b* as the explicit polynomial ratio for general sigma=full-cycle, k=n; (ii) prove the
    averaging inequality b* <= maxbias with equality iff all biases equal and all relevant conditionals
    coincide; (iii) in the equality case, exhibit the extra contraction step and prove strict drop using
    o_common < 1; (iv) re-run the exact brute force on the ~4/3000 symmetrization-overshoot cases to
    confirm the composed map fixes them. Must also handle: full support (all Z>0, guaranteed), n=1
    (reduces to plain odds-squaring), and biases tied at the max.

Angle 2 — Induction on n by gluing out the argmax coordinate.
  Proves: the full theorem, by reducing an n-coordinate instance to a strictly smaller / strictly easier one.
  Construction: let i* = argmax. Glue coordinate i* across two copies (or k copies). On the diagonal this
    sends bias_{i*} -> p^2/(p^2+q^2) < p (odds-squaring, since o_{i*}<1). Treat the conditioned distribution
    as a new full-support distribution and argue the global max strictly decreased.
  Skeleton:
    1. bias_{i*} strictly drops — by odds-squaring (o_{i*} < 1 from maxbias<1/2). [Always true.]
    2. Control the risers: bias_j(P') for j != i*. Need: after the glue, max_j bias_j(P') < maxbias(P).
    3. If some riser equals the new max, glue THAT coordinate next (recurse), with a measure that the
       recursion terminates (a potential strictly decreasing each round).
  Hard step: step 2 — the riser bound. The naive bound bias_j(P') <= max(bias_j,bias_{i*}) is FALSE
    (scout pt.3, confirmed: a negatively-correlated j rises because P(X_j=1,X_i=0) is reweighted by q_i>p_i).
    The mechanism must be a CORRECTED bound or a potential: e.g. show sum_j (odds of bias_j) or a softmax
    of biases strictly decreases under the i*-glue, so even if one riser increases, no coordinate can
    exceed the OLD max after finitely many glues. This is the genuinely open part — there is no proven
    riser inequality yet, and the survey could not find a fixed finite k that bounds all risers (the
    riser is a conditional with no 1/2 cap).
  Check: search for a true riser/potential inequality symbolically using the exact degree-2 marginal map
    (scout pt.3) for the i*-glue; verify on the XOR-like and anti-correlated stress cases that the chosen
    potential strictly decreases; prove termination.

Angle 3 — Existence via extremality / compactness over a rich glue family (non-constructive-leaning fallback).
  Proves: the existence of (k,S) with strict reduction (satisfies the theorem; weaker on "detail the
    construction" but the family is explicit).
  Construction family: all cyclic permutation-glues { (k, sigma) : k>=1, sigma in S_n } — explicitly
    parameterized; numerics show it covers all but a measure-tiny boundary set (mb -> 1/2).
  Skeleton:
    1. Define g(P) = inf over (k,sigma) of maxbias of the glued conditional. The family is countable/explicit.
    2. On the compact set { maxbias <= 1/2 - eps } show g(P) < maxbias(P) by a limiting argument: as
       k -> infinity along the right sigma, the glued marginals converge to a value strictly below maxbias
       except on a set ruled out by maxbias<1/2.
    3. Handle the boundary maxbias -> 1/2 by an explicit estimate (the odds-squaring contraction is
       quantitative: o -> o^2 with o<1 gives a uniform multiplicative gap bounded away from 1 on compacts).
  Hard step: proving the infimum is attained strictly below maxbias uniformly — because the contraction
    o -> o^2 on the equalized coordinate has multiplicative gain o < 1 - delta(eps) on { maxbias <= 1/2-eps },
    so for large enough k the contracted coordinate beats any bounded riser growth.
  Check: make the limiting argument quantitative; verify the uniform gap on { maxbias <= 1/2 - eps };
    confirm by brute force that increasing k along the best sigma drives the stubborn near-boundary cases
    below maxbias (the survey saw monotone improvement but did not push k high enough to close two cases —
    the proof-builder must verify the limit, not a finite k).

Angle 4 — Two-move constructive dichotomy with a CORRECT second block (constructive, less elegant).
  Proves: the full theorem, but as a case split the user explicitly disfavors. Kept as a safety net.
  Construction: Move A = best single same-coordinate cross-copy pair (k=2). Move B = force a chosen
    coordinate SUBSET T (and target value) constant within a copy, then odds-square via k copies; choose
    T and value to minimize the resulting block bias (NOT necessarily T = all coords).
  Skeleton: (1) if Move A reduces, done. (2) else prove the correlation structure that makes A fail forces
    some block-collapse B to reduce, with T chosen by the rarest-orbit pattern.
  Hard step: prove the two cases EXHAUST all maxbias<1/2 P with the CORRECT choice of T — because when A
    fails, the argmax coordinate is strongly anti-correlated with a riser, which makes some all-equal-on-T
    pattern rare, so collapsing T concentrates mass off the high coordinates. The survey showed the naive
    T = {all coords} version fails (n=3, 10/20000); the corrected version must choose T per P, so this is
    a genuine case analysis, not one elegant construction.
  Check: define the T-selection rule explicitly; prove for every A-failing P that the selected T gives
    block bias < maxbias; brute-force-verify on all stress cases.

### Ranking
Angle 1 first: it is the closest thing to the single elegant uniform construction the user asked for —
one symmetrizing glue that, by symmetry, collapses all n marginals to a single value, reducing the
problem to "lower one number," plus a clean odds-squaring contraction for the equalized case. Its hard
step (the averaging-dominates-the-max inequality + the extra contraction in the tie case) is the only
genuine gap, and it is a single inequality rather than a case tree.

Fall back to Angle 2 (induction on n) if the symmetrization inequality resists — induction localizes the
difficulty to ONE riser bound/potential, which may be easier to prove than the global symmetrized bound,
and it is also elegant. Fall back to Angle 3 if a clean finite construction cannot be closed: the
quantitative contraction on the compact { maxbias <= 1/2 - eps } gives an honest existence proof matching
the existential statement, at the cost of "detail the construction." Use Angle 4 only as a last resort —
it works numerically but is the case-bash the user wants to avoid.

Key tradeoff: Angles 1-3 all hinge on the SAME inequality in different dress — that the odds-squaring
contraction (multiplicative gain o<1, the only place maxbias<1/2 is used) eventually dominates the
conditional-probability riser growth. Whichever framing makes THAT inequality cleanest is the one to
build. Spec review is REQUIRED: the top angle's load-bearing inequality is novel and unproven, and it is
not yet obvious the symmetrized value is always below maxbias (4/3000 overshoot cases exist that the extra
contraction step must provably fix).

---

## Round-1 build record (proof-builder) — committed angle: DIRECT maxbias, P-dependent (k=2 absorb + k=mn cyclic)

**Outcome:** proof INCOMPLETE — blocked at one precise inequality (Lemma B3). Everything else
rigorous. Full writeup in `proof.md`; verification scripts in this dir (`final_verify.py`,
`construct.py`, `cyclic.py`, `combined2.py`, `stress.py`; reuse `harness.py`).

### What worked (now rigorous, with exact closed forms verified vs brute force)
- Reduction S→partition (S0) and well-definedness via full support (S1).
- **Move I** single same-coord cross-copy glue, closed form `bias_i=p^2/Z`, `bias_j=(a1 p+a0 q)/Z`
  (Lemma A1, 20/20 brute match). Diagonal `o->o^2`, `o<1` strict drop — the ONLY use of mb<1/2;
  symbolic factorization `p - p^2/Z = p(p-1)(2p-1)/(2p^2-2p+1) > 0` (Lemma A2).
- **Move II** absorb-block glue: `bias_{u in B}=A1^2/Z`, `bias_{u∉B}=(A0 Su0+A1 Su1)/Z`
  (Lemma A3, 20/20 brute match). CLEAN PROVABLE sub-result (Lemma A3a): block (incl. whole-copy
  collapse) reduces maxbias IFF `A1/A0 < sqrt(mb/(1-mb))`. This is the rigorous riser fix
  (Lemma A3b: absorbing a riser swaps its uncapped conditional for the squared block-odds).
- Explicit terminating **Rule R** (glue argmax, absorb any coord ≥ mb into its block). Correct
  when it stops below mb. NOT universal (fails on anti-correlated residual: block grows to all,
  whole-collapse threshold violated).
- **Move III backstop**, k=mn cyclic glue: all marginals equal `b*` (Lemma B1, brute 20/20),
  and `b*_{mn} -> ham(O*)/n` where O* maximizes the GEOMETRIC-MEAN orbit weight (Lemma B2,
  verified). This is the clean reformulation of the backstop.

### What did NOT work / dead ends confirmed this round
- The spec's `Φ_p` power-mean potential: refuted by critic, not used. Confirmed correct call.
- The critic's explicit "glue i* + absorb risers" Rule R is NOT universal (fails 18/3751 n=3,
  3/332 n=4 stressed) — exactly the anti-correlated residual. Matches critic's prediction.
- "best over ALL k=2 partitions" is also NOT universal: spec's n=3 counterexample
  [.0352,.3315,.4299,.00033,.0545,.1069,.00028,.0415] has best-k2 = identity (.4802, no
  reduction), needs k=3 cyclic (->.3347). CONFIRMED k=2 genuinely insufficient.
- Cyclic backstop is NOT universally good either: `b*>=1/2` for many non-residual P
  (n=4: 30/1191). It ONLY works on the residual — `ham(O*)/n < mb` fails 274/1891 general n=4.
  So BOTH pieces are individually non-universal; the combined "k=2 else cyclic" is what's 0-fail.
- Orbit-by-orbit rearrangement for B3 (`G(O)>=G(Ō)` for low-weight O) is FALSE even on residual
  (violated 18/20 n=3). So b* < 1/2 is an aggregate, not termwise, fact — resists easy proof.
- Multi-copy single-coord glue limit -> conditional `P(Xj=1|Xi*=0)` which can be >1/2 (0.83 on
  the counterexample): dead end, confirms no 1/2 cap on conditionals.
- Iterating best-k2 (treat 2n-joint as new dist, repeat): doesn't compose on n coords; Bell(12)
  search infeasible. Abandoned.

### The single open gap (Lemma B3)
> Residual (no k=2 partition reduces mb)  ⇒  ham(O*)/n < mb, where O* maximizes the geometric-mean
> cyclic-orbit weight `G(O)=(Π_{y∈O}P(y))^{1/|O|}` (tie-average strictly below mb).
Numerically 0 violations on every residual instance found (n=3 margin ≥ 0.097, b*≈1/3); the
residual hypothesis is load-bearing (conclusion false without it). Missing: a proof that
k=2-insufficiency forces the geometric-mean-maximizing orbit to low Hamming weight.

### CONJECTURE (unproven, for next round)
Lemma B3 as stated. Plausible attack: show residual ⇒ a majorization/log-supermodularity
condition on P that forces the max-geomean orbit below weight `n·mb`. Alternatively, find a
DIFFERENT residual move whose reduction is an explicit polynomial-sign condition (like A3a),
sidestepping the cyclic geometric-mean analysis entirely.

### Empirics: combined construction (best k=2 else k=mn cyclic) = 0 failures over 30,000+
adversarial/near-boundary/residual instances at n=2,3,4. Theorem almost certainly TRUE.
