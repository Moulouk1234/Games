# labyrinth_game.py

import pygame
import sys
import time
from config import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Labyrinth Quest – Trouvez la sortie !")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    # État initial
    player_pos = list(START_POS)
    start_time = time.time()
    game_won = False
    game_lost = False

    running = True
    while running:
        current_time = time.time()
        elapsed = current_time - start_time
        time_left = max(0, TIME_LIMIT - int(elapsed))

        if time_left == 0 and not game_won:
            game_lost = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not (game_won or game_lost) and event.type == pygame.KEYDOWN:
                dx, dy = 0, 0
                if event.key == pygame.K_UP:
                    dx = -1
                elif event.key == pygame.K_DOWN:
                    dx = 1
                elif event.key == pygame.K_LEFT:
                    dy = -1
                elif event.key == pygame.K_RIGHT:
                    dy = 1

                # Nouvelle position
                new_x = player_pos[0] + dx
                new_y = player_pos[1] + dy

                # Vérifier les bords et les murs
                if (0 <= new_x < GRID_SIZE and 
                    0 <= new_y < GRID_SIZE and 
                    MAZE[new_x][new_y] == 0):
                    player_pos = [new_x, new_y]

                    # Vérifier victoire
                    if (new_x, new_y) == EXIT_POS:
                        game_won = True

        # --- Dessiner ---
        screen.fill(BACKGROUND)

        # Grille
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if MAZE[x][y] == 1:
                    pygame.draw.rect(screen, WALL_COLOR, rect)
                else:
                    pygame.draw.rect(screen, PATH_COLOR, rect)
                    pygame.draw.rect(screen, (60, 60, 80), rect, 1)

        # Sortie
        exit_rect = pygame.Rect(EXIT_POS[1] * CELL_SIZE, EXIT_POS[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, EXIT_COLOR, exit_rect)

        # Joueur
        player_rect = pygame.Rect(player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.circle(screen, PLAYER_COLOR, player_rect.center, CELL_SIZE // 2 - 5)

        # Texte
        if game_won:
            msg = f"🎉 GAGNÉ ! Temps restant : {time_left}s"
            color = (0, 255, 150)
        elif game_lost:
            msg = "💀 Temps écoulé ! Vous avez perdu."
            color = (255, 50, 50)
        else:
            msg = f"Temps restant : {time_left}s | Utilisez les flèches pour vous déplacer"
            color = TEXT_COLOR

        text_surf = font.render(msg, True, color)
        screen.blit(text_surf, (10, HEIGHT - 40))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()