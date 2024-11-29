import sys
import os

# Añadir el directorio src al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.scenes.menu_scene import MenuScene
from src.scenes.game_scene import GameScene
from src.scenes.pause_scene import PauseScene
from src.scenes.intro_scene import IntroScene
from src.utils.constants import *
from src.core.managers.mongo_high_score_manager import MongoHighScoreManager
import pygame

# Inicialitzar Pygame
pygame.init()
pygame.mixer.init()  # Asegúrate de que el mixer está inicializado

# Funció per carregar música amb gestió d'errors
def load_music(path):
    try:
        pygame.mixer.music.load(path)
        print(f"Música carregada: {path}")
    except pygame.error as e:
        print(f"Error carregant música {path}: {e}")

# Crear instància de HighScoreManager
high_score_manager = MongoHighScoreManager()

class Game:
    def __init__(self):
        # Inicialitzar en mode finestra
        self.screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))
        pygame.display.set_caption("Asteroids")
        self.clock = pygame.time.Clock()
        
        # Guardar l'estat de la pantalla
        self.is_fullscreen = False
        
        self.menu_scene = MenuScene(high_score_manager)
        self.game_scene = None
        self.pause_scene = PauseScene()
        self.intro_scene = IntroScene()
        self.current_scene = "INTRO"
        
        # Flags per càrrega de música
        self.menu_music_loaded = False
        self.game_music_loaded = False
    
    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            # Obtenir la resolució real de la pantalla
            info = pygame.display.Info()
            self.screen = pygame.display.set_mode((info.current_w, info.current_h), FULLSCREEN_MODE)
            print("Mode Fullscreen activat.")
        else:
            self.screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), WINDOW_MODE)
            print("Mode finestra activat.")
    
    def run(self):
        try:
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        # Only allow pausing when in the GAME scene
                        if event.key == pygame.K_ESCAPE and self.current_scene == "GAME":
                            pause_music()  # Pause music when entering pause
                            self.current_scene = "PAUSE"

                if self.current_scene == "INTRO":
                    self._handle_intro(events)
                elif self.current_scene == "MENU":
                    self._handle_menu(events)
                elif self.current_scene == "GAME":
                    self._handle_game(events)
                elif self.current_scene == "PAUSE":
                    self._handle_pause(events)
                elif self.current_scene == "NEW_HIGHSCORE":
                    self._handle_new_highscore(events)

                pygame.display.flip()
                self.clock.tick(FPS)
        except KeyboardInterrupt:
            print("Game interrupted by user.")
            pygame.quit()
            sys.exit()
    
    def _handle_intro(self, events):
        if not self.game_music_loaded:
            load_music('src/assets/music/game_music.mp3')
            pygame.mixer.music.play(-1)
            self.game_music_loaded = True
            print("Música inicial carregada.")
            
        result = self.intro_scene.update()
        if result == "MENU":
            self.current_scene = "MENU"
            self.game_music_loaded = False
        
        self.intro_scene.draw(self.screen)
    
    def _handle_menu(self, events):
        if not self.menu_music_loaded:
            pygame.mixer.music.stop()  # Detener música anterior
            load_music('src/assets/music/menu_music.mp3')
            pygame.mixer.music.play(-1)  # Reproducir en bucle
            self.menu_music_loaded = True
            self.game_music_loaded = False  # Resetear flag de música del juego
            print("Música del menú activada.")
        
        for event in events:
            result = self.menu_scene.handle_input(event)
            if result == "PLAY":
                pygame.mixer.music.stop()  # Detener música del menú
                self.game_scene = GameScene(high_score_manager)
                self.current_scene = "GAME"
                self.menu_music_loaded = False
            elif result == "QUIT":
                pygame.quit()
                sys.exit()
        
        self.menu_scene.draw(self.screen)
    
    def _handle_game(self, events):
        update_result = self.game_scene.update()
        if update_result == "MENU":
            pygame.mixer.music.stop()  # Detener música actual
            self.current_scene = "MENU"
            self.menu_music_loaded = False
            self.game_music_loaded = False
            self.game_scene = None  # Reiniciar la instància de GameScene
            return
        elif update_result == "NEW_HIGHSCORE":
            self.current_scene = "NEW_HIGHSCORE"
            return

        if not self.game_music_loaded:
            pygame.mixer.music.stop()  # Detener música anterior
            load_music('src/assets/music/game_music.mp3')
            pygame.mixer.music.play(-1)  # Reproducir en bucle
            self.game_music_loaded = True
            self.menu_music_loaded = False
            print("Música del joc activada.")
        
        # Pass all events to GameScene.handle_input
        for event in events:
            result = self.game_scene.handle_input(event)
            if result == "QUIT":
                pygame.quit()
                sys.exit()
            elif result == "MENU":
                self.current_scene = "MENU"
            elif result == "NEW_HIGHSCORE":
                self.current_scene = "NEW_HIGHSCORE"
            elif result == "TOGGLE_FULLSCREEN":
                self.toggle_fullscreen()

        self.game_scene.draw(self.screen)
    
    def _handle_pause(self, events):
        for event in events:
            result = self.pause_scene.handle_input(event)
            if result == "RESUME":
                unpause_music()  # Reanudar la música al salir de la pausa
                self.current_scene = "GAME"
            elif result == "MENU":
                pygame.mixer.music.stop()  # Opcionalmente detener la música si se va al menú
                self.current_scene = "MENU"
        self.pause_scene.draw(self.screen)
    
    def _handle_new_highscore(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.game_scene:  # Verificar si existeix game_scene
                    if event.key == pygame.K_RETURN:
                        name = self.game_scene.player_name.strip() or "AAA"
                        high_score_manager.add_high_score(name, self.game_scene.score)
                        print(f"Nou punç alt guardat: {name} - {self.game_scene.score}")
                        self.current_scene = "MENU"
                        self.game_scene = None
                    elif event.key == pygame.K_BACKSPACE:
                        self.game_scene.player_name = self.game_scene.player_name[:-1]
                        print(f"Eliminant l'última lletra del nom: {self.game_scene.player_name}")
                    else:
                        if len(self.game_scene.player_name) < 3 and event.unicode.isalpha():
                            self.game_scene.player_name += event.unicode.upper()
                            print(f"Llitura de nom actual: {self.game_scene.player_name}")
        
        if self.game_scene:  # Només dibuixa si existeix game_scene
            self.game_scene.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()