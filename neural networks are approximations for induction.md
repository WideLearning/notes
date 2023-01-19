# neural networks are approximations for induction
From [[deep learning]]
$\physics$
In [Is SGD a Bayesian sampler? Well, almost](https://arxiv.org/abs/2006.15191) the authors show that the architecture of neural network itself, that is, the way it uses its weights to act as a model, is enough to explain most of the generalization that neural networks are famous for. More precisely, they replaced SGD with a more random method and still got a good generalization.

So it might be that neural networks are doing something similar (but computable) to [[Solomonoff’s induction]]: There is more probability during optimization to find a set of weights encoding a simple function than a complex one. So it’s even good that methos like SGD or random trials don’t guarantee the optimal solution — doing an exhaustive search over all possible parameters would kill this inductive properties and cause a huge overfitting.