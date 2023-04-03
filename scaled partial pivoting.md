# scaled partial pivoting
From [[Gaussian elimination]]
$\physics$
## Algorithm
pivoting — pivot element is chosen not arbitrary.
partial — columns are not exchanged.
scaled — maximize `a[i].abs()[col] / a[i].abs().max()` when selecting pivot on each step.