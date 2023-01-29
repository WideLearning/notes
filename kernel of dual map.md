# kernel of dual map
From [[dual map]]

## Statement
$$T \in \L(V, W) \implies \begin{cases}
\ker T' &= (\im T)^{0}_{W}\\
\dim \ker T' &= \dim \ker T + \dim W - \dim U
\end{cases}$$

## Proof
First, let's recall definitions:
$$T' \in \L(\L(W, F),\ \L(V, F)): f \mapsto f \circ T$$
$$\ker T' = \{ f \in \L(W, F) \mid T'(f) = 0 \}$$
$$ (\im T)^{0}_{W} = \{ f \in \L(W, F) \mid f(\im T) = \{0\}\}$$
$$ T'(f) = 0 \eq \im(f \circ T) = 0 \eq f(\im T) = \{0\}$$
Taking it all together we prove the first point.

Adding [[annihilator dimension]] and [[rank-nullity theorem]] we prove the second:
$$\begin{split}
\dim \ker T'
&= \dim (\im T)^{0}_{W}\\
&= \dim W - \dim \im T\\
&= \dim W - \dim V + \dim \ker T
\end{split}$$

Note that from the second line we derive [[surjectivity is injectivity of dual]] and the first part of [[image of dual map]].