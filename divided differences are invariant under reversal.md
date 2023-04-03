# divided differences are invariant under reversal
From [[divided differences]]
$\physics$
## Statement
Denote $[n]' = (n, n - 1, \dots, 2, 1)$, then:
$$[y_{[n]}] = [y_{[n]'}]$$

## Proof
Base: $n = 1$, nothing to reverse
Step: $n \to n + 1$
$$\begin{split}
[y_{[n+1]}] &= \frac{y_{[2:n+1]} - y_{[1:n]}}{x_{n+1} - x_{1}}\\
&= \frac{y_{[1:n]} - y_{[2:n+1]}}{x_{1} - x_{n+1}}\\
&= \frac{y_{[1:n]'} - y_{[2:n+1]'}}{x_{1} - x_{n+1}}\\
&= [y_{[n+1]'}]
\end{split}$$