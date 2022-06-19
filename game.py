import pygame
import game_module as gm
import os
from level import *

class Game():
    def __init__(self, player, game_deck, list_of_enemies) -> None:
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.running = True
        self.screen = pygame.display.set_mode(gm.SCREEN_SIZE)
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.level = Level(self.screen, player, game_deck, list_of_enemies)

    def game_loop(self):
        pygame.event.clear()
        while self.running:
            self.level.draw()
            self.level.handle_events()
            # if self.level.is_player_turn:
            #     self.level.player_turn()
            # self.level.switch_turns()
            # if not self.level.is_player_turn:
            #     self.level.enemies_turn()
            # self.level.switch_turns()
            self.level.update_enemies_status()
            # self.level.draw_cards()
            pygame.display.flip()
            self.clock.tick(30)
