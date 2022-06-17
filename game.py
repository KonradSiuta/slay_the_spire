import pygame
import game_module as gm
import os
from level import *

class Game():
    def __init__(self, player, level_deck, list_of_enemies) -> None:
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.running = True
        self.screen = pygame.display.set_mode(gm.SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.level = Level(self.screen, player, level_deck, list_of_enemies)

    def game_loop(self):
        while self.running:
            self.level.draw_level()
            self.level.handle_events()
            pygame.display.flip()
            self.clock.tick(30)
