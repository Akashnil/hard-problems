"""Clean library for Lemma B3 analysis (no module-level side effects).
Cyclic shift S: (Sx)_i = x_{(i-1) mod n}. Geometric mean over cyclic orbits.
"""
import numpy as np, itertools
from harness import (patterns, biases, maxbias, glue_marginals,
                     cond_marginals_general, all_k_partitions_search,
                     all_k2_partitions_search, joint)

def shift(x):
    n = len(x)
    return tuple(x[(i-1) % n] for i in range(n))

def orbit(x):
    x = tuple(x)
    seen = [x]; y = shift(x)
    while y != x:
        seen.append(y); y = shift(y)
    return seen

def all_orbits(n):
    seen = set(); orbits = []
    for x in itertools.product([0, 1], repeat=n):
        if x in seen: continue
        o = orbit(x)
        for z in o: seen.add(z)
        orbits.append(o)
    return orbits

def Pdict(P, n):
    pats = patterns(n)
    return {tuple(x): P[idx] for idx, x in enumerate(pats)}

def geomean(o, Pd):
    return float(np.exp(np.mean([np.log(Pd[y]) for y in o])))

def ostar_info(P, n, tol=1e-9):
    """Return (tie-averaged ham(O*)/n, list of winning orbits, gmax)."""
    Pd = Pdict(P, n)
    orbs = all_orbits(n)
    gms = [geomean(o, Pd) for o in orbs]
    gmax = max(gms)
    winners = [o for o, g in zip(orbs, gms) if g > gmax * (1 - tol)]
    hams = [sum(o[0]) for o in winners]   # ham is orbit-invariant
    return float(np.mean(hams)) / n, winners, gmax

def is_residual(P, n):
    """Full Bell-lattice k=2 search: residual iff no k=2 set-partition reduces maxbias."""
    best, bestS, mb0 = all_k_partitions_search(P, n, 2)
    return best >= mb0 - 1e-12, mb0, best

def cheap_reduces(P, n):
    """Fast sufficient test that P is NOT a residual (some cheap k=2 move reduces)."""
    mb = maxbias(P, n)
    for i in range(n):
        if glue_marginals(P, n, i).max() < mb - 1e-12:
            return True
    best, _, _ = all_k2_partitions_search(P, n, maxpairs=2)
    return best < mb - 1e-12
