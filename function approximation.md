# function approximation
From [[reinforcement learning]]
$\physics$
For large state spaces it is often intractable to store value function estimates for all values, and also it is intractable to visit all states, so we want to be able to generalize to all states with a finite amount of experience and memory.

## Parametric
Here our approximation has a finite representation capacity and the data only helps to find more accurate parameter values.

- Linear methods, here we can update iteratively or use least-squares which requires more computation but less data
	- Polynomials
	- Fourier basis
	- Coarse coding and tile coding
	- Radial basis functions
	- Neural networks

## Non-parametric
These methods don’t update anything while learning, only do queries to the data when the approximation is need. The more data is available, the more complex will be the approximation.

- kNN (remember [[data structures for nearest neighbor search]])
- Kernel methods (though still can be used with kNN data structures to improve speed)