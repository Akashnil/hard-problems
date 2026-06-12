"""Round-5 advances on Lemma B3 (problem_11), Angle 1 (orbit-average reduction of B3-a').

This round establishes / re-confirms:

  (R5-1) [PROVED, general, no residual] Monotone-support bound:
         for every full-support P and every pattern z of weight w>=1,
             P(z) <= min_{i in supp(z)} bias_i <= GM_{i in supp(z)} bias_i.
  (R5-2) [PROVED, combinatorial] Cyclic incidence: each coordinate i appears in
         exactly w of the n cyclic shifts S^0 y,...,S^{n-1} y of a weight-w pattern y.
  (R5-3) [PROVED, R5-1 + R5-2 + AM-GM] Shift-product cap:
             prod_{s=0}^{n-1} P(S^s y)  <=  prod_{i=1}^{n} bias_i
         for every pattern y with weight w >= 1.  (General, no residual.)
  (R5-4) [VERIFIED safe-direction AM-GM, the survey's step-2]:
             prod_s P(S^s y) <= Pbar_O^n,   Pbar_O = (1/d) sum_{z in O} P(z).
  (R5-5) [VERIFIED, residual-only] Orbit-average facts (0 violations on all residuals):
             Pbar_O < AM_i(P(e_i)),  Pbar_O < max_i P(e_i),
             P(0^n) < G(O_1),  P(1^n) < G(O_1),
         where G(O_1) = (prod_i P(e_i))^{1/n}.
  (BROKEN, recorded) the survey's M_w/d route: M_1/d >= G(O_1) ALWAYS, and
         M_w/d >= Pbar_O ALWAYS -- so M_w/d < G(O_1) is strictly stronger than (star)
         and routes the wrong way.  Confirmed numerically here.

  OPEN (the exact remaining gap):
     (star)  Pbar_O < G(O_1)  for every orbit O of weight != 1.
     Equivalently (and the actual need, via AM-GM step R5-4):
     (B3-a') prod_s P(S^s y) < prod_i P(e_i)  for ham(y) != 1.
   Both are RESIDUAL facts (fail ~55% on general mb<1/2 P; 0 violations on all residuals).

Run: PYTHONPATH=. python3 b3_round5.py
"""
import os.path, pickle, numpy as np, itertools
from b3lib import (patterns, biases, maxbias, Pdict, all_orbits, orbit, geomean)
from harness import glue_marginals

HERE = os.path.dirname(os.path.abspath(__file__))


def shift(x):
    n = len(x)
    return tuple(x[(i - 1) % n] for i in range(n))


def shifts(y, n):
    out = []
    z = tuple(y)
    for s in range(n):
        out.append(z)
        z = shift(z)
    return out


def main():
    rng = np.random.default_rng(12345)
    print("=" * 72)
    print("ROUND-5 B3 ADVANCES (Angle 1: orbit-average reduction of B3-a')")
    print("=" * 72)

    # ---- R5-1: P(z) <= min_supp bias_i <= GM_supp bias_i  (general, PROVED monotonicity) ----
    bad1 = 0
    tot1 = 0
    for n in [3, 4, 5]:
        for _ in range(3000):
            P = rng.dirichlet(np.ones(2 ** n) * rng.uniform(0.1, 2))
            b = biases(P, n)
            Pd = Pdict(P, n)
            for z in patterns(n):
                w = sum(z)
                if w < 1:
                    continue
                tot1 += 1
                gm = float(np.prod([b[i] for i in range(n) if z[i] == 1]) ** (1.0 / w))
                if Pd[z] > gm + 1e-14:
                    bad1 += 1
    print(f"\n[R5-1] P(z) <= GM_supp(bias_i)  (general): violations = {bad1}/{tot1}")

    # ---- R5-2: cyclic incidence ----
    inc_ok = True
    for n in [3, 4, 5, 6]:
        for y in patterns(n):
            w = sum(y)
            if w == 0:
                continue
            cnt = np.zeros(n, dtype=int)
            for z in shifts(y, n):
                for i in range(n):
                    cnt[i] += z[i]
            if not all(c == w for c in cnt):
                inc_ok = False
    print(f"[R5-2] cyclic incidence (each coord in exactly w of n shifts): {inc_ok}")

    # ---- R5-3: prod_s P(S^s y) <= prod_i bias_i  (general, PROVED) ----
    bad3 = 0
    tot3 = 0
    for n in [3, 4, 5]:
        for _ in range(3000):
            P = rng.dirichlet(np.ones(2 ** n) * rng.uniform(0.1, 2))
            b = biases(P, n)
            Pd = Pdict(P, n)
            pb = float(np.prod(b))
            for y in patterns(n):
                if sum(y) < 1:
                    continue
                tot3 += 1
                lhs = float(np.prod([Pd[z] for z in shifts(y, n)]))
                if lhs > pb + 1e-18:
                    bad3 += 1
    print(f"[R5-3] prod_s P(S^s y) <= prod_i bias_i  (general): violations = {bad3}/{tot3}")

    # ---- residual checks ----
    for n in [3, 4, 5]:
        f = os.path.join(HERE, f"res_n{n}.pkl")
        if not os.path.exists(f):
            continue
        res = pickle.load(open(f, "rb"))

        a_amgm = [0, 0]    # R5-4: prod_s P <= Pbar^n
        a_star = [0, 0]    # (star): Pbar_O < G(O1)
        a_b3a = [0, 0]     # (B3-a'): prod_s P < prod e_i
        a_AM = [0, 0]      # Pbar < AM(e)
        a_MAX = [0, 0]     # Pbar < max(e)
        a_sing = [0, 0]    # P(0^n),P(1^n) < G
        a_capgap = [0, 0]  # PROVED cap holds: prod_s P <= prod bias on residuals
        # broken survey route
        a_M1d = [0, 0]     # M_1/d >= G(O1)  (broken: should be 100%)
        a_Mwd = [0, 0]     # M_w/d >= Pbar   (broken: should be 100%)

        min_star_rel = 1e9
        for d in res:
            P = d["P"]
            Pd = Pdict(P, n)
            b = biases(P, n)
            e = [Pd[tuple(1 if k == i else 0 for k in range(n))] for i in range(n)]
            G = float(np.prod(e) ** (1.0 / n))
            AM = float(np.mean(e))
            emax = max(e)
            M1 = sum(e)
            pb = float(np.prod(b))
            p0 = Pd[tuple([0] * n)]
            p1 = Pd[tuple([1] * n)]
            # layer masses
            Mw = {}
            for x in patterns(n):
                w = sum(x)
                Mw[w] = Mw.get(w, 0.0) + Pd[x]

            a_sing[0] += 2
            a_sing[1] += int(p0 < G) + int(p1 < G)

            for o in all_orbits(n):
                w = sum(o[0])
                if w == 1:
                    continue
                dlen = len(o)
                pbar = float(np.mean([Pd[z] for z in o]))
                prods = float(np.prod([Pd[z] for z in shifts(o[0], n)]))
                # R5-4 AM-GM safe direction
                a_amgm[0] += 1
                a_amgm[1] += int(prods <= pbar ** n + 1e-15)
                # (star)
                a_star[0] += 1
                a_star[1] += int(pbar < G)
                min_star_rel = min(min_star_rel, (G - pbar) / G)
                # B3-a'
                a_b3a[0] += 1
                a_b3a[1] += int(prods < G ** n - 1e-18)
                # Pbar < AM, < max
                a_AM[0] += 1; a_AM[1] += int(pbar < AM)
                a_MAX[0] += 1; a_MAX[1] += int(pbar < emax)
                # PROVED cap on residuals
                a_capgap[0] += 1; a_capgap[1] += int(prods <= pb + 1e-18)
                # broken survey route
                a_M1d[0] += 1; a_M1d[1] += int(M1 / dlen >= G - 1e-15)
                a_Mwd[0] += 1; a_Mwd[1] += int(Mw[w] / dlen >= pbar - 1e-15)

        print(f"\nn={n}: {len(res)} residuals")
        print(f"  [R5-4] prod_s P <= Pbar^n (safe AM-GM)         : {a_amgm[1]}/{a_amgm[0]}")
        print(f"  [R5-3 on residuals] prod_s P <= prod bias_i    : {a_capgap[1]}/{a_capgap[0]}")
        print(f"  (star)  Pbar_O < G(O1)   [OPEN]                : {a_star[1]}/{a_star[0]}  min rel margin={min_star_rel:.4f}")
        print(f"  (B3-a') prod_s P < prod e_i [OPEN, = via R5-4] : {a_b3a[1]}/{a_b3a[0]}")
        print(f"  Pbar_O < AM_i(e_i)  [VERIFIED]                 : {a_AM[1]}/{a_AM[0]}")
        print(f"  Pbar_O < max_i(e_i) [VERIFIED]                 : {a_MAX[1]}/{a_MAX[0]}")
        print(f"  P(0^n),P(1^n) < G(O1) [VERIFIED]               : {a_sing[1]}/{a_sing[0]}")
        print(f"  BROKEN survey route M_1/d >= G(O1) (=100%)     : {a_M1d[1]}/{a_M1d[0]}")
        print(f"  BROKEN survey route M_w/d >= Pbar  (=100%)     : {a_Mwd[1]}/{a_Mwd[0]}")


if __name__ == "__main__":
    main()
