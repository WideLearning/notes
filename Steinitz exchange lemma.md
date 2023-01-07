# Steinitz exchange lemma
From [[linear dependence]]

## Statement
Suppose $u_{[m]}$ is independent in $V$ and $w_{[n]}$ spans $V$.
Then $m \leq n$.

## Proof
After $k$ steps we have linearly independent prefix of size $k$ in $w$ and also size of $u$ is $m - k$. Then we take arbitrary vector from $u$ and put it to the end of independent prefix in $w$. Because $w$ was spanning, now it must be linearly dependent, so by [[linear dependence lemma]] we can remove one of the old vectors from there now and it will still span $V$.

After $m$ steps we will have a (linearly independent) prefix of size $m$ in $w$, which means that its size is not less. 