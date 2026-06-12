import numpy as np
import harness as h
from cyclic import cyclic_glue_marginals

def rand_P_boundary(n,rng):
    """sample P with maxbias near 1/2."""
    m=2**n
    for _ in range(200):
        mode=rng.integers(4)
        if mode==0: w=rng.random(m)
        elif mode==1: w=rng.dirichlet(np.ones(m)*0.3)
        elif mode==2: w=rng.random(m)**4
        else:
            # explicit anti-correlated: heavy on low-weight + some on 1^n
            w=rng.random(m)**3
            # boost 1^n and low weight
            w[-1]*=rng.uniform(1,8)
        w=w/w.sum()
        b=h.biases(w,n)
        if b.max()<0.5 and b.max()>0.40:  # near boundary
            return w
    return None

def combined2(P,n):
    b=h.biases(P,n); mb=b.max()
    best,part,_=h.all_k_partitions_search(P,n,2)
    if best < mb - 1e-13: return 'k2', best, part
    return 'kn', cyclic_glue_marginals(P,n), None

if __name__=='__main__':
    for n in [2,3,4]:
        rng=np.random.default_rng(11000+n)
        valid=0;fails=0;used_kn=0;ff=[]
        trials=20000 if n==2 else (8000 if n==3 else 1500)
        for _ in range(trials):
            P=rand_P_boundary(n,rng)
            if P is None: continue
            b=h.biases(P,n);mb=b.max();valid+=1
            tag,val,part=combined2(P,n)
            if tag=='kn':used_kn+=1
            if not(val<mb-1e-13):
                fails+=1;ff.append((P.copy(),b.copy(),mb,tag,val))
        print(f'n={n}: near-boundary valid={valid} used_kn={used_kn} fails={fails}')
        for f in ff[:8]:
            print('   FAIL biases',np.round(f[1],4),'mb',round(f[2],5),'tag',f[3],'val',round(f[4],5))
