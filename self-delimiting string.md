# self-delimiting string
From [[algorithmic information theory]]
$\physics$
We want a function that maps strings to strings in such way that the set of encodings is prefix-free. We will define it as map from numbers to strings because of [[string to number correspondence]].

$$E_{i} = \begin{cases}
1^{x}0 & i  = 0\\
E_{i-1}(l(x))x & i > 0
\end{cases}$$

$E_1(x)$ is denoted $\bar x$ and is called the self-delimiting version of binary string $x$. 
$$\bar x = 1^{l(x)}0x \quad l(\bar x) = 2l(x) + 1$$
Sometimes $E_{2}(x)$ is also used, for it $l(E_{2}(x)) = l(x) + 2l(l(x)) + 1$.

Note that $l(E_{1}(x)) \leq l(x) + 2 \leq x + 2$ and $l(E_{2}(x)) \leq x + 3$.
| x   | $E_0(x)$ | $E_{1}(x)$ | $E_{2}(x)$ |
| --- | -------- | ---------- | ---------- |
| 0   | 0        | 0          | 0          |
| 1   | 10       | 100        | 1000       |
| 2   | 110      | 101        | 1001       |
| 3   | 1110     | 11000      | 10100      |
| 4   | 11110    | 11001      | 10101      |
| 5   | 111110   | 11010      | 10110           |
| 6   | 1111110  | 11011      |  10111          |
| 7   | 11111110 | 1110000    |  11000000          |

````python
alphabet = 2

def s2n(s):
    n = 0
    for i in range(len(s)):
        n += (s[-(i + 1)] + 1) * alphabet ** i
    return n

def n2s(n):
    if not n:
        return []
    s = [n]
    while s[-1] > alphabet:
        t = (s[-1] - 1) // alphabet
        s[-1] -= t * alphabet
        s.append(t)
    return [x - 1 for x in s[::-1]]

def E(i, x):
    if i == 0:
        return "1" * x + "0"
    else:
        x_s = ''.join(map(str, n2s(x)))
        return E(i - 1, len(x_s)) + x_s
```