# prioritized sweeping
From [[model-based methods]]
$\physics$
## Definition
```python
# S - current state
# Q(s, a) - action value approximation
# model(s, a) - deterministic approximation of environment
# pq - priority queue for updates

while True:
	A = sample(policy(S, Q))
	R, S_new = env(S, A)
	model(s, a) = (R, S_new)
	P = abs(R + gamma * max(Q(S_new, a)) - Q(S, A))
	pq.insert(P, (S, A))
	for _ in range(n) and while pq:
		S, A = pq.pop()
		R, S_new = model(S, A)
		Q(S, A) += alpha * (R + gamma * max(Q(S_new, a)) - Q(S, A))
		for (S_p, A_p) if model(S_p, A_p)[1] == S:
			R_p = model(S_p, A_p)[0]
			P = abs(R_p + gamma * max(Q(S, a)) - Q(S_p, A_p))
			pq.insert(P, (S_p, A_p))
```

## See also
- [[trajectory sampling]] is another optimization of sweeping. How are they related?