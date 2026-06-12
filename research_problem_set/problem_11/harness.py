import itertools, numpy as np
from itertools import product

def rand_P(n, mode='unif', rng=None):
    rng = rng or np.random
    m = 2**n
    if mode=='unif':
        w = rng.random(m)
    elif mode=='dirichlet_low':
        w = rng.dirichlet(np.ones(m)*0.3)
        return w/ w.sum()
    elif mode=='anti':
        # put more mass on patterns that are anti-correlated; just heavy-tailed
        w = rng.random(m)**4
    w = w/ w.sum()
    return w

def patterns(n):
    return list(product([0,1], repeat=n))

def biases(P, n):
    pats = patterns(n)
    b = np.zeros(n)
    for idx,x in enumerate(pats):
        for i in range(n):
            if x[i]==1: b[i]+=P[idx]
    return b

def maxbias(P,n):
    return biases(P,n).max()

# single cross-copy same-coordinate glue: k=2, equate coord i of copy0 with coord i of copy1.
# closed form from scout: by symmetry both copies have identical marginals.
# bias_i' = p_i^2/Z, Z=p_i^2+q_i^2
# bias_j' = [P(Xj=1,Xi=1) p_i + P(Xj=1,Xi=0) q_i]/Z
def joint(P,n,j,vj,i,vi):
    pats=patterns(n); s=0
    for idx,x in enumerate(pats):
        if x[j]==vj and x[i]==vi: s+=P[idx]
    return s

def glue_marginals(P,n,i):
    b=biases(P,n)
    p_i=b[i]; q_i=1-p_i
    Z=p_i**2+q_i**2
    out=np.zeros(n)
    for j in range(n):
        if j==i:
            out[j]=p_i**2/Z
        else:
            a1=joint(P,n,j,1,i,1)
            a0=joint(P,n,j,1,i,0)
            out[j]=(a1*p_i+a0*q_i)/Z
    return out

# verify glue_marginals against brute force
def brute_glue(P,n,i):
    pats=patterns(n)
    # two copies, coords 0..n-1 and n..2n-1; condition copy0[i]==copy1[i]
    tot=0; numer=np.zeros(2*n); 
    weights={}
    for x in pats:
        for y in pats:
            if x[i]==y[i]:
                w=P[pats.index(x)]*P[pats.index(y)]
                z=tuple(x)+tuple(y)
                weights[z]=w; tot+=w
    bm=np.zeros(2*n)
    for z,w in weights.items():
        for c in range(2*n):
            if z[c]==1: bm[c]+=w
    bm/=tot
    return bm  # first n should match glue_marginals

if __name__=='__main__':
    rng=np.random.default_rng(0)
    for _ in range(5):
        n=3; P=rand_P(n,rng=rng)
        i=0
        cf=glue_marginals(P,n,i)
        bf=brute_glue(P,n,i)
        print("closed:",np.round(cf,5),"brute first n:",np.round(bf[:n],5),"match:",np.allclose(cf,bf[:n]))

def odds_sum(b):
    return np.sum(b/(1-b))

def odds_max(b):
    return np.max(b/(1-b))

def log_odds_sum(b):
    return np.sum(np.log(b/(1-b)))

def test_potential(n, ntrials, modes, rng):
    res = {'maxbias_best_glue_fail':0,'oddsum_best_glue_fail':0,'oddsmax_best_glue_fail':0,
           'maxbias_argmax_fail':0,'count':0}
    fails_oddsum=[]
    fails_maxbias=[]
    for _ in range(ntrials):
        mode=modes[np.random.default_rng().integers(len(modes))] if False else rng.choice(modes)
        P=rand_P(n,mode=mode,rng=rng)
        b=biases(P,n)
        if b.max()>=0.5: continue  # only valid instances
        res['count']+=1
        mb=b.max()
        os0=odds_sum(b); om0=odds_max(b)
        # try every coordinate i for the single cross-copy glue
        best_mb=np.inf; best_os=np.inf; best_om=np.inf
        argmax=int(np.argmax(b))
        for i in range(n):
            bg=glue_marginals(P,n,i)
            best_mb=min(best_mb,bg.max())
            best_os=min(best_os,odds_sum(bg))
            best_om=min(best_om,odds_max(bg))
            if i==argmax:
                argmax_mb=bg.max()
        if not(best_mb<mb-1e-12): res['maxbias_best_glue_fail']+=1; fails_maxbias.append((P,b))
        if not(best_os<os0-1e-12): res['oddsum_best_glue_fail']+=1; fails_oddsum.append((P,b))
        if not(best_om<om0-1e-12): res['oddsmax_best_glue_fail']+=1
        if not(argmax_mb<mb-1e-12): res['maxbias_argmax_fail']+=1
    return res, fails_oddsum, fails_maxbias

if __name__=='__main__' and False:
    pass

def cond_marginals_general(P, n, k, S):
    """General: k copies (coords 0..nk-1, copy c coord i -> c*n+i), condition X_u==X_v for (u,v) in S.
    Return marginals of all nk coords. Use union-find -> components forced constant."""
    nk=n*k
    parent=list(range(nk))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[ra]=rb
    for (u,v) in S: union(u,v)
    comps={}
    for c in range(nk):
        comps.setdefault(find(c),[]).append(c)
    complist=list(comps.values())
    pats=patterns(n)
    Pd={tuple(x):P[idx] for idx,x in enumerate(pats)}
    # iterate over all copy assignments
    tot=0.0; bm=np.zeros(nk)
    for assign in product(pats, repeat=k):
        # assign[c] is the value vector of copy c
        full=[]
        for c in range(k):
            full.extend(assign[c])
        ok=True
        for comp in complist:
            vals={full[c] for c in comp}
            if len(vals)>1: ok=False;break
        if not ok: continue
        w=1.0
        for c in range(k): w*=Pd[assign[c]]
        tot+=w
        for c in range(nk):
            if full[c]==1: bm[c]+=w
    if tot==0: return None
    bm/=tot
    return bm

def all_k2_partitions_search(P,n,maxpairs=3):
    """Search best maxbias over k=2 partitions with up to maxpairs cross pairs (any u,v in 0..2n-1)."""
    import itertools as it
    nk=2*n
    allpairs=[(u,v) for u in range(nk) for v in range(u+1,nk)]
    mb0=maxbias(P,n)
    best=np.inf; bestS=None
    for r in range(1,maxpairs+1):
        for S in it.combinations(allpairs,r):
            bm=cond_marginals_general(P,n,2,list(S))
            if bm is None: continue
            m=bm.max()
            if m<best: best=m; bestS=S
    return best,bestS,mb0

def all_k_partitions_search(P,n,k,maxpairs=None):
    """Search over ALL set-partitions of nk coords (full design space for given k), best maxbias.
    Use Bell-number enumeration of partitions of nk elements."""
    import itertools as it
    nk=n*k
    mb0=maxbias(P,n)
    best=np.inf; bestpart=None
    # enumerate set partitions of range(nk)
    def partitions(collection):
        collection=list(collection)
        if len(collection)==1:
            yield [collection]; return
        first=collection[0]
        for smaller in partitions(collection[1:]):
            for i,subset in enumerate(smaller):
                yield smaller[:i]+[[first]+subset]+smaller[i+1:]
            yield [[first]]+smaller
    for part in partitions(range(nk)):
        # build S from partition (chain edges within each block)
        S=[]
        for block in part:
            for a,b in zip(block,block[1:]):
                S.append((a,b))
        bm=cond_marginals_general(P,n,k,S)
        if bm is None: continue
        m=bm.max()
        if m<best: best=m; bestpart=part
    return best,bestpart,mb0
