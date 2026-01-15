# environment.py

import numpy as np

class TikTokEnv:
    def __init__(self):
        self.followers = 100
        self.engagement = 0.5
        self.day = 1
        self.max_days = 10
        self.troll_chance = 0.1
        self.burnout_threshold = 0.8
        
        self.action_space = 5
        self.observation_space = 3
    
    def reset(self):
        self.followers = 100
        self.engagement = 0.5
        self.day = 1
        return np.array([self.followers, self.engagement, self.day])
    
    def step(self, action):
        reward = 0
        done = False
        
        if action == 0:  # Publier
            reward += 5
            self.followers += np.random.randint(5, 20)
            self.engagement += 0.05
        elif action == 1:  # Liker
            reward += 1
            self.engagement += 0.01
        elif action == 2:  # Commenter
            reward += 2
            self.engagement += 0.03
        elif action == 3:  # Partager
            reward += 3
            self.followers += np.random.randint(2, 10)
        elif action == 4:  # Se reposer
            reward += 0.5
            self.engagement -= 0.02
        
        # Risque de troll
        if np.random.random() < self.troll_chance:
            reward -= 10
            self.followers -= np.random.randint(5, 15)
            self.engagement -= 0.1
        
        # Burnout
        if self.engagement > self.burnout_threshold:
            reward -= 20
            self.engagement -= 0.3
        
        self.day += 1
        if self.day > self.max_days:
            done = True
        
        obs = np.array([self.followers, self.engagement, self.day])
        return obs, reward, done, {}