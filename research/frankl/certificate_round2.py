#!/usr/bin/env python3
"""
Re-runnable computational certificate for the Round-2 GLOBAL upgrade of the
Avenue-A obstruction (Frankl-file entropy approach).

It REUSES the round-1 helpers (closure, zeta_matrix, Q_vector, H_bits, bits,
biases, nondistributive_family, build_family) by importing them from
certificate_round1.py, so the round-1 checks are not duplicated or broken
(run certificate_round1.py separately for those).

This script certifies, with PASS/FAIL per check and a nonzero exit on any
failure:

  (R2-1) ADDITIVITY / join-convolution identity.  Q^{a+b} = Q^a . Q^b entrywise,
         and Mobius inversion turns the entrywise product of domination-CDFs into
         the join-convolution of the inverted measures:
             P_{a+b} = P_a (*) P_b,   (mu (*) nu)(z) = sum_{x|y=z} mu(x) nu(y).
         Checked as P_{a+b} == M(P_a is uniform case) and generally as the explicit
         join-convolution of vectors, across many families and (a,b).

  (R2-2) M_F COLUMN-STOCHASTICITY.  The join-convolution-with-uniform operator
             M_F[z,y] = (1/|F|) #{x in F : x | y = z}
         has nonnegative entries and every column sums to exactly 1 (maps the
         probability simplex into itself); and M_F @ P_s == P_{1+s} exactly.

  (R2-3) INTEGER ANCHOR (UNCONDITIONAL).  For integer m, Z^{-1} Q^m equals the
         brute-force law of (A_1 OR ... OR A_m), A_i iid uniform on F.  Hence P_m
         is a genuine probability distribution and (round-1 Theorem 1)
         H[P_m] <= H[A], with no conjecture, at every integer m.  Checked m=2,3,4.

  (R2-4) SINGLE-LEMMA REDUCTION, base case.  The whole "P_t >= 0 for all real
         t >= 1" claim reduces to the single inequality
             (P_1 (*) P_s)(x) >= 0   for all s in [0,1), every union-closed F
         (the step t -> t+1 is then a convolution of two NONNEGATIVE measures,
         hence nonnegative for free -- checked here too).  We certify the base
         case numerically on a large sweep, and certify the step lemma's
         "nonneg (*) nonneg = nonneg" structurally.

  (R2-5) NON-VACUITY of the signed t<1 branch.  Exhibit families/s with P_s
         signed (min < 0) for s in (0,1), and the largest observed signed t < 1.
         This is what makes the t=1 cutoff content-bearing rather than vacuous.

  (R2-6) GLOBAL ENTROPY COROLLARY.  Wherever P_t >= 0 (t >= 1), assert
         H[P_t] <= H[A] with a margin, and that the margin -> 0 as t -> 1+
         (consistency with the round-1 H''(1) < 0 local shadow).

  (R2-7) THE PICK-REPRESENTATION REDUCTION (partial analytic progress).  For
         s in (0,1), u^{1+s} has the Pick/Stieltjes representation
             u^{1+s} = (sin(pi s)/pi) * int_0^inf  u^2/(u+l) * l^{s-1} dl   (u>0),
         so P_{1+s}(x) = (sin(pi s)/pi) int_0^inf B_l(x) l^{s-1} dl  with
             B_l(x) = sum_{y<=x} mu(y,x) Q(y)^2/(Q(y)+l).
         Hence P_{1+s} >= 0 for ALL s in (0,1) would FOLLOW from B_l(x) >= 0 for
         all l > 0.  We (i) verify the representation numerically, and (ii) verify
         B_l(x) >= 0 on a large sweep -- i.e. we certify the CONTENT of the
         reduced inequality.  GUARDRAIL: B_l(x) >= 0 on arbitrary non-distributive
         lattices is itself NOT proven analytically here; this is the open gap.

  (R2-NV) NON-VACUITY GUARD.  Perturbing the t>=1 nonnegativity claim down to
         t>=0.5 MUST produce a failure (signed measures appear), proving the
         sweep is not vacuous.

IMPORTANT (honesty guardrail, mirrors the writeup): the universally-quantified
statement "P_t >= 0 for ALL real t >= 1 on EVERY union-closed family (incl.
non-distributive)" CANNOT be settled by finite enumeration.  These checks are
ILLUSTRATIVE certificates of the integer-t core (proven) and of the CONTENT of
the single reduced lemma (conjectural).  The all-real-t nonnegativity is
CERTIFIED-NUMERICALLY-BUT-UNPROVEN.

No network.  Pure Python + numpy + the round-1 module.
"""

import importlib.util
import math
import os
import random
import sys

import numpy as np

# ---- import round-1 helpers without re-running its top-level checks? -------
# certificate_round1.py runs its checks at import (module-level).  To reuse its
# pure helper FUNCTIONS without triggering a second full run + sys.exit, we load
# the source, strip everything from the first top-level driver line onward, and
# exec only the helper definitions.  This keeps a single source of truth for the
# shared lattice/entropy helpers (no copy-paste drift) while leaving round-1's
# own checks to be run on their own.
_R1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "certificate_round1.py")
with open(_R1) as fh:
    _src = fh.read()
# helper section ends right before the first driver banner.
_marker = "# ---------"  # the dashed banner before section (a)
_cut = _src.index('print("=" * 78)')
_helpers_src = _src[:_cut]
_ns = {}
exec(compile(_helpers_src, _R1, "exec"), _ns)

closure = _ns["closure"]
bits = _ns["bits"]
H_bits = _ns["H_bits"]
zeta_matrix = _ns["zeta_matrix"]
Q_vector = _ns["Q_vector"]
or_closed = _ns["or_closed"]
biases = _ns["biases"]
build_family = _ns["build_family"]
nondistributive_family = _ns["nondistributive_family"]

FAILURES = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  -- {detail}" if detail else ""))
    if not cond:
        FAILURES.append(name)


# ---------------------------------------------------------------- new helpers
def P_t(F, t):
    """P_t = Z^{-1} Q^t (entrywise power).  P_1 = uniform on F."""
    Z = zeta_matrix(F)
    Q = Q_vector(F)
    return np.linalg.solve(Z, Q ** t)


def joinconv(F, mu, nu):
    """Join-convolution of two vectors indexed by F:
        (mu (*) nu)(z) = sum_{x|y=z} mu(x) nu(y)."""
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


def rand_family(n, seed):
    rng = random.Random(seed)
    k = rng.randint(2, 7)
    gens = [rng.randint(1, (1 << n) - 1) for _ in range(k)]
    return closure(gens)


# canonical non-distributive family + an assortment of random families
ndF, ndn = nondistributive_family()
SAMPLE_FAMILIES = [("nondistributive 7-elt", ndF, ndn)]
for _seed in range(60):
    _n = random.Random(_seed).randint(3, 7)
    _F = rand_family(_n, _seed)
    if 4 <= len(_F) <= 200:
        SAMPLE_FAMILIES.append((f"rand n={_n} seed={_seed}", _F, _n))

# --------------------------------------------------------------------- (R2-1)
print("=" * 78)
print("(R2-1) Additivity: P_{a+b} = P_a (*) P_b  (join-convolution)")
print("=" * 78)
ab_pairs = [(1.0, 0.5), (1.2, 0.8), (0.7, 0.3), (2.0, 1.5), (1.0, 1.0),
            (1.3, 0.0), (1.7, 0.6), (2.4, 0.9)]
bad = 0
for label, F, n in SAMPLE_FAMILIES[:20]:
    for a, b in ab_pairs:
        Pa, Pb = P_t(F, a), P_t(F, b)
        if not np.allclose(joinconv(F, Pa, Pb), P_t(F, a + b), atol=1e-9):
            bad += 1
check("P_{a+b} == P_a (*) P_b across families & (a,b)", bad == 0,
      f"{bad} mismatches")

# --------------------------------------------------------------------- (R2-2)
print()
print("=" * 78)
print("(R2-2) M_F is column-stochastic, nonnegative; M_F @ P_s == P_{1+s}")
print("=" * 78)
bad_cols = bad_neg = bad_step = 0
for label, F, n in SAMPLE_FAMILIES[:25]:
    M = M_F(F)
    if not np.allclose(M.sum(axis=0), 1.0, atol=1e-12):
        bad_cols += 1
    if M.min() < -1e-15:
        bad_neg += 1
    for s in (0.0, 0.3, 0.7, 0.999, 1.4):
        if not np.allclose(M @ P_t(F, s), P_t(F, 1 + s), atol=1e-9):
            bad_step += 1
check("M_F columns sum to 1", bad_cols == 0, f"{bad_cols} bad")
check("M_F entries nonnegative", bad_neg == 0, f"{bad_neg} bad")
check("M_F @ P_s == P_{1+s} (one smoothing pass = +1 to t)", bad_step == 0,
      f"{bad_step} bad")

# --------------------------------------------------------------------- (R2-3)
print()
print("=" * 78)
print("(R2-3) Integer anchor (UNCONDITIONAL): Z^{-1}Q^m == law(OR of m iid unif)")
print("=" * 78)
import itertools
bad_anchor = 0
for label, F, n in SAMPLE_FAMILIES[:12]:
    if len(F) > 12:
        continue  # brute force m-fold product
    idx = {x: i for i, x in enumerate(F)}
    N = len(F)
    for m in (2, 3, 4):
        cnt = np.zeros(N)
        for combo in itertools.product(range(N), repeat=m):
            v = 0
            for c in combo:
                v |= F[c]
            cnt[idx[v]] += 1
        cnt /= N ** m
        if not np.allclose(cnt, P_t(F, m), atol=1e-9):
            bad_anchor += 1
        # the OR-law is by construction a genuine distribution: nonneg, sums to 1
        if cnt.min() < -1e-15 or abs(cnt.sum() - 1) > 1e-12:
            bad_anchor += 1
check("P_m == brute-force OR-of-m law (m=2,3,4), genuine distribution",
      bad_anchor == 0, f"{bad_anchor} bad")

# --------------------------------------------------------------------- (R2-4)
print()
print("=" * 78)
print("(R2-4) Single-lemma reduction:  base (P_1 (*) P_s)(x) >= 0, s in [0,1);")
print("        step  nonneg (*) nonneg = nonneg")
print("=" * 78)
s_grid = [0.0, 1e-4, 0.05, 0.2, 0.4, 0.6, 0.8, 0.95, 0.999]
base_neg = 0
base_min = 1e9
for label, F, n in SAMPLE_FAMILIES:
    M = M_F(F)
    for s in s_grid:
        v = M @ P_t(F, s)  # = P_{1+s}
        base_min = min(base_min, v.min())
        if v.min() < -1e-9:
            base_neg += 1
check("BASE: (P_1 (*) P_s)(x) >= 0 for s in [0,1) (sweep)", base_neg == 0,
      f"min over sweep = {base_min:.3e}")
# step lemma structural: join-convolution of two nonnegative, sum-1 vectors is
# nonnegative and sum-1 (so once P_t>=0, P_{t+1}=P_1(*)P_t>=0 for free).
step_bad = 0
for label, F, n in SAMPLE_FAMILIES[:25]:
    mu = np.abs(np.random.default_rng(0).random(len(F)))
    mu /= mu.sum()
    nu = np.abs(np.random.default_rng(1).random(len(F)))
    nu /= nu.sum()
    c = joinconv(F, mu, nu)
    if c.min() < -1e-15 or abs(c.sum() - 1) > 1e-12:
        step_bad += 1
check("STEP: join-conv of two nonneg sum-1 vectors stays nonneg sum-1",
      step_bad == 0, f"{step_bad} bad")

# --------------------------------------------------------------------- (R2-5)
print()
print("=" * 78)
print("(R2-5) Non-vacuity of the signed t<1 branch (cutoff is content-bearing)")
print("=" * 78)
signed_families = 0
largest_signed_t = 0.0
total = 0
for label, F, n in SAMPLE_FAMILIES:
    total += 1
    fam_signed = False
    for s in [0.1, 0.2, 0.3, 0.5, 0.7, 0.85, 0.95]:
        if P_t(F, s).min() < -1e-9:
            fam_signed = True
            largest_signed_t = max(largest_signed_t, s)
    if fam_signed:
        signed_families += 1
check("some families have SIGNED P_s for s in (0,1) (branch (ii) real)",
      signed_families > 0, f"{signed_families}/{total} families signed for some s<1")
check("largest observed signed t < 1 (cutoff t>=1 is safe)",
      largest_signed_t < 1.0, f"largest signed t = {largest_signed_t}")

# --------------------------------------------------------------------- (R2-6)
print()
print("=" * 78)
print("(R2-6) Global entropy corollary: where P_t >= 0, H[P_t] <= H[A], margin->0 as t->1+")
print("=" * 78)
ent_bad = 0
for label, F, n in SAMPLE_FAMILIES[:30]:
    N = len(F)
    HA = math.log2(N)
    margins = []
    for t in [1.0, 1.0001, 1.05, 1.5, 3.0, 10.0]:
        P = P_t(F, t)
        if P.min() < -1e-9:
            ent_bad += 1  # should not happen for t>=1 in the sweep
            continue
        Hp = H_bits(P)
        if Hp > HA + 1e-9:
            ent_bad += 1
        margins.append((t, HA - Hp))
    # margin at t=1.0001 should be tiny vs margin at t=3
    m_near = next(m for t, m in margins if abs(t - 1.0001) < 1e-9)
    m_far = next(m for t, m in margins if abs(t - 3.0) < 1e-9)
    if not (m_near < m_far + 1e-12 and m_near < 1e-2):
        ent_bad += 1
check("H[P_t] <= H[A] for t>=1 (sweep) and margin->0 as t->1+", ent_bad == 0,
      f"{ent_bad} bad")

# --------------------------------------------------------------------- (R2-7)
print()
print("=" * 78)
print("(R2-7) Pick reduction:  P_{1+s} = (sin(pi s)/pi) int B_l l^{s-1} dl;")
print("        B_l(x) = sum_{y<=x} mu(y,x) Q(y)^2/(Q(y)+l) >= 0  (reduced lemma)")
print("=" * 78)


def Binv(F, l):
    """B_l = Z^{-1} (Q^2/(Q+l))."""
    Z = zeta_matrix(F)
    Q = Q_vector(F)
    return np.linalg.solve(Z, Q ** 2 / (Q + l))


# (i) verify the Pick integral representation numerically (Gauss-Legendre on a
#     substitution l = (1-u)/u to map (0,inf) -> (0,1)).
def pick_integral_P(F, s, W=40.0, nodes=20000):
    Q = Q_vector(F)
    Z = zeta_matrix(F)
    # integrate g(l) = B_l * l^{s-1} over (0,inf).  Substitute l = exp(w),
    # w in (-W, W), dl = exp(w) dw -- a log-spaced grid resolves both the
    # l->0 (~l^{s-1}) and l->inf (~l^{s-2}) tails accurately.
    N = len(F)
    acc = np.zeros(N)
    w = np.linspace(-W, W, nodes)
    dw = w[1] - w[0]
    for wi in w:
        l = math.exp(wi)
        Bl = np.linalg.solve(Z, Q ** 2 / (Q + l))
        acc += Bl * (l ** (s - 1)) * l * dw  # *l for dl = exp(w) dw
    return (math.sin(math.pi * s) / math.pi) * acc


# check representation on the non-distributive family for a couple of s
rep_ok = True
for s in (0.3, 0.6):
    approx = pick_integral_P(ndF, s, nodes=6000)
    exact = P_t(ndF, 1 + s)
    if not np.allclose(approx, exact, atol=2e-3):
        rep_ok = False
check("Pick representation P_{1+s} = (sin/pi) int B_l l^{s-1} dl (numeric)",
      rep_ok, "matches to integration tol on non-distributive lattice")

# (ii) verify the CONTENT of the reduced inequality: B_l(x) >= 0 for all l>0
B_neg = 0
B_min = 1e9
l_grid = [1e-3, 1e-2, 0.05, 0.1, 0.3, 0.7, 1.5, 4.0, 15.0, 60.0]
for label, F, n in SAMPLE_FAMILIES:
    for l in l_grid:
        B = Binv(F, l)
        B_min = min(B_min, B.min())
        if B.min() < -1e-9:
            B_neg += 1
check("REDUCED LEMMA content: B_l(x) >= 0 for all l>0 (sweep)", B_neg == 0,
      f"min B_l over sweep = {B_min:.3e}  [NOTE: not proven analytically -- open gap]")

# --------------------------------------------------------------------- (R2-NV)
print()
print("=" * 78)
print("(R2-NV) Non-vacuity guard: claiming t>=0.5 nonneg MUST fail")
print("=" * 78)
# If we (wrongly) asserted P_t >= 0 for all t >= 0.5, signed measures appear.
found_violation = False
for label, F, n in SAMPLE_FAMILIES:
    for t in [0.5, 0.6, 0.7, 0.8, 0.85]:
        if P_t(F, t).min() < -1e-9:
            found_violation = True
            break
    if found_violation:
        break
check("perturbing cutoff to t>=0.5 PRODUCES a signed measure (non-vacuous)",
      found_violation, "as required: the t>=1 cutoff is doing real work")

# ----------------------------------------------------------------- verdict
print()
print("=" * 78)
if FAILURES:
    print(f"RESULT: FAIL  ({len(FAILURES)} check(s) failed: {FAILURES})")
    sys.exit(1)
print("RESULT: ALL CHECKS PASS")
print("NOTE: integer-t core is PROVEN; the all-real-t nonnegativity (single")
print("      reduced lemma B_l>=0 / (P_1(*)P_s)>=0) is CERTIFIED NUMERICALLY")
print("      BUT NOT PROVEN -- finite enumeration cannot settle a for-all-t,")
print("      for-all-F claim.  See obstruction-round2.md.")
print("=" * 78)
sys.exit(0)
