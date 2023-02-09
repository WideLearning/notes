# gymnasium
From [[reinforcement learning]]
$\physics$
It is a popular open-source framework for RL in python.

- [documentation main page](https://gymnasium.farama.org/)
- [creating custom environment](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/#sphx-glr-tutorials-gymnasium-basics-environment-creation-py)
- [vectorized environments](https://gymnasium.farama.org/tutorials/gymnasium_basics/vector_envs_tutorial/)

## simple custom environment
```python
import gymnasium as gym
import numpy as np
from gymnasium import spaces


class Bandit(gym.Env):
    metadata = {"render_modes": ["ansi"], "render_fps": 4}

    def __init__(self, render_mode=None, means=np.zeros(1), stds=np.ones(1)):
        assert means.shape == stds.shape
        assert means.ndim == 1
        self.k = means.size
        self.means = means
        self.stds = stds
        self.observation_space = spaces.Box(low=0, high=1, shape=(1,))
        self.action_space = spaces.Discrete(self.k)

    def _get_obs(self):
        return np.zeros(1, dtype=np.float32)

    def _get_info(self):
        return {}

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        # reset the state here if needed
        observation = self._get_obs()
        info = self._get_info()
        # render here if needed
        return observation, info

    def step(self, action):
        assert self.action_space.contains(action)

        terminated = False
        reward = self.np_random.normal(self.means[action], self.stds[action])
        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, False, info
```