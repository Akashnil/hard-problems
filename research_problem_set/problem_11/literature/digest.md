# Literature digest — problem_11 (bias amplification by conditioning on equality)

## Search outcome
The exact statement (full-support P on {0,1}^n, maxbias<1/2, take k copies, condition
on coordinate-equality events to strictly reduce maxbias) was NOT found verbatim in the
literature. It reads like an original / competition-style construction problem. Adjacent
bodies of work:

- **Agreement testing / biased hypercube structure** (Dinur–Filmus–Harsha,
  "Analyzing Boolean functions on the biased hypercube via higher-dimensional agreement
  tests", https://www.cs.toronto.edu/~yuvalf/DFH-ks-agree.pdf). Uses the idea of
  conditioning on an *agreement event* across copies and taking a "restricted global"
  majority to boost agreement probability. Mechanism (condition on agreement to sharpen)
  is morally related but the goal (structure theorems for low-degree functions) differs.
- **Bias amplification via nonlocal boxes / majority** (arXiv:1604.05663): 3-input
  majority is the unique optimal bias amplifier; bias amplification = pushing |bias| of
  output beyond |bias| of input. Different setting (functions of inputs, not conditioning).
- **Polarization / Arikan-style** and **noise-stability (Mossel/O'Donnell)** are the
  natural TCS neighbours but none gives this exact conditioning lemma.

## The one analytic fact that IS clean and load-bearing
For a SINGLE Bernoulli(b) coordinate, b<1/2: take k independent copies and condition
them all equal. New bias = b^k / (b^k + (1-b)^k). Since b/(1-b) < 1, this is < b for all
k>=2 and -> 0 as k->inf. This is the kernel that makes the theorem plausible. The whole
difficulty is that in a *correlated* P, conditioning one coordinate equal across copies
distorts the marginals of OTHER coordinates (via P's internal correlation), and those can
rise ABOVE the original maxbias.

## Conclusion
Treat this as an original construction problem. No off-the-shelf theorem to cite; the
single-coordinate amplification fact above is the reusable building block.
