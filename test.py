import pygame, os
import game_module as gm
from card import *
from deck import *
from character import *
import copy

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screen = pygame.display.set_mode(gm.SCREEN_SIZE)
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
status_bar = pygame.Surface.subsurface(screen, (0, 0, gm.SB_WIDTH, gm.SB_HEIGHT))
status_bar_rect = status_bar.get_rect()
chosen_card = pygame.Surface.subsurface(screen, (0, gm.SB_HEIGHT, gm.C_WIDTH, gm.C_HEIGHT))
deck_surface = pygame.Surface.subsurface(screen, (gm.C_WIDTH, gm.SB_HEIGHT, gm.SB_WIDTH - gm.C_WIDTH, gm.SC_HEIGHT))
chosen_card_rect = chosen_card.get_rect()
player_surface = pygame.Surface.subsurface(screen, 0, gm.SB_HEIGHT + gm.C_HEIGHT, gm.S_WIDTH / 3, gm.S_HEIGHT / 2)
player_surface_rect = player_surface.get_rect()
enemies_surface = pygame.Surface.subsurface(screen, (player_surface_rect.right, gm.SB_HEIGHT + gm.C_HEIGHT, gm.S_WIDTH - player_surface_rect.right, gm.S_HEIGHT / 2))
enemies_surface_rect = enemies_surface.get_rect()
platform_surface = pygame.Surface.subsurface(screen, (0, gm.SB_HEIGHT + gm.C_HEIGHT + enemies_surface_rect.bottom, gm.S_WIDTH, gm.S_HEIGHT - (gm.SB_HEIGHT + gm.C_HEIGHT + enemies_surface_rect.bottom)))

window_open = True

player = Player(gm.PLAYER_TEST_IMAGE, 25, 5)
enemy1 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy2 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy3 = Enemy(gm.ENEMY_TEST_IMAGE, 5)

list_of_enemies = [enemy1, enemy2, enemy3]

deck = Deck()
level_deck = LevelDeck()
card1 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball", "Deal 3 damage to an enemy", 2)
card2 = HealCard(gm.CARD_TEST_IMAGE, "Nourish", "Restore 5 health", 1)
card3 = ArmorCard(gm.CARD_TEST_IMAGE, "Block", "Gain 1 armor", 1)
cards_list = [card1, card2, card3]
deck.add_cards(cards_list)

level_deck.copy_deck(deck.card_list)
   
while window_open:
    screen.blit(gm.BG_IMAGE, (0, 0))
    # enemies_surface.fill(gm.RED)
    platform_surface.fill(gm.BLACK)
    #pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
            if event.key == pygame.K_LEFT:
                level_deck.choose_card(False)
            if event.key == pygame.K_RIGHT:
                level_deck.choose_card(True)
            if event.key == pygame.K_SPACE:
                level_deck.pop_card()

    level_deck.print_highlited_card(chosen_card)
    
    level_deck.print_level_deck(deck_surface)

    player.draw(player_surface, player_surface_rect.midbottom)
    player.draw_health_bar(player_surface, player_surface_rect)

    status_bar.fill(gm.LIGHTBLUE)
    status_bar.blit(gm.HEALTH_ICON, (15, gm.SB_HEIGHT / 2 - 20))
    player.print_health_status(status_bar, (60, gm.SB_HEIGHT / 2 - 17))
    status_bar.blit(gm.ENERGY_ICON, (150, gm.SB_HEIGHT / 2 - 20))
    player.print_energy_status(status_bar, (190, gm.SB_HEIGHT / 2 - 17))

    for i in range(len(list_of_enemies)):
        if i < len(list_of_enemies) / 2:
            list_of_enemies[i].draw(enemies_surface, (enemies_surface_rect.centerx - (int(len(list_of_enemies) / 2) - i) * 150, enemies_surface_rect.centery))
            list_of_enemies[i].draw_health_bar(enemies_surface, (enemies_surface_rect.centerx - (int(len(list_of_enemies) / 2) - i) * 150, enemies_surface_rect.centery - 80))
            list_of_enemies[i].draw_selection_indicator(enemies_surface, (enemies_surface_rect.centerx - (int(len(list_of_enemies) / 2) - i) * 150, enemies_surface_rect.centery - 140))
        elif i == int(len(list_of_enemies) / 2):
            list_of_enemies[i].draw(enemies_surface, (enemies_surface_rect.centerx, enemies_surface_rect.centery))
            list_of_enemies[i].draw_health_bar(enemies_surface, (enemies_surface_rect.centerx, enemies_surface_rect.centery - 80))
            list_of_enemies[i].draw_selection_indicator(enemies_surface, (enemies_surface_rect.centerx, enemies_surface_rect.centery - 140))
        elif i > len(list_of_enemies) / 2: 
            list_of_enemies[i].draw(enemies_surface, (enemies_surface_rect.centerx + (i- int(len(list_of_enemies) / 2)) * 150, enemies_surface_rect.centery))
            list_of_enemies[i].draw_health_bar(enemies_surface, (enemies_surface_rect.centerx + (i - int(len(list_of_enemies) / 2) ) * 150, enemies_surface_rect.centery - 80))
            list_of_enemies[i].draw_selection_indicator(enemies_surface, (enemies_surface_rect.centerx + (i - int(len(list_of_enemies) / 2) ) * 150, enemies_surface_rect.centery - 140))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()