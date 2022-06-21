import pygame, os, sys
import game_module as gm

pygame.init()

class Scene():
    def __init__(self, name, screen, image) -> None:
        self.name = name
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = image
        self.next_scene = None

    def get_next_scene(self):
        return self.next_scene

    def switch_scene(self, scene):
        self.next_scene = scene

class MainMenu(Scene):
    def __init__(self, name, screen, image) -> None:
        super().__init__(name, screen, image)
        # self.switch_scene()

    def draw(self):
        title_text = gm.GAME_TITLE_FONT.render("SLAY THE SPIRE", True, gm.WHITE)
        title_text_rect = title_text.get_rect()
        text_play = gm.GAME_OPTIONS_FONT.render("Press F1 to continue", True, gm.WHITE)
        text_play_rect = text_play.get_rect()
        text_quit = gm.GAME_OPTIONS_FONT.render("Press Escape to quit", True, gm.WHITE)
        text_quit_rect = text_quit.get_rect()

        self.screen.blit(self.image, (0, 0))

        self.screen.blit(title_text, (self.screen_rect.centerx - title_text_rect.centerx, self.screen_rect.top + 100))
        self.screen.blit(text_play, (self.screen_rect.centerx - text_play_rect.centerx, self.screen_rect.top + 500))
        self.screen.blit(text_quit, (self.screen_rect.centerx - text_quit_rect.centerx, self.screen_rect.top + 550))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # window_open = False
                pygame.quit()
                # sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # window_open= False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_F1:
                    self.switch_scene("LEVEL")

    def get_next_scene(self):
        super().get_next_scene()

    def switch_scene(self, scene):
        super().switch_scene(scene)

    def scene_loop(self):
        self.draw()
        self.handle_events()

class PauseMenu(Scene):
    def __init__(self, name, screen, image) -> None:
        super().__init__(name, screen, image)
        self.image.set_alpha(128)

    def draw(self):
        title_text = gm.GAME_TITLE_FONT.render("SLAY THE SPIRE", True, gm.WHITE)
        title_text_rect = title_text.get_rect()
        pause_text = gm.GAME_TITLE_FONT.render("Pause menu", True, gm.WHITE)
        pause_text_rect = pause_text.get_rect()
        text_play = gm.GAME_OPTIONS_FONT.render("Press F1 to continue", True, gm.WHITE)
        text_play_rect = text_play.get_rect()
        text_quit = gm.GAME_OPTIONS_FONT.render("Press Escape to go to main menu", True, gm.WHITE)
        text_quit_rect = text_quit.get_rect()

        self.screen.blit(self.image, (0, 0))

        self.screen.blit(title_text, (self.screen_rect.centerx - title_text_rect.centerx, self.screen_rect.top + 100))
        self.screen.blit(pause_text, (self.screen_rect.centerx - pause_text_rect.centerx, self.screen_rect.top + 160))
        self.screen.blit(text_play, (self.screen_rect.centerx - text_play_rect.centerx, self.screen_rect.top + 500))
        self.screen.blit(text_quit, (self.screen_rect.centerx - text_quit_rect.centerx, self.screen_rect.top + 550))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # window_open = False
                pygame.quit()
                # sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.switch_scene("LEVEL")
                if event.key == pygame.K_ESCAPE:
                    self.switch_scene("MAINMENU")

    def scene_loop(self):
        self.draw()
        self.handle_events()

    def switch_scene(self, scene):
        super().switch_scene(scene)

class WinScene(Scene):
    def __init__(self, name, screen, image) -> None:
        super().__init__(name, screen, image)

    def draw(self):
        title_text = gm.GAME_TITLE_FONT.render("YOU WON!", True, gm.WHITE)
        title_text_rect = title_text.get_rect()
        text_play = gm.GAME_OPTIONS_FONT.render("Press F1 to continue", True, gm.WHITE)
        text_play_rect = text_play.get_rect()
        text_quit = gm.GAME_OPTIONS_FONT.render("Press Escape to go to main menu", True, gm.WHITE)
        text_quit_rect = text_quit.get_rect()

        self.screen.blit(self.image, (0, 0))

        self.screen.blit(title_text, (self.screen_rect.centerx - title_text_rect.centerx, self.screen_rect.top + 100))
        self.screen.blit(text_play, (self.screen_rect.centerx - text_play_rect.centerx, self.screen_rect.top + 500))
        self.screen.blit(text_quit, (self.screen_rect.centerx - text_quit_rect.centerx, self.screen_rect.top + 550))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.switch_scene("MAINMENU")
                if event.key == pygame.K_F1:
                    self.switch_scene("LEVEL1")

    def get_next_scene(self):
        super().get_next_scene()

    def switch_scene(self, scene):
        super().switch_scene(scene)

    def scene_loop(self):
        self.draw()
        self.handle_events()


class LoseScene(Scene):
    def __init__(self, name, screen, image) -> None:
        super().__init__(name, screen, image)

    def draw(self):
        title_text = gm.GAME_TITLE_FONT.render("YOU LOST!", True, gm.WHITE)
        title_text_rect = title_text.get_rect()
        text_quit = gm.GAME_OPTIONS_FONT.render("Press Escape to go to main menu", True, gm.WHITE)
        text_quit_rect = text_quit.get_rect()

        self.screen.blit(self.image, (0, 0))

        self.screen.blit(title_text, (self.screen_rect.centerx - title_text_rect.centerx, self.screen_rect.top + 100))
        self.screen.blit(text_quit, (self.screen_rect.centerx - text_quit_rect.centerx, self.screen_rect.top + 550))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.switch_scene("MAINMENU")

    def get_next_scene(self):
        super().get_next_scene()

    def switch_scene(self, scene):
        super().switch_scene(scene)

    def scene_loop(self):
        self.draw()
        self.handle_events()