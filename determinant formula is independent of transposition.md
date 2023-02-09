# determinant formula is independent of transposition
From [[determinant]]
$\physics$
## Statement
For $f$ from [[formula for antisymmetric polylinear forms]] we have:
$$f(A) = f(A^{T})$$

## Proof
$$f(A) = f(I)\sum\limits_{p \in \sigma_{n}} \mathrm{sgn}(p) \prod A_{p_{i}, i}$$
$$\begin{split}
f(A^{T})
&= f(I)\sum\limits_{p \in \sigma_{n}} \mathrm{sgn}(p) \prod A_{i, p(i)}\\
&= f(I)\sum\limits_{p \in \sigma_{n}} \mathrm{sgn}(p) \prod A_{p^{-1}(i), i}\\
&= f(I)\sum\limits_{p \in \sigma_{n}} \mathrm{sgn}(p^{-1}) \prod A_{p^{-1}(i), i}\\
&= f(I)\sum\limits_{p \in \sigma_{n}} \mathrm{sgn}(p) \prod A_{p(i), i}\\
&= f(A)
\end{split}$$
