# definition of adjunction through commutative diagram
From [[adjunction]]
$\physics$
## Statement
Definition of [[adjunction]] $F: \cat{C} \to \cat{D}, U: \cat{D} \to \cat{C}$ requires [[natural isomorphism]] $\varphi: \hom(F -, -) \to \hom(-, U -)$. Equivalent condition is that for
$$\begin{split}
\forall v, u \in \ob(\cat{C}),\\
v', u' \in \ob(\cat{D}),\\
f \in \hom_{\cat{C}}(u, v)\\
f' \in \hom_{\cat{D}}(v', u'),\\
h \in \hom_{\cat{D}}(Fv, v').\\
\end{split}$$
the following square commutes:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] u && {Uv'} \\ \\ v && {Uu'} \arrow["f"', from=1-1, to=3-1] \arrow["{\varphi_{u,v'}(h \circ Ff)}", from=1-1, to=1-3] \arrow["{U f'}", from=1-3, to=3-3] \arrow["{\varphi_{v,v'}(h)}", from=3-1, to=1-3] \arrow["{\varphi_{v, u'}(f' \circ h)}"', from=3-1, to=3-3] \end{tikzcd}
\end{document}
```
That is:
$$\begin{cases}
\varphi_{u, v'}(h \circ Ff) = \varphi_{v, v'}(h) \circ f\\
\varphi_{v, u'}(f' \circ h) = Uf' \circ \varphi_{v, v'}(h)\\
\end{cases}$$
## Proof
First, we use [[natural transformation for bifunctors]] and decompose naturality condition into naturality in each argument. Second, morphisms on $\cat{Set}$ are functions, so to check they equality it’s enough to check their equality pointwise.

Naturality in the first argument, where the second is fixed to $a \in \ob(\cat{D})$. For arbitrary $f^{op} \in \hom(\cat{C}^{op})$:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] v && {\mathrm{Hom}(Fv, a)} && {\mathrm{Hom}(v, Ua)} \\ \\ u && {\mathrm{Hom}(Fu, a)} && {\mathrm{Hom}(u, Ua)} \arrow["f"', from=1-1, to=3-1] \arrow["{\varphi_{v, a}}", from=1-3, to=1-5] \arrow["{\varphi_{u, a}}"', from=3-3, to=3-5] \arrow["{\mathrm{Hom}(Ff, a)}"', from=1-3, to=3-3] \arrow["{\mathrm{Hom}(f, Ua)}", from=1-5, to=3-5] \end{tikzcd}
\end{document}
```
Note that $f^{op} \in \hom_{\cat{C}^{op}}(v, u)$, so we have the corresponding $f \in \hom_{\cat{C}}(u, v)$. For arbitrary $h: Fv \to a$:
$$\varphi_{u, a}(\hom(Ff^{op}, a)(h)) = \hom(f^{op}, Ua)(\varphi_{v, a}(h))$$
$$\forall f \in \hom_{\cat{C}}(u, v), h \in \hom_{\cat{D}}(Fv, a). \varphi_{u, a}(h \circ Ff) = \varphi_{v, a}(h) \circ f$$


Naturality in the second argument, where the first is fixed to $a \in \ob(\cat{C}^{op})$. For arbitrary $f \in \hom(\cat{D})$:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] v && {\mathrm{Hom}(Fa, v)} && {\mathrm{Hom}(a, Uv)} \\ \\ u && {\mathrm{Hom}(Fa, u)} && {\mathrm{Hom}(a, Uu)} \arrow["f"', from=1-1, to=3-1] \arrow["{\varphi_{a, v}}", from=1-3, to=1-5] \arrow["{\varphi_{a, u}}"', from=3-3, to=3-5] \arrow["{\mathrm{Hom}(Fa, f)}"', from=1-3, to=3-3] \arrow["{\mathrm{Hom}(a, Uf)}", from=1-5, to=3-5] \end{tikzcd}
\end{document}
```
For arbitrary $h: Fa \to v$:
$$\varphi_{a, u}(\hom(Fa, f)(h)) = \hom(a, Uf)(\varphi_{a, v}(h))$$
$$\varphi_{a, u}(f \circ h) = Uf \circ \varphi_{a, v}(h)$$

Finally, we can bring it back together by setting first $a = v'$, second $a = v$, and second $v, u = v', u'$:

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large] u && {Uv'} \\ \\ v && {Uu'} \arrow["f"', from=1-1, to=3-1] \arrow["{\varphi_{u,v'}(h \circ Ff)}", from=1-1, to=1-3] \arrow["{U f'}", from=1-3, to=3-3] \arrow["{\varphi_{v,v'}(h)}", from=3-1, to=1-3] \arrow["{\varphi_{v, u'}(f' \circ h)}"', from=3-1, to=3-3] \end{tikzcd}
\end{document}
```