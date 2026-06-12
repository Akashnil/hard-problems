# Faster residual confirmation: vectorized cond_marginals for k=2 partitions.
# A k=2 set partition of 2n coords -> components forced constant. We only need maxbias.
# Reuse all_k_partitions_search but it's the bottleneck. Instead: precompute joint over 2 copies.
import numpy as np, itertools
from b3lib import patterns, biases, maxbias

def fast_is_residual_k2(P,n):
    """Residual iff no k=2 set-partition reduces maxbias. Enumerate partitions of 2n coords.
    Vectorize the conditional-marginal computation using the two-copy joint."""
    pats=list(itertools.product([0,1],repeat=n))
    m=len(pats)
    Parr=np.array(P)
    mb0=maxbias(P,n)
    # two-copy configs: (x,y) with weight P(x)P(y); coords 0..n-1 = x, n..2n-1 = y
    # We'll enumerate set partitions; for each, condition each block constant.
    nk=2*n
    # represent each two-copy config as a length-2n bit vector and weight
    cfgs=[]; ws=[]
    for ix,x in enumerate(pats):
        for iy,y in enumerate(pats):
            cfgs.append(x+y); ws.append(Parr[ix]*Parr[iy])
    cfgs=np.array(cfgs,dtype=np.int8); ws=np.array(ws)
    def partitions(coll):
        coll=list(coll)
        if len(coll)==1: yield [coll]; return
        first=coll[0]
        for sm in partitions(coll[1:]):
            for i in range(len(sm)): yield sm[:i]+[[first]+sm[i]]+sm[i+1:]
            yield [[first]]+sm
    best=np.inf
    for part in partitions(range(nk)):
        # mask configs where every block is constant
        keep=np.ones(len(ws),dtype=bool)
        for block in part:
            if len(block)>1:
                col=cfgs[:,block]
                keep &= (col.min(1)==col.max(1))
        tot=ws[keep].sum()
        if tot<=0: continue
        bm=(cfgs[keep]*ws[keep,None]).sum(0)/tot
        m=bm.max()
        if m<best: best=m
        if best<mb0-1e-12: return False, mb0, best  # reduces -> not residual
    return best>=mb0-1e-12, mb0, best

if __name__=='__main__':
    # sanity vs slow on a few n=3
    from b3lib import is_residual, cheap_reduces
    rng=np.random.default_rng(3)
    import time
    for _ in range(5):
        from harness import rand_P
        P=rand_P(3,rng=rng)
        if maxbias(P,3)>=0.5: continue
        a=is_residual(P,3); b=fast_is_residual_k2(P,3)
        print("slow",a[0],round(a[1],4),round(a[2],4),"| fast",b[0],round(b[1],4),round(b[2],4),"match:",a[0]==b[0])

def _sanity():
    from b3lib import is_residual
    from harness import rand_P
    import numpy as np, time
    rng=np.random.default_rng(11)
    cnt=0; tslow=0; tfast=0
    while cnt<8:
        P=rand_P(3,rng=rng)
        if maxbias(P,3)>=0.5: continue
        cnt+=1
        t=time.time(); a=is_residual(P,3); tslow+=time.time()-t
        t=time.time(); b=fast_is_residual_k2(P,3); tfast+=time.time()-t
        print("slow",a[0],round(a[2],4),"| fast",b[0],round(b[2],4),"match:",a[0]==b[0])
    print(f"slow time {tslow:.2f}s fast time {tfast:.2f}s")
