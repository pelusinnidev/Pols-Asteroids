from src.utils.button import Button
from src.utils.constants import *
from src.core.managers.mongo_high_score_manager import MongoHighScoreManager

class MenuScene:
    def __init__(self, high_score_manager: MongoHighScoreManager):
        self.version_font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', 48)  # Increased size for better visibility
        self.highscore_font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', 28)  # Larger font for scores
        self.buttons = [
            Button("PLAY", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)),
            Button("CONTROLS", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)),  # Increased separation
            Button("HIGH SCORES", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 160)),  # Increased separation
            Button("QUIT", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 240))      # Increased separation
        ]
        self.show_controls = False
        self.show_highscores = False
        self.high_score_manager = high_score_manager
        self.highscores = self.high_score_manager.get_high_scores()
        self.selected_button = 0  # Track which button is selected
        # Set initial button as selected
        self.buttons[0].selected = True

        # Carregar i escalar la imatge del logo
        try:
            original = pygame.image.load('src/assets/images/placeholder.jpg')
            self.logo = pygame.transform.scale(original, (600, 300))
            print("Logo carregat correctament al menú.")
        except pygame.error as e:
            print(f"Error carregant el logo: {e}")
            self.logo = None

    def handle_input(self, event):
        if self.show_controls:
            if event.type == pygame.KEYDOWN:
                self.show_controls = False
                print("Tornada al menú principal des de CONTROLS.")
            return None
        if self.show_highscores:
            if event.type == pygame.KEYDOWN:
                self.show_highscores = False
                print("Tornada al menú principal des de HIGH SCORES.")
            return None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Move selection up
                self.buttons[self.selected_button].selected = False
                self.selected_button = (self.selected_button - 1) % len(self.buttons)
                self.buttons[self.selected_button].selected = True
                print(f"Seleccionat botó: {self.buttons[self.selected_button].text}")
                
            elif event.key == pygame.K_DOWN:
                # Move selection down
                self.buttons[self.selected_button].selected = False
                self.selected_button = (self.selected_button + 1) % len(self.buttons)
                self.buttons[self.selected_button].selected = True
                print(f"Seleccionat botó: {self.buttons[self.selected_button].text}")

        # Handle button events
        for button in self.buttons:
            if button.handle_event(event):
                if button.text == "PLAY":
                    print("Botó PLAY seleccionat.")
                    return "PLAY"
                elif button.text == "CONTROLS":
                    self.show_controls = True
                    print("Mostrant CONTROLS.")
                elif button.text == "HIGH SCORES":
                    self.show_highscores = True
                    self.highscores = self.high_score_manager.get_high_scores()
                    print("Mostrant HIGH SCORES.")
                elif button.text == "QUIT":
                    print("Botó QUIT seleccionat.")
                    return "QUIT"
        return None

    def draw(self, screen):
        screen.fill(BLACK)

        if not self.show_controls and not self.show_highscores:
            # Dibuixar el logo més amunt només quan no estem mostrant una secció
            if self.logo:
                logo_rect = self.logo.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
                screen.blit(self.logo, logo_rect)

            # Dibuixa la versió
            version = self.version_font.render(GAME_VERSION, True, WHITE)
            version_rect = version.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10))
            screen.blit(version, version_rect)

        if self.show_controls:
            self._draw_controls(screen)
        elif self.show_highscores:
            self._draw_highscores(screen)
        else:
            for button in self.buttons:
                button.draw(screen)

    def _draw_controls(self, screen):
        controls = [
            "CONTROLS:",
            "",
            "Fleches / WASD - Mou la nau",
            "UP/W - Endavant",
            "DOWN/S - Endarrere",
            "LEFT/A, RIGHT/D - Rotar",
            "SPACE - Disparar",
            "ESC - Pausar",
            "",
            "Prem qualsevol tecla per tornar"
        ]

        font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', 24)  # Consistent retro font
        y = SCREEN_HEIGHT // 3

        for line in controls:
            text = font.render(line, True, WHITE)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
            screen.blit(text, rect)
            y += 40
        print("Mostrant la secció CONTROLS.")

    def _draw_highscores(self, screen):
        # Assegurar-se que les puntuacions estan actualitzades
        self.highscores = self.high_score_manager.get_high_scores()

        # Disseny retro
        screen.fill(BLACK)

        # Títol retro
        title = self.title_font.render("HIGH SCORES", True, GREEN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))
        screen.blit(title, title_rect)

        # Mostrar mensaje de estado
        status_message = self.high_score_manager.get_status_message()
        if status_message:
            status_font = pygame.font.Font(None, 24)
            status_text = status_font.render(status_message, True, YELLOW)
            status_rect = status_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            screen.blit(status_text, status_rect)

        # Separador
        pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3), 
                        (3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3), 2)

        # Mostrar les puntuacions amb millor espaiat
        y_start = SCREEN_HEIGHT // 2.5
        spacing = 50  # Incrementat per millorar la llegibilitat
        for idx in range(self.high_score_manager.max_scores):
            if idx < len(self.highscores):
                entry = self.highscores[idx]
                score_text = f"{idx + 1}. {entry['name']} - {entry['score']}"
            else:
                score_text = f"{idx + 1}. ---- - 0"

            text = self.highscore_font.render(score_text, True, WHITE)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_start + idx * spacing))
            screen.blit(text, rect)

        # Instruccions per sortir
        exit_text = self.highscore_font.render("Prem qualsevol tecla per tornar", True, WHITE)
        exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT // 12))
        screen.blit(exit_text, exit_rect)

        print("Mostrant la secció HIGH SCORES.")
