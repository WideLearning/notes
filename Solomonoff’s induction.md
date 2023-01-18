# Solomonoff’s induction
From [[Bayesian inference]]
$\physics$
We want to make a Bayesian inference, but we don’t want to restrict ourselves to any specific [[prior distribution]]. Maybe we just don’t know what kind of data we actually have, and therefore want to be as general as possible. The prior itself is a probability distribution over possible models. And a model is itself a probability distribution. What we want to achieve is to assign a positive probability to every model. But in general, there might be an uncountable number of them, and we will fail.

Here comes the trick: we will restrict ourselves to computable models. If we want to make inference later, it is only natural, because you can’t to much with something you can’t compute. But it makes the set of models countable and we can now assign positive probabilities to them, $0.5, 0.25, 0.125, \dots$ will do, for example. 

Fortunately, we can do even better. Each model is now associated with its algorithm (which takes data and outputs its probability, it can use any language, e.g. Python), and we can consider the lengths of these algorithms. Let’s give more probability mass to the shorter programms, namely $P(m) = 0.5^{\abs{m}}$ where $m$ is a model and $\abs{m}$ is the length of its program. 

Not only we now have possible probabilities for all models, we also get something like Occam’s razor: simpler models are given more weight. It implies that if there are actually any regularities in data (and regularity means something computable) than as we see more and more samples from the data, the algorithm the shortest algorithms (=model) that is able to find this regularities (all of them) will get more (asymptotically) likelihood than the ones that can’t find them, inlcuding all simpler models. So with enough samples and time to enumerate infinitely countable set of algorithms the induction will work. The only problem here is that we don’t have infinite time.

## See also
- Gödel machine
- Levin’s universal search
- [Hutter’s universal search](http://www.hutter1.net/ai/pfastprg.pdf)