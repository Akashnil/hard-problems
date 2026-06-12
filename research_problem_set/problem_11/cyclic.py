import itertools, numpy as np
from itertools import product
import harness as h

def cyclic_glue_marginals(P,n):
    """k=n full-cycle glue: force copy c = S^c (cyclic shift) of copy 0.
    Feasible configs: orbit tuples (x, Sx, ..., S^{n-1}x), weight w(x)=prod_c P(S^c x).
    All marginals equal b* = sum_x w(x)*ham(x)/n / sum_x w(x)."""
    pats=h.patterns(n)
    def shift(x):  # S: (x_{sigma^-1(i)}); define S^c x as rotate
        return tuple(x[(i-1)%n] for i in range(n))  # one rotation
    Z=0.0; num=0.0
    for x in pats:
        w=1.0
        y=tuple(x)
        for c in range(n):
            w*=P[pats.index(y)]
            y=shift(y)
        ham=sum(x)
        Z+=w; num+=w*(ham/n)
    if Z==0: return None
    return num/Z

def cyclic_brute(P,n):
    """brute force k=n full cycle glue, return common marginal (verify)."""
    # glue (c,i) ~ (c+1 mod n, (i+1) mod n)? Let's match spec: force each copy a cyclic shift of copy0.
    # Use cond_marginals_general with S gluing (c,i)~(c+1 mod n, sigma(i)) sigma=(i+1)%n
    S=[]
    k=n
    for c in range(k):
        for i in range(n):
            u=c*n+i
            v=((c+1)%k)*n + ((i+1)%n)
            S.append((u,v))
    bm=h.cond_marginals_general(P,n,k,S)
    return bm

if __name__=='__main__':
    rng=np.random.default_rng(7)
    for _ in range(8):
        n=3;P=h.rand_P(n,mode='anti',rng=rng)
        b=h.biases(P,n)
        if b.max()>=0.5: continue
        cf=cyclic_glue_marginals(P,n)
        bf=cyclic_brute(P,n)
        print('biases',np.round(b,4),'b*_closed',round(cf,5),'brute',np.round(bf,5) if bf is not None else None)
