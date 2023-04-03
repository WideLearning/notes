# important properties of conjugate gradient method
From [[conjugate gradient method]]
$\physics$
## Statement
Until the solution is found, the following properties hold on $k$-th iteration:
1. $\forall i < k. r_{i}^{T}r_{k} = 0$
2. $\exists c_{k}. p_{k} = c_{k} A^{k}r_{0} + v_{k}, v_{k} \in \ev{p_{0}, \dots, p_{k-1}}$
3. $\ev{r_{0}, r_{1}, \dots, r_{k}} = \ev{r_{0}, Ar_{0}, \dots, A^{k} r_{0}}$
4. $\ev{p_{0}, p_{1}, \dots, p_{k}} = \ev{r_{0}, Ar_{0}, \dots, A^{k} r_{0}}$
5. $\forall i < k. p_{k}^{T}Ap_{i} = 0$

## Proof
First, let’s recall the equations:
$$\begin{cases}
r_{k} = Ax_{k} - b\\
p_{k+1} = -r_{k+1} + \beta_{k+1}p_{k}\\
x_{k+1} = x_{k} + \alpha_{k}p_{k}\\
\alpha_{k} = -\frac{r_{k}^{T}p_{k}}{p_{k}^{T}Ap_{k}}\\
\beta_{k+1} = \frac{r_{k+1}^{T}Ap_{k}}{p_{k}^{T}Ap_{k}} \\
\end{cases}$$
For $k = 0$ all this obviously holds. Now $k \to k + 1$:
1. From [[expanding subspace minimization]] we know $r_{k+1} \in \ev{p_{0}, \dots, p_{k}}^{T} = \ev{r_{0}, \dots, r_{k}}^{T}$ (used (3) and (4) in transition).
2. From (3), $r_{k+1} \in c_{k}A^{k}r_{0} + \ev{r_{0}, Ar_{0}, \dots, A^{k} r_{0}}$. With (4) we replace it by $r_{k} \in c_{k} A^{k}r_{0} + \ev{p_{[0:k]}}$.
3. $r_{k+1} = Ax_{k+1} - b = A(x_{k} + \alpha_{k} p_{k}) - b = r_{k} + \alpha_{k} A p_{k}$. From (2), $r_{k+1} = r_{k} + \alpha_{k} c_{k} A^{k+1}r_{0}$. It also proves the other direction, because $A^{k+1}r_{0} = \frac{r_{k+1} - r_{k}}{\alpha_{k}c_{k}}$.
4. $p_{k+1} = \beta_{k+1}p_{k} - r_{k+1}$, where $r_{k+1} \in \alpha_{k} c_{k} A^{k+1}r_{0} + \ev{r_{0}, \dots, A^{k} r_0}$ and $p_{k} \in \ev{r_{0}, \dots, A^{k} r_{0}}$, so $p_{k+1} \in -\alpha_{k} c_{k} A^{k+1}r_{0} + \ev{r_{0}, \dots, A^{k} r_0}$. It also means $c_{k+1} = \prod\limits_{[k]} (-\alpha_{i})$.
5. $p_{k+1}^{T}Ap_{i} = -p_{k+1}^{T}Ar_{i} + \beta_{k+1} p_{k}^{T}Ap_{i}$. $Ar_{i} \in A\ev{r_{0}, \dots, A^{i}r_{0}} = \ev{r_{0}, \dots, A^{i+1}r_{0}} = \ev{r_{0}, \dots, r_{i+1}}$, so the first term is zero for $i < k$ (and for $i = k$ everything is ok by construction) by [[expanding subspace minimization]]. And the second term is also zero for $i < k$, by induction hypothesis.