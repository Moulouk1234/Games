# agent.py

import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

def create_agent(env):
    env = DummyVecEnv([lambda: env])
    model = PPO("MlpPolicy", env, verbose=0, n_steps=128)
    return model

def train_agent(model, total_timesteps=5000):
    print("🚀 Entraînement de l'agent...")
    model.learn(total_timesteps=total_timesteps)
    print("✅ Entraînement terminé !")
    return model

def get_action(model, obs):
    obs = obs.reshape(1, -1)
    action, _ = model.predict(obs, deterministic=True)
    return int(action[0])