# canonical encoding of Turing machine
From [[applications of Kolmogorov complexity]]
$\physics$
Suppose we have [[Turing machine]] with states $Q$ over alphabet $A$ and its transition function $\delta$ is given by $r$ tuples $(p_{i}, t_{i}, s_{i}, q_{i})$ where $p_{i}$ is the state in which you start, $t_{i}$ is the scanned symbol, $s_{i} \in (A \cup \{ L, R\})$ is the action to take and $q_{i}$ is the state to go. And the start state is $q_{1}$ ($q$ of the first tuple).

$$E(T) = \bar s \bar r E(p_{1})E(t_{1})E(s_{1})E(q_{1})\dots E(p_{r})E(t_{r})E(s_{r})E(q_{r})$$
Here $E(x)$ can be [[self-delimiting string]] for $x$, but here we write $s = \lceil \log_{2} (|Q| + |A| + 2) \rceil$ in the beginning and then fit all numbers in $s$ bits. Note $r \leq 3\abs{Q}$, $p_{i}, q_{i} \leq |Q|$, $t_{i} \leq |A|$, $s_{i} \leq |A| + 2$.
Suppose $|A| = 3$ for simplicity:
$$\begin{split}
l(E(T)) &\leq l(\bar s) + l(\bar r) + r \cdot (s + \lceil \log_{2}(3 \cdot 5)\rceil + s)\\
&\leq (s + 2) + (s + 2 + 2) + (2s + 4)r\\
&= 2rs + 4r + 2s + 6
\end{split}$$
Li & Vitany give $l(E(T)) \leq 4rs + 2 \log rs + 4$, idk why.

The resulting encoding is not one-to-one. For a given string we still need to check that it isn’t interrupted before it is finished, that there are no index errors, rules don’t repeat (or we can just say that only the first entrance of rule should have effect), and maybe someting else. To have a one-to-one mapping, use [[Godel number]].