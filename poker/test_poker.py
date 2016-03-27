import unittest
from poker import poker, normalize_value

DECK = {'valete': 11, 'dama': 12, 'rei': 13, 'as': 14}


class TestPoker(unittest.TestCase):
    def test_a_higher_number_card_must_win(self):
        winner_hand = [3, 2, 8, 5, 10]
        loser_hand = [4, 5, 7, 2, 8]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_a_higher_card_in_hand_must_win(self):
        winner_hand = [3, 7, 2, 9, 'dama']
        loser_hand = [5, 3, 7, 4, 'valete']
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_one_pair_must_win_higher_card(self):
        winner_hand = [7, 5, 8, 8, 9]
        loser_hand = [2, 5, 7, 9, 'valete']
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_two_pair_must_win_one_pair(self):
        winner_hand = [3, 3, 8, 7, 8]
        loser_hand = ['dama', 6, 8, 'dama', 'as']
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_toak_must_win_one_pair(self):
        winner_hand = [4, 5, 8, 8, 8]
        loser_hand = [3, 5, 10, 10, 'as']
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_foak_must_win_toak(self):
        winner_hand = [4, 8, 8, 8, 8]
        loser_hand = ['as', 5, 'as', 10, 'as']
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_straight_must_win_two_pair(self):
        winner_hand = [4, 5, 6, 7, 8]
        loser_hand = [5, 5, 'as', 10, 'as']
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_full_house_must_win_toak(self):
        winner_hand = [4, 6, 6, 4, 6]
        loser_hand = ['as', 5, 'as', 10, 'as']
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')


unittest.main()
