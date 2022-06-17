from game import *

player = Player(gm.PLAYER_TEST_IMAGE, 25, 5)
enemy1 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy2 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy3 = Enemy(gm.ENEMY_TEST_IMAGE, 5)

list_of_enemies = [enemy1, enemy2, enemy3]

deck = Deck()
level_deck = LevelDeck()
card1 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball", "Deal 3 damage to an enemy", 2)
card2 = HealCard(gm.CARD_TEST_IMAGE, "Nourish", "Restore 5 health", 1)
card3 = ArmorCard(gm.CARD_TEST_IMAGE, "Block", "Gain 1 armor", 1)
cards_list = [card1, card2, card3]
deck.add_cards(cards_list)
level_deck.copy_deck(deck.card_list)

if __name__ == "__main__":
    game = Game(player, level_deck, list_of_enemies)
    game.game_loop()