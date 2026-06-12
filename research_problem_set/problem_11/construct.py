import itertools, numpy as np
from itertools import product
import harness as h

def absorb_block_marginals_closed(P,n,B):
    pats=h.patterns(n)
    Bl=set(B)
    A0=0.0;A1=0.0
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
        if u in Bl: out[u]=A1**2/Z
        else: out[u]=(A0*Su0[u]+A1*Su1[u])/Z
    return out

def construct_rule(P,n,verbose=False):
    """Glue i*=argmax across copies, absorb risers into block iteratively until no coord > mb."""
    b=h.biases(P,n)
    mb=b.max()
    istar=int(np.argmax(b))
    B={istar}
    for _ in range(n+1):  # at most n rounds
        bm=absorb_block_marginals_closed(P,n,B)
        if bm is None: return None,B,mb
        # risers = coords with bias >= mb (use >= mb - tiny to be safe; we want strict < mb)
        risers=[u for u in range(n) if bm[u] >= mb - 1e-15 and u not in B]
        if verbose: print('B',sorted(B),'bm',np.round(bm,5),'risers',risers)
        if not risers:
            return bm,B,mb
        for u in risers: B.add(u)
    bm=absorb_block_marginals_closed(P,n,B)
    return bm,B,mb

if __name__=='__main__':
    # stress test the rule on many valid instances
    for n in [2,3,4]:
        rng=np.random.default_rng(100+n)
        modes=['unif','dirichlet_low','anti']
        fails=[];valid=0;trials=30000 if n<=3 else 5000
        for _ in range(trials):
            mode=rng.choice(modes)
            P=h.rand_P(n,mode=mode,rng=rng)
            b=h.biases(P,n); mb=b.max()
            if mb>=0.5: continue
            valid+=1
            bm,B,mb=construct_rule(P,n)
            if bm is None or not (bm.max() < mb - 1e-14):
                fails.append((P.copy(),b.copy(),bm,sorted(B),mb))
        print(f'n={n}: valid={valid} fails={len(fails)}')
        for f in fails[:5]:
            print('  FAIL biases',np.round(f[1],4),'mb',round(f[4],4),'-> bm',np.round(f[2],4) if f[2] is not None else None,'B',f[3])
