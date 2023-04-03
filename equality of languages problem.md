# equality of languages problem
From [[theory of computability]]
$\physics$
## Statement
The following is not a [[recursively enumerable language]] (and therefore not a [[decidable language]]):
$$EQ_{TM} = \{ \ev{M_{1}, M_{2}} \mid M_{1}, M_{2} \text{ are TMs, } L(M_{1}) = L(M_{2}) \}$$

## Proof
We will use a [[mapping reduction]] from [[acceptance problem]] to the complement of this. We need to build a conversion $f$ that takes a TM $M$ and input $w$ to it, returns two TMs, and their languages are equal iff $M$ accepts $w$.
For example, it can produce $M_1$ with empty language and $M_{2}$ that accepts any string iff $M$ accepts $w$ (simulation here).