import copy
import pygame
import game_module as gm

class Deck():
    def __init__(self) -> None:
        self.card_list = []

    def add_cards(self, cards_list):
        for card in cards_list:
            self.card_list.append(card)

    def pop_card(self, index):
        del self.card_list[index]

class GameDeck(Deck):
    def __init__(self) -> None:
        super().__init__()

    def add_card(self, card):
        super().add_card(card)

class LevelDeck(Deck):
    def __init__(self) -> None:
        super().__init__()
        self.highlited_card = 0

    def copy_deck(self, deck):
        super().add_cards(copy.copy(deck))

    def choose_card(self, increment):
        if increment:
            self.highlited_card = (self.highlited_card + 1) % len(self.card_list)
        else:
            if not increment:
                if self.highlited_card == 0:
                    self.highlited_card = len(self.card_list) - 1
                else:
                    self.highlited_card -= 1
    
    def print_highlited_card(self, surface):
        self.card_list[self.highlited_card].draw(surface, (0, 0), False)

    def print_level_deck(self, surface):
        for i in range(len(self.card_list)):
            self.card_list[i].draw(surface, (i * gm.SC_WIDTH, 0), True)

    def pop_card(self):
        super().pop_card(self.highlited_card)
        self.choose_card(False)
