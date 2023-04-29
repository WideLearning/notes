# per-decision importance sampling
From [[importance sampling]]
$\physics$
## Definition
It is an improvement of [[importance sampling]] for the special case where the sampled value can be decomposed into a sum of values from [[Markov decision process]]:
$$G = \sum\limits_{t \leq T} \gamma^{t}R_{t}$$
$$\rho_{l:r} = \frac{\prod_{k=l}^{r}\pi(A_{k}\mid S_{k})p(S_{k+1}\mid S_{k}, A_{k})}{\prod_{k=l}^{r}b(A_{k}\mid S_{k})p(S_{k+1}\mid S_{k}, A_{k})} = \frac{\prod_{k=l}^{r}\pi(A_{k}\mid S_{k})}{\prod_{k=l}^{r}b(A_{k}\mid S_{k})}$$
Then ordinary importance sampling is:
$$E_{\pi}(G) = E_{b}(\rho_{0:T-1}G)$$
And per-decision version is:
$$E_{\pi}\left(\sum\limits_{t \leq T} R_{t}\right) = E_{b}\left(\sum\limits_{t \leq T} \rho_{0:t-1}R_{t}\right)$$
And [[weighted importance sampling]] in this case means dividing sum of weighted rewards by $\frac{B}{T}\sum\limits_{t \leq T} \rho_{0:t-1}$ instead of $B$, where $B$ is the number of available samples.

## Proof
We need to check it for a single reward:
$$E_{b}(\rho_{0:T-1}R_{t}) = E_{b}(\rho_{0:t-1}R_{t})$$
Which follows from:
$$\forall s. E_{b}(\rho_{t:T-1} \mid S_{t} = s) = 1$$
$$E_{b}(\rho_{t:T-1} \mid S_{t} = s) = \sum\limits_{\text{paths from } s} \left(\frac{\prod \pi(A_{k} \mid S_{k})p(S_{k+1} \mid S_{k}, A_k)}{\prod b(A_{k} \mid S_{k})p(S_{k+1} \mid S_{k}, A_{k})}\prod b(A_{k} \mid S_{k})p(S_{k+1} \mid S_{k}, A_{k})\right) = 1$$
## See also
- [[per-decision importance sampling with control variates]] for the case where we have a baseline value closer to $\E_{b}(R_{t})$ than zero.

## Test implementation
```python
import torch


def run_episode(
    pi: torch.tensor,
    b: torch.tensor,
    r: torch.tensor,
    gamma: float,
    T: int,
    batch_size: int,
):
    """
    importance sampling for batch_size episodes with length T,
    target policy pi, behavior policy b, transition reward r and discount factor gamma
    """
    # start always in 0
    v = torch.zeros(batch_size, dtype=torch.long)
    # log of importance sampling ratio
    rho = torch.zeros(batch_size)
    # running total of weighted rewards
    numerator = torch.zeros(batch_size)
    # running total of weights
    denominator = torch.zeros(batch_size)
    # do T iterations
    for t in range(T):
        # choose next state according to b
        u = torch.multinomial(b[v], 1).squeeze()
        # current reward
        R = r[v, u]
        # update importance sampling ratio
        rho += pi[v, u].log() - b[v, u].log()
        # update total
        numerator += rho.exp() * R * (gamma**t)
        # numerator += R * (gamma**t)
        denominator += rho.exp() / T
        # update state
        v = u
    # compute results
    ordinary = numerator.sum() / batch_size
    weighted = numerator.sum() / denominator.sum()
    return ordinary, weighted


# size of MDP
n = 10
# target policy
pi = torch.softmax(torch.randn((n, n)), dim=1)
# behavior policy
b = torch.softmax(torch.randn((n, n)), dim=1)
# transition reward matrix
r = torch.randn((n, n))
# discount factor
gamma = 0.9

# number of episodes to average from
num_episodes = 10**3
# length of each episode
T = 10
# number of experiments
samples = 100

# matrix with results
res = torch.zeros((0, 6))

for it in range(samples):
    # measure rewards directly (b = pi)
    dir_o, dir_w = run_episode(pi, pi, r, gamma, T, num_episodes)
    # now with importance sampling
    imp_o, imp_w = run_episode(pi, b, r, gamma, T, num_episodes)
    # and directly for b
    chk_b, chk_w = 0, 0  # run_episode(b, b, r, gamma, T, num_episodes)
    # vector with current results
    res = torch.cat(
        (res, torch.tensor([dir_o, dir_w, imp_o, imp_w, chk_b, chk_w]).unsqueeze(0)),
        dim=0,
    )
    # means
    res_mean = res.mean(dim=0)
    # stds
    res_std = res.std(dim=0) / torch.sqrt(torch.tensor(it) + 1)
    # show results
    print(
        f"{res_mean[0]:0.3f}±{res_std[0]:0.3f}\t{res_mean[1]:0.3f}±{res_std[1]:0.3f}\t{res_mean[2]:0.3f}±{res_std[2]:0.3f}\t{res_mean[3]:0.3f}±{res_std[3]:0.3f}"  # \t{res_mean[4]:0.3f}±{res_std[4]:0.3f}\t{res_mean[5]:0.3f}±{res_std[5]:0.3f}"
    )
```