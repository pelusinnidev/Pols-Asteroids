import pygame
from pygame.math import Vector2
import math
from src.entities.base_entity import BaseEntity
from src.utils.constants import *

class Spaceship(BaseEntity):
    def __init__(self, position):
        super().__init__(position)
        self.shape = [
            Vector2(0, -20),    # Punta
            Vector2(-10, 20),   # Cantonada esquerra
            Vector2(0, 10),     # Centre base
            Vector2(10, 20)     # Cantonada dreta
        ]
        self.thrust = False
        self.radius = 20
    
    def rotate(self, angle):
        self.angle += angle
    
    def accelerate(self, forward=True):
        self.thrust = True
        direction = -1 if forward else 1  # -1 per endavant, 1 per enrere
        thrust_vector = Vector2(0, direction * PLAYER_ACCELERATION).rotate(-self.angle)
        self.velocity += thrust_vector
        
        # Limitar velocitat màxima
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity.scale_to_length(PLAYER_MAX_SPEED)
    
    def update(self):
        super().update()
        self.thrust = False
        self.velocity *= PLAYER_FRICTION
    
    def draw(self, screen):
        # Dibuixar la nau
        points = [p.rotate(-self.angle) + self.position for p in self.shape]
        pygame.draw.polygon(screen, WHITE, points, 2)
        
        # Dibuixar propulsió si s'està accelerant
        if self.thrust:
            flame_points = [
                Vector2(0, 15).rotate(-self.angle) + self.position,
                Vector2(-5, 25).rotate(-self.angle) + self.position,
                Vector2(5, 25).rotate(-self.angle) + self.position
            ]
            pygame.draw.polygon(screen, RED, flame_points)
    
    def get_radius(self):
        return self.radius
    
    def can_shoot(self):
        return True
    
    def shoot(self):
        return True
