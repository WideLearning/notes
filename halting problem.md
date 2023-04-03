# halting problem
From [[theory of computability]]
$\physics$
## Statement
Language $\{ \ev{M, w} \mid \text{M halts on w}\}$ is undecidable.

## Proof
Assume there is a decider $H(\ev{M, w}) = [M \text{ halts on } w]$, it allows us to build $D(\ev{M})$ that accepts when $H(\ev{M, \ev{M}})$ accepts and halts when it rejects.

Let’s write all TMs in some order: $M_{1}, M_{2}, \dots$. Suppose $D = M_{i}$. If $D$ accepts $\ev{D}$, then $D$ must halt on $D$ by its definition. And if $D$ doesn’t accept $\ev{D}$, it halts (it never rejects by construction), $D$ must accept $\ev{D}$ by definition.

## Alternative proof
If halting is decidable, we can use it to filter out not halting cases and then solve [[acceptance problem]] just by simulation. But we know that acceptance is also undecidable.