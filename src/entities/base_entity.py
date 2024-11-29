import pygame
from pygame.math import Vector2
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class BaseEntity:
    def __init__(self, position, velocity=Vector2(0, 0)):
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.angle = 0
        self.active = True
    
    def update(self):
        self.position += self.velocity
        
        # Wrap around screen edges
        self.position.x = self.position.x % SCREEN_WIDTH
        self.position.y = self.position.y % SCREEN_HEIGHT
    
    def draw(self, screen):
        pass  # Serà implementat per les classes filles
    
    def get_radius(self):
        return 1  # Serà sobreescrit per les classes filles
    
    def collides_with(self, other):
        distance = (self.position - other.position).length()
        return distance < (self.get_radius() + other.get_radius())
