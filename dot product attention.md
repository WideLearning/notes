# dot product attention
From [[attention]]

First, let's denote the sizes of all matrices:
$K \in \mathbb{R}^{d_{in} \times T}$ (keys are columns of this matrix)
$V \in \mathbb{R}^{d_{out} \times T}$ (values are also in columns)
$q \in \mathbb{R}^{d_{in}}$ (query is a column-vector)

Here we have a simple similarity score, which is just a dot product:
$$S(k_{i}, q) = \langle k_{i}, q \rangle = k_{i}^{T} q, \quad S(K, q) = K^{T} q \in \mathbb{R}^{T}$$$$\begin{split}
\mathrm{Attention}(K, V, q) 
&= \sum\limits_{i=1}^{n} S(k_{i}, q) v_{i}\\
&= \sum\limits_{i=1}^{n} k_{i}^{T} q v_{i}\\
&= \sum\limits_{i=1}^{n} v_{i} (K^{T} q)_{i}\\
&= V K^{T} q\\
\end{split}$$