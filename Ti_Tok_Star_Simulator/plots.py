# plots.py

import matplotlib.pyplot as plt
import numpy as np
import os

def plot_performance(algorithms, rewards, lengths, success_rates, save_path="results/"):
    """
    Génère et sauvegarde 3 graphiques :
    - Récompense moyenne
    - Longueur moyenne de l'épisode
    - Taux de succès (%)
    
    Sauvegardés dans le dossier `save_path`
    """
    # Créer le dossier s'il n'existe pas
    os.makedirs(save_path, exist_ok=True)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # 1. Récompense moyenne
    axes[0].bar(algorithms, rewards, color='skyblue')
    axes[0].set_title('Récompense moyenne')
    axes[0].set_ylabel('Récompense')
    axes[0].set_xticklabels(algorithms, rotation=45)
    
    # 2. Longueur moyenne de l'épisode
    axes[1].bar(algorithms, lengths, color='lightgreen')
    axes[1].set_title('Longueur moyenne de l’épisode')
    axes[1].set_ylabel('Nombre de pas')
    axes[1].set_xticklabels(algorithms, rotation=45)
    
    # 3. Taux de succès
    axes[2].bar(algorithms, success_rates, color='salmon')
    axes[2].set_title('Taux de succès (%)')
    axes[2].set_ylabel('Pourcentage')
    axes[2].set_ylim(0, 100)
    axes[2].set_xticklabels(algorithms, rotation=45)
    
    plt.tight_layout()
    
    # Sauvegarder l'image
    filename = "performance_comparison.png"
    filepath = os.path.join(save_path, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"✅ Courbes sauvegardées dans : {filepath}")
    
    # Afficher aussi à l'écran (optionnel)
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    algorithms = ["DP", "Monte Carlo", "SARSA", "Q-learning", "Double Q-learning"]
    rewards = [10, 9.8, 9.5, 9.7, 10]
    lengths = [10, 9.5, 10.5, 9.8, 10]
    success_rates = [100, 99, 98, 99, 100]
    plot_performance(algorithms, rewards, lengths, success_rates, save_path="results/")