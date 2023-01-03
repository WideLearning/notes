# attention
From [[deep learning]]

Attention is a powerful mechanism which resembles support vector machines.
Usually, there is a sequence of keys $k_{n} \in \mathbb{R}^{d_{in}}$, a sequence of values $v_{n} \in \mathbb{R}^{d_{out}}$ and a query $q \in \mathbb{R}^{d_{in}}$. Also we need a function $S: \mathbb{R}^{d_{in}} \times \mathbb{R}^{d_{in}} \to \mathbb{R}$ that will calculate similarities between the keys and queries. Then the attention is defined as:
$$\mathrm{Attention}(K, V, q) = \sum\limits_{i=1}^{n} S(k_{i}, q) v_{i} = \langle S(K, q), V \rangle$$
An example of such attention is [[dot product attention]].

The definition is not rigid. We can add some nonlinearities, as in [[softmax attention]] or [cosFormer](https://arxiv.org/abs/2202.08791). Also, keys and queries don't have to be of same dimension or even to be real vectors, as long as $S$ can work with them.
