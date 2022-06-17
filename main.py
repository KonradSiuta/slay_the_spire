import pygame, os
import game_module as gm

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screen = pygame.display.set_mode(gm.SCREEN_SIZE)
clock = pygame.time.Clock()

window_open = True
text = gm.CARD_TITLE_FONT.render('quit', True, (255, 255, 255))

while window_open:
    screen.blit(gm.BG_IMAGE, (0, 0))
    screen.blit(text, (640, 360))

    #pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()