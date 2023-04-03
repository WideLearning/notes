# sample average as action value
From [[action-value methods for bandit problem]]
$\physics$
## Definition
$$Q_{t}(a) = \frac{\sum\limits_{i \in [t-1]} [A_{i} = a]R_{i}}{\sum\limits_{i\in [t-1]} [A_{i} = a]}$$
Or in incremental way:
$$Q_{t}(a) = Q_{t-1}(a) + \frac{1}{t}\Big[R_{t}(a) - Q_{t}(a)\Big]$$
## Properties
Works well for stationary problems. If reward distribution changes over time [[exponential weighted average as action value]] might work better.