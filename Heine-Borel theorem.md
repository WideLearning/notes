# Heine-Borel theorem
From [[real analysis]]
$\physics$
## Statement
Bounded and closed $X \subset \mathbb{R}$ is a compact.

## Proof
First, let $X = [a, b]$ and $C$ be an open cover of it. Then consider all prefixes of it that can be covered by finite subset of $C$, let $r$ be $\sup$ of their right ends. Note $a \leq r \leq b$, because empty prefix is coverable and all prefixes must still be contained in $X$. Assume $r < b$, then we can take any open set from $C$ that covers $r$ and increase it, contradiction.

Now, for arbitrary bounded and closed $X$. Take a bounded and closed $Y \supset X$. For any cover of $X$ we can add $\mathbb{R} \setminus X$, which will be now a cover of $Y$ too, make it finite, then remove $\mathbb{R} \setminus X$ if necessary, and we have a finite subcover of $X$.