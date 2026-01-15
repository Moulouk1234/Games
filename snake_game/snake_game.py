# snake_game.py

import pygame
import random
from config import *

def run_snake():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game – Joué par El Feki H. Moulouk")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    # Initial state
    snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
    direction = RIGHT
    food = spawn_food(snake)
    score = 0
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        return run_snake()  # Restart
                    elif event.key == pygame.K_q:
                        return
                else:
                    if event.key == pygame.K_UP and direction != DOWN:
                        direction = UP
                    elif event.key == pygame.K_DOWN and direction != UP:
                        direction = DOWN
                    elif event.key == pygame.K_LEFT and direction != RIGHT:
                        direction = LEFT
                    elif event.key == pygame.K_RIGHT and direction != LEFT:
                        direction = RIGHT

        if not game_over:
            # Move snake
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = ((head_x + dx) % GRID_SIZE, (head_y + dy) % GRID_SIZE)

            # Wall collision (optional: remove `% GRID_SIZE` above to enable hard walls)
            if (new_head[0] < 0 or new_head[0] >= GRID_SIZE or
                new_head[1] < 0 or new_head[1] >= GRID_SIZE or
                new_head in snake):
                game_over = True
            else:
                snake.insert(0, new_head)

                # Check food
                if new_head == food:
                    score += 10
                    food = spawn_food(snake)
                else:
                    snake.pop()  # Remove tail

        # Draw
        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_food(screen, food)
        
        # Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render("GAME OVER! Press R to restart, Q to quit", True, RED)
            screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2))

        pygame.display.flip()
        clock.tick(8 + score // 20)  # Speed increases with score

    pygame.quit()

def spawn_food(snake):
    while True:
        pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if pos not in snake:
            return pos

def draw_snake(screen, snake):
    for i, (x, y) in enumerate(snake):
        color = GREEN if i == 0 else (0, 200, 0)  # Head brighter
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

def draw_food(screen, food):
    x, y = food
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, rect)
    pygame.draw.rect(screen, WHITE, rect, 1)