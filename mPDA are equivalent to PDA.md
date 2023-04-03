# mPDA are equivalent to PDA
From [[modified pushdown automaton]] and [[pushdown automaton]]
$\physics$
## Statement
For each [[pushdown automaton]] there is a [[modified pushdown automaton]] with the same language.

## Proof
We achieve single accepting state by adding $v, \varepsilon, \varepsilon \to u, \varepsilon$ transitions where $v$ is old accepting state and $u$ is new accepting state.

To detect whether stack is empty we add new symbol $\$$ to $\Gamma$. Now before doing anything else, we put $\$$ onto the stack. In the end we clean stack until we read $\$$ before accepting.

Then we replace pop-and-push transitions with two, where the first pops, goes to new state (from which the taken symbol can be identified), and then pushes. And transitions that don’t interact with the stack we also split — first they push arbitrary symbol, then remove it.