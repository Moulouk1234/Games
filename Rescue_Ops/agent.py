# agent.py

import numpy as np
import random

class QLearningAgent:
    def __init__(self, state_size, action_size, lr=0.1, gamma=0.99, epsilon=1.0):
        self.state_size = state_size
        self.action_size = action_size
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def discretize_state(self, state):
        # Discrétiser l'état continu en tuple entier
        x, y, fuel, civ = state
        return (int(x), int(y), int(fuel // 5), int(civ))

    def choose_action(self, state):
        disc_state = self.discretize_state(state)
        if disc_state not in self.q_table:
            self.q_table[disc_state] = np.zeros(self.action_size)

        if random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)
        else:
            return np.argmax(self.q_table[disc_state])

    def update(self, state, action, reward, next_state, done):
        s = self.discretize_state(state)
        s_next = self.discretize_state(next_state)

        if s not in self.q_table:
            self.q_table[s] = np.zeros(self.action_size)
        if s_next not in self.q_table:
            self.q_table[s_next] = np.zeros(self.action_size)

        target = reward
        if not done:
            target += self.gamma * np.max(self.q_table[s_next])

        self.q_table[s][action] += self.lr * (target - self.q_table[s][action])

    def decay_epsilon(self, min_eps=0.1):
        if self.epsilon > min_eps:
            self.epsilon *= 0.995