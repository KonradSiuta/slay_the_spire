from game import *

player = Player(gm.PLAYER_TEST_IMAGE, 25, 5)
enemy1 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy2 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy3 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy4 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy5 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy6 = Enemy(gm.ENEMY_TEST_IMAGE, 5)
enemy7 = Enemy(gm.ENEMY_TEST_IMAGE, 5)

list_of_enemies1 = [enemy3, enemy4, enemy5, enemy6, enemy7]
list_of_enemies2 = [enemy1, enemy2]

# deck = Deck()
game_deck1 = GameDeck()
game_deck2 = GameDeck()
card1 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball1", "Deal 3 damage to an enemy", 2, 3)
card2 = HealCard(gm.CARD_TEST_IMAGE, "Nourish", "Restore 5 health", 1, 5)
card3 = ArmorCard(gm.CARD_TEST_IMAGE, "Block", "Gain 6 armor", 1, 6)
card4 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball2", "Deal 3 damage to an enemy", 2, 3)
card5 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball3", "Deal 3 damage to an enemy", 2, 3)
card6 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball4", "Deal 3 damage to an enemy", 2, 3)
card7 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball5", "Deal 3 damage to an enemy", 2, 3)
card8 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball6", "Deal 3 damage to an enemy", 2, 3)
card9 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball7", "Deal 3 damage to an enemy", 2, 3)
card10 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball8", "Deal 3 damage to an enemy", 2, 3)
card11 = AttackCard(gm.CARD_TEST_IMAGE, "Fireball9", "Deal 3 damage to an enemy", 2, 3) 
cards_list1 = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11]
cards_list2 = [card1, card2, card3, card4, card5, card6, card7]
# deck.add_cards(cards_list1)
game_deck1.copy_deck(cards_list1)
game_deck2.copy_deck(cards_list2)
# level_deck.copy_deck(game_deck.card_list)

if __name__ == "__main__":
    game = Game(player, game_deck1, game_deck2, list_of_enemies1, list_of_enemies2)
    game.game_loop()

    pygame.quit()