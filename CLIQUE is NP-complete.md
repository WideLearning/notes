# CLIQUE is NP-complete
From [[time complexity]]
$\physics$
## Statement
The problem of checking for $\ev{G, k}$ whether there is a clique of size $k$ in the undirected graph $G$ is [[NP-complete]].

## Proof
We will use [[polynomial time reducibility]] to 3-SAT, as [[3-SAT is NP-complete]].

Consider a 3-SAT formula:
$$F = \bigwedge\limits_{i \in [k]} (L_{i, 1} \vee L_{i, 2} \vee L_{i, 3})$$
Then we take variables ($L_{i,j}$) as vertices. We want a clique of size $n$ (the number of clauses) in $G$ to mean which literals can be set to true to satisfy all clauses. To do so we add edges between all pairs of vertices, except for the ones from the same clause (so now only one variable can be chosen from each) and for negations (so $x$ and $\bar x$ can’t be chosen together). Now any valid assignment gives a clique of size $n$, because we can select one true literal from each clause. Conversely, any such clique guarantees that we get a valid assignment by setting the variables from the clique to true and others to false. 

Note that $L_{i,j}$ stores the name of the variable and they don’t need to be unique, so we can have e.g. $L_{2, 2} = L_{4, 1}$. 