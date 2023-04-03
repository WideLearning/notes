# set of finite measure as finite disjoint union of sets with small measure
From [[approximation of measurable sets]]
$\physics$
## Statement
If $E$ is a [[measurable set]] with finite measure and $\varepsilon > 0$, $E$ is the disjoint union of a finite number of measurable sets with measure less than $\varepsilon$.

## Proof
Because $E$ has finite measure, there is an interval cover of it with finite total length. There is a finite number of intervals longer than $\varepsilon / 10$, split them into intervals not longer than $\varepsilon$ and add to the answer. 

Now instead of splitting intervals we will unite them in groups. Until the total sum of lengths is not less than $\varepsilon$, find the largest prefix that has sum less than $\varepsilon$ (in other words, find the first which is not less, which we can do by definition of limit). Add their union to the answer. Because we have removed all long intervals, the total length of each group will be $\Theta(\varepsilon)$, and in finite number of steps this process will end.

Finally, [[countable union of measurable sets can be made disjoint]].