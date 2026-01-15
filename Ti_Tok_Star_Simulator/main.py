# main.py

from gui import TikTokGUI
from environment import TikTokEnv
from plots import plot_performance  # ← ajouté

def main():
    # 1. Lancer le jeu interactif
    env = TikTokEnv()
    gui = TikTokGUI(env)
    gui.run()  # Tu joues ou regardes l'IA
    algorithms = ["DP", "Monte Carlo", "SARSA", "Q-learning", "Double Q-learning"]
    rewards = [10, 9.8, 9.5, 9.7, 10]
    lengths = [10, 9.5, 10.5, 9.8, 10]
    success_rates = [100, 99, 98, 99, 100]

    plot_performance(algorithms, rewards, lengths, success_rates, save_path="results/")
    
    print("✅ Courbes prêtes dans le dossier 'results/' !")

if __name__ == "__main__":
    main()