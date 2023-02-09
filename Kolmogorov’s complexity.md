# Kolmogorov’s complexity
From [[algorithmic information theory]], type of [[information complexity]], related to [[algorithmic probability]]

## Definition
For a given signal it’s the length of a shortest program that will produce that signal.

## Special cases
First, programms that are longer than the data are useless. There is always a program that puts all probability on the observed data and its length is $\abs{\text{data}} + O(1)$.

Second, if you have an algorithm that computes the whole sequence, the length of program you need for the first $n$ elements is $O(\log n)$, because you need to write $n$ there and it takes $\log_{2} n$ bits.