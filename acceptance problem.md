# acceptance problem
From [[theory of computability]]
$\physics$
## Statement
$\{ \ev{M, w} \mid M \text{ is a TM and it accepts } w\}$  is undecidable.

## Proof
Assume there is a decider $H(\ev{M, w}) = [M \text{ accepts } w]$, it allows us to build $D(\ev{M}) = \neg H(\ev{M, \ev{M}}) = [M \text{ not accepts } \ev{M}]$.

Let’s write all TMs in some order: $M_{1}, M_{2}, \dots$. Suppose $D = M_{i}$. If $D$ accepts $\ev{D}$, then $D$ must reject $D$ by its definition. And if $D$ doesn’t accept $\ev{D}$ (rejects or halts), $D$ must accept $\ev{D}$ by definition.
