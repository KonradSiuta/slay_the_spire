import pygame, os
from pygame.locals import *
import game_module as gm

class Card(pygame.sprite.Sprite):
    def __init__(self, image, title, description, cost):
        super().__init__()
        # atrybuty graficzne
        self.image = image
        self.image_rect = None
        self._shape = pygame.Surface((gm.C_WIDTH, gm.C_HEIGHT))
        self.rect = None
        self.title = title
        self.title_text = gm.CARD_TITLE_FONT.render(self.title, True, (255, 255, 255))
        self.title_rect = None
        self.description = description
        self.description_text = gm.CARD_DESCRIPTION_FONT.render(self.description, True, (255, 255, 255))
        self.description_rect = None
        self.downscaled = False
        self.energy_cost = cost
        self.energy_text = gm.CARD_TITLE_FONT.render(str(self.energy_cost), True, gm.GREEN)
        self.energy_rect = None

    def set_rects(self):
        self.image_rect = self.image.get_rect()
        self.rect = self._shape.get_rect()
        self.title_rect = self.title_text.get_rect() 
        self.description_rect = self.description_text.get_rect() 
        self.energy_rect = self.energy_text.get_rect()

    def draw(self, surface, cords, scaled):
        if scaled:
            self.downscale()

        self.set_rects()
        
        self._shape.fill((89, 89, 89))
        self._shape.blit(self.image, (self.rect.centerx - self.image_rect.centerx, self.rect.top + 10))
        self._shape.blit(self.title_text, (self.rect.centerx - self.title_rect.centerx, self.image_rect.bottom + 15))
        self._shape.blit(self.energy_text, (self.rect.x + 5, self.rect.y + 5))

        if not self.downscaled:
            self._shape.blit(self.description_text, (self.rect.centerx - self.description_rect.centerx, self.image_rect.bottom + self.title_rect.bottom + 20))
        
        surface.blit(self._shape, cords)

        self.upscale()

    def downscale(self):
        self._shape = pygame.transform.scale(self._shape, gm.SCALED_CARD_SIZE)
        self.image = pygame.transform.scale(self.image, gm.SCALED_CARD_IMAGE_SIZE)
        self.title_text = gm.SCALED_TITLE_FONT.render(self.title, True, (255, 255, 255))
        self.downscaled = True
    
    def upscale(self):
        self._shape = pygame.transform.scale(self._shape, gm.CARD_SIZE)
        self.image = pygame.transform.scale(self.image, gm.CARD_IMAGE_SIZE)
        self.title_text = gm.CARD_TITLE_FONT.render(self.title, True, (255, 255, 255))
        self.downscaled = False

class AttackCard(Card):
    def __init__(self, image, title, description, cost):
        super().__init__(image, title, description, cost)

    def set_rects(self):
        return super().set_rects()

    def draw(self, surface, cords, scaled):
        super().draw(surface, cords, scaled)
        card_type = gm.CARD_TYPE_FONT.render("Attack", True, (255, 255, 255))
        card_type_rect = card_type.get_rect()
        
        if not self.downscaled:
            surface.blit(card_type, (gm.C_WIDTH / 2 - card_type_rect.centerx, gm.C_HEIGHT - card_type_rect.bottom - 5))

class HealCard(Card):
    def __init__(self, image, title, description, cost):
        super().__init__(image, title, description, cost)

    def set_rects(self):
        return super().set_rects()

    def draw(self, surface, cords, scaled):
        super().draw(surface, cords, scaled)
        # if not self.downscaled:
        card_type = gm.CARD_TYPE_FONT.render("Heal", True, (255, 255, 255))
        card_type_rect = card_type.get_rect()
        surface.blit(card_type, (gm.C_WIDTH / 2 - card_type_rect.centerx, gm.C_HEIGHT - card_type_rect.bottom - 5))

class ArmorCard(Card):
    def __init__(self, image, title, description, cost):
        super().__init__(image, title, description, cost)

    def set_rects(self):
        return super().set_rects()

    def draw(self, surface, cords, scaled):
        super().draw(surface, cords, scaled)
        if not self.downscaled:
            card_type = gm.CARD_TYPE_FONT.render("Armor", True, (255, 255, 255))
            card_type_rect = card_type.get_rect()
            surface.blit(card_type, (gm.C_WIDTH / 2 - card_type_rect.centerx, gm.C_HEIGHT - card_type_rect.bottom - 5))