# discounting-aware importance sampling
From [[importance sampling]]
$\physics$
## Definition
It is a version of [[per-decision importance sampling]] where in calculation of the denominator we give more weight to the importance sampling ratios appearing early on, namely, proportional to their $\gamma^{t}$. It helps to reduce variance. In a sense, it applies [[weighted importance sampling]] both along batch and time dimensions.

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
        gamma_sum = (1 - gamma**T) / (1 - gamma)
        denominator += rho.exp() * (gamma**t) / gamma_sum
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
gamma = 0.5

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