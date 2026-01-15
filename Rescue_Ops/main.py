# main.py

import sys

def show_menu():
    print("\n🧠 Rescue Ops – Évacuation Urbaine")
    print("=" * 40)
    print("1. Jouer toi-même (mode humain)")
    print("2. Regarder l'IA jouer (entraînement + démo)")
    print("3. Quitter")
    print("=" * 40)
    return input("Choisis une option (1/2/3) : ").strip()

def train_and_demo():
    from agent import QLearningAgent
    from environment import RescueOpsEnv
    import time

    env = RescueOpsEnv()
    agent = QLearningAgent(state_size=4, action_size=5)
    episodes = 3000

    print("\n🚀 Entraînement de l'agent...")
    for ep in range(episodes):
        obs, _ = env.reset(seed=ep)
        done = False
        while not done:
            action = agent.choose_action(obs)
            next_obs, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            agent.update(obs, action, reward, next_obs, done)
            obs = next_obs
        agent.decay_epsilon()

    print("✅ Entraînement terminé ! Démonstration...")
    env = RescueOpsEnv(render_mode="human")
    obs, _ = env.reset()
    done = False
    while not done:
        action = agent.choose_action(obs)
        obs, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        env.render()
        time.sleep(0.3)
    env.close()

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            from human_play import run_human
            run_human()
        elif choice == "2":
            train_and_demo()
        elif choice == "3":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Option invalide. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()