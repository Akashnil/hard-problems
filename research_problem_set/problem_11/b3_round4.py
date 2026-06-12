"""Round-4 advances on Lemma B3 (problem_11).

Verifies the RIGOROUS reformulations and conditional chains produced in round 4,
on every independently-isolated residual at n=3,4,5. These are the building blocks
of the round-4 write-up in proof.md (section "Hard step (expanded, R4)").

Run: PYTHONPATH=. python3 b3_round4.py
"""
import os.path, pickle, numpy as np, itertools
from b3lib import (patterns, biases, maxbias, Pdict, all_orbits, orbit, geomean)
from harness import glue_marginals, joint

HERE = os.path.dirname(os.path.abspath(__file__))


def shifts(y, n):
    """The n cyclic shifts S^0 y, ..., S^{n-1} y (with multiplicity if orbit < n)."""
    out = []
    z = list(y)
    for s in range(n):
        zz = tuple(z[(i - 1) % n] for i in range(n)) if s > 0 else tuple(z)
        z = list(zz)
        out.append(zz)
    return out


def check(label, cond, acc):
    acc[0] += 1
    acc[1] += int(cond)
    if not cond:
        print("   VIOLATION:", label)


def main():
    print("=" * 72)
    print("ROUND-4 B3 ADVANCES: rigorous reformulations + conditional chains")
    print("=" * 72)

    # ---- R4-1: orbit-geomean = shift-product identity (PROVED combinatorially) ----
    rng = np.random.default_rng(0)
    ok = True
    for n in [3, 4, 5]:
        P = rng.dirichlet(np.ones(2 ** n))
        Pd = Pdict(P, n)
        for o in all_orbits(n):
            g1 = geomean(o, Pd)
            g2 = float(np.exp(np.mean([np.log(Pd[z]) for z in shifts(o[0], n)])))
            ok &= abs(g1 - g2) < 1e-12
    print(f"\n[R4-1] G(O) = (prod_{{s}} P(S^s y))^(1/n) identity (PROVED): exact={ok}")

    # ---- R4-2: riser upper bound bias_j' <= p_j q_i/(p_i^2+q_i^2) (PROVED for mb<1/2) ----
    bad = 0
    chk = 0
    for n in [3, 4]:
        for _ in range(2000):
            P = rng.dirichlet(np.ones(2 ** n) * rng.uniform(0.2, 2))
            b = biases(P, n)
            if b.max() >= 0.5:
                continue
            chk += 1
            for i in range(n):
                p = b[i]
                q = 1 - p
                Z = p * p + q * q
                g = glue_marginals(P, n, i)
                for j in range(n):
                    if j == i:
                        continue
                    if g[j] > b[j] * q / Z + 1e-12:
                        bad += 1
    print(f"[R4-2] riser bound bias_j' <= p_j q_i/Z on {chk} valid P: violations={bad}")

    # ---- residual-dependent checks ----
    for n in [3, 4, 5]:
        f = os.path.join(HERE, f"res_n{n}.pkl")
        if not os.path.exists(f):
            continue
        res = pickle.load(open(f, "rb"))
        # accumulators: [count, ok]
        a_eham = [0, 0]      # E[ham] = sum bias
        a_decomp = [0, 0]    # E[ham]-1 = sum_{w>=2}P(x)(ham-1) - P(0^n)
        a_b3a = [0, 0]       # (B3-a) shift-product: prod_s P(S^s y) < prod_i P(e_i) for w != 1
        a_wc = [0, 0]        # whole-collapse failure: P(1^n) >= sqrt(mb/(1-mb)) P(0^n)
        a_chain = [0, 0]     # E[ham] >= 1 + [(n-1)sqrt(mb/(1-mb)) - 1] P(0^n)
        a_weak = [0, 0]      # weaker bound mb > 1/((n-1)^2+1)
        a_b3b = [0, 0]       # mb > 1/n
        for d in res:
            P = d["P"]
            Pd = Pdict(P, n)
            pats = patterns(n)
            b = biases(P, n)
            mb = b.max()
            Eham = b.sum()
            p0 = Pd[tuple([0] * n)]
            p1 = Pd[tuple([1] * n)]
            thr = np.sqrt(mb / (1 - mb))
            prodE = float(np.prod([Pd[tuple(1 if k == i else 0 for k in range(n))]
                                   for i in range(n)]))

            check("E[ham]=sum bias", abs(Eham - sum(Pd[x] * sum(x) for x in pats)) < 1e-12, a_eham)
            lhs = sum(Pd[x] * (sum(x) - 1) for x in pats if sum(x) >= 2)
            check("decomp", abs((Eham - 1) - (lhs - p0)) < 1e-12, a_decomp)
            for y in pats:
                if sum(y) == 1:
                    continue
                prodY = float(np.prod([Pd[z] for z in shifts(y, n)]))
                check(f"B3a {y}", prodY < prodE - 1e-18, a_b3a)
            check("wc-fail", p1 >= thr * p0 - 1e-12, a_wc)
            check("chain", Eham >= 1 + ((n - 1) * thr - 1) * p0 - 1e-9, a_chain)
            check("weak", mb > 1.0 / ((n - 1) ** 2 + 1), a_weak)
            check("b3b", mb > 1.0 / n + 1e-12, a_b3b)

        print(f"\nn={n}: {len(res)} residuals")
        print(f"  E[ham]=sum bias (identity)                 : {a_eham[1]}/{a_eham[0]}")
        print(f"  E[ham]-1 = sum_{{w>=2}}P(ham-1) - P(0^n)     : {a_decomp[1]}/{a_decomp[0]}")
        print(f"  (B3-a) prod_s P(S^s y) < prod_i P(e_i)      : {a_b3a[1]}/{a_b3a[0]}")
        print(f"  whole-collapse fail P(1^n)>=sqrt..P(0^n)    : {a_wc[1]}/{a_wc[0]}")
        print(f"  chain E[ham] >= 1+[(n-1)sqrt-1]P(0^n)       : {a_chain[1]}/{a_chain[0]}")
        print(f"  weaker bound mb > 1/((n-1)^2+1)             : {a_weak[1]}/{a_weak[0]}")
        print(f"  (B3-b) mb > 1/n                             : {a_b3b[1]}/{a_b3b[0]}")


if __name__ == "__main__":
    main()
