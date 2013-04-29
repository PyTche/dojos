from __future__ import division
import unittest
from poker import PokerHands

class TestPoker(unittest.TestCase):

    def setUp(self):
        self.hand1 = PokerHands([1,2,3,5,5])
        self.hand2 = PokerHands([1,1,1,3,10])
        self.hand3 = PokerHands([2,1,2,1,8])
        self.hand4 = PokerHands([1,1,1,2,2])

    def test_hand(self):
        self.assertEqual(self.hand1.has_cards(), True)

    def test_one_pair(self):
        self.assertEqual(self.hand1.which_hand(), "one pair")

    def test_three_of_kind(self):
        self.assertEqual(self.hand2.which_hand(), "three kind")

    def test_fullhouse(self):
        self.assertEqual(self.hand4.which_hand(),"FullHouse")
    def test_two_pairs(self):
        self.assertEqual(self.hand3.which_hand(), "two pairs")


    def test_count_cards(self):
        number = self.hand1.count_number_of_each()
        number2 = self.hand2.count_number_of_each()
        self.assertEqual(number[5], 2)
        self.assertEqual(number[1], 1)
        self.assertEqual(number2[1], 3)
        self.assertNotEqual(number2[3], 2)
if __name__ == "__main__":
    unittest.main()