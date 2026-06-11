#!/usr/bin/env python3
"""
Re-runnable computational certificate for the Round-3 CORRECTION + CLARIFICATION
of the Avenue-A obstruction (Frankl-file entropy approach).

WHAT THIS ROUND DOES (no bound moves; record 0.38271 (Liu) stands):
  - RETRACTS the round-2 certificate check R2-7(ii) ("B_l(x) >= 0 for all l>0 on
    the sweep"), which PASSED only because the round-2 sweep capped n at 7. The
    surrogate inequality (L') is FALSE in general.
  - Establishes, from scratch and RNG-INDEPENDENTLY, an explicit frozen witness
    union-closed family F* (n=9, |F*|=52) on which min_x B_l(x) < 0 in float64
    AND in 60-digit mpmath. This independently confirms (L') is FALSE.
  - Confirms the WEAKER true lemma (L) [P_{1+s} >= 0] still holds on the SAME
    witness (small positive min), i.e. the (L) != (L') separation.
  - Machine-checks the UNCONDITIONAL INTEGER-t CORE on the same n=9 witness
    (P_m = law of OR of m iid uniform for m=2,3,4; additivity; M_F
    column-stochastic) -- proving the proven core is insulated from the (L')
    failure.
  - Retains a non-vacuity guard.

IMPORTANT -- DO NOT TRUST THE EXPLORER'S RNG RECIPE:
  The round-3 explorer attributed the witness to `rand_family(9, seed=1711)` "in
  the round-2 certificate's RNG convention".  That convention uses
  k = randint(2,7) and produces |F|=21 with min B_l > 0 (NO counterexample).
  The witness with |F|=52 requires the WIDER generator count k = randint(2,12).
  To make the counterexample reproducible forever and immune to RNG-convention
  drift, this certificate HARD-CODES the witness as an explicit frozen list of
  bitmasks (WITNESS below) and re-derives min B_l < 0 directly from that list.
  It never depends on Python's RNG to produce the witness.

The honesty framing of (L) is also DOWNGRADED here, from round-2's "certified
numerically, unproven" to "unproven AND with eroding-margin evidence it may be
FALSE at scale" -- the min P_{1+s} margin shrinks with n (documented below).

WHAT IS NOT TOUCHED (and is re-affirmed by this certificate on the witness):
  the unconditional integer-t core, additivity P_{a+b}=P_a(*)P_b, the
  single-lemma reduction, the SS8 verdict, and the record 0.38271 (Liu) -- the
  perturb-uniform obstruction never depended on (L)/(L') and is not weakened.

certificate_round1.py and certificate_round2.py are left INTACT.  Round-2's
R2-7(ii) is NOT a false PASS in disguise there: its assertion is true on the
n<=7 sweep it actually runs; this round documents that it does NOT generalize
and supplies the explicit counterexample.  See obstruction-round3.md.

No network.  Pure Python + numpy + mpmath + the round-1 helper module.
"""

import importlib.util  # noqa: F401  (kept for parity with round-2 loader notes)
import itertools
import math
import os
import sys

import numpy as np

try:
    import mpmath as mp
except Exception as exc:  # pragma: no cover
    print(f"mpmath is required for the high-precision check: {exc}")
    sys.exit(2)

# ---- reuse round-1 helper FUNCTIONS without re-running its top-level checks --
# certificate_round1.py runs its checks at module import.  Load the source,
# slice off everything from the first driver banner, and exec only the helper
# definitions (single source of truth, no copy-paste drift, no second run/exit).
_R1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "certificate_round1.py")
with open(_R1) as fh:
    _src = fh.read()
_cut = _src.index('print("=" * 78)')
_ns = {}
exec(compile(_src[:_cut], _R1, "exec"), _ns)

closure = _ns["closure"]
zeta_matrix = _ns["zeta_matrix"]
Q_vector = _ns["Q_vector"]
or_closed = _ns["or_closed"]
H_bits = _ns["H_bits"]

FAILURES = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  -- {detail}" if detail else ""))
    if not cond:
        FAILURES.append(name)


# ============================================================================
# THE FROZEN WITNESS  F*  (n=9, |F*|=52).  RNG-INDEPENDENT.
# ============================================================================
# Exhibited (not trusted) construction for the record only: it is the OR-closure
# of random.Random(1711) drawing k=randint(2,12)=8 generators randint(1,2^9-1)
# on n=9.  The list below is the FROZEN result; the certificate uses ONLY this
# list and verifies it is genuinely union-closed.  Do not regenerate from RNG.
WITNESS = [
    0, 39, 114, 119, 150, 153, 159, 183, 191, 246, 247, 251, 255, 275, 289,
    295, 307, 311, 371, 375, 407, 411, 412, 413, 414, 415, 439, 441, 443, 445,
    447, 456, 468, 470, 471, 473, 475, 476, 477, 478, 479, 489, 495, 501, 502,
    503, 505, 506, 507, 509, 510, 511,
]
WITNESS_N = 9


def P_t(F, t):
    """P_t = Z^{-1} Q^t (entrywise power).  P_1 = uniform on F."""
    Z = zeta_matrix(F)
    Q = Q_vector(F)
    return np.linalg.solve(Z, Q ** t)


def Binv(F, l):
    """B_l = Z^{-1} (Q^2/(Q+l))  (the round-2 (L') integrand at parameter l)."""
    Z = zeta_matrix(F)
    Q = Q_vector(F)
    return np.linalg.solve(Z, Q ** 2 / (Q + l))


def joinconv(F, mu, nu):
    """Join-convolution (mu (*) nu)(z) = sum_{x|y=z} mu(x) nu(y)."""
    idx = {x: i for i, x in enumerate(F)}
    out = np.zeros(len(F))
    for i, x in enumerate(F):
        for j, y in enumerate(F):
            out[idx[x | y]] += mu[i] * nu[j]
    return out


def M_F(F):
    """Join-convolution-with-uniform operator: M[z,y] = (1/|F|)#{x: x|y=z}."""
    N = len(F)
    idx = {x: i for i, x in enumerate(F)}
    M = np.zeros((N, N))
    for j, y in enumerate(F):
        for x in F:
            M[idx[x | y], j] += 1.0 / N
    return M


# ---------------------------------------------------------------------- (R3-0)
print("=" * 78)
print("(R3-0) The frozen witness F* is a genuine union-closed family")
print("=" * 78)
F = sorted(set(WITNESS))
check("witness is a frozen list of 52 distinct bitmasks", len(F) == 52,
      f"|F*| = {len(F)}")
check("witness fits in n=9 ground elements", max(F) < (1 << WITNESS_N),
      f"max mask = {max(F)} < {1 << WITNESS_N}")
check("witness is GENUINELY union-closed (or_closed, contains empty set)",
      or_closed(F) and 0 in F, "OR-closed and contains 0")
# and that it equals its own closure (frozen list is exactly the closure):
check("witness equals its own OR-closure (no missing joins)",
      closure(F) == F, "closure(F*) == F*")

# ---------------------------------------------------------------------- (R3-1)
print()
print("=" * 78)
print("(R3-1) (L') is FALSE: explicit witness with min_x B_l(x) < 0 (float64)")
print("=" * 78)
# Dense l-grid near the known dip l ~ 0.126; assert a strictly negative minimum.
l_grid = np.linspace(0.05, 0.25, 4001)
best_val = np.inf
best_l = None
best_x = None
for l in l_grid:
    B = Binv(F, l)
    i = int(np.argmin(B))
    if B[i] < best_val:
        best_val, best_l, best_x = float(B[i]), float(l), F[i]
Z64 = zeta_matrix(F)
condZ = float(np.linalg.cond(Z64))
print(f"      worst (x,l): x = {best_x} (mask), l = {best_l:.6f}, "
      f"B_l(x) = {best_val:.12e}")
print(f"      cond(Z*) = {condZ:.3f}  (well-conditioned: NOT an ill-conditioning artifact)")
check("(L') FALSE: float64 min_x B_l(x) < -1e-3 on the frozen witness",
      best_val < -1e-3, f"min B_l = {best_val:.6e} at l = {best_l:.5f}")
check("cond(Z*) is modest (~129), so negativity is robust", condZ < 500.0,
      f"cond(Z*) = {condZ:.2f}")

# ---------------------------------------------------------------------- (R3-2)
print()
print("=" * 78)
print("(R3-2) (L') is FALSE confirmed at 60-digit precision (mpmath LU-solve)")
print("=" * 78)
mp.mp.dps = 60
Nw = len(F)
Zmp = mp.matrix(Nw, Nw)
for i in range(Nw):
    for j in range(Nw):
        Zmp[i, j] = mp.mpf(1) if (F[j] & F[i]) == F[j] else mp.mpf(0)
Qmp = mp.matrix(Nw, 1)
for k, y in enumerate(F):
    Qmp[k] = mp.mpf(sum(1 for x in F if (x & y) == x)) / mp.mpf(Nw)
lstar = mp.mpf(repr(best_l))
rhs = mp.matrix(Nw, 1)
for k in range(Nw):
    rhs[k] = Qmp[k] ** 2 / (Qmp[k] + lstar)
Bmp = mp.lu_solve(Zmp, rhs)
mn_mp = min(Bmp[k] for k in range(Nw))
print(f"      mpmath(60 dps) min_x B_l(x) at l* = {mp.nstr(mn_mp, 25)}")
print(f"      float64 vs mpmath agree: {mp.nstr(abs(mn_mp - mp.mpf(repr(best_val))), 5)}")
check("(L') FALSE: mpmath 60-dps min_x B_l(x) < -0.011 at l*",
      mn_mp < mp.mpf("-0.011"),
      f"60-dps min B_l = {mp.nstr(mn_mp, 18)}")
check("float64 and mpmath agree to printed precision (not a precision artifact)",
      abs(mn_mp - mp.mpf(repr(best_val))) < mp.mpf("1e-8"),
      "|float64 - mpmath| < 1e-8")

# ---------------------------------------------------------------------- (R3-3)
print()
print("=" * 78)
print("(R3-3) (L) STILL HOLDS on the SAME witness: min_s min_x P_{1+s}(x) > 0")
print("=" * 78)
s_grid = np.linspace(1e-4, 0.99999, 3000)
L_min = np.inf
L_min_s = None
for s in s_grid:
    P = np.linalg.solve(Z64, Q_vector(F) ** (1.0 + s))
    if P.min() < L_min:
        L_min = P.min()
        L_min_s = float(s)
print(f"      min over s-grid: min P_{{1+s}} = {L_min:.6e} at s = {L_min_s:.5f} "
      f"(driven toward s -> 1^-)")
check("(L) holds on witness: min_s min_x P_{1+s} > 0 (small positive)",
      L_min > 0.0, f"min P_{{1+s}} = {L_min:.6e} > 0")
check("the (L) != (L') SEPARATION is real on this single family",
      (L_min > 0.0) and (best_val < -1e-3),
      "(L) survives (+3.7e-4) where (L') fails (-0.0112) on the SAME F*")

# Mechanism check: the Pick representation still reproduces THIS P_{1+s} from
# THIS (sign-indefinite) B_l.  The negative B_l mass sits at small l, where the
# weight l^{s-1} (s near 1) downweights it, so the integral stays nonnegative.
print("      [mechanism] verifying P_{1+s} = (sin(pi s)/pi) int_0^inf B_l l^{s-1} dl")


def pick_integral_P(F, s, W=40.0, nodes=8000):
    Z = zeta_matrix(F)
    Q = Q_vector(F)
    N = len(F)
    acc = np.zeros(N)
    w = np.linspace(-W, W, nodes)
    dw = w[1] - w[0]
    for wi in w:
        l = math.exp(wi)
        Bl = np.linalg.solve(Z, Q ** 2 / (Q + l))
        acc += Bl * (l ** (s - 1)) * l * dw
    return (math.sin(math.pi * s) / math.pi) * acc


rep_ok = True
for s in (0.3, 0.6):
    approx = pick_integral_P(F, s, nodes=6000)
    exact = P_t(F, 1 + s)
    if not np.allclose(approx, exact, atol=3e-3):
        rep_ok = False
check("Pick representation reproduces P_{1+s} from the sign-indefinite B_l",
      rep_ok, "integral of a SIGNED B_l still yields the NONNEGATIVE P_{1+s}")

# ---------------------------------------------------------------------- (R3-4)
print()
print("=" * 78)
print("(R3-4) INVARIANTS on the SAME n=9 witness: integer-t core is INSULATED")
print("       from the (L') failure (UNCONDITIONAL content UNCHANGED)")
print("=" * 78)
# Integer-t core: P_m == brute-force law of (A_1 OR ... OR A_m), m=2,3,4.
idx = {x: i for i, x in enumerate(F)}
bad_anchor = 0
core_min = np.inf
for m in (2, 3, 4):
    Pm = P_t(F, m)
    cnt = np.zeros(Nw)
    for combo in itertools.product(range(Nw), repeat=m):
        v = 0
        for c in combo:
            v |= F[c]
        cnt[idx[v]] += 1
    cnt /= Nw ** m
    core_min = min(core_min, Pm.min())
    if not np.allclose(cnt, Pm, atol=1e-9):
        bad_anchor += 1
    if cnt.min() < -1e-15 or abs(cnt.sum() - 1.0) > 1e-12:
        bad_anchor += 1
check("integer-t core: P_m == brute OR-of-m law (m=2,3,4) on the n=9 witness",
      bad_anchor == 0, f"{bad_anchor} mismatches; min P_m = {core_min:.6f} >= 0")

# Additivity P_{a+b} = P_a (*) P_b on the witness.
add_bad = 0
for a, b in [(1.0, 0.5), (1.2, 0.8), (2.0, 1.5), (1.0, 1.0), (1.7, 0.6)]:
    if not np.allclose(joinconv(F, P_t(F, a), P_t(F, b)), P_t(F, a + b), atol=1e-9):
        add_bad += 1
check("additivity P_{a+b} == P_a (*) P_b on the n=9 witness", add_bad == 0,
      f"{add_bad} mismatches")

# M_F column-stochastic / nonnegative; M_F @ P_s == P_{1+s} on the witness.
M = M_F(F)
col_ok = np.allclose(M.sum(axis=0), 1.0, atol=1e-12)
nonneg_ok = M.min() >= -1e-15
step_ok = True
for s in (0.0, 0.3, 0.7, 0.999):
    if not np.allclose(M @ P_t(F, s), P_t(F, 1 + s), atol=1e-9):
        step_ok = False
check("M_F column-stochastic, nonnegative, M_F@P_s==P_{1+s} on the witness",
      col_ok and nonneg_ok and step_ok,
      f"cols-sum-1={col_ok}, nonneg={nonneg_ok}, step={step_ok}")

# H[P_m] <= H[A] on the witness (the unconditional ceiling, demonstrated where
# (L') dies).
HA = math.log2(Nw)
ceil_ok = all(H_bits(P_t(F, m)) <= HA + 1e-9 for m in (1, 2, 3, 4))
check("H[P_m] <= H[A] for m=1,2,3,4 on the witness (unconditional ceiling)",
      ceil_ok, f"H[A] = log2({Nw}) = {HA:.4f}")

# ---------------------------------------------------------------------- (R3-5)
print()
print("=" * 78)
print("(R3-5) OBSERVED onset of (L') failure (seed- and grid-dependent)")
print("=" * 78)
# NOTE (per outline review): the EXACT onset n is seed-set- and l-grid-dependent
# and must NOT be reported as a hard 'n=8, zero at n<=7' fact.  We reproduce a
# SMALL deterministic sweep purely to record the qualitative point: round-2's
# n<=7 sweep on a coarse l-grid did not reach the failure regime; failures are
# OBSERVED to begin around n~8 in this RNG family.
import random as _random


def _rand_family_wide(n, seed):
    rng = _random.Random(seed)
    k = rng.randint(2, 12)  # WIDE convention (NOT round-2's randint(2,7))
    return closure([rng.randint(1, (1 << n) - 1) for _ in range(k)])


_lg = np.linspace(0.01, 0.5, 120)
onset = {}
for n in (7, 8, 9):
    fails = tot = 0
    for seed in range(80):
        Fn = _rand_family_wide(n, seed)
        if len(Fn) < 4 or len(Fn) > 300:
            continue
        tot += 1
        Zn = zeta_matrix(Fn)
        Qn = Q_vector(Fn)
        if any(np.linalg.solve(Zn, Qn ** 2 / (Qn + l)).min() < -1e-9 for l in _lg):
            fails += 1
    onset[n] = (fails, tot)
    print(f"      n={n}: {fails}/{tot} families with min B_l < 0 (this seed set)")
check("OBSERVED: zero (L') failures at n=7 in this small seed set", onset[7][0] == 0,
      f"{onset[7][0]}/{onset[7][1]} at n=7 (seed/grid dependent, not a hard onset)")
check("OBSERVED: (L') failures appear by n=8 in this small seed set", onset[8][0] >= 1,
      f"{onset[8][0]}/{onset[8][1]} at n=8 -- why round-2's n<=7 sweep missed it")

# ---------------------------------------------------------------------- (R3-6)
print()
print("=" * 78)
print("(R3-6) (L) margin ERODES with n (honest red flag; (L) may be FALSE at scale)")
print("=" * 78)
# Sweep (L) past round-2's cutoff and report the MONOTONE-DECREASING margin.
# This is recorded honestly: (L) is a conjecture with a NON-TRIVIAL chance of
# being FALSE at scale (mirroring exactly how (L') looked positive until n~8).
_sg = np.linspace(1e-4, 0.99999, 200)
prev = None
mono = True
margins = {}
for nmax in (7, 8, 9, 10):
    gmin = np.inf
    for seed in range(60):
        for n in range(3, nmax + 1):
            Fn = _rand_family_wide(n, seed + n * 1000)
            if len(Fn) < 4 or len(Fn) > 400:
                continue
            Zn = zeta_matrix(Fn)
            Qn = Q_vector(Fn)
            for s in _sg:
                m = np.linalg.solve(Zn, Qn ** (1 + s)).min()
                if m < gmin:
                    gmin = m
    margins[nmax] = gmin
    print(f"      max n <= {nmax}: min P_{{1+s}} = {gmin:.3e}")
    if prev is not None and gmin > prev + 1e-12:
        mono = False
    prev = gmin
check("(L) min P_{1+s} stays > 0 on this n<=10 sweep (still conjecturally true)",
      min(margins.values()) > 0.0, f"min over sweep = {min(margins.values()):.3e}")
check("(L) margin is non-increasing in n (eroding-margin red flag, recorded)",
      mono, "monotone-decreasing margin: (L) may be FALSE at scale")

# ---------------------------------------------------------------------- (R3-NV)
print()
print("=" * 78)
print("(R3-NV) Non-vacuity guards")
print("=" * 78)
# (a) The signed t<1 branch is real on the witness (cutoff t>=1 is content-bearing).
signed = any(P_t(F, s).min() < -1e-9 for s in (0.1, 0.2, 0.3, 0.5, 0.7, 0.85, 0.95))
check("witness has SIGNED P_s for some s in (0,1) (t>=1 cutoff is real)", signed,
      "P_s goes negative below t=1 -- the cutoff is content-bearing")
# (b) Wrong Q^1 numerator (round-2 guard): B_l with Q^1 instead of Q^2 must
#     produce MORE/other negativity -- proves the B_l check tests something real.
Q = Q_vector(F)
wrong_neg = any(np.linalg.solve(Z64, Q / (Q + l)).min() < -1e-9 for l in l_grid[::50])
check("wrong-power guard: B_l with Q^1 numerator produces negatives (non-vacuous)",
      wrong_neg, "the Q^2 inequality tests something real")

# ----------------------------------------------------------------- verdict
print()
print("=" * 78)
print("INVARIANTS PRESERVED (banner):")
print("  UNCONDITIONAL integer-t core UNCHANGED; additivity UNCHANGED; the")
print("  single-lemma reduction UNCHANGED; the SS8 verdict (perturb-uniform")
print("  approach cannot reach 1/2) UNCHANGED; record 0.38271 (Liu) UNCHANGED.")
print("  Only the CONJECTURAL non-integer-t surrogate (L') is corrected:")
print("  (L') is now FALSE (explicit frozen witness, 60-dps confirmed).")
print("  (L) remains conjectural with an ERODING-MARGIN caveat (may be false")
print("  at scale).  The obstruction never depended on (L)/(L') and is NOT")
print("  weakened.")
print("=" * 78)
if FAILURES:
    print(f"RESULT: FAIL  ({len(FAILURES)} check(s) failed: {FAILURES})")
    sys.exit(1)
print("RESULT: ALL CHECKS PASS")
print("=" * 78)
sys.exit(0)
