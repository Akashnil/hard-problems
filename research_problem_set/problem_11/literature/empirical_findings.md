# Empirical findings — problem_11 (throwaway scripts run round 1)

All over random full-support P on {0,1}^n (n=2,3,4), maxbias<1/2, exact enumeration.

## Single-coordinate kernel (WORKS, exact)
n=1, b<1/2, k=2, condition X1=X2: new bias = b^2/((1-b)^2+b^2) < b always. Verified b=0.1..0.49.

## Constructions that DO NOT universally work (dead ends)
- **Full match / Q ∝ P(x)^2** (k=2, match every coord of the two copies): can INCREASE
  maxbias. Concrete: P on {0,1}^2 with biases (0.444,0.464), maxbias 0.464 -> 0.507. Confirms
  the run_state warning.
- **Full consensus P^k** (all copies equal): concentrates on the most-likely point; if that
  point has a 1 in some coord, bias->1. Failed to reduce in 36/59 (k=4).
- **Match only the argmax coordinate across 2 copies** (single pair S={(j,n+j)}): the argmax
  coord ALWAYS drops (0/229 failures on that coord), BUT another coordinate can rise above
  the old max -> maxbias not reduced in 7/229. Mechanism (seed278, n=3): biases
  (0.457,0.363,0.455), match coord0 -> coord0 drops 0.457->0.415 but coord2 rises
  0.455->0.463 and overtakes. Root cause: Pr_P(x_2=1 | x_0=0) = 0.543 > maxbias.
- **All-coords-equal-to-anchor chain** (force the whole vector constant + copies equal):
  conditional lives on {0...0, 1...1}; bias = Pr(1..1)^k/(Pr(0..0)^k+Pr(1..1)^k). Fails
  exactly when Pr(1..1) >= Pr(0..0), which CAN happen with maxbias<1/2. Failed 8/229 (k=8).
- **Match high-bias coords across k copies**: fails 13/39 (k=3).
- **Match all-except-argmax**: fails 136/229.

## Theorem appears TRUE, but NO fixed universal construction found
Per-instance brute/sampled search over (k<=2, many S) ALWAYS found some reducing S:
n=2 k=2: 0/100 no-reduction; n=3: 0/17; n=4: 0/5. So the winning S is DATA-DEPENDENT.
Example winner (seed278, n=3, k=2): S={(0,2),(0,3),(0,5)} drives maxbias 0.457 -> 0.2945
(matching the argmax coord0 to coord2-of-copy1, coord0-of-copy2, coord2-of-copy2).

## Takeaway for the proof
The proof likely needs EITHER (a) a data-dependent S (e.g. tie the argmax coordinate to a
carefully chosen partner/anchor that does not have a negatively-correlated coordinate
problem), OR (b) a non-constructive/existence argument (potential function that strictly
decreases), OR (c) a clever universal gadget the searches above did not parametrize.
The single-coordinate kernel b->b^2/(b^2+(1-b)^2) is the right intuition but coupling is
the whole game.
