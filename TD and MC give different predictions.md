# TD and MC give different predictions
From [[temporal-difference learning]] and [[Monte Carlo methods]]
$\physics$
## Statement
For the task of [[policy evaluation]] with a finite amount of training data TD and MC methods converge to different estimates, though each of them is optimal in some sense.
[[Monte Carlo methods]] calculate for each state the average return after visiting it. It minimizes mean square error from observed returns, without using [[Markov decision process]] structure in any way.
And [[temporal-difference learning]] also minimize mean square error from observed errors, but with restriction that the resulting estimates of value functions must be consistent with each other. By using this extra structure it needs less data to produce estimates that generalize well.

## Example
Consider the following MDP:
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
	&&&&& C \\
	\\
	A &&& B \\
	\\
	&&&&& C
	\arrow["{1.0, r = 0}"{description}, from=3-1, to=3-4]
	\arrow["{0.75, r = 1}"{description}, from=3-4, to=1-6]
	\arrow["{0.25, r = 0}"{description}, from=3-4, to=5-6]
\end{tikzcd}
\end{document}
```
And suppose we have the following data:
A, 0, B, 0
B, 1 (x6)
B, 0

Then MC would estimate $V(A) = 0$, because all returns after visiting $A$ ended in $0$. And TD will estimate $V(A)$ to be $v_{\pi}(A)$ in the scheme above, so $V(A) = \frac{3}{4}$.