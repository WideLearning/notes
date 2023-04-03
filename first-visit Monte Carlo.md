# first-visit Monte Carlo
From [[Monte Carlo methods]]
$\physics$
## Definition
The main difference from [[every-visit Monte Carlo]] is for the cases where one state is encountered several times during the episode. This method adds the return only ones for each unique state.

## Properties
- Estimates converge at $\order{\frac{1}{\sqrt{n}}}$ rate, where $n$ is the number of averaged episodes. Because in this case samples are independent, it follows from [[central limit theorem]].