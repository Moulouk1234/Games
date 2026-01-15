# game_renderer.py

import pygame
from config import *

def render_game(env):
    if not hasattr(env, 'screen'):
        pygame.init()
        env.screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
        pygame.display.set_caption("Rescue Ops – Évacuation Urbaine")
        env.clock = pygame.time.Clock()

    screen = env.screen
    screen.fill(BACKGROUND)

    # Dessiner grille
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (50, 50, 70), rect, 1)

    # Dessiner sortie
    exit_rect = pygame.Rect(env.exit_pos[1] * CELL_SIZE, env.exit_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, EXIT_COLOR, exit_rect)

    # Dessiner civils
    for c in env.civilians:
        civ_rect = pygame.Rect(c[1] * CELL_SIZE, c[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.circle(screen, CIVILIAN_COLOR, civ_rect.center, CELL_SIZE // 3)

    # Dessiner zombies
    for z in env.zombies:
        zomb_rect = pygame.Rect(z[1] * CELL_SIZE, z[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, ZOMBIE_COLOR, zomb_rect)

    # Dessiner agent
    agent_rect = pygame.Rect(env.agent_pos[1] * CELL_SIZE, env.agent_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.circle(screen, AGENT_COLOR, agent_rect.center, CELL_SIZE // 2)

    # Infos
    font = pygame.font.SysFont(None, 24)
    info = f"Carburant: {env.fuel} | Civils: {len(env.civilians)}"
    text = font.render(info, True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    env.clock.tick(4)