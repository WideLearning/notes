# Kolmogorov’s complexity
From [[applications of Kolmogorov complexity]], type of [[information complexity]]

## Definition
As in [[invariance theorem]] and [[conditional invariance theorem]], fix some universal $\phi_{0}$ and define:
$$K(x) = C_{\phi_{0}}(x) = C_{\phi_{0}}(x \mid \varepsilon)$$
$$K(x \mid y) = C_{\phi_{0}}(x \mid y)$$

## Properties
- [[invariance theorem]]
- [[conditional invariance theorem]]
- $K(x) \leq l(x) + \order{1}$
- $K(x \mid y) \leq K(x) + \order{1}$
- $K(\ev{x, y}) \leq K(x) + K(y) + 2 \log \min(K(x), K(y)) + \order{1}$
- $K(x^{*} \mid x) = K(K(x) \mid x) \leq K(K(x)) \leq \log  l(x)$ where $x^{*}$ is the first program to halt with output $x$ among the programs with length $K(x)$
- [[assigning small complexity to complex objects]]

## Special cases
First, programms that are longer than the data are useless. There is always a program that puts all probability on the observed data and its length is $\abs{\text{data}} + O(1)$.

Second, if you have an algorithm that computes the whole sequence, the length of program you need for the first $n$ elements is $O(\log n)$, because you need to write $n$ there and it takes $\log_{2} n$ bits.

## See also
- [[algorithmic probability]]