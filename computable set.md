# computable set
From [[algorithmic information theory]]
$\physics$
## Definition
A subset of natural numbers is computable if there is a [[Turing machine]] that accepts it and always halts.

## Second definition
It must be [[computably enumerable set]] and [[co-computably enumberable set]].

## Third definition
A [[computably enumerable set]] where the enumerating function is monotonically increasing.

## Proof of equivalence
$1 \implies 2$: Trivial, just use the given characteristic function to test if an element lies in set (or complement). By the second definition it means [[computably enumerable set]].

$2 \implies 1$: Let’s use the second definition again. We have two computable functions, one can in finite time check that element lies in set, otherwise it might halt. The other can in finite time check that it lies in the complement. So we can just run them in turns, increasing time limits, and eventually one of them will give us the answer.

$1 \implies 3$: Also easy, for a given $i$ go through natural numbers in increasing order testing them, return the $i$-th of those which lie in set.

$3 \implies 1$: Go through the enumeration. At some point you will reach element not less then input. If it is equal — accept, if greater — reject.

## Examples
- empty set
- natural numbers
- every set that is finite or has finite complement
- prime numbers