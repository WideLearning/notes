# Cook-Levin theorem
From [[time complexity]]
$\physics$
## Statement
Boolean satisfability (SAT) is [[NP-complete]].

## Proof
First, clearly SAT is in [[class NP]], because we can verify a given assignment in a polynomial time.
Now we want to show [[polynomial time reducibility]] from arbitrary $A \in \textbf{NP}$ to $SAT$. Let’s consider not $A$, but its nondeterministic decider $N$. Fix some polynomial upper bound $p(n)$ such that for an input of size $n$ the decider $N$ does no more than $p(n)$ steps before halting.
Now consider a $(p(n) + 1) \times (p(n) + 3)$ table, where each row is of the form $\#c_{0}c_{1}\dots c_{i} q c_{i+1} \dots c_{p(n)-1} \#$ ([[configuration of Turing machine]]). We add to our boolean formula clauses that fix the first row to be equal to start configuration for the given instance of $A$. Then we add clause that somewhere in the table there must be an accepting configuration (row with $q = q_{accept}$). And for each pair of adjacent rows we add clauses which check that the first one yields the second. Also, of course, there must be conditions saying that there is exactly one symbol in each cell.
Our conversion is polynomial time because the table has $\order{p(n)^{2}}$ size and the number of clauses and variables is also $\order{p(n)^{2}}$. To store them we need to use indices, so the total size of encoding for the formula will be $\order{p(n)^{2}\log n}$.