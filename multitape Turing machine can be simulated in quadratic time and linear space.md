# multitape Turing machine can be simulated in quadratic time and linear space
From [[Turing machine]] and [[multitape Turing machine]]
$\physics$
## Statement
Let $M$ be a $k$-tape [[Turing machine]]. There is a single-tape TM $S$ that produces the same output and for each input $w$ if $M$ worked in $t(w)$ time and $s(w)$ space (= used tape cells), $S$ works in $\order{t^{2}(w)}$ and $\order{s^{2}(w)}$.

## Proof
We put the contents of all $k$ tapes as contiguous blocks separated by `#`.
For example:
```
01010
aaa
ba
```
Will be converted to:
```
#01010#aaa#ba#
```
Then we extend the tape alphabet to store an extra bit with each symbol, which will mark where the head is for each tape.
So, if we want to simulate $M$ on `abacaba` the initial tape for single-tape $S$ will look as follows:
```
#(a)bacaba#(B)#(B)#...#(B)#
```
For a single move of $M$ we have $S$ to do:
- Go to the leftmost `#` (we store number of `#` to the left in the state)
- Go to the rightmost `#` and store $k$ symbols under heads in state
- Go back, when going over one of the symbols under heads apply the transition.
- Go to the right again, if there is `(#)`, it means that the current tape needs to be extended. We have $k$ tapes, so we need to store at most $k$ symbols in the state to extend all of them in a single pass.