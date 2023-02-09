# reversibility implies stationarity
from [[Markov chain]]

consider a [[Markov chain]] with matrix $Q$ which is [[reversibility of markov chain|reversible]], with distribution $s$. suppose we don’t assume it to be [[stationary distribution]], now we will prove that it actually is:
$$ \forall i: s_{i}Q' = \sum\limits_{p} s_{p} Q'_{p,i} = \sum\limits_{p} s_{p} Q_{i,p} \frac{s_{i}}{s_{p}} = s_{i} \sum\limits_{p} Q_{i,p} = s_{i} $$