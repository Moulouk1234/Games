# config.py

import pygame

# Grille
GRID_SIZE = 10
CELL_SIZE = 50

# Couleurs
BACKGROUND = (30, 30, 50)
AGENT_COLOR = (0, 200, 255)     # Bleu ciel
CIVILIAN_COLOR = (255, 255, 0)  # Jaune
ZOMBIE_COLOR = (200, 0, 0)      # Rouge
EXIT_COLOR = (0, 255, 0)        # Vert
WALL_COLOR = (100, 100, 100)    # Gris

# Récompenses
REWARD_CIVILIAN = +10
REWARD_EXIT = +50
REWARD_ZOMBIE = -100
REWARD_STEP = -0.1
REWARD_FUEL_EMPTY = -50

# Carburant initial
FUEL_MAX = 50