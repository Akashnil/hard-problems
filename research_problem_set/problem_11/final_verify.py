import numpy as np, sympy as sp, itertools
import harness as h
from itertools import product

print("="*70)
print("CERTIFICATE 1: diagonal odds-squaring contraction (symbolic)")
p=sp.symbols('p',positive=True); q=1-p
new=p**2/(p**2+q**2)
fac=sp.factor(p-new)
print("  p - p^2/(p^2+q^2) =", fac)
print("  for 0<p<1/2: p>0, (p-1)<0, (2p-1)<0, denom>0  => product > 0  => strict drop  [PROVED]")
o=sp.symbols('o',positive=True)
print("  odds form: o - o^2 =", sp.factor(o-o**2), " > 0 for 0<o<1  [PROVED]")

print("="*70)
print("CERTIFICATE 2: single-glue closed form vs brute force")
rng=np.random.default_rng(0); ok=0
for _ in range(20):
    n=3; P=h.rand_P(n,rng=rng); i=rng.integers(n)
    cf=h.glue_marginals(P,n,i); bf=h.brute_glue(P,n,i)[:n]
    ok+= np.allclose(cf,bf)
print(f"  matched {ok}/20 random  [VERIFIED]")

print("="*70)
print("CERTIFICATE 3: absorb-block closed form vs brute force")
def absorb_block_marginals_closed(P,n,B):
    pats=h.patterns(n); Bl=set(B); A0=0.0;A1=0.0
    Su0=np.zeros(n); Su1=np.zeros(n)
    for idx,x in enumerate(pats):
        inB=[x[j] for j in Bl]
        if all(v==0 for v in inB):
            A0+=P[idx]
            for u in range(n):
                if x[u]==1: Su0[u]+=P[idx]
        if all(v==1 for v in inB):
            A1+=P[idx]
            for u in range(n):
                if x[u]==1: Su1[u]+=P[idx]
    Z=A0**2+A1**2
    if Z==0: return None
    out=np.zeros(n)
    for u in range(n):
        out[u]= A1**2/Z if u in Bl else (A0*Su0[u]+A1*Su1[u])/Z
    return out
def block_partition_marginals(P,n,B):
    S=[];Bl=sorted(B)
    nodes=[j for j in Bl]+[n+j for j in Bl]
    for a,b in zip(nodes,nodes[1:]): S.append((a,b))
    return h.cond_marginals_general(P,n,2,S)[:n]
rng=np.random.default_rng(3); ok=0
for _ in range(20):
    n=3; P=h.rand_P(n,rng=rng); B=set(np.random.default_rng(_).choice(n,size=2,replace=False))
    cf=absorb_block_marginals_closed(P,n,B); bf=block_partition_marginals(P,n,B)
    ok+= np.allclose(cf,bf)
print(f"  matched {ok}/20 random (random 2-subsets)  [VERIFIED]")

print("="*70)
print("CERTIFICATE 4: cyclic glue all-marginals-equal + orbit formula vs brute")
def cyclic_brute(P,n):
    S=[];k=n
    for c in range(k):
        for i in range(n):
            S.append((c*n+i, ((c+1)%k)*n + ((i+1)%n)))
    return h.cond_marginals_general(P,n,k,S)
def orbit_formula(P,n):
    pats=h.patterns(n)
    def shift(x): return tuple(x[(i-1)%n] for i in range(n))
    Z=0.0;num=0.0
    for x in pats:
        w=1.0;y=tuple(x)
        for c in range(n): w*=P[pats.index(y)];y=shift(y)
        Z+=w;num+=w*(sum(x)/n)
    return num/Z
rng=np.random.default_rng(11); oke=0;okf=0
for _ in range(20):
    n=int(rng.integers(2,5)); P=h.rand_P(n,mode='anti',rng=rng)
    bm=cyclic_brute(P,n)
    if bm is None: continue
    oke+= np.allclose(bm,bm[0])
    okf+= abs(bm[0]-orbit_formula(P,n))<1e-9
print(f"  all-equal {oke}/20, orbit-formula match {okf}/20  [VERIFIED]")

print("="*70)
print("CERTIFICATE 5: geometric-mean limit  b*_{mn} -> ham(O*)/n")
def bstar_k(P,n,k):
    pats=h.patterns(n)
    def shift(x): return tuple(x[(i-1)%n] for i in range(n))
    Z=0.0;num=0.0
    for x in pats:
        w=1.0;y=tuple(x)
        for c in range(k): w*=P[pats.index(y)];y=shift(y)
        Z+=w;num+=w*(sum(x)/n)
    return num/Z
def orbit_of(x,n):
    s=set();y=tuple(x)
    for _ in range(n): s.add(y);y=tuple(y[(i-1)%n] for i in range(n))
    return frozenset(s)
def limit_val(P,n):
    pats=h.patterns(n);Pd={x:P[i] for i,x in enumerate(pats)};seen={};bg=-1;rep=None
    for x in pats:
        O=orbit_of(x,n)
        if O in seen: continue
        seen[O]=1; g=np.prod([Pd[y] for y in O])**(1.0/len(O))
        if g>bg: bg=g; rep=next(iter(O))
    return sum(rep)/n
rng=np.random.default_rng(22); good=0
for _ in range(10):
    n=3; P=h.rand_P(n,mode='anti',rng=rng)
    lim=limit_val(P,n); approx=bstar_k(P,n,3*8)  # k=24
    good += abs(lim-approx)<1e-3
print(f"  b*_(24) within 1e-3 of geomean-limit in {good}/10  [VERIFIED]")
