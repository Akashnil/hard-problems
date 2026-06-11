**Definitions and Given Conditions:**
Let $P$ be a full support probability distribution over the boolean hypercube $\{0, 1\}^n$. 

For any coordinate $i \in \{1, \dots, n\}$, define the bias of $P$ at $i$ as the marginal probability:
$$bias_i(P) = \Pr_{x \sim P}(x_i = 1)$$

Define the maximum bias of the distribution $P$ as:
$$maxbias(P) = \max_{1 \le i \le n} bias_i(P)$$

Assume that $maxbias(P) < \frac{1}{2}$.

Let $P^k$ denote the product distribution resulting from $k$ independent samples of $P$. Thus, $P^k$ is a probability distribution over $\{0, 1\}^{nk}$. Let $X$ be a random vector drawn from $P^k$, indexed by coordinates $1 \le u \le nk$.

**Theorem to Prove:**
Prove that for any such distribution $P$, there always exists an integer $k \ge 1$ and a set of index pairs $S \subseteq \{(u, v) \mid 1 \le u, v \le nk\}$, such that if we define $P'$ as the distribution $P^k$ conditioned on the event that $X_u = X_v$ for all $(u, v) \in S$, then:
$$maxbias(P') < maxbias(P)$$

**Context and Goal:**
The objective is to establish a general construction that amplifies the bias (pushing the maximum probability of $1$ further toward $0$) by taking independent copies of a distribution and imposing strict equality constraints between chosen coordinates. Please detail the construction of $k$ and $S$, and mathematically verify that the conditioning strictly reduces the maximum bias.
