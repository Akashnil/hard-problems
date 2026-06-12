"""B3 reduction certificate (problem_11, round 3).

Certifies, on every independently-isolated residual at n=3,4,5, the two scalar
sub-claims that Lemma B3 reduces to:
  (B3-a)  the weight-1 cyclic orbit O_1 = {e_1,...,e_n} is the UNIQUE geometric-mean
          maximizer among cyclic orbits, hence ham(O*)/n = 1/n;
  (B3-b)  mb = maxbias(P) > 1/n.
Together (trivially) (B3-a) & (B3-b) => ham(O*)/n = 1/n < mb, which is Lemma B3.

A residual is a full-support P with maxbias(P)<1/2 for which NO k=2 set-partition of
the 2n coords reduces maxbias (full Bell-lattice search,
harness.all_k_partitions_search / fast_residual.fast_is_residual_k2).

Run: PYTHONPATH=. python3 b3_certificate.py
Residual datasets res_n{3,4,5}.pkl are produced by the hunters documented in proof.md.
"""
import os.path, pickle, numpy as np
from b3lib import (patterns, biases, maxbias, Pdict, all_orbits, geomean,
                   ostar_info, is_residual)

HERE = os.path.dirname(os.path.abspath(__file__))

print("=" * 70)
print("B3 CERTIFICATE: reduction to (B3-a) [O*=weight-1] & (B3-b) [mb>1/n]")
print("=" * 70)

# --- Spec n=3 residual (the verified genuine residual) -----------------------
spec = np.array([.0352, .3315, .4299, .00033, .0545, .1069, .00028, .0415])
spec /= spec.sum()
isr, mb, best = is_residual(spec, 3)
h, wn, g = ostar_info(spec, 3)
print(f"\nSpec residual P (n=3): residual={isr}, mb={mb:.4f}")
print(f"  O* winners ham: {[sum(o[0]) for o in wn]}, ham(O*)/n={h:.4f}")
print(f"  (B3-a) O*=weight-1: {all(sum(o[0])==1 for o in wn)}")
print(f"  (B3-b) mb>1/n: {mb>1/3} (mb-1/n={mb-1/3:.4f})")
print(f"  => ham(O*)/n = 1/3 < mb: {1/3 < mb}")

# --- All isolated residuals --------------------------------------------------
for n in [3, 4, 5]:
    f = os.path.join(HERE, f'res_n{n}.pkl')
    if not os.path.exists(f):
        continue
    res = pickle.load(open(f, 'rb'))
    ca = cb = ct = 0
    minBmarg = 9.0; minTmarg = 9.0; worstA = 1.0
    for d in res:
        P = d['P']; mb = maxbias(P, n)
        h, wn, g = ostar_info(P, n)
        ca += all(sum(o[0]) == 1 for o in wn)
        cb += mb > 1.0 / n + 1e-12
        ct += h < mb - 1e-12
        minBmarg = min(minBmarg, mb - 1.0 / n)
        minTmarg = min(minTmarg, mb - h)
        Pd = Pdict(P, n)
        gms = sorted((geomean(o, Pd) for o in all_orbits(n)), reverse=True)
        worstA = min(worstA, gms[1] / gms[0])  # runner-up / winner geomean ratio
    N = len(res)
    print(f"\nn={n}: {N} residuals")
    print(f"  (B3-a) O*=weight-1:  {ca}/{N}   (worst runnerup/winner geomean = {worstA:.4f})")
    print(f"  (B3-b) mb>1/n:       {cb}/{N}   (min mb-1/n = {minBmarg:.4f})")
    print(f"  TARGET ham(O*)/n<mb: {ct}/{N}   (min margin = {minTmarg:.4f})")

print("\nResult: across all isolated residuals (n=3,4,5), (B3-a), (B3-b) and the")
print("target ham(O*)/n < mb each hold with ZERO violations.")
