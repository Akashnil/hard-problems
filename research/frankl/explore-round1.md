## frankl  (C_frankl: Frankl's union-closed sets conjecture — max element bias >= 1/2; entropy/information-theoretic approach)

- Current bounds (entropy method): lower = 0.38271 [Liu, arXiv:2306.08824, "conditionally iid coupling"], target = 0.5 (the conjecture, OPEN).
  - Gilmer 2022 [arXiv:2211.09055]: first constant ~0.01.
  - iid OR method tight value = (3-sqrt5)/2 = 1-1/phi = 0.3819660... [Alweiss-Huang-Sellke 2211.11504, Chase-Lovett, Pebody, Sawin].
  - Sawin dependent two-sample linear combination, solved exactly by Cambie [arXiv:2212.12500]: 0.3823455.
  - Liu [arXiv:2306.08824]: 0.38271 — CURRENT RECORD for the entropy method.
  Verified identity: 1-1/phi = (3-sqrt5)/2 = 0.38196601125 (both forms in the Frankl file/run_state agree).

- Softer target: there is NO genuinely soft side here. The "lower bound" (this constant) is the only attackable side, but it sits behind a stack of PROVEN sharpness barriers, each refinement buying ~1e-3 to 1e-4. The mandated jump to 1/2 (delta = +0.117) is a famous open problem; no entropy variant has come within 0.11 of it. Treat any "reached 1/2" claim as almost certainly a bug. Realistic deliverable: a precise obstruction write-up (the run_state's explicit fallback), not a bound improvement.

- How the record was achieved (from the papers, full bodies read):
  - Gilmer/iid: A,B iid uniform on OR-closed F; C=A OR B is supported on F, so H[C] <= H[A]=log2|F|. Chain rule + data processing gives H[C] >= sum_i E[h(p_i q_i)] (p_i,q_i = Pr(coord=0 | prefix)). A binary-entropy lemma (arXiv:2301.09664) closes it at (3-sqrt5)/2. SHARP: Chase-Lovett's approximate-union-closed family ([n] choose psi*n+g(n)) U ([n] choose >=(1-psi)n), psi=(3-sqrt5)/2, attains it.
  - Sawin/Cambie: sample B element-wise DEPENDENT on A (both still marginally uniform on F, negatively correlated so unions are smaller and land in F more often), take a linear combination of the iid strategy and the dependent strategy. Cambie solves Sawin's "Question 2" EXACTLY and proves the sharp value 0.382345533366703 via an explicit 2-atom distribution (P(p=1)=a~0.0789, P(p=b)=1-a, b~0.32945).
  - Liu: A,B iid CONDITIONED on an auxiliary variable (richer coupling than Sawin's two-strategy mix) -> 0.38271, defined by an analytic equation.

- Where the slack is (honest): essentially none in the single-coordinate two-sample entropy comparison. Cambie Subsec 2.3 PROVES Sawin's exact approach cannot exceed 0.3823455; Liu's auxiliary-variable coupling only reaches 0.38271. Cambie's paper itself states the constant "is not 1/2 and another core method will be needed for the full resolution." Any further gain must come from a genuinely different object than "compare H[A OR B] to H[A] coordinate-by-coordinate."

- Assessment of the two mandated avenues:
  - Avenue A (fractional unions Q_t = Q^t via Mobius inversion): I implemented it. sum P_t = 1 always (Q(top)=1). For INTEGER t it is exactly the OR of t iid samples. For non-integer t it is in general a SIGNED measure (nonnegativity is not guaranteed for non-distributive union-closed posets; only special lattices stay nonnegative). Decisive numerical result: for every t>1 where P_t is a valid distribution, bias INCREASES (good direction) but H[P_t] STRICTLY DECREASES (dH<0, e.g. t=1.1 -> dH=-0.0064, t=2 -> dH=-0.34). So Avenue A is a textbook instance of "perturbing uniform A lowers entropy." It cannot produce H[C]>H[A]. The "1+epsilon samples" idea is analytically coherent only as a signed-measure interpolation, not as a probability distribution, and it moves entropy the wrong way.
  - Avenue B (B concentrated on 0^n): C = A OR B. As mass(B at empty)->1, C->A, so H[C]->H[A]^- from below and bias->bias(A); there is NO regime where H[C]>H[A] (again uniform A is the entropy max on its support, and C stays supported on F). Worse, the smallest-set intuition behind B is killed outright by Ellis-Ivan-Leader 2023: there exist union-closed families whose unique smallest set has size k but every element of it has frequency only (1+o(1))(log k)/(2k) -> 0. So "concentrate near the bottom to expose a frequent element" provably fails.

- Honest assessment of the Frankl file's central claim ("exploit the false hypothesis to paradoxically force H[C]>H[A]"): This is a TRAP, not a sound program. C is always supported on the OR-closed family F, A is uniform on F, hence H[C] <= H[A] = log2|F| is an unconditional theorem (max-entropy of uniform), INDEPENDENT of any hypothesis about bias. The bias hypothesis (<1/2) does not and cannot reverse this. Gilmer's contradiction works the OTHER way: he keeps the true H[C] <= H[A] and shows the false bias hypothesis forces a LOWER bound on H[C] that exceeds H[A] — the false hypothesis inflates the conditional-entropy sum, it does not make the actual H[C] exceed H[A]. The Frankl file inverts this and asks to make the *actual* H[C] exceed H[A] by a perturbation; that is mathematically impossible for any C supported on F. The phrase "standard calculation gives H[C]<H[A] but that does not mean the construction failed" is exactly backwards: H[C]<=H[A] is the truth, and the lower-bound-on-H[C] machinery (not the value of H[C]) is where the bias hypothesis enters.

- Where (if anywhere) the gap is genuinely exploitable: NOT via Avenue A or B as written. The only live entropy-style directions in the literature are (i) richer couplings beyond Liu's auxiliary variable, and (ii) the more-general inequality |F OR F| > |F|^{c(eps)} when all biases < 1/2-eps (suggested in Cambie's survey 2306.12351) — but both are conjectured to still fall short of 1/2, and the two-sample single-coordinate framework is PROVEN capped at ~0.3823455 (Sawin form) / ~0.38271 (Liu). A correct deliverable for this run is the obstruction analysis itself (run_state's stated fallback).

- Dead ends (do not retry): (1) any perturbation C of uniform A that stays supported on F, expecting H[C]>H[A] — impossible by max-entropy. (2) Avenue A fractional t>1 as a probability distribution — lowers entropy, and is a signed measure for non-integer t. (3) Avenue B concentration near 0^n — C->A, no entropy gain; smallest-set route killed by Ellis-Ivan-Leader. (4) "Exploiting the false hypothesis" to flip H[C] vs H[A] — category error; the hypothesis bounds the conditional-entropy SUM, not the true H[C].

- Digests saved: /home/agentuser/repo/research/frankl/literature/digests.md ; PDFs in /home/agentuser/repo/research/frankl/literature/pdfs/ (2212.12500 Cambie, 2211.11504 AHS, 2306.12351 Cambie survey) with extracted .txt.

Sources:
- [Gilmer 2022, arXiv:2211.09055](https://arxiv.org/abs/2211.09055)
- [Alweiss-Huang-Sellke, arXiv:2211.11504](https://arxiv.org/abs/2211.11504)
- [Cambie, "Better bounds...", arXiv:2212.12500](https://arxiv.org/abs/2212.12500)
- [Yu, "Dimension-Free Bounds", arXiv:2212.00658](https://arxiv.org/abs/2212.00658)
- [Liu, "Conditionally IID Coupling", arXiv:2306.08824](https://arxiv.org/abs/2306.08824)
- [Cambie survey, arXiv:2306.12351](https://arxiv.org/abs/2306.12351)
- [Binary entropy inequality, arXiv:2301.09664](https://arxiv.org/abs/2301.09664)
