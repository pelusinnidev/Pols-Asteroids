import pygame
import os
from src.utils.constants import *
from src.utils.transitions import Transition

def create_placeholder_image():
    # Create directories if they don't exist
    os.makedirs("src/assets/images", exist_ok=True)
    
    # Create a placeholder surface
    placeholder = pygame.Surface((400, 200))
    placeholder.fill((50, 50, 50))  # Dark gray background
    
    # Add text to the placeholder
    font = pygame.font.Font(None, 36)
    text = font.render("Placeholder Image", True, (255, 255, 255))
    text_rect = text.get_rect(center=(200, 100))
    placeholder.blit(text, text_rect)
    
    # Save the placeholder image
    try:
        pygame.image.save(placeholder, "src/assets/images/placeholder.jpg")
        print("Successfully created placeholder image")
    except Exception as e:
        print(f"Error creating placeholder image: {e}")

class IntroScene:
    def __init__(self):
        self.slides = [
            {
                'image': 'developer_logo.jpg',
                'duration': 0.5,
                'text': 'A Game By PelusinniDev',
                'text_offset': 150,
                'size': (400, 200)
            },
            {
                'image': 'lasalle_logo.jpg',
                'duration': 0.5,
                'text': 'La Salle Gràcia',
                'text_offset': 150,
                'size': (400, 200)
            }
        ]
        self.current_slide = 0
        self.fade_in = Transition(0.25)
        self.fade_out = Transition(0.25)
        self.slide_timer = 0
        self.state = 'FADE_IN'
        
        # Carregar fonts i imatges
        try:
            self.font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', 36)
        except:
            print("No s'ha pogut carregar la font. Utilitzant font per defecte.")
            self.font = pygame.font.Font(None, 36)
        
        self.images = {}
        
        # Carregar les imatges reals
        for slide in self.slides:
            image_path = f"src/assets/images/{slide['image']}"
            try:
                original = pygame.image.load(image_path).convert_alpha()
                self.images[slide['image']] = pygame.transform.scale(original, slide['size'])
            except pygame.error as e:
                print(f"Error carregant la imatge {image_path}: {e}")
                # Crear una imatge temporal en lloc de sortir
                temp_surface = pygame.Surface(slide['size'])
                temp_surface.fill((50, 50, 50))
                font = pygame.font.Font(None, 36)
                text = font.render(slide['text'], True, (255, 255, 255))
                text_rect = text.get_rect(center=(slide['size'][0]/2, slide['size'][1]/2))
                temp_surface.blit(text, text_rect)
                self.images[slide['image']] = temp_surface

    def update(self):
        current_time = pygame.time.get_ticks()
        
        if self.state == 'FADE_IN':
            if not self.fade_in.is_active:
                self.fade_in.start()
            elif self.fade_in.is_finished():
                self.state = 'DISPLAY'
                self.slide_timer = pygame.time.get_ticks()
                
        elif self.state == 'DISPLAY':
            if current_time - self.slide_timer >= self.slides[self.current_slide]['duration'] * 1000:
                self.state = 'FADE_OUT'
                self.fade_out.start()
                
        elif self.state == 'FADE_OUT':
            if self.fade_out.is_finished():
                self.current_slide += 1
                if self.current_slide >= len(self.slides):
                    return "MENU"
                self.state = 'FADE_IN'
                self.fade_in = Transition(0.25)
                self.fade_out = Transition(0.25)
        
        return None
    
    def draw(self, screen):
        screen.fill(BLACK)
        
        if self.current_slide >= len(self.slides):
            return
            
        current_image = self.images[self.slides[self.current_slide]['image']]
        current_text = self.slides[self.current_slide]['text']
        text_offset = self.slides[self.current_slide]['text_offset']
        
        # Calculate image position (centered)
        image_rect = current_image.get_rect()
        image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        # Calculate text position (below image)
        text_surface = self.font.render(current_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + text_offset))
        
        # Draw with appropriate fade
        alpha = 255
        if self.state == 'FADE_IN':
            alpha = self.fade_in.get_alpha()
        elif self.state == 'FADE_OUT':
            alpha = 255 - self.fade_out.get_alpha()
        
        # Draw image with fade
        temp_surface = current_image.copy()
        temp_surface.set_alpha(alpha)
        screen.blit(temp_surface, image_rect)
        
        # Draw text with fade
        text_surface.set_alpha(alpha)
        screen.blit(text_surface, text_rect)
