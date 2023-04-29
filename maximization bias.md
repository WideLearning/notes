# maximization bias
From [[temporal-difference learning]]
$\physics$
## Statement
Maximum of estimates is a positively biased estimate of maximum. Therefore algorithms like [[Q-learning]] that use maximum of estimates will tend to overestimate value functions. 

It can be fixed if we use two separate estimates: one for choosing which of the options is maximum, another to get the estimate for this option. It is the idea of [[double Q-learning]].