# human_play.py

import pygame
import sys
import numpy as np
from environment import RescueOpsEnv
from config import *

def run_human():
    # 🔥 INITIALISER PYGAME ICI, AVANT TOUT
    pygame.init()
    
    # Créer l'environnement
    env = RescueOpsEnv(render_mode="human")
    obs, _ = env.reset(seed=42)
    
    print("🎮 Mode Joueur Humain - Sauvez les civils !")
    print("Flèches : Déplacer | Espace : Rester sur place | ESC : Quitter")
    
    running = True
    done = False
    
    # Afficher l'état initial
    env.render()
    
    while running and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                action = None
                if event.key == pygame.K_UP:
                    action = 0  # Haut
                elif event.key == pygame.K_DOWN:
                    action = 1  # Bas
                elif event.key == pygame.K_LEFT:
                    action = 2  # Gauche
                elif event.key == pygame.K_RIGHT:
                    action = 3  # Droite
                elif event.key == pygame.K_SPACE:
                    action = 4  # Rester
                elif event.key == pygame.K_ESCAPE:
                    running = False
                
                if action is not None:
                    obs, reward, terminated, truncated, _ = env.step(action)
                    done = terminated or truncated
                    env.render()
                    
                    # Afficher info
                    print(f"Action: {['Haut','Bas','Gauche','Droite','Rester'][action]} | Récompense: {reward:.1f}")
                    
                    if done:
                        if reward > 0:
                            print("🎉 Mission réussie ! Tous les civils sont sauvés !")
                        else:
                            print("💀 Mission échouée...")
                        pygame.time.wait(2000)
    
    env.close()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run_human()