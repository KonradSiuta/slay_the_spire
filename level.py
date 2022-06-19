import sys
import pygame, os
import game_module as gm
from card import *
from deck import *
from character import *
import copy
from random import randint


class Level():
    def __init__(self, screen, player, game_deck, list_of_enemies) -> None:
        self.display = True

        self.screen = screen

        self.player = player

        self.list_of_enemies = []
        
        self.game_deck = game_deck

        self.level_deck = LevelDeck()

        self.list_of_enemies = list_of_enemies

        self.is_player_turn = True
        
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

    def switch_turns(self):
        if self.is_player_turn:
            self.is_player_turn = False
        else:
            self.is_player_turn = True

    def draw(self):
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
        self.status_bar.blit(gm.BLOCK_ICON, (250, gm.SB_HEIGHT / 2 - 20))
        self.player.print_block_status(self.status_bar, (300, gm.SB_HEIGHT / 2 - 17))

        self.draw_enemies()

    def draw_enemies(self):
        for i in range(len(self.list_of_enemies)):
            if i < len(self.list_of_enemies) / 2:
                self.list_of_enemies[i].draw(self.enemies_surface, (self.enemies_surface_rect.centerx - (int(len(self.list_of_enemies) / 2) - i) * 150, self.enemies_surface_rect.centery))
                self.list_of_enemies[i].draw_health_bar(self.enemies_surface, (self.enemies_surface_rect.centerx - (int(len(self.list_of_enemies) / 2) - i) * 150, self.enemies_surface_rect.centery - 80))
                self.list_of_enemies[i].draw_selection_indicator(self.enemies_surface, (self.enemies_surface_rect.centerx - (int(len(self.list_of_enemies) / 2) - i) * 150, self.enemies_surface_rect.centery - 140))
                self.list_of_enemies[i].draw_block_status(self.enemies_surface, (self.enemies_surface_rect.centerx - (int(len(self.list_of_enemies) / 2) - i) * 150, self.enemies_surface_rect.bottom - 150))
            elif i == int(len(self.list_of_enemies) / 2):
                self.list_of_enemies[i].draw(self.enemies_surface, (self.enemies_surface_rect.centerx, self.enemies_surface_rect.centery))
                self.list_of_enemies[i].draw_health_bar(self.enemies_surface, (self.enemies_surface_rect.centerx, self.enemies_surface_rect.centery - 80))
                self.list_of_enemies[i].draw_selection_indicator(self.enemies_surface, (self.enemies_surface_rect.centerx, self.enemies_surface_rect.centery - 140))
                self.list_of_enemies[i].draw_block_status(self.enemies_surface, (self.enemies_surface_rect.centerx , self.enemies_surface_rect.bottom - 150))
            elif i > len(self.list_of_enemies) / 2: 
                self.list_of_enemies[i].draw(self.enemies_surface, (self.enemies_surface_rect.centerx + (i- int(len(self.list_of_enemies) / 2)) * 150, self.enemies_surface_rect.centery))
                self.list_of_enemies[i].draw_health_bar(self.enemies_surface, (self.enemies_surface_rect.centerx + (i - int(len(self.list_of_enemies) / 2) ) * 150, self.enemies_surface_rect.centery - 80))
                self.list_of_enemies[i].draw_selection_indicator(self.enemies_surface, (self.enemies_surface_rect.centerx + (i - int(len(self.list_of_enemies) / 2) ) * 150, self.enemies_surface_rect.centery - 140))
                self.list_of_enemies[i].draw_block_status(self.enemies_surface, (self.enemies_surface_rect.centerx + (i - int(len(self.list_of_enemies) / 2) ) * 150, self.enemies_surface_rect.bottom - 150))

    def find_selected_enemy(self) -> int:
        i = 0
        for enemy in self.list_of_enemies:
            i = (i + 1) % len(self.list_of_enemies)
            if enemy.selected:
                break
       
        return i

    def select_enemy(self):       
        i = self.find_selected_enemy()

        for enemy in self.list_of_enemies:
            enemy.selected = False

        self.list_of_enemies[i].selected = True

    def update_enemies_status(self):
        for enemy in self.list_of_enemies:
            if enemy.health == 0:
                del self.list_of_enemies[self.list_of_enemies.index(enemy)]

    def enemies_turn(self):
        # self.switch_turns()
        print ("enemy turn")
        for enemy in self.list_of_enemies:
            enemy.selected = True
            action_type = randint(0, 2)

            if action_type == 0:
                enemy.attack_player(self.player, randint(1, int(self.player.max_health / len(self.list_of_enemies) * 0.3)))
            elif action_type == 1:
                enemy.heal_up(randint(1, int(enemy.max_health * 0.5)))
            elif action_type == 2:
                enemy.gain_block(randint(1, 3))

            print(enemy.block)
            
            enemy.selected = False
        self.switch_turns()


    def player_turn(self):
        print("player turn")
        self.player.restore_energy()
        self.draw_cards()
        # self.handle_player_events()
        self.switch_turns()
        
    def handle_player_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # window_open = False
                sys.exit()
                # pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.level_deck.choose_card(False)
                if event.key == pygame.K_RIGHT:
                    self.level_deck.choose_card(True)
                if event.key == pygame.K_SPACE:
                            # self.level_deck.pop_card()
                    if len(self.level_deck.card_list) > 0:
                        if isinstance((self.level_deck.card_list[self.level_deck.highlited_card]), AttackCard):
                            self.level_deck.play_card(self.list_of_enemies[self.find_selected_enemy() - 1], self.player)
                        elif isinstance((self.level_deck.card_list[self.level_deck.highlited_card]), HealCard):
                            self.level_deck.play_card(self.player, self.player)
                        elif isinstance((self.level_deck.card_list[self.level_deck.highlited_card]), ArmorCard):
                            self.level_deck.play_card(self.player, self.player)
                if event.key == pygame.K_UP:
                    self.select_enemy()


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
                    # self.level_deck.pop_card()
                    if len(self.level_deck.card_list) > 0:
                        if isinstance((self.level_deck.card_list[self.level_deck.highlited_card]), AttackCard):
                            self.level_deck.play_card(self.list_of_enemies[self.find_selected_enemy() - 1], self.player)
                        elif isinstance((self.level_deck.card_list[self.level_deck.highlited_card]), HealCard):
                            self.level_deck.play_card(self.player, self.player)
                        elif isinstance((self.level_deck.card_list[self.level_deck.highlited_card]), ArmorCard):
                            self.level_deck.play_card(self.player, self.player)
                if event.key == pygame.K_UP:
                    self.select_enemy()
                if event.key == pygame.K_BACKSPACE:
                    if self.is_player_turn:
                        self.player_turn()
                    else:
                        self.enemies_turn()

    def draw_cards(self):
        if len(self.game_deck.card_list) > 0:
            i = 0
            while len(self.level_deck.card_list) < self.level_deck.max_size - 1 and i < 5:
                if len(self.game_deck.card_list) > 0:
                    self.level_deck.add_single_card(self.game_deck.card_list[0])
                    self.game_deck.pop_card(0)
                i += 1
