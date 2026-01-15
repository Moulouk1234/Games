# config.py

import pygame

# Taille
GRID_SIZE = 10          # 10x10 cases
CELL_SIZE = 50
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE + 60  # espace pour texte

# Couleurs
BACKGROUND = (25, 25, 40)
WALL_COLOR = (80, 80, 100)
PATH_COLOR = (40, 40, 60)
PLAYER_COLOR = (0, 200, 255)   # Cyan
EXIT_COLOR = (0, 255, 100)     # Vert
TEXT_COLOR = (240, 240, 240)

# Labyrinthe fixe (0 = chemin, 1 = mur)
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

START_POS = (1, 1)
EXIT_POS = (8, 8)
TIME_LIMIT = 60  # secondes