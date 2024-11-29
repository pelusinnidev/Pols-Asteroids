import pygame
from src.utils.button import Button
from src.utils.constants import *

class PauseScene:
    def __init__(self):
        self.buttons = [
            Button("RESUME", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)),
            Button("MENU", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
        ]
        self.title_font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', 48)  # Retro font
        self.selected_button = 0  # Track which button is selected
        self.buttons[self.selected_button].selected = True  # Set initial button as selected

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Move selection up
                self.buttons[self.selected_button].selected = False
                self.selected_button = (self.selected_button - 1) % len(self.buttons)
                self.buttons[self.selected_button].selected = True
            elif event.key == pygame.K_DOWN:
                # Move selection down
                self.buttons[self.selected_button].selected = False
                self.selected_button = (self.selected_button + 1) % len(self.buttons)
                self.buttons[self.selected_button].selected = True
            elif event.key == pygame.K_RETURN:
                # Activate the selected button
                return self.buttons[self.selected_button].text

        return None
        
    def draw(self, screen):
        # Enfosqueix la pantalla amb un overlay semi-transparent
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(150)  # Augmentat per una millor visibilitat
        screen.blit(overlay, (0, 0))
        
        # Dibuixa el títol de pausa amb estil retro
        title = self.title_font.render("PAUSED", True, GREEN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        screen.blit(title, title_rect)
        
        # Dibuixa els botons
        for button in self.buttons:
            button.draw(screen)
