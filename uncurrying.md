# uncurrying
from [[constructions and operations in category theory]]

it’s the opposite of [[currying]], so it’s a transformation from $z \to (a \Rightarrow b)$ to $z \times a \to b$. this way it’s also unique, because if we have $eval$ which takes $(f, x)$ and returns $f(x)$, then $(z \times a \to b) = eval \circ (z \times (a \Rightarrow b) \times id)$ (i.e. we take $(z, a)$, replace $z$ with $f = h(z)$, which is a partially applied version of result and then return $f(a)$).