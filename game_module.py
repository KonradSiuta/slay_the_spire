import pygame, os

pygame.font.init()
pygame.mixer.init()
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

GAME_TITLE_FONT = pygame.font.Font(pygame.font.get_default_font(), 50)

GAME_OPTIONS_FONT = pygame.font.Font(pygame.font.get_default_font(), 38)

LIGHTBLUE = pygame.color.THECOLORS['lightblue']
GREEN = pygame.color.THECOLORS['green']
RED = pygame.color.THECOLORS['red']
BLACK = pygame.color.THECOLORS['black']
DARKRED = pygame.Color(117, 11, 4)
WHITE = pygame.color.THECOLORS['white']


#### ASSETY

#https://opengameart.org/content/backgrounds-for-2d-platformers
BG_LEVEL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "background3-720.png")).convert(), SCREEN_SIZE)

#https://opengameart.org/content/forest-background
CARD_TEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "parallax-forest.png")).convert_alpha(), (CI_WIDTH, CI_HEIGHT))

#https://opengameart.org/content/mountain-at-dusk-background
BG_MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "parallax-mountain.png")).convert(), SCREEN_SIZE)
BG_PAUSE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "parallax-mountain.png")).convert_alpha(), SCREEN_SIZE)

#assety pochodzące z gry tworzonej na zajęciach
PLAYER_TEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "player_stand_R.png")).convert_alpha(), (P_WIDTH, P_HEIGHT))
ENEMY_TEST_IMAGE1 = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "bat_fly1_L.png")).convert_alpha(), (80, 60))
ENEMY_TEST_IMAGE2 = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "bat_fly2_L.png")).convert_alpha(), (80, 60))
ENEMY_IMAGES = [ENEMY_TEST_IMAGE1, ENEMY_TEST_IMAGE2]

HEALTH_ICON = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "heart.png")).convert_alpha(), (40, 40))

#https://opengameart.org/content/energy-icon
ENERGY_ICON = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "Energia.png")).convert_alpha(), (40, 40))

#https://opengameart.org/content/kite-shield-64x64
BLOCK_ICON = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "a_shield_kite_bronze.png")).convert_alpha(), (40, 40))
SMALLER_BLOCK_ICON = pygame.transform.scale(pygame.image.load(os.path.join(assets_path, "a_shield_kite_bronze.png")).convert_alpha(), (30, 30))

#https://opengameart.org/content/spell-sounds-starter-pack
HEAL_SOUND = pygame.mixer.Sound(os.path.join(assets_path, "heal.ogg"))
#https://opengameart.org/content/rpg-sound-pack
ARMOR_SOUND = pygame.mixer.Sound(os.path.join(assets_path, "armor-light.wav"))
ATTACK_SOUND = pygame.mixer.Sound(os.path.join(assets_path, "chainmail1.wav"))

#https://opengameart.org/content/crystal-cave-song18
BG_MUSIC = os.path.join(assets_path, "song18.mp3")