import pygame

# Versió del joc
GAME_VERSION = "v2.2.4"

# Dimensions de la pantalla (per defecte)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Configuració del joc
FPS = 60
PLAYER_ACCELERATION = 0.15
PLAYER_MAX_SPEED = 4
PLAYER_ROTATION_SPEED = 5
PLAYER_FRICTION = 0.98

# Configuració dels projectils
PROJECTILE_SPEED = 12

# Configuració dels asteroides
ASTEROID_SPEEDS = {
    'large': 1,
    'medium': 2,
    'small': 3
}

ASTEROID_SCORES = {
    'large': 20,
    'medium': 50,
    'small': 100
}

# Tecles de control
KEY_FULLSCREEN = pygame.K_F11
KEY_EXIT_FULLSCREEN = pygame.K_ESCAPE

# Afegir aquestes constants
WINDOW_MODE = 0  # Mode finestra
FULLSCREEN_MODE = pygame.FULLSCREEN
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
