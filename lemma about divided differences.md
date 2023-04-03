# lemma about divided differences
From [[divided differences]]
$\physics$
## Statement
If $P(x)$ is the unique polynomial of degree $\leq n - 1$ passing through $x_{[n]}, y_{[n]}$, then for any $(x_{n+1}, y_{n+1})$:
$$[y_{[n]}, y_{n+1}]\prod\limits_{i \in [n]} (x_{n+1} -x_{i}) = y_{n+1} - P(x_{n+1})$$

## Proof
Base: $n = 1$
$$P(x) = y_{1}$$
And statement follows from definition of divided differences:
$$[y_{1}, y_{2}](x_{2} - x_{1}) = y_{2} - y_{1}$$
Step: $n \to n+1$
Let $Q(x)$ be the unique polynomial of degree $\leq n - 1$ for points $2\dots n+1$.
$$\begin{split}
[y_{[n+1]}, y_{n+2}]\prod\limits_{[n+1]} (x_{n+2} - x_{i}) &= \frac{[y_{[2:n+2]}] - [y_{[n+1]}]}{x_{n+2} - x_{1}}\prod\limits_{[n+1]} (x_{n+2} - x_{i})\\
&= ([y_{[2:n+2]}] - [y_{[n+1]}]) \prod\limits_{[2:n+1]} (x_{n+2} - x_{i})\\
&= (y_{n+2} - Q(x_{n+2})) - [y_{[n+1]}]\prod\limits_{[2:n+1]} (x_{n+2} - x_{i})\\
&= y_{n+2} - \qty(Q(x_{n+2}) + [y_{[n+1]}]\prod\limits_{[2:n+1]} (x_{n+2} - x_{i}))\\
\end{split}$$
Now we need to show $Q(x) + [y_{[n+1]}]\prod\limits_{[2:n+1]} (x - x_{i}) = P(x)$. We already know they are equal in $x_{[2:n+1]}$, let’s check $x_1$.
Because [[divided differences are invariant under reversal]]:
$$\begin{split}
Q(x_{1}) + [y_{[2:n+1]}, y_{1}]\prod\limits_{[2:n+1]} (x_{1} - x_{i}) &= Q(x_{1}) + (y_{1}- Q(x_{1}))\\
&= y_{1}
\end{split}$$
