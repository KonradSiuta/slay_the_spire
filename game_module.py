import pygame, os, sys
from card import *

pygame.font.init()
assets_path = os.path.join(os.path.dirname(__file__), "assets")

SCREEN_SIZE = S_WIDTH, S_HEIGHT = 1280, 720
screen = pygame.display.set_mode(SCREEN_SIZE)

CARD_SIZE = C_WIDTH, C_HEIGHT = 220, 220
CARD_IMAGE_SIZE = CI_WIDTH, CI_HEIGHT = 210, 120

STATUS_BAR = SB_WIDTH, SB_HEIGHT = 1280, 50

SCALED_CARD_SIZE = SC_WIDTH, SC_HEIGHT = 110, 110
SCALED_CARD_IMAGE_SIZE = SCI_WIDTH, SCI_HEIGHT = 105, 60

PLAYER_SIZE = P_WIDTH, P_HEIGHT = 90, 200

HEALTH_BAR_SIZE = HB_UNIT_WIDTH, HB_UNIT_HEIGHT = 5, 15

CARD_TITLE_FONT = pygame.font.Font(pygame.font.get_default_font(), 28)

SCALED_TITLE_FONT = pygame.font.Font(pygame.font.get_default_font(), 16)

CARD_DESCRIPTION_FONT = pygame.font.Font(pygame.font.get_default_font(), 14)

CARD_TYPE_FONT = pygame.font.Font(pygame.font.get_default_font(), 10)

LIGHTBLUE = pygame.color.THECOLORS['lightblue']
GREEN = pygame.color.THECOLORS['green']
RED = pygame.color.THECOLORS['red']
BLACK = pygame.color.THECOLORS['black']
DARKRED = pygame.Color(117, 11, 4)

BG_IMAGE = pygame.image.load(os.path.join(assets_path, "background3-720.png")).convert()
CARD_TEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "parallax-forest.png")).convert(), (CI_WIDTH, CI_HEIGHT))

PLAYER_TEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "player_stand_R.png")).convert_alpha(), (P_WIDTH, P_HEIGHT))
ENEMY_TEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "bat_fly1_L.png")).convert_alpha(), (80, 60))
HEALTH_ICON = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "heart.png")).convert_alpha(), (40, 40))
ENERGY_ICON = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "Energia.png")).convert_alpha(), (40, 40))
BLOCK_ICON = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "a_shield_kite_bronze.png")).convert_alpha(), (40, 40))
SMALLER_BLOCK_ICON = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "a_shield_kite_bronze.png")).convert_alpha(), (30, 30))
