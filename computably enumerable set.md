# computably enumerable set
From [[algorithmic information theory]]
$\physics$
## Definition
A subset of natural numbers is called computably enumerable if it is the range of some total [[computable function]]. Note that the function must output an element of this set given any natural number (= binary string) as input, but it doesn’t need to be injective, so finite sets are also allowed.

## Equivalent definition
A subset must be accepted by [[Turing machine]]. That is, for each element of the subset the machine halts in a special accepting state, and for others it halts rejecting or doesn’t halt at all.

## Proof of equivalence
$\implies:$ (every element in the subset must be enumerated at some finite moment)
Denote the enumerating function by $f$. Then there is a Turing machine that iteratively applies $f$ to every natural number and halts with acceptance if it produces the given element. For any element in the subset such process will halt, because some natural number must be mapped to it. And for elements outside of the subset it won’t halt.

$\impliedby:$ (every element in the subset must be accepted in a finite amount of time)
We need to order evaluations in such a way that every element gets infinitely many time in the limit. For example, let’s first spend one step to test $1$, then two steps for $1, 2$ (two for each of them), then three for $1, 2, 3$, etc. Then we will reach any element eventually, and also will spend as much time as needed to test it. 

## Examples
- every [[computable set]]
- [[halting set]]