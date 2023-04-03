# configuration of Turing machine
From [[Turing machine]]
$\physics$
## Definition
It is a triple $(u, q, v)$, where:
- $u \in \Gamma^{*}$: tape content to the left
- $q \in Q$: current state
- $v \in \Gamma^{\omega}$: tape content to the right

Here $\Gamma^{\omega}$ means all infinite strings over $\Gamma$. There will be only finite number of non-blanks, though, so the set of configurations is still countable.

## Equivalent definition
It is a triple $(x, q, k)$, where:
- $x \in \Gamma^{*}$:  tape content, without infinite blanks to the left and right
- $q \in Q:$ current state
- $k \in \mathbb{N}$: position of head in the tape content