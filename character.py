import pygame
import game_module as gm

class Character(pygame.sprite.Sprite):
    def __init__(self, image, max_health) -> None:
        super().__init__()
        self.max_health = max_health
        self.health = self.max_health
        self.image = image
        self.rect = self.image.get_rect()

        self.block = 0

    def take_damage(self, value):
        if self.block > 0:
            if self.block >= value:
                self.block -= value
            if self.block < value:
                value -= self.block
                self.health -= value
                self.block = 0
        else:
            if value <= self.health:
                self.health -= value
            else:
                self.health = 0

    def heal_up(self, value):
        if value + self.health >= self.max_health:
            self.health = self.max_health
        else:
            self.health += value

    def gain_block(self, value):
        self.block += value

class Player(Character):
    def __init__(self, image, max_health, max_energy) -> None:
        super().__init__(image, max_health)
        # self.health = 10
        self.max_energy = max_energy
        self.energy = max_energy

    def restore_energy(self):
        self.energy = self.max_energy

    def take_damage(self, damage):
        super().take_damage(damage)
    
    def draw(self, surface, cords):
        surface.blit(self.image, (cords[0] - self.rect.centerx, cords[1] - self.rect.bottom))

    def draw_health_bar(self, surface, surface_rect):
        health_bar_subsurface = pygame.Surface.subsurface(surface, (surface_rect.centerx - (self.max_health * gm.HB_UNIT_WIDTH / 2), surface_rect.top + 50 , self.max_health * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))
        health_bar_rect = health_bar_subsurface.get_rect()
        remaining_health_bar = pygame.Surface.subsurface(health_bar_subsurface, (health_bar_rect.left, health_bar_rect.top, self.health * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))
        remaining_health_bar_rect = remaining_health_bar.get_rect()
        lost_health_bar = pygame.Surface.subsurface(health_bar_subsurface, (remaining_health_bar_rect.right, health_bar_rect.top, (self.max_health - self.health) * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))

        text = gm.CARD_TYPE_FONT.render(f"{self.health}/{self.max_health}", True, (255,255,255))
        text_rect = text.get_rect()
        
        remaining_health_bar.fill(gm.RED)
        lost_health_bar.fill(gm.DARKRED)

        health_bar_subsurface.blit(text, (health_bar_rect.centerx - text_rect.centerx, health_bar_rect.centery - text_rect.centery))

    def print_health_status(self, surface, cords):
        text = gm.CARD_TITLE_FONT.render(f"{self.health}/{self.max_health}", True, (255,255,255))
        surface.blit(text, cords)
    
    def print_energy_status(self, surface, cords):
        text = gm.CARD_TITLE_FONT.render(f"{self.energy}/{self.max_energy}", True, (255,255,255))
        surface.blit(text, cords)
    
    def print_block_status(self, surface, cords):
        text = gm.CARD_TITLE_FONT.render(f"{self.block}", True, (255,255,255))
        surface.blit(text, cords)

class Enemy(Character):
    def __init__(self, image, max_health) -> None:
        super().__init__(image, max_health)
        self.selected = False

    def take_damage(self, damage):
        super().take_damage(damage)
    
    def heal_up(self, value):
        super().heal_up(value)

    def gain_block(self, value):
        super().gain_block(value)

    def attack_player(self, player, value):
        player.take_damage(value)

    def draw(self, surface, cords):
        surface.blit(self.image, (cords[0] - self.rect.centerx, cords[1] - self.rect.bottom))

    def draw_health_bar(self, surface, surface_rect):
        health_bar_subsurface = pygame.Surface.subsurface(surface, surface_rect[0] - (self.max_health * gm.HB_UNIT_WIDTH / 2), surface_rect[1] - gm.HB_UNIT_HEIGHT, self.max_health * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT)
        health_bar_rect = health_bar_subsurface.get_rect()
        remaining_health_bar = pygame.Surface.subsurface(health_bar_subsurface, (health_bar_rect.left, health_bar_rect.top, self.health * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))
        remaining_health_bar_rect = remaining_health_bar.get_rect()
        lost_health_bar = pygame.Surface.subsurface(health_bar_subsurface, (remaining_health_bar_rect.right, health_bar_rect.top, (self.max_health - self.health) * gm.HB_UNIT_WIDTH, gm.HB_UNIT_HEIGHT))

        text = gm.CARD_TYPE_FONT.render(f"{self.health}/{self.max_health}", True, (255,255,255))
        text_rect = text.get_rect()

        remaining_health_bar.fill(gm.RED)
        lost_health_bar.fill(gm.DARKRED)
        health_bar_subsurface.blit(text, (health_bar_rect.centerx - text_rect.centerx, health_bar_rect.centery - text_rect.centery))
    
    def draw_selection_indicator(self, surface, cords):
        if self.selected:
            pygame.draw.polygon(surface, gm.RED, [(cords[0] - 20, cords[1]), (cords[0] + 20, cords[1]), (cords [0], cords[1] + 30)])

    def draw_block_status(self, surface, cords):
        if self.block >= 0:
            text = gm.CARD_TITLE_FONT.render(f"{self.block}", True, (255, 255, 255))
            text_rect = text.get_rect()

            surface.blit(gm.SMALLER_BLOCK_ICON, (cords[0] - text_rect.centerx - 30, cords[1] + 10))
            surface.blit(text, (cords[0] - text_rect.centerx , cords[1] + 10))