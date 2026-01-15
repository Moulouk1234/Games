# config.py

import pygame

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)      # Snake body
RED = (255, 50, 50)      # Food
WHITE = (255, 255, 255)  # Text

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)