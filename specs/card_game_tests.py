import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card = Card("clubs", 2)
        self.card1 = Card("spades", 1)
        self.card2 = Card("diamonds", 6)
        self.cards = [self.card1, self.card2]

    def test_card__is_not_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card))

    def test_card__is_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card1))

    def test_highest_card__is_card2(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))

    def test_highest_card__is_card(self):
        self.assertEqual(self.card, CardGame.highest_card(self, self.card, self.card1))

    def test_cards_total__is_7(self):
        self.assertEqual('You have a total of7', CardGame.cards_total(self, self.cards))

    def test_cards_total__is_17(self):
        card1 = Card("hearts", 9)
        card2 = Card("hearts", 8)
        cards_list = [card1, card2]
        self.assertEqual('You have a total of17', CardGame.cards_total(self, cards_list))
