# yoneda lemma
from [[category theory]]

### statement
let $C$ be an arbitrary [[category]], $a$ – any of its objects, $F$ – a functor from $C$ to $Set$. the set of [[natural transformation|natural transformations]] from $C(a, -)$ to $F$ is isomorphic to $F a$:
$$ Nat(C(a, -), F) \cong Fa $$(note the implication that there is at least one [[natural transformation]] from $C(a, -)$ to $F$ when $F a \ne \varnothing$).

[[Haskell]] form (here instead of [[natural transformation]] we use polymorphic function, because [[parametric polymorphic functions are natural transformations]]): $$ (\forall x. (a \to x) \to F x )\cong F a $$
### proof
consider $f :: x \to y$ in $C$. there must be also $C(a, f) :: C(a, x) \to C(a, y)$ and $F f :: F x \to F y$ in $Set$, together with $\alpha_{x} :: C(a, x) \to F x$ and $\alpha_{y} :: C(a, y) \to F y$. they form a commuting square:
$$ \alpha_{y} \circ C(a, f) = (F f) \circ \alpha_{x}$$
consider it point-wise, at some $h \in C(a, x)$ (and remember that $C(a, f)h = f \circ h$):
$$ \alpha_{y} (f \circ h) = (F f)(\alpha_{x} h)$$
it turns out to be a very strong condition, it’s enough to consider $x = a$ and $h = id_{a}$:
$$  \alpha_{y} f = (F f)(\alpha_{a} id_{a}) $$
note that now $f$ has type $a \to y$ and thus is an element of $C(a, y)$. it means that for any $y$ we can completely define $\alpha_{y} :: C(a, y) \to F y$ by selecting appropriate $f$, all we need to know is $\alpha_{a} :: C(a, a) \to F a$, or actually, only it’s action on $id_{a}$, which is an arbitrary element of $F a$. so, once we select the value of $\alpha_{a}(id_{a})$ from $F a$, we know the whole $\alpha$. conversely, if we know the $\alpha$, we can evaluate it’s component for $a$ on $id_{a}$ and get a point from $F a$.

### naturality
 $$  Nat(C(a, -), F) \cong Fa $$
it turns out that this isomorphism between sets can be seen as a [[natural isomorphism]]. to do so let’s see both parts as a functors from $[C, Set] \times C$ to $Set$ ($F$ is from $[C, Set]$ and $a$ is obviously from $C$). to show that they are indeed functors let’s consider how they act on morphisms. 
 
because $[C, Set] \times C$ is a product category (considering product as a [[bifunctor]]), its morphisms are actually the pairs of morphisms. so a morphism $(F, a) \to (G, b)$  is a pair of morphisms $(\Phi, f)$ (where $\Phi$ can be sees as [[natural transformation]], because it’s a morphism between functors). 
 
so we can lift $(\Phi, f) :: (F, a) \to (G, b)$ to $(G f) \circ \Phi_{a} :: Fa \to Gb$. because $\Phi$ is [[natural transformation]] it’s the same as $\Phi_{b} \circ (F f)$. it finishes the case for the right part (eval functor).

now for the left. we know about $F, a, G, b, \Phi, f$, also are given $\alpha \in Nat(C(a, -), F)$ and need to produce $\beta \in Nat(C(b, -), G)$. we can build it by [[vertical composition]] as $\beta = \delta \circ \alpha \circ \gamma$ where $\gamma \in Nat(C(b, -), C(a, -))$ and $\delta \in Nat(F, G)$. but by [[yoneda embedding]] we can get $\gamma$ from $C(a, b)$ which is just $f$, and $\delta$ is simply $\Phi$.

the component of natural transformation mapping from $Nat(C(a, -), F)$ to $Fa$: it takes $\alpha$ which is a natural transformation between $C(a, -)$ and $F$, so it maps $C(a, x)$ to $F x$ for every $x \in C$. then we can just take its component at $a$ and apply it to $id_{a}$, because $\alpha_{a} id_{a} \in F a$ (and it’s what we used in the proof of this lemma).

## see also
- [[yoneda embedding]]