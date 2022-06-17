import pygame
import game_module as gm

class Character(pygame.sprite.Sprite):
    def __init__(self, image, max_health) -> None:
        super().__init__()
        self.max_health = max_health
        self.health = self.max_health
        self.image = image
        self.rect = self.image.get_rect()

    # def draw(self, surface, cords):
    #     surface.blit(self.image, (cords[2] / 2, cords[3] + 100))

class Player(Character):
    def __init__(self, image, max_health) -> None:
        super().__init__(image, max_health)
    
    def draw(self, surface, cords):
        surface.blit(self.image, (cords[0] - self.rect.centerx, cords[1] - self.rect.bottom))

    def draw_health_bar(self, surface, surface_rect):
        health_bar_subsurface = pygame.Surface.subsurface(surface, (surface_rect.centerx - (self.max_health * gm.HB_UNIT_WIDTH / 2), surface_rect.top + 50 , self.max_health * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))
        health_bar_rect = health_bar_subsurface.get_rect()
        remaining_health_bar = pygame.Surface.subsurface(health_bar_subsurface, (health_bar_rect.left, health_bar_rect.top, self.health * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))
        remaining_health_bar_rect = remaining_health_bar.get_rect()
        lost_health_bar = pygame.Surface.subsurface(health_bar_subsurface, (remaining_health_bar_rect.right, health_bar_rect.top, (self.max_health - self.health) * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))

        remaining_health_bar.fill(gm.RED)
        lost_health_bar.fill(gm.DARKRED)

class Enemy(Character):
    def __init__(self, image, max_health) -> None:
        super().__init__(image, max_health)

    def draw(self, surface, cords):
        surface.blit(self.image, (cords[0] - self.rect.centerx, cords[1] - self.rect.bottom))

    def draw_health_bar(self, surface, surface_rect):
        health_bar_subsurface = pygame.Surface.subsurface(surface, surface_rect[0] - (self.max_health * gm.HB_UNIT_WIDTH / 2), surface_rect[1] - gm.HB_UNIT_HEIGHT, self.max_health * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT)
        health_bar_rect = health_bar_subsurface.get_rect()
        remaining_health_bar = pygame.Surface.subsurface(health_bar_subsurface, (health_bar_rect.left, health_bar_rect.top, self.health * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))
        remaining_health_bar_rect = remaining_health_bar.get_rect()
        lost_health_bar = pygame.Surface.subsurface(health_bar_subsurface, (remaining_health_bar_rect.right, health_bar_rect.top, (self.max_health - self.health) * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))

        remaining_health_bar.fill(gm.RED)
        lost_health_bar.fill(gm.DARKRED)
