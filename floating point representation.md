# floating point representation
From [[numerical methods]]
$\physics$
## Definition
Normalized floating point representation of $x$ with base $b$ has form
$$x = 0.a_{1}a_{2}\dots a_{k} \cdot b^{n}, a_{1} \ne 0$$
where $k$ is precision, $n$ is exponent, $\overline{a_{1}\dots a_{k}}$ is mantissa.

For $b = 2$ there is no need to store $a_{1} = 1$ explicitly, this trick is called implicit leading bit.

Actually, in IEEE-754, normalized numbers have form $a_{1}.a_{2}a_{3}\dots a_{k} \cdot b_{n}$ with $a_{1} \ne 0$, without leading zero.

## Examples
For single-precision (aka `float`) bits are distributed as follows:
- 1: mantissa sign
- 1+7: exponent (in biased form, ranging from -127 to 128, the ends are reserved for special numbers)
- 24-1: mantissa (precision is 24, but only 23 bits are stored)

- [[problematic subtraction]]