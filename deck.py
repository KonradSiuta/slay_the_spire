import copy
import game_module as gm
from card import *

class Deck():
    def __init__(self) -> None:
        self.card_list = []

    def add_single_card(self, card):
        self.card_list.append(card)

    def add_cards(self, cards_list):
        for card in cards_list:
            self.add_single_card(card)

    def pop_card(self, index):
        del self.card_list[index]

class GameDeck(Deck):
    def __init__(self) -> None:
        super().__init__()

    def copy_deck(self, deck):
        super().add_cards(copy.copy(deck))

class LevelDeck(Deck):
    def __init__(self) -> None:
        super().__init__()
        self.highlited_card = 0
        self.max_size = 9

    def copy_deck(self, deck):
        super().add_cards(copy.copy(deck))

    def choose_card(self, increment):
        if len(self.card_list) > 0:  
            if increment:
                self.highlited_card = (self.highlited_card + 1) % len(self.card_list)
            else:
                if not increment:
                    if self.highlited_card == 0:
                        self.highlited_card = len(self.card_list) - 1
                    else:
                        self.highlited_card -= 1
    
    def print_highlited_card(self, surface):
        if len(self.card_list) > 0:
            self.card_list[self.highlited_card].draw(surface, (0, 0), False)
        else:
            text = gm.CARD_TITLE_FONT.render("Empty hand", True, gm.WHITE)
            surface.blit(text, (0, 0))

    def print_level_deck(self, surface):
        for i in range(len(self.card_list)):
            self.card_list[i].draw(surface, (i * gm.SC_WIDTH, 0), True)

    def pop_card(self):
        super().pop_card(self.highlited_card)
        self.choose_card(False)

    def play_card(self, target, player_status, surface, surface_rect):
        if self.card_list[self.highlited_card].energy_cost <= player_status.energy:
            self.card_list[self.highlited_card].cast(target)
            player_status.energy -= self.card_list[self.highlited_card].energy_cost
            self.pop_card()
        else:
            text = gm.CARD_TITLE_FONT.render("Not enough energy", True, gm.WHITE)
            text_rect = text.get_rect()
            surface.blit(text, (surface_rect.centerx - text_rect.centerx, surface_rect.centery - text_rect.centery))