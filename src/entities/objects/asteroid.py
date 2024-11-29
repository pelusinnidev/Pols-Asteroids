import pygame
from pygame.math import Vector2
import random
import math
from src.entities.base_entity import BaseEntity
from src.utils.constants import *

class Asteroid(BaseEntity):
    def __init__(self, position=None, size='large', speed_multiplier=1.0):
        # Si no es proporciona posició, genera una posició aleatòria als marges
        if position is None:
            position = self._generate_spawn_position()
        
        super().__init__(position)
        
        self.size = size
        self.radius = self._get_size_radius()
        self.points = []
        self.rotation_speed = random.uniform(-3, 3)
        
        # Velocitat basada en la mida i multiplicador de nivell
        base_speed = ASTEROID_SPEEDS[size]
        speed = base_speed * speed_multiplier
        angle = random.uniform(0, math.pi * 2)
        self.velocity = Vector2(math.cos(angle), math.sin(angle)) * speed
        
        # Genera la forma irregular de l'asteroide
        self._generate_shape()
    
    def _generate_spawn_position(self):
        # Genera una posició aleatòria fora de la pantalla
        side = random.choice(['top', 'right', 'bottom', 'left'])
        if side == 'top':
            return Vector2(random.randint(0, SCREEN_WIDTH), -50)
        elif side == 'right':
            return Vector2(SCREEN_WIDTH + 50, random.randint(0, SCREEN_HEIGHT))
        elif side == 'bottom':
            return Vector2(random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + 50)
        else:  # left
            return Vector2(-50, random.randint(0, SCREEN_HEIGHT))
    
    def _get_size_radius(self):
        return {
            'large': 40,
            'medium': 20,
            'small': 10
        }[self.size]
    
    def _generate_shape(self):
        # Genera una forma irregular amb variacions al radi
        num_points = random.randint(8, 12)
        for i in range(num_points):
            angle = (i / num_points) * math.pi * 2
            distance = self.radius * random.uniform(0.8, 1.2)
            point = Vector2(math.cos(angle), math.sin(angle)) * distance
            self.points.append(point)
    
    def update(self):
        super().update()
        self.angle += self.rotation_speed
    
    def draw(self, screen):
        # Dibuixa l'asteroide rotant els punts
        transformed_points = []
        for point in self.points:
            rotated = point.rotate(self.angle)
            transformed = rotated + self.position
            transformed_points.append(transformed)
        
        pygame.draw.polygon(screen, WHITE, transformed_points, 2)
    
    def split(self):
        # Retorna nous asteroides més petits quan es destrueix
        if self.size == 'large':
            return [Asteroid(self.position, 'medium') for _ in range(2)]
        elif self.size == 'medium':
            return [Asteroid(self.position, 'small') for _ in range(2)]
        return []
    
    def get_radius(self):
        return self.radius
    
    def get_score(self):
        return ASTEROID_SCORES[self.size]
