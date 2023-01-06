import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", 12)
        self.card1 = Card("Diamond", 3)
        self.card2 = Card("Spade", 1)
        self.card3 = Card("Clubs", 2)
        self.card_game = CardGame()

    def test_can_check_true_ace(self):
        self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, self.card2.value == 1)

    def test_can_check_false_ace(self):
        self.card_game.check_for_ace(self.card2)
        self.assertEqual(False, self.card2.value == 3)

    def test_can_check_highest_number(self):
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1, self.card2))

    def test_check_for_highest_number_final_card(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card2, self.card3))

    def test_cards_total(self):
        cards = [self.card, self.card1, self.card2, self.card3]
        self.assertEqual("You have a total of 18", self.card_game.cards_total(cards))