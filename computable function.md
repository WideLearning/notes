# computable function
From [[algorithmic information theory]]
$\physics$
## $\mathbb{N} \to \mathbb{N}$
It is a function that is implemented by some [[Turing machine]]. It is total if the machine halts for all inputs and partial otherwise.

## $\mathbb{N} \to \mathbb{R}$, $\mathbb{Q} \to \mathbb{R}$
First, $\mathbb{N}$ and $\mathbb{Q}$ as input are not very different, because we are able to encode tuples. Let’s focus on $\Q$, for example.

To encode $f: \mathbb{Q} \to \mathbb{R}$ we use $g: \mathbb{Q} \times \mathbb{N} \to \mathbb{Q}$, such that $\lim\limits_{k \to \infty} g(x, k) = f(x)$. 
We call $f$ a [[semicomputable function]] if it can be bounded by $g$ from at least one side. If we can get bounds from both sides, it is computable (see equivalent definition in [[semicomputable function]]).