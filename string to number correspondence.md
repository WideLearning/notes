# string to number correspondence
From [[algorithmic information theory]]
$\physics$
Common binary representation doesn’t provide a convenient bijection between  strings and numbers. Instead, let’s sort strings first by length then lexicographically and use such order to map them to numbers:
```
0 
1 0
2 1
3 00
4 01
5 10
6 11
7 000
8 001
9 010
10 011
11 100
12 101
13 110
14 111
15 0000
16 0001
17 0010
18 0011
19 0100
```

There is an efficient algorithm for conversion, where we do almost the same as for common representation, but now use $1, 2, \dots, n$ instead of $0, 1, \dots, n - 1$ as numbers for $n$-ary system. And zero corresponds to an empty string.
```python
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
```