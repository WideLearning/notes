# Markov chain
from [[probability theory concepts]]

when we have many [[random variables]] that may depend on each other, saying anything about them is very hard, so it’s convenient to merge them in such way, that only neighbors are dependent.
more precisely, the markov chain is $n$ [[random variables]] $X_{1}, \dots, X_{n}$ where every variable might depent only on the previous, that is:
$$ P[X_{i+1}=a \mid X_{1} = a_{1}, \dots, X_{i} = a_{i}] = P[X_{i+1}=a \mid X_{i} = a_{i}] $$
also, often it’s assumed that the chain is _time-homogeneous_, that is $P[X_{i+1}=a \mid X_{i}= a_{i}]$ is the same for all $i$. in this case the distribution of all variables is described by one transition matrix. note, that we multiply by this matrix from the right, not as usually in linear algebra.

there are [[transient states]] and [[recurrent states]]. there are also [[periodic states]] and _aperiodic_, if all states are aperiodic, chain itself is also called _aperiodic_.

chain is called _irreducible_ if for any two states there is a positive probability of reaching one from the other (in finite time). note, that from it follows, tha all states are recurrent, but not vice versa. for irreducible chains there exists a unique [[stationary distribution]].

there is also [[reversibility of markov chain]], which sometimes allows to find [[stationary distribution]] easier, because [[reversibility implies stationarity]] and checking it might be easier.

[[Markov Chain Monte Carlo (MCMC)]] uses the markov chains to simulate many interesting distributions.
