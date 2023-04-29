# simplified definition of monad
From [[monad]]
$\physics$
## Definition
A [[monad]] in $\cat{C}$ is a triple $(T, \eta, \beta)$, where:
- $T: \ob(\cat{C}) \to \ob(\cat{C})$ is a function
- $\forall A \in \ob(\cat{C}). \eta_{A}: A \to TA$ is a morphism
- $\forall A, B \in \ob(\cat{C}). \beta_{A, B}: \hom(A, TB) \to \hom(TA, TB)$ is a morphism
And they satisfy the following laws:
1. $\beta_{A, A}(\eta_{A}) = \id_{TA}$
2. $\forall f: A \to TB. \beta_{A, B}(f) \circ \eta_{A} = f$
3. $\forall f: A \to TB, g: B \to TC. \beta_{B, C}(g) \circ \beta_{A, B}(f) = \beta_{A, C}(\beta_{B, C}(g) \circ f)$

Note that $T$ is not required to be a functor, $\eta$ and $\beta$ are not required to be natural.

## Proof of equivalence
First, let’s derive the main definition of [[monad]] from this one.

1. $T$ can be completed to a functor.
We define it on morphisms like `Tf x = x >>= (\x -> return x)`:
$$\forall f: A \to B. Tf = \beta_{A, B}(\eta_{TB} \circ f)$$
Then $\id$ is preserved:
$$T \id = \beta(\eta \circ \id) =\beta(\eta) = \id$$
And composition:
$$Tg \circ Tf = \beta(\eta \circ g)\circ \beta(\eta \circ f) = \beta(\beta(\eta \circ g) \circ \eta \circ f) = \beta(\eta \circ g \circ f) = T(g \circ f)$$
2. $\eta$ is natural.
We want to show for arbitrary $f: A \to B$:
$$\eta_{B} \circ f = Tf \circ \eta_{A}$$
Expand it by definition:$$\eta \circ f = \beta(\eta \circ f) \circ \eta$$Which is the second law.
3. There is a natural $\mu: T^{2} \to T$.
Define $\mu_{A}: T^{2}A \to TA$ as `join x = x >>= id` or `join x = x >>= (\x -> (x >>= return))`:
$$\mu_{A} = \beta(\id_{TA}) = \beta(\beta(\eta))$$
Haskell reference: For example, on `List` it will take `x` which is a list of lists, then pass each of them to `id`, and then concatenate into one list. And on `Maybe` it will first unwrap the value, if it was `Just`, and then return it, or directly return `Nothing` otherwise. So it indeed composes two monad wrappers into one.
Want to show for arbitrary $f: A \to B$:
$$\mu_{B} \circ T^{2}f = Tf \circ \mu_{A}$$
Expand by definition:
$$\beta(\id) \circ \beta(\eta \circ \beta(\eta \circ f)) = \beta(\eta \circ f) \circ \beta(\id)$$
$$\beta(\beta(\id) \circ \eta \circ \beta(\eta \circ f)) = \beta(\beta(\eta \circ f) \circ \id)$$
$$\beta(\beta(\eta \circ f)) = \beta(\beta(\eta \circ f))$$
4. Associativity law.
For $A \in \ob(\cat{C})$:
$$\mu_{A} \circ T\mu_{A} = \mu_{A} \circ \mu_{TA}$$
Expanding definitions:
$$\beta(\id) \circ \beta(\eta \circ \beta(\id)) = \beta(\id) \circ \beta(\id)$$
$$\beta(\beta(\id) \circ \eta \circ \beta(\id)) = \beta(\beta(\id) \circ \id)$$
$$\beta(\beta(\id)) = \beta(\beta(\id))$$
5. Unit laws:
$$\mu_{A} \circ T\eta_{A} = \id_{TA} = \mu \circ \eta_{TA}$$
$$\beta(\id) \circ \beta(\eta \circ \eta) = \beta(\id) \circ \eta$$
$$\beta(\beta(\id) \circ \eta \circ \eta) = \id$$
$$\beta(\eta) = \id$$

Now, let’s derive this definition from the [[monad]] laws. Define $\beta_{A, B}(f) = \mu_{B} \circ Tf$.
1. $\beta(\eta) = \mu \circ T\eta = \id$ by upper triangle in unit laws.
2. $\beta(f) \circ \eta = \mu \circ Tf \circ \eta = \mu \circ \eta \circ f = f$ by naturality and lower triangle in unit laws.
3. $\beta(g) \circ \beta(f) = \beta(\beta(g) \circ f)$:
$$\begin{split}
&\mu \circ Tg \circ \mu \circ Tf\\
&= \mu \circ \mu T \circ T^{2}g \circ Tf\\
&= \mu \circ T\mu \circ T^{2}g \circ Tf\\
&= \mu \circ T((\mu \circ Tg) \circ f)

\end{split}$$

## See also
- [[monads in haskell]]