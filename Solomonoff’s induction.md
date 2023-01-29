# Solomonoff’s induction
From [[Bayesian inference]] and [[Information theory]], related to [[algorithmic probability]]
Based on http://www.raysolomonoff.com/publications/isis96.pdf
$\physics$
## First definition
We consider all programs that take observations and output a real number. To make it a valid likelihood we can explicitly apply softmax to it, aggregating over all possible inputs. Then we take a [[prior distribution]] that is $\text{alphabet size}^{-\text{program length}}$ and combine it with the [[likelihood function]] described above. We get a [[posterior distribution]] of programs (models) and can do inference of the next observations from it.

Maybe the program should return real numbers after each observations and then we can get not  $P(x)$ but $P(x\dots)$, which is more useful, if we consider predicting continuations of sequences.

## Second definition
Here we simply use [[algorithmic probability]]: $P(x1\dots \mid x\dots) = \frac{P(x1\dots)}{P(x\dots)}$.

## Special cases
In some cases the shortest model might be not the one which directly defines the regularity, but which finds for this regularity in an efficient way. For example, if the data is nicely described by a neural network, the shortest program might just train a neural network, instead of hardcoding all the weights from beginning. But in general it is not free lunch, because to train a network with $N$ parameters you usually need $O(N)$ samples, so you simpy exchange the length of you program for the quality of your predictions (on the first samples).



## See also
- Gödel machine
- Levin’s universal search
- [Hutter’s universal search](http://www.hutter1.net/ai/pfastprg.pdf)