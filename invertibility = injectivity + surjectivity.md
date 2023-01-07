# invertibility = injectivity + surjectivity
From [[invertibility]]

## Statement
$$\begin{cases}
T \in W^{V}\\
\forall x_{1}, x_{2} \in V: T(x_{1}) \ne T(x_{2})\\
\forall y \in W \exists x \in V: T(x) = y
\end{cases} \implies \exists T^{-1}$$
## Proof
For some $y \in W$ consider $\{ x \in V \mid T(x) = y \}$. There is at most one element because of injectivity and at least one element because of surjectivity.
Then we can define $S(y)$ that will return such $x$ and we get $T \circ S = I$ from this definition. And if we take some $x \in V$ we have $T(x) = T(S(T(x)))$ from previous property, which means $x = S(T(x))$ by injectivity, so $S \circ T = I$ too.