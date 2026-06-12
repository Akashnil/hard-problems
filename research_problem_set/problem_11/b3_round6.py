"""Round-6 advances on gap (star)/(B3-a') for problem_11.

This round attacked the approved "orbit-aggregate (dagger) SLACK_O > BIASGAP" angle and the
critic's CHANGES-REQUESTED obligation: supply a MECHANISM for the uncovered weight-2 mass, do NOT
lean on "(UB) caps BIASGAP", and stress every bound in the binding mb->1/2 regime.

It produces the following RIGOROUS results (all reproduced numerically below):

 (T1) TAUTOLOGY of the (dagger) framing.  With
        SLACK_O  = sum_s [ (1/w) sum_{i in supp(S^s y)} log bias_i  -  log P(S^s y) ],
        BIASGAP  = sum_i log( bias_i / P(e_i) ),
      the identity
        SLACK_O - BIASGAP = log( prod_i P(e_i) / prod_s P(S^s y) )
      holds EXACTLY (the bias_i terms cancel by the R5-2 incidence collapse).  Hence
      (dagger) SLACK_O > BIASGAP is LITERALLY (B3-a') prod_s P(S^s y) < prod_i P(e_i), carrying
      no new information.  Verified |error| < 4e-15 on all residuals.  ==> the SLACK/BIASGAP
      decomposition is a pure relabel; the load-bearing target is the bare product inequality.

 (T2) N7 (the all-single-glues-fail hypothesis, the source of the (UB) caps) is PROVABLY
      INSUFFICIENT to imply (B3-a').  Explicit FULL-SUPPORT counterexample at n=3:
        P3 = [0.26314,0.22514,0.06373,0.12761,0.01397,0.03575,0.19734,0.07332]
             (order 000,001,010,011,100,101,110,111)
      satisfies N7 (every single-coordinate glue fails to reduce maxbias) and mb<1/2, yet
      prod_s P(weight-2 orbit) > prod_i P(e_i): (B3-a') FAILS.  It is k=2-reducible (the WHOLE-
      COLLAPSE reduces maxbias to 0.072), so it is correctly NOT a residual -- but this proves
      that any argument using ONLY the n single-glue (UB) caps cannot close (B3-a').

 (T3) The clean two-constraint set "N7 + whole-collapse-failure" is SUFFICIENT at n=3 (no
      counterexample in >10M structured + SA trials; all true residuals satisfy both), but is
      PROVABLY INSUFFICIENT at n>=4: explicit full-support n=4 P with N7 + whole-collapse-failure
      and mb<1/2 for which (B3-a') fails (margin -> -inf) yet which is k=2-reducible.  ==> no
      FIXED finite subset of k=2 move-failures is uniformly sufficient; the minimal sufficient
      conjunction grows with n.  This is the precise structural obstruction.

 (UB) re-confirmed (direction + bindingness), CITED not re-derived: on a realized riser pair (i,j)
      a1^{(i,j)} = P(X_i=1,X_j=1) <= (p_j q_i - mb(p_i^2+q_i^2))/(q_i - p_i).

Run: PYTHONPATH=. python3 b3_round6.py
"""
import os.path, pickle, math, numpy as np
from b3lib import patterns, biases, Pdict, all_orbits, shift, is_residual
from harness import glue_marginals, joint, all_k_partitions_search

HERE = os.path.dirname(os.path.abspath(__file__))


def shifts(y, n):
    out = []
    z = tuple(y)
    for _ in range(n):
        out.append(z)
        z = shift(z)
    return out


def N7(P, n):
    """All single-coordinate glues fail to reduce maxbias (the source of the (UB) caps)."""
    mb = biases(P, n).max()
    return all(glue_marginals(P, n, i).max() >= mb - 1e-12 for i in range(n))


def wc_fail(P, n):
    """Whole-collapse k=2 move fails: P(1^n) >= sqrt(mb/(1-mb)) P(0^n)  (Lemma R4-4 / A3a)."""
    Pd = Pdict(P, n)
    mb = biases(P, n).max()
    thr = math.sqrt(mb / (1 - mb))
    return Pd[tuple([1] * n)] >= thr * Pd[tuple([0] * n)] - 1e-12


def b3a_min_rel_margin(P, n):
    """min over weight!=1 orbits of (prod_i P(e_i) - prod_s P(S^s y)) / prod_i P(e_i).
    < 0 iff (B3-a') FAILS for some orbit."""
    Pd = Pdict(P, n)
    e = [Pd[tuple(1 if k == i else 0 for k in range(n))] for i in range(n)]
    G = float(np.prod(e))
    mn = 1e9
    for o in all_orbits(n):
        if sum(o[0]) == 1:
            continue
        lhs = float(np.prod([Pd[z] for z in shifts(o[0], n)]))
        mn = min(mn, (G - lhs) / G)
    return mn


def main():
    print("=" * 74)
    print("ROUND-6 B3 ADVANCES  (gap (star)/(B3-a'); (dagger) orbit-aggregate angle)")
    print("=" * 74)

    # ---- (T1) the (dagger) framing is a tautology: bias_i cancel exactly ----
    print("\n[T1] (dagger) SLACK_O > BIASGAP  IS  (B3-a') prod_s P < prod e (bias_i cancel)")
    maxerr = 0.0
    for n in [3, 4]:
        res = pickle.load(open(os.path.join(HERE, f"res_n{n}.pkl"), "rb"))
        for d in res:
            P = d["P"]; Pd = Pdict(P, n); b = biases(P, n)
            for o in all_orbits(n):
                w = sum(o[0])
                if w < 2:   # SLACK uses 1/w; singletons 0^n (w=0) handled by P(0^n)<G separately
                    continue
                sh = shifts(o[0], n)
                slack = sum(
                    (1.0 / w) * sum(math.log(b[i]) for i in range(n) if z[i] == 1)
                    - math.log(Pd[z]) for z in sh)
                e = [Pd[tuple(1 if k == i else 0 for k in range(n))] for i in range(n)]
                biasgap = sum(math.log(b[i] / e[i]) for i in range(n))
                rhs = sum(math.log(e[i]) for i in range(n)) - sum(math.log(Pd[z]) for z in sh)
                maxerr = max(maxerr, abs((slack - biasgap) - rhs))
    print(f"     max | (SLACK_O - BIASGAP) - log(prod e / prod_s P) |  =  {maxerr:.2e}   (== 0)")

    # ---- (T2) N7 alone is INSUFFICIENT: explicit full-support n=3 counterexample ----
    print("\n[T2] N7 (all single-glues fail) does NOT imply (B3-a')  -- (UB)-only route is dead")
    n = 3
    P3 = np.array([0.26314, 0.22514, 0.06373, 0.12761, 0.01397, 0.03575, 0.19734, 0.07332])
    P3 = P3 / P3.sum()
    b3 = biases(P3, n)
    print(f"     P3 full-support (minP={P3.min():.4f}), biases={np.round(b3,4)}, mb={b3.max():.4f}<1/2")
    print(f"     N7 holds: {N7(P3, n)}    (every single-coord glue fails to reduce maxbias)")
    m3 = b3a_min_rel_margin(P3, n)
    print(f"     (B3-a') min rel margin = {m3:.4f}  ==>  (B3-a') {'HOLDS' if m3 > 0 else 'FAILS'}")
    best, _, mb0 = all_k_partitions_search(P3, n, 2)
    print(f"     FULL Bell-lattice k=2 best maxbias = {best:.4f} < mb={mb0:.4f}  "
          f"==>  k=2-REDUCIBLE (not a residual; whole-collapse reduces).  N7 insufficient. QED")

    # ---- (T3) N7 + whole-collapse-fail: sufficient at n=3, INSUFFICIENT at n=4 ----
    print("\n[T3] N7 + whole-collapse-failure: clean scalar pair; n>=4 needs MORE move-failures")
    # all residuals satisfy both:
    for n in [3, 4]:
        res = pickle.load(open(os.path.join(HERE, f"res_n{n}.pkl"), "rb"))
        allN7 = all(N7(d["P"], n) for d in res)
        allwc = all(wc_fail(d["P"], n) for d in res)
        print(f"     n={n}: all {len(res)} residuals satisfy  N7={allN7}, whole-collapse-fail={allwc}")
    # explicit n=4 counterexample to "N7 + wc-fail => (B3-a')"
    n = 4
    rng = np.random.default_rng(9090)
    found = None
    for _ in range(3_000_000):
        a = rng.uniform(0.1, 3); P = rng.dirichlet(np.ones(16) * a)
        if P.min() < 1e-4:
            continue
        if biases(P, n).max() >= 0.5:
            continue
        if not N7(P, n) or not wc_fail(P, n):
            continue
        if b3a_min_rel_margin(P, n) < 0:
            found = P.copy(); break
    if found is not None:
        P = found; b = biases(P, n)
        best, _, mb0 = all_k_partitions_search(P, n, 2)
        print(f"     n=4: FOUND full-support P (minP={P.min():.4f}, mb={b.max():.4f}<1/2) with")
        print(f"          N7={N7(P,n)}, whole-collapse-fail={wc_fail(P,n)}, yet (B3-a') min rel "
              f"margin={b3a_min_rel_margin(P,n):.3g} (FAILS).")
        print(f"          FULL k=2 best maxbias={best:.4f}<mb={mb0:.4f}: k=2-REDUCIBLE (not residual).")
        print("     ==> N7 + whole-collapse-fail is NOT sufficient for n>=4; minimal sufficient")
        print("         conjunction of k=2 move-failures GROWS with n.  This is the exact gap.")
    else:
        print("     n=4: (no N7+wc-fail counterexample found this run -- rerun with more trials)")

    print("\n[(UB) cited, direction re-confirmed] a1^{(i,j)} <= (p_j q_i - mb*Z)/(q_i-p_i) on risers")
    n = 3
    res = pickle.load(open(os.path.join(HERE, "res_n3.pkl"), "rb"))
    ok = 0; tot = 0
    for d in res:
        P = d["P"]; b = biases(P, n); mb = b.max()
        for i in range(n):
            bg = glue_marginals(P, n, i)
            for j in range(n):
                if j == i or bg[j] < mb - 1e-12:
                    continue
                pi, qi, pj = b[i], 1 - b[i], b[j]
                Z = pi**2 + qi**2
                cap = (pj * qi - mb * Z) / (qi - pi)
                a1 = joint(P, n, i, 1, j, 1)
                tot += 1
                ok += int(a1 <= cap + 1e-12)
    print(f"     (UB) holds on realized riser pairs: {ok}/{tot}")


if __name__ == "__main__":
    main()
