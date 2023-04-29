# adjoint functor is unique
From [[adjunction]]
$\physics$
## Statement
1. If $F \dashv U, F' \dashv U$ then there is a [[natural isomorphism]] $F \cong F'$.
2. If $F \dashv U, F \dashv U'$ then there is a [[natural isomorphism]] $U \cong U'$.

## Proof
Enough to prove one, another is dual.

2. Because [[unit of adjunction is a universal morphism]] we have two universal morphisms: $\eta_{A}: A \to UFA$ and $\eta_{A}': A \to U'FA$. By definition, there is a unique morphism that decomposes second through the first, and vice versa, so there is an isomorphism between $UFA$ and $U'FA$.


By definition of [[adjunction]]: $$\forall A \in \ob(\cat{C}), B \in \ob(\cat{D}). \hom_{\cat{C}}(A, UB) \cong \hom_{\cat{D}}(FA, B) \cong \hom_{\cat{C}}(A, U'B)$$
Moreover, isomorphism $\varphi_{A, B}: \hom(A, UB) \to \hom(A, U'B)$ is natural in both arguments.
Take $\alpha_{v} = \varphi_{Uv, v}(\id_{Uv}) \in \hom(Uv, U'v)$ and $\alpha_{v}^{-1} = \varphi_{Uv, v}^{-1}(\id_{Uv})$. Let’s see that they are indeed inverse of each other.
What means naturality in the first argument? For arbitrary $f^{op}: B \to C$ (in opposite category):
$$\varphi_{C, A} \circ \hom(f^{op}, UA) = \hom(f^{op}, U'A) \circ \varphi_{B, A}$$
$$\forall h \in \hom(B, UA). \varphi(h \circ f) = \varphi(h) \circ f$$
That’s what we need:
$$\alpha \circ \alpha^{-1} = \varphi(\id) \circ \varphi^{-1}(\id) = \varphi(\id \circ \varphi^{-1}(\id)) = \id$$
And the other identity, perhaps, follows from naturality of $\varphi^{-1}$ in the first argument.

Now, for naturality we want to check: $\forall f \in \hom_{\cat{D}}(v, u). \alpha_{u} \circ Uf = U'f \circ \alpha_{v}$.
As in [[definition of adjunction through commutative diagram]], we use naturality of $\varphi$ in both arguments.
For the first argument we have the following commuting square:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large]
{\mathrm{Hom}(Uu, Uu)} && {\mathrm{Hom}(Uu, U'u)} \\
\\
{\mathrm{Hom}(Uv, Uu)} && {\mathrm{Hom}(Uv, U'u)}
\arrow["{\varphi_{Uu, u}}", from=1-1, to=1-3]
\arrow["{\varphi_{Uv, u}}", from=3-1, to=3-3]
\arrow["{\mathrm{Hom}((Uf)^{op}, Uu)}"{description}, from=1-1, to=3-1]
\arrow["{\mathrm{Hom}((Uf)^{op}, U'u)}"{description}, from=1-3, to=3-3]
\end{tikzcd}
\end{document}
```
Let’s follow it for $\id_{Uu}$:
$$\varphi_{Uv, u}(\hom((Uf)^{op}, Uu)(\id_{Uu})) = \hom((Uf)^{op}, U'u)(\varphi_{Uu, u}(\id_{Uu}))$$
$$\varphi_{Uv, u}(\id_{Uu} \circ U f) = \varphi_{Uu, u}(\id_{Uu}) \circ Uf$$
$$\varphi_{Uv, u}(U f) = \alpha_{u} \circ Uf$$

For the second we have the following commuting square:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] {\mathrm{Hom}(Uv, Uv)} && {\mathrm{Hom}(Uv, U'v)} \\ \\ {\mathrm{Hom}(Uv, Uu)} && {\mathrm{Hom}(Uv, U'u)} \arrow["{\varphi_{Uv, v}}", from=1-1, to=1-3] \arrow["{\varphi_{Uv, u}}", from=3-1, to=3-3] \arrow["{\mathrm{Hom}(Uv, Uf)}"{description}, from=1-1, to=3-1] \arrow["{\mathrm{Hom}(Uv, U'f)}"{description}, from=1-3, to=3-3] \end{tikzcd}
\end{document}
```
Follow it for $\id_{Uv}$:
$$\varphi_{Uv, u}(\hom(Uv, Uf)(\id_{Uv})) = \hom(Uv, U'f)(\varphi_{Uv, v}(\id_{Uv}))$$
$$\varphi_{Uv, u}(Uf \circ \id_{Uv}) = U'f \circ \varphi_{Uv, v}(\id_{Uv})$$
$$\varphi_{Uv, u}(Uf) = U'f \circ \alpha_{v}$$
So, $\alpha_{u} \circ Uf = \varphi_{Uv, u}(Uf) = U'f \circ \alpha_{v}$.