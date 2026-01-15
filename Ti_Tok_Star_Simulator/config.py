# config.py

import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FPS = 30

# Couleurs modernes (inspirées de TikTok)
BACKGROUND = (25, 25, 25)     # Noir profond
TEXT_COLOR = (255, 255, 255)   # Blanc
ACCENT = (18, 187, 149)        # Vert TikTok
BUTTON_HOVER = (30, 30, 30)    # Gris foncé
BUTTON_ACTIVE = ACCENT         # Vert actif

FONT_SIZE = 24
TITLE_FONT_SIZE = 36

ACTIONS = {
    0: "Publier vidéo",
    1: "Liker",
    2: "Commenter",
    3: "Partager",
    4: "Se reposer"
}

REWARDS = {
    0: 5,
    1: 1,
    2: 2,
    3: 3,
    4: 0.5
}