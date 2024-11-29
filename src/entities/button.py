import pygame

class Button:
    def __init__(self, text, position, font=None, font_size=36, text_color=(255, 255, 255), button_color=(0, 0, 0), selected=False):
        self.text = text
        self.position = position
        self.font = pygame.font.Font(font, font_size) if font else pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.button_color = button_color
        self.selected = selected

        self.rendered_text = self.font.render(self.text, True, self.text_color)
        self.rect = self.rendered_text.get_rect(center=self.position)

    def draw(self, screen):
        if self.selected:
            # Dibuja un rectángulo alrededor del botón para indicar que está seleccionado
            pygame.draw.rect(screen, self.text_color, self.rect.inflate(20, 20), 2)
        screen.blit(self.rendered_text, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos) 