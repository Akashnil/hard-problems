# Entropy-method literature digests — Frankl's union-closed conjecture

Constant identity: 1 - 1/phi = (3 - sqrt5)/2 = 0.38196601125... (smaller root of x^2-3x+1=0).

## Gilmer 2022 (arXiv:2211.09055), "A constant lower bound..."
- Method: A,B iid uniform on union-closed F (binary strings, OR-closed). C = A OR B.
  Since A is uniform on its support and C is supported on F (OR-closed), H[C] <= H[A] = log2|F|.
  Chain rule + data processing: H[C] >= sum_i E[h(p_i q_i)] where p_i=Pr(A_i=0|prefix), q_i similar.
  Core lemma: if p,q iid in [0,1] with E >= constant, then E[h(pq)] vs E[h(p)] gives the bound.
- Value: first constant bound ~0.01, conjectured pushable to (3-sqrt5)/2.

## Alweiss-Huang-Sellke (arXiv:2211.11504), Chase-Lovett, Pebody, Sawin (late 2022)
- Independently sharpened Gilmer to the tight iid value c = (3-sqrt5)/2 = 1-1/phi = 0.38197.
- Tightness hinges on minimizing h(x)/... type ratio; the binary-entropy inequality (arXiv:2301.09664).
- Chase-Lovett proved the iid approach is SHARP for *approximate* union-closed families:
  the family F = (k=psi*n+g(n)) U (k>=(1-psi)n) with psi=(3-sqrt5)/2 is approx union-closed and
  has min frequency ~psi. This SUGGESTED 0.382 was the ceiling of the iid OR method.

## Sawin (note, late 2022) — escapes the iid ceiling
- Observation: the approx-union-closed sharp example only blocks the *iid independent* sampling.
  If B is sampled DEPENDENTLY on A (element-wise, both still marginally uniform on F, but
  negatively correlated so unions are smaller / land in F more often), one can do strictly better.
- Sawin's element-wise dependent coupling -> the union has size ~(0.5+o(1))n for the bad example.

## Yu (arXiv:2212.00658) "Dimension-Free Bounds"
- Formalized Sawin's idea as an optimization; used Krein-Milman to bound support of the joint
  distribution by 4 values; numerically obtained ~0.38234.

## Cambie (arXiv:2212.12500) "Better bounds ... entropy approach"  *** KEY PAPER ***
- Solves Sawin's "Question 2" EXACTLY: max c with alpha in [0,1] s.t. for all iid p,q,r in [0,1]
  with E < c (p,q indep; p,r arbitrarily/negatively correlated):
    (1-alpha) E[H(p+q-pq)] + alpha E[H(max(p,r,min(p+r,1/2)))] >= E[H(p)].
- Theorem 3: union-closed bound c ~ 0.3823455.
- *** CEILING RESULT (Subsec 2.3) ***: the answer to Question 2 is EXACTLY
    c = 0.382345533366703  and this is SHARP for Sawin's approach.
  Sharp construction: 2-atom distribution P(p=1)=a, P(p=b)=1-a with b=b2~0.32945 (root of
  h(x)(2-h(x)) - h(2x-x^2)), a~0.078877; at this point both entropy terms EQUAL E[H(p)], so no
  linear combination beats it strictly; local perturbation (raising a) gives counterexamples once
  c is larger. => "one cannot aim to prove the result with a constant better than 0.382345533366703
  with the exact suggested approach of Sawin." Linear combination is NECESSARY (single term gives <0.37).

## Liu (arXiv:2306.08824) "Conditionally IID Coupling"  *** CURRENT RECORD ***
- Different coupling: A,B iid CONDITIONED on an auxiliary random variable (richer than Sawin's
  two-strategy linear combination). New class of finite-dimensional optimization bounds.
- Value: c ~ 0.38271 (defined as solution of an analytic equation). Best published entropy bound.

## Ellis-Ivan-Leader 2023 (smallest-set obstruction) — relevant to Avenue B
- For every k there is a union-closed family whose unique smallest set has size k, yet each element
  of that smallest set has frequency only (1+o(1)) log k /(2k) -> 0.
- => "focusing on the smallest set cannot work in the strongest possible sense." Directly kills the
  intuition that concentrating mass near small/empty sets exposes a frequent element.

## Bottom line on the ceiling
- iid OR method: provably tight at (3-sqrt5)/2 = 0.38197 (Chase-Lovett approx-union-closed example).
- Sawin's element-wise dependent two-sample linear-combination method: provably tight at 0.3823455
  (Cambie, Subsec 2.3 — explicit sharp 2-atom distribution).
- Richer conditional-iid coupling (Liu): 0.38271. Still far below 1/2.
- No single-element-at-a-time two-sample entropy comparison H[C] vs H[A] is known to reach 1/2;
  each refinement buys ~1e-3 to 1e-4 and meets a provable sharp barrier. Cambie's own paper states
  the constant is "not 1/2 and another core method will be needed for the full resolution."
