# dual form of linear transformation
From [[deep learning]], based on [The Dual Form of Neural Networks Revisited: Connecting Test Time Predictions to Training Patterns via Spotlights of Attention](https://arxiv.org/pdf/2202.05798.pdf)
$\require{physics}{}$
## Statement
I will use notation from [[dot product attention]] here.
The following two functions are equal:
- $S_{1}(x) = Wx$ (linear layer)
- $S_{2}(x) = \mathrm{Attention}(K, V, x)$
with $W = \sum\limits_{i=1}^{T} v_{t} k_{t}^{T} = V K^{T} \in \mathbb{R}^{d_{out}\times d_{in}}$

## Proof
Algebraically, we just need to recall the formula for [[dot product attention]]:
$$\mathrm{Attention}(K, V, q) = (V K^{T}) q$$


But let's get another view. First, suppose that we have only one key-value pair:
$$S_{2}(x) = \langle k_{1},  x \rangle v_{1},\quad k_{1}, x \in \mathbb{R}^{d_{in}}, v_{1} \in \mathbb{R}^{d_{out}}$$
Here it's easier to see why $W = v_{1} k_{1}^{T}$ will do the same. It's hard to explain intuitively, but with algrebra it is $\ev{k_{1}, x} v_{1} = v_{1}(k_{1}^{T} x) = (v_{1} k_{1}^{T}) x$.

Now note that we can find a sum of two linear models, and we can merge key-value pairs from two attention models. So we do this trick to all $T$ key-value pairs and sum up their matrices.

## Exercise 1
There is an explicit formula for conversion from $S_{2}$ to $S_{1}$. Now suppose you have a matrix $W = \begin{pmatrix}1 & 2 & 3\\2 & 3 & 1\\3 & 1 & 2\end{pmatrix}$ and want to find it's representation with $T = 3$ key-value pairs. Can you do it with $T = 2$, with $T = 4$?

## Exercise 2
We can find a more useful decomposition if we know how we got the matrix $W$.
Suppose we are training a linear model on points $x_{T}$ with gradient descent and some error function $\mathcal{L}: \mathbb{R}^{d_{out}\times d_{in}} \to \mathbb{R}$. The initial weights are $W_{0}$.

- Find how to express $\dv{\mathcal{L}}{W}$ on $t$-th training sample in terms of $x_{T}$
- Decompose $Wx$ into $W_{0}x + \mathrm{Attention}(\dots, \dots, x)$

## Hint
To avoid multidimensional tensors let's take this derivative of $f(x) = \mathcal{L}(Wx)$ component-wise:
$$\begin{split}
\dv{f(x)}{W_{i,j}}
&= \dv{\mathcal{L}(x)}{x} \dv{(Wx)}{W_{i,j}}\\
&= \mathcal{L}'(x)
\left(\dv{W}{W_{i,j}}x + \dv{x}{W_{i,j}}W\right),
\quad \mathcal{L'(x)} \in \mathbb{R}^{1 \times d_{out}}\\
&= \mathcal{L}'(x)(e_{i} e_{j}^{T}x + 0),
\quad e_{i} \in \mathbb{R}^{d_{out}}, e_{j} \in \mathbb{R}^{d_{in}}\\
&= \qty(\mathcal{L}'(x)e_{i})\qty(e_{j}^{T}x)\\
&= \qty(\mathcal{L}'(x))_{i}\ x_{j}
\end{split}$$
And summing it up (remember $\mathcal{L}'(x)$ is a row):
$$\dv{f(x)}{W} = \mathcal{L}'(x)^{T} x^{T}$$
So the final expression is:
$$Wx = W_{0}x + \mathrm{Attention}\qty((x_{1},\dots x_{T}), (\mathcal{L}'(x_{1})^{T},\dots \mathcal{L}'(x_{T})^{T}), x)$$
In other words, training points will be keys, errors from each step of gradient descent will be values and the argument will be a query.