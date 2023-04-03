# mPDA and context-free grammars are equivalent
From [[modified pushdown automaton]] and [[context-free grammar]]
$\physics$
## Statement
For any [[modified pushdown automaton]] $P = (Q, \Sigma, \Gamma, \delta, q_{0}, \{ q_{accept} \})$ there is a [[context-free grammar]] $G(P) = (V, \Sigma, R, S)$ which generates those and only those strings that are accepted by $P$.

## Proof
Take $V = \{ A_{p,q} \mid p, q \in Q \}$ and $S = A_{q_{0}, q_{accept}}$. Consider the following rules as $R$:
1. $\forall i \in Q. A_{i, i} \to \varepsilon$
2. $\forall i, j, i \in Q. A_{i,k} \to A_{i,j} A_{j,k}$
3. $\forall \delta(i, a, \varepsilon) \ni (p, t), \delta(q, b, t) \ni (j, \varepsilon). A_{i, j} \to a A_{p, q} b$ (conditions mean that these two transitions push and pop the same symbol from the stack)

We want to prove that $A_{p, q}$ generates exactly those strings that bring $P$ from state $p$ with empty stack to state $q$ with empty stack. It would mean that $S = A_{q_{0}, q_{accept}}$ will bring it from the starting state to accepting state.

$\text{Generates} \implies \text{Accepted}$:
Denote by $k$ the number of rule applications in which $G(P)$ generates $x$ from $A_{p, q}$.
$k = 1$:
Here $\varepsilon$-transition was necessarily used, and it indeed brings $P$ from $(p, \varepsilon)$ to $(p, \varepsilon)$.
$k \to k + 1$: 
If the first applied rule were of the second kind, we know for both halves the induction statement, so for the $A_{p, q}$ it will also work.
Else, we know that the inner part can take from $(p, \varepsilon)$ to $(q, \varepsilon)$, then it can take from $(p, t)$ to $(q, t)$ as well. And this $t$ is added and removed before and after it, so $A_{p, q}$ brings from $(p, \varepsilon)$ to $(q, \varepsilon)$.

$\text{Accepted} \implies \text{Generates}$:
Here $k$ is the number of steps (edges) in computation that accepts $x$.
$k = 0$:
It means $q_{0} = q_{accept}$, and there is a rule $A_{q_{0}, q_{accept}} \to \varepsilon$ in this case.
$k \to k + 1$:
If stack never becomes empty, the first pushed symbol is popped the last, and we can use a rule of the third kind for that.
Otherwise, we can split this path into two and use a rule of the second kind.