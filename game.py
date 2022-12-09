import pygame
import game_module as gm
import os
from level import *
from scene import *

class Game():
    def __init__(self, player, game_deck1, game_deck2, list_of_enemies1, list_of_enemies2) -> None:
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.running = True
        self.screen = pygame.display.set_mode(gm.SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        # self.level = Level(self.screen, player, game_deck, list_of_enemies)
        self.scenes = {"MAINMENU": MainMenu("MAINMENU",self.screen, gm.BG_MENU_IMAGE), "PAUSEMENU": PauseMenu("PAUSEMENU", self.screen, gm.BG_PAUSE_IMAGE), "LOSESCREEN": LoseScene("LOSESCREEN", self.screen, gm.BG_PAUSE_IMAGE), "VICTORYSCREEN": WinScene("VICTORYSCREEN", self.screen, gm.BG_PAUSE_IMAGE), "LEVEL1": Level("LEVEL1", self.screen, gm.BG_LEVEL_IMAGE, player, game_deck1, list_of_enemies1), "LEVEL": Level("LEVEL", self.screen, gm.BG_LEVEL_IMAGE, player, game_deck2, list_of_enemies2)}
        self.current_scene = self.scenes["MAINMENU"]
    
        pygame.mixer.init()
        pygame.mixer.music.load(gm.BG_MUSIC)
        pygame.mixer.music.play(-1, fade_ms = 1000)
        pygame.mixer.music.set_volume(0.15)
            
    def game_loop(self):
        pygame.event.clear()
        while self.running:
            self.current_scene.draw()
            self.current_scene.handle_events()

            if self.current_scene.next_scene is not None and self.current_scene.next_scene in self.scenes:
                scene = self.current_scene.next_scene
                self.current_scene.next_scene = None
                self.current_scene = self.scenes[scene]
                
            pygame.display.flip()
            self.clock.tick(5)
