import unittest
from poker import poker


class TestPoker(unittest.TestCase):
    def test_a_higher_number_card_must_win(self):
        winner_hand = [(3, 'H'), (2, 'C'), (8, 'D'), (5, 'H'), (10, 'D')]
        loser_hand = [(4, 'C'), (5, 'C'), (7, 'H'), (2, 'C'), (8, 'D')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_a_higher_card_in_hand_must_win(self):
        winner_hand = [(3, 'H'), (7, 'H'), (2, 'H'), (9, 'C'), ('dama', 'H')]
        loser_hand = [(5, 'C'), (3, 'H'), (7, 'H'), (4, 'H'), ('valete', 'H')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_one_pair_must_win_higher_card(self):
        winner_hand = [(7, 'C'), (5, 'H'), (8, 'H'), (8, 'H'), (9, 'C')]
        loser_hand = [(2, 'C'), (5, 'H'), (7, 'H'), (9, 'C'), ('valete', 'H')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_two_pair_must_win_one_pair(self):
        winner_hand = [(3, 'C'), (3, 'H'), (8, 'C'), (7, 'H'), (8, 'H')]
        loser_hand = [(2, 'C'), (6, 'H'), (8, 'H'), (2, 'H'), ('as', 'H')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_toak_must_win_one_pair(self):
        winner_hand = [(4, 'H'), (5, 'H'), (8, 'H'), (8, 'H'), (8, 'C')]
        loser_hand = [(3, 'H'), (5, 'H'), (10, 'H'), (10, 'C'), ('as', 'C')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_foak_must_win_toak(self):
        winner_hand = [(4, 'H'), (8, 'H'), (8, 'C'), (8, 'H'), (8, 'C')]
        loser_hand = [(5, 'H'), (5, 'C'), (5, 'H'), (10, 'C'), ('as', 'H')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_straight_must_win_two_pair(self):
        winner_hand = [(4, 'H'), (5, 'C'), (6, 'H'), (7, 'H'), (8, 'C')]
        loser_hand = [(5, 'D'), (5, 'D'), ('as', 'C'), (10, 'H'), ('as', 'C')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_full_house_must_win_toak(self):
        winner_hand = [(4, 'S'), (6, 'C'), (6, 'C'), (4, 'C'), (6, 'D')]
        loser_hand = [('as', 'C'), (5, 'C'), ('as', 'S'), (2, 'D'), ('as', 'H')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')

    def test_flush_must_straight(self):
        winner_hand = [(4, 'H'), (6, 'H'), (3, 'H'), (8, 'H'), ('as', 'H')]
        loser_hand = [(3, 'C'), (4, 'H'), (5, 'H'), (6, 'H'), (7, 'C')]
        self.assertEqual(poker(winner_hand, loser_hand), 'Player_1')
        self.assertEqual(poker(loser_hand, winner_hand), 'Player_2')


unittest.main()
