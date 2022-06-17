import sys
import pygame, os
import game_module as gm
from card import *
from deck import *
from character import *
import copy


class Level():
    def __init__(self, screen, player, level_deck, list_of_enemies) -> None:
        self.display = True

        self.screen = screen

        self.player = player

        self.list_of_enemies = []

        self.level_deck = level_deck

        self.list_of_enemies = list_of_enemies
        
        self.status_bar = pygame.Surface.subsurface(self.screen, (0, 0, gm.SB_WIDTH, gm.SB_HEIGHT))
        self.chosen_card = pygame.Surface.subsurface(self.screen, (0, gm.SB_HEIGHT, gm.C_WIDTH, gm.C_HEIGHT))
        self.deck_surface = pygame.Surface.subsurface(self.screen, (gm.C_WIDTH, gm.SB_HEIGHT, gm.SB_WIDTH - gm.C_WIDTH, gm.SC_HEIGHT))
        self.chosen_card_rect = self.chosen_card.get_rect()
        self.player_surface = pygame.Surface.subsurface(self.screen, 0, gm.SB_HEIGHT + gm.C_HEIGHT, gm.S_WIDTH / 3, gm.S_HEIGHT / 2)
        self.player_surface_rect = self.player_surface.get_rect()
        self.enemies_surface = pygame.Surface.subsurface(self.screen, (self.player_surface_rect.right, gm.SB_HEIGHT + gm.C_HEIGHT, gm.S_WIDTH - self.player_surface_rect.right, gm.S_HEIGHT / 2))
        self.enemies_surface_rect = self.enemies_surface.get_rect()
        self.platform_surface = pygame.Surface.subsurface(self.screen, (0, gm.SB_HEIGHT + gm.C_HEIGHT + self.enemies_surface_rect.bottom, gm.S_WIDTH, gm.S_HEIGHT - (gm.SB_HEIGHT + gm.C_HEIGHT + self.enemies_surface_rect.bottom)))

    def switch_display(self):
        if self.display:
            self.display = False
        else:
            self.display = True

    def draw_level(self):
        self.screen.blit(gm.BG_IMAGE, (0, 0))
        self.platform_surface.fill(gm.BLACK)
        
        self.level_deck.print_highlited_card(self.chosen_card)
    
        self.level_deck.print_level_deck(self.deck_surface)

        self.player.draw(self.player_surface, self.player_surface_rect.midbottom)
        self.player.draw_health_bar(self.player_surface, self.player_surface_rect)

        self.status_bar.fill(gm.LIGHTBLUE)
        self.status_bar.blit(gm.HEALTH_ICON, (15, gm.SB_HEIGHT / 2 - 20))
        self.player.print_health_status(self.status_bar, (60, gm.SB_HEIGHT / 2 - 17))
        self.status_bar.blit(gm.ENERGY_ICON, (150, gm.SB_HEIGHT / 2 - 20))
        self.player.print_energy_status(self.status_bar, (190, gm.SB_HEIGHT / 2 - 17))

        self.draw_enemies()

    def draw_enemies(self):
        for i in range(len(self.list_of_enemies)):
            if i < len(self.list_of_enemies) / 2:
                self.list_of_enemies[i].draw(self.enemies_surface, (self.enemies_surface_rect.centerx - (int(len(self.list_of_enemies) / 2) - i) * 150, self.enemies_surface_rect.centery))
                self.list_of_enemies[i].draw_health_bar(self.enemies_surface, (self.enemies_surface_rect.centerx - (int(len(self.list_of_enemies) / 2) - i) * 150, self.enemies_surface_rect.centery - 80))
                self.list_of_enemies[i].draw_selection_indicator(self.enemies_surface, (self.enemies_surface_rect.centerx - (int(len(self.list_of_enemies) / 2) - i) * 150, self.enemies_surface_rect.centery - 140))
            elif i == int(len(self.list_of_enemies) / 2):
                self.list_of_enemies[i].draw(self.enemies_surface, (self.enemies_surface_rect.centerx, self.enemies_surface_rect.centery))
                self.list_of_enemies[i].draw_health_bar(self.enemies_surface, (self.enemies_surface_rect.centerx, self.enemies_surface_rect.centery - 80))
                self.list_of_enemies[i].draw_selection_indicator(self.enemies_surface, (self.enemies_surface_rect.centerx, self.enemies_surface_rect.centery - 140))
            elif i > len(self.list_of_enemies) / 2: 
                self.list_of_enemies[i].draw(self.enemies_surface, (self.enemies_surface_rect.centerx + (i- int(len(self.list_of_enemies) / 2)) * 150, self.enemies_surface_rect.centery))
                self.list_of_enemies[i].draw_health_bar(self.enemies_surface, (self.enemies_surface_rect.centerx + (i - int(len(self.list_of_enemies) / 2) ) * 150, self.enemies_surface_rect.centery - 80))
                self.list_of_enemies[i].draw_selection_indicator(self.enemies_surface, (self.enemies_surface_rect.centerx + (i - int(len(self.list_of_enemies) / 2) ) * 150, self.enemies_surface_rect.centery - 140))

    def select_enemy(self, increment):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # window_open = False
                sys.exit()
                # pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # window_open= False
                    sys.exit()
                    # pygame.quit()
                if event.key == pygame.K_LEFT:
                    self.level_deck.choose_card(False)
                if event.key == pygame.K_RIGHT:
                    self.level_deck.choose_card(True)
                if event.key == pygame.K_SPACE:
                    self.level_deck.pop_card()
