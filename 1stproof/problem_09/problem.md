**Problem 9:**

Let $n\ge5$. Let $A^{(1)},...,A^{(n)}\in\mathbb{R}^{3\times4}$ be Zariski-generic. For $\alpha,\beta,\gamma,\delta\in[n]$, construct $Q^{(\alpha\beta\gamma\delta)}\in\mathbb{R}^{3\times3\times3\times3}$ so that its $(i,j,k,l)$ entry for $1\le i,j,k,l\le3$ is given by $Q_{ijkl}^{(\alpha\beta\gamma\delta)}=det[A^{(\alpha)}(i,:); A^{(\beta)}(j,:); A^{(\gamma)}(k,:); A^{(\delta)}(l,:)]$. Here $A(i,:)$ denotes the ith row of a matrix A, and semicolon denotes vertical concatenation. We are interested in algebraic relations on the set of tensors $\{Q^{(\alpha\beta\gamma\delta)}:\alpha,\beta,\gamma,\delta\in[n]\}$. More precisely, does there exist a polynomial map $F:\mathbb{R}^{81n^{4}}\rightarrow\mathbb{R}^{N}$ that satisfies the following three properties?

- The map F does not depend on $A^{(1)},...A^{(n)}$.
- The degrees of the coordinate functions of F do not depend on n.
- Let $\lambda\in\mathbb{R}^{n\times n\times n}$ satisfy $\lambda_{\alpha\beta\gamma\delta}\ne0$ for precisely $\alpha,\beta,\gamma,\delta\in[n]$ that are not identical. Then $F(\lambda_{\alpha\beta\gamma\delta}Q^{(\alpha\beta\gamma\delta)}:\alpha,\beta,\gamma,\delta\in[n])=0$ holds if and only if there exist $u,v,w,x\in(\mathbb{R}^{*})^{n}$ such that $\lambda_{\alpha\beta\gamma\delta}=u_{\alpha}v_{\beta}w_{\gamma}x_{\delta}$ for all $\alpha,\beta,\gamma,\delta\in[n]$ that are not identical.
