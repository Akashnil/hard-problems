import numpy as np
import harness as h
from cyclic import cyclic_glue_marginals

def combined2(P,n):
    """best k=2 full partition; if reduces, use it. Else k=n cyclic."""
    b=h.biases(P,n); mb=b.max()
    best,part,_=h.all_k_partitions_search(P,n,2)
    if best < mb - 1e-13:
        return 'k2', best, part
    bstar=cyclic_glue_marginals(P,n)
    return 'kn', bstar, None

if __name__=='__main__':
    for n in [2,3,4]:
        rng=np.random.default_rng(1300+n)
        modes=['unif','dirichlet_low','anti']
        valid=0;fails=0;used_kn=0;ff=[]
        trials=3000 if n==2 else (1500 if n==3 else 500)
        for _ in range(trials):
            mode=rng.choice(modes);P=h.rand_P(n,mode=mode,rng=rng)
            b=h.biases(P,n);mb=b.max()
            if mb>=0.5:continue
            valid+=1
            tag,val,part=combined2(P,n)
            if tag=='kn':used_kn+=1
            if not(val<mb-1e-13):
                fails+=1;ff.append((P.copy(),b.copy(),mb,tag,val))
        print(f'n={n}: valid={valid} used_kn={used_kn} fails={fails}')
        for f in ff[:6]:
            print('   biases',np.round(f[1],4),'mb',round(f[2],4),'tag',f[3],'val',round(f[4],5))
