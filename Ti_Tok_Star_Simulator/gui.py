# gui.py

import pygame
import sys
from config import *

class TikTokGUI:
    def __init__(self, env):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("TikTok Star Simulator")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", FONT_SIZE)
        self.title_font = pygame.font.SysFont("Arial", TITLE_FONT_SIZE, bold=True)
        self.env = env
        self.running = True
        self.mode = "menu"  # menu, human, ai
        self.selected_action = 0
        self.history = []
        
        # Boutons
        self.buttons = []
        for i in range(5):
            x = 50 + (i * 180)
            y = 400
            w = 160
            h = 60
            self.buttons.append(pygame.Rect(x, y, w, h))
    
    def draw_menu(self):
        self.screen.fill(BACKGROUND)
        
        title = self.title_font.render("TikTok Star Simulator", True, ACCENT)
        self.screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 50))
        
        instructions = self.font.render("Choisissez votre mode :", True, TEXT_COLOR)
        self.screen.blit(instructions, (WINDOW_WIDTH//2 - instructions.get_width()//2, 150))
        
        options = ["Jouer toi-même", "Regarder l'IA jouer", "Quitter"]
        for i, opt in enumerate(options):
            color = ACCENT if i == self.selected_action else TEXT_COLOR
            text = self.font.render(opt, True, color)
            self.screen.blit(text, (WINDOW_WIDTH//2 - text.get_width()//2, 220 + i*60))
        
        pygame.display.flip()
    
    def draw_game(self):
        self.screen.fill(BACKGROUND)
        
        # Titre
        title = self.title_font.render(f"Jour {self.env.day}", True, ACCENT)
        self.screen.blit(title, (50, 30))
        
        # Stats
        stats = [
            f"Followers: {int(self.env.followers)}",
            f"Engagement: {self.env.engagement:.2f}",
            f"Action: {ACTIONS[self.selected_action]}"
        ]
        for i, stat in enumerate(stats):
            text = self.font.render(stat, True, TEXT_COLOR)
            self.screen.blit(text, (50, 100 + i*40))
        
        # Boutons d'action
        for i, rect in enumerate(self.buttons):
            color = BUTTON_HOVER if i == self.selected_action else BUTTON_ACTIVE
            pygame.draw.rect(self.screen, color, rect, border_radius=10)
            text = self.font.render(ACTIONS[i], True, TEXT_COLOR)
            self.screen.blit(text, (rect.x + rect.width//2 - text.get_width()//2, 
                                   rect.y + rect.height//2 - text.get_height()//2))
        
        # Instructions
        instr = self.font.render("↑↓ pour choisir | Enter pour confirmer", True, TEXT_COLOR)
        self.screen.blit(instr, (50, 500))
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                
                if self.mode == "menu":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.selected_action = max(0, self.selected_action - 1)
                        elif event.key == pygame.K_DOWN:
                            self.selected_action = min(2, self.selected_action + 1)
                        elif event.key == pygame.K_RETURN:
                            if self.selected_action == 0:
                                self.mode = "human"
                                self.env.reset()
                            elif self.selected_action == 1:
                                self.mode = "ai"
                                self.run_ai()
                            elif self.selected_action == 2:
                                self.running = False
                
                elif self.mode == "human":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.selected_action = max(0, self.selected_action - 1)
                        elif event.key == pygame.K_DOWN:
                            self.selected_action = min(4, self.selected_action + 1)
                        elif event.key == pygame.K_RETURN:
                            obs, reward, done, _ = self.env.step(self.selected_action)
                            self.history.append(reward)
                            if done:
                                self.mode = "menu"
                                print(f"🎉 Fin ! Score final : {sum(self.history):.1f}")
                                self.history = []
                            else:
                                pygame.time.wait(500)
            
            if self.mode == "menu":
                self.draw_menu()
            elif self.mode == "human":
                self.draw_game()
            elif self.mode == "ai":
                self.draw_game()
            
            self.clock.tick(FPS)
    
    def run_ai(self):
        from agent import create_agent, train_agent, get_action
        model = create_agent(self.env)
        model = train_agent(model, 1000)
        
        obs = self.env.reset()
        done = False
        while not done and self.running:
            action = get_action(model, obs)
            obs, reward, done, _ = self.env.step(action)
            self.selected_action = action
            self.draw_game()
            pygame.display.flip()
            pygame.time.wait(500)