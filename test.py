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
chosen_card = pygame.Surface.subsurface(screen, (0, gm.SB_HEIGHT, gm.C_WIDTH, gm.C_HEIGHT))
deck_surface = pygame.Surface.subsurface(screen, (gm.C_WIDTH, gm.SB_HEIGHT, gm.SB_WIDTH - gm.C_WIDTH, gm.SC_HEIGHT))
chosen_card_rect = chosen_card.get_rect()
player_surface = pygame.Surface.subsurface(screen, 0, gm.SB_HEIGHT + gm.C_HEIGHT, gm.S_WIDTH / 3, gm.S_HEIGHT / 2)
player_surface_rect = player_surface.get_rect()
enemies_surface = pygame.Surface.subsurface(screen, (player_surface_rect.right, gm.SB_HEIGHT + gm.C_HEIGHT, gm.S_WIDTH - player_surface_rect.right, gm.S_HEIGHT / 2))
enemies_surface_rect = enemies_surface.get_rect()
platform_surface = pygame.Surface.subsurface(screen, (0, gm.SB_HEIGHT + gm.C_HEIGHT + enemies_surface_rect.bottom, gm.S_WIDTH, gm.S_HEIGHT - (gm.SB_HEIGHT + gm.C_HEIGHT + enemies_surface_rect.bottom)))

window_open = True

player = Player(gm.PLAYER_TEST_IMAGE, 25)
enemy1 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy2 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy3 = Enemy(gm.ENEMY_TEST_IMAGE, 5)

list_of_enemies = []
list_of_enemies.append(enemy1)
list_of_enemies.append(enemy2)
list_of_enemies.append(enemy3)
list_of_enemies.append(enemy3)
list_of_enemies.append(enemy3)

deck = Deck()
level_deck = LevelDeck()
card1 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball", "Deal 3 damage to an enemy", 2)
card2 = HealCard(gm.CARD_TEST_IMAGE, "Nourish", "Restore 5 health", 1)
card3 = ArmorCard(gm.CARD_TEST_IMAGE, "Block", "Gain 1 armor", 1)
deck.add_card(card1)
deck.add_card(card2)
deck.add_card(card3)

level_deck.copy_deck(deck.card_list)

scaled_card = copy.copy(card1)
card1.set_rects()
scaled_card.downscale()
scaled_card.set_rects()
    

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
                # print(screen.get_locked())
                # print(player_surface.get_locked())
                # print(f"{player_surface_rect.right}, {gm.S_WIDTH - player_surface_rect.right}")
            if event.key == pygame.K_RIGHT:
                level_deck.choose_card(True)
            if event.key == pygame.K_SPACE:
                level_deck.pop_card()

    level_deck.print_highlited_card(chosen_card)
    
    level_deck.print_level_deck(deck_surface)

    player.draw(player_surface, player_surface_rect.midbottom)
    player.draw_health_bar(player_surface, player_surface_rect)

    for i in range(len(list_of_enemies)):
        if i < len(list_of_enemies) / 2:
            list_of_enemies[i].draw(enemies_surface, (enemies_surface_rect.centerx - (int(len(list_of_enemies) / 2) - i) * 150, enemies_surface_rect.centery))
            list_of_enemies[i].draw_health_bar(enemies_surface, (enemies_surface_rect.centerx - (int(len(list_of_enemies) / 2) - i) * 150, enemies_surface_rect.centery - 80))
        elif i == int(len(list_of_enemies) / 2):
            list_of_enemies[i].draw(enemies_surface, (enemies_surface_rect.centerx, enemies_surface_rect.centery))
            list_of_enemies[i].draw_health_bar(enemies_surface, (enemies_surface_rect.centerx, enemies_surface_rect.centery - 80))
        elif i > len(list_of_enemies) / 2: 
            list_of_enemies[i].draw(enemies_surface, (enemies_surface_rect.centerx + (i- int(len(list_of_enemies) / 2)) * 150, enemies_surface_rect.centery))
            list_of_enemies[i].draw_health_bar(enemies_surface, (enemies_surface_rect.centerx + (i - int(len(list_of_enemies) / 2) ) * 150, enemies_surface_rect.centery - 80))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()