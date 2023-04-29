# class NP
From [[time complexity]]
$\physics$
## Definition
$$\textbf{NP} = \textbf{NTIME}(n^{\order{1}}) = \bigcup\limits_{k \in \N} \textbf{NTIME}(n^{k})$$

## Equivalent definition
A language is in $\textbf{NP}$ if there is a [[verifier]] for it with a polynomial (in the input size, not certificate size) running time.

## Proof of equivalence
$\implies$:
Take the construction from [[NTM can be simulated by TM]] and consider certificate $c$ to be the encoding of computation path in that tree of computations. If we have it and have a nondeterministic polynomial time decider, we can run it deterministically (using $c$ to choose branches) and get the result.

$\impliedby$:
Let $A$ be a language and $V_{A}$ its polynomial time verifier. Denote $m(n)$ the length of the longest certificate that can be used for an input of size $n$ (and be accepted by $V_{A}$). We know that $m(n)$ is $\order{n^{k}}$ for some $k$, because $V_{A}$ must somehow read it in polynomial time.

Then we have the following polynomial time nondeterministic decider:
1. Select $c. l(c) \leq m(n)$ nondeterministically.
2. Run $V_{A}$ on $\ev{w, c}$
3. Accept iff it accepts