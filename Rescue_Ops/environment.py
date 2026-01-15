# environment.py

import gymnasium as gym
from gymnasium import spaces
import numpy as np
from config import GRID_SIZE, FUEL_MAX

class RescueOpsEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode
        self.grid_size = GRID_SIZE
        self.fuel_max = FUEL_MAX

        # Actions: 0=Haut, 1=Bas, 2=Gauche, 3=Droite, 4=Rester
        self.action_space = spaces.Discrete(5)

        # Observation: position agent (x,y), fuel, civilians restants
        self.observation_space = spaces.Box(
            low=0, high=max(GRID_SIZE, FUEL_MAX), shape=(4,), dtype=np.float32
        )

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        if seed is not None:
            np.random.seed(seed)

        # Position agent
        self.agent_pos = [np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)]

        # Position sortie
        self.exit_pos = [np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)]
        while self.exit_pos == self.agent_pos:
            self.exit_pos = [np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)]

        # Civils (3)
        self.civilians = []
        for _ in range(3):
            pos = [np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)]
            while pos in [self.agent_pos, self.exit_pos] or pos in self.civilians:
                pos = [np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)]
            self.civilians.append(pos)

        # Zombies (2)
        self.zombies = []
        for _ in range(2):
            pos = [np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)]
            while pos in [self.agent_pos, self.exit_pos] or pos in self.civilians or pos in self.zombies:
                pos = [np.random.randint(0, self.grid_size), np.random.randint(0, self.grid_size)]
            self.zombies.append(pos)

        self.fuel = self.fuel_max
        self.rescued = 0
        self.done = False

        return self._get_obs(), {}

    def _get_obs(self):
        return np.array([
            self.agent_pos[0],
            self.agent_pos[1],
            self.fuel,
            len(self.civilians)
        ], dtype=np.float32)

    def step(self, action):
        reward = -0.1
        terminated = False
        truncated = False

        # Déplacement
        moves = [(-1,0), (1,0), (0,-1), (0,1), (0,0)]
        dx, dy = moves[action]
        new_x = max(0, min(self.grid_size - 1, self.agent_pos[0] + dx))
        new_y = max(0, min(self.grid_size - 1, self.agent_pos[1] + dy))
        self.agent_pos = [new_x, new_y]

        # Consommer carburant
        if action != 4:  # Ne pas consommer si "rester"
            self.fuel -= 1

        # Collision zombie
        if self.agent_pos in self.zombies:
            reward += -100
            terminated = True

        # Ramasser civil
        if self.agent_pos in self.civilians:
            self.civilians.remove(self.agent_pos)
            self.rescued += 1
            reward += 10

        # Atteindre sortie avec tous les civils
        if self.agent_pos == self.exit_pos and len(self.civilians) == 0:
            reward += 50
            terminated = True

        # Carburant épuisé
        if self.fuel <= 0:
            reward += -50
            terminated = True

        return self._get_obs(), reward, terminated, truncated, {}

    def render(self):
        if self.render_mode == "human":
            from game_renderer import render_game
            render_game(self)

    def close(self):
        pass