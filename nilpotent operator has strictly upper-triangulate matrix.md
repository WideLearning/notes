# nilpotent operator has strictly upper-triangulate matrix
From [[nilpotent operator]]
$\physics$
## Statement
Suppose $T \in \L(V)$ is a [[nilpotent operator]]. Then there is a basis w.r.t. which $[T]$ has the form:
$$\begin{pmatrix}
0 &         & *  \\
  & \ddots &    \\
0 &         & 0 \\
\end{pmatrix}$$

## Proof
To have such matrix we need to ensure that $i$-th basis vector is made zero by $T^{i}$. To do so first choose the basis of $\ker T$, then extend it to basis of $\ker T^{2}$ and so on until we have basis $\ker T^{n}$ which is just $V$. Each extension will bring at least one new vector, because by [[lemma about sequence of kernels]], if on some iteration kernel didn’t extend, it won’t extend anymore.