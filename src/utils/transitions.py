import pygame

class Transition:
    def __init__(self, duration=1.0):
        self.duration = duration * 1000  # Convert to milliseconds
        self.start_time = None
        self.is_active = False
        
    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.is_active = True
        print("Transició iniciada.")
        
    def get_alpha(self):
        if not self.is_active:
            return 0
        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.start_time
        progress = min(1.0, elapsed / self.duration)
        alpha = int(255 * progress)
        return alpha
        
    def is_finished(self):
        if not self.is_active:
            return False
        return pygame.time.get_ticks() - self.start_time >= self.duration
