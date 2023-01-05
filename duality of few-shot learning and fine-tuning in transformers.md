# duality of few-shot learning and fine-tuning in transformers
From [[deep learning]], based on [Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient Descent as Meta-Optimizers](https://arxiv.org/pdf/2212.10559.pdf)
$\require{physics}{}$
## Introduction
Few-shot learning means that we take a pretrained language model (e.g. GPT), feed into it a few sample queries with answers and then our actual query, for which we don't know the answer.

Fine-tuning means making a dataset from those sample queries and training the model for a few epochs on this small dataset.

We have $t$ $d$-dimensional tokens, $X \in \R^{d \times t}$, that correspond to the actual text given to a language model, without the last token. The last token is $x \in \R^{d}$.  Also we have $t'$ $d$-dimensional tokens of sample queries, $X' \in \R^{d \times t'}$ (both queries and answers, as a single piece of text).

Our model will be just one layer of [[dot product attention]]. To convert tokens into values, keys and queries we will use $W_{V}, W_{K}, W_{Q} \in \R^{d\times d}$ correspondingly. I use the same $d$ for all dimensions for simplicity, it can be different. Also, denote $q = W_{Q}x$.

## Few-shot learning regime
$$\begin{split}
y
&= \mathrm{Attn}(W_{K}[X'; X], W_{V}[X'; X], q)\\
&= W_{V}[X'; X]\qty(W_{K}[X'; X])^{T}q\\
&= \qty[W_{V}X'; W_{V}X]\qty[W_{K}X'; W_{K}X]^{T} q\\
&= W_{V}X'X'^{T}W_{K}^{T}q + W_{V}XX^{T}W_{K}^{T}q\\
\end{split}$$

Let's denote $w(D) = W_{V}DD^{T}W_{K}$. We can can think that after reading tokens denoted by $D$ our model acts as a linear model w.r.t. the next token and $w(D)$ is the weight matrix for this linear model. Then we get a beautiful equation:
$$y = \qty(w(X) + w(X'))q$$

## Fine-tuning regime
$$\begin{split}
y
&= \mathrm{Attn}\qty\Big((W_{K} + \Delta W_{K})X,
(W_{V} + \Delta W_{V}) X, q)\\
&= (W_{V} + \Delta W_{V})XX^{T}(W_{K} + \Delta W_{K}) q\\
&= \qty\Big(w(X) + W_{V}XX^{T}\Delta W_{K} + \Delta W_{V}XX^{T}W_{K} + \Delta W_{V}XX^{T}\Delta W_{K})q\\
&= (w(X) + \Delta w) q
\end{split}$$

## Comparison
As we can see, both approaches changed the weights of the linear model for the next token.
In the first one it happened by literally adding the linear model from sample queries.
In the second one the actual weights (only $W_{K}$ and $W_{V}$ in this case, though we possibly could fine-tune $W_{Q}$ too) changed during fine-tuning and it also changed the weights of linear model.

To make even deeper analogy recall the relation between gradient descent and attention from [[dual form of linear transformation]]:
$$Wx = W_{0}x + \mathrm{Attn}\qty(X, \mathcal{L}'(X), x)$$
And now look again at the equation for the few-shot regime:
$$\begin{split}
y
&= \mathrm{Attn}(W_{K}[X'; X], W_{V}[X'; X], q)\\
&=  W_{V}XX^{T}W_{K}^{T}q + W_{V}X'X'^{T}W_{K}^{T}q\\
&= w(X)q + \mathrm{Attn}(W_{K}X', W_{V}X', q)
\end{split}$$
As we can see, $W_{K}X'$ acts as a dataset and $W_{V}X'$ as gradients. Note that they are not the actual gradients, but only an output from a part of the model.

According to the authors of the paper, the real gradients and these $W_{V}X'$ are somewhat similar.

## Exercise 1
There is a trick called sign gradient descent, where you do updates as follows:
$$x_{i+1} = x_{i} + \alpha\ \mathrm{sign}(\nabla f(x_{i}))$$
So it should be equivalent to replacing our model with:
$$y = \mathrm{Attn}\qty\Big(W_{K}X, \alpha\ \mathrm{sign}(W_{V}X), q)$$
And $\alpha$ here might be either a constant, or a learnable parameter, or a function of $X$.
How it will behave?