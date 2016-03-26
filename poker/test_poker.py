import unittest
from poker import poker, normalize_value

DECK = {'valete': 11, 'dama': 12, 'rei': 13, 'as': 14}


class TestPoker(unittest.TestCase):
    def test_a_higher_number_card_must_win(self):
        self.assertEqual(poker([4, 5, 7, 2, 8],
                        [3, 2, 8, 5, 10]), 'Player_2')

    def test_a_higher_card_in_hand_must_win(self):
        self.assertEqual(poker([3, 7, 2, 9, 'dama'],
                        [5, 3, 7, 4, 'valete']), 'Player_1')

    def test_one_pair_must_win_higher_card(self):
        self.assertEqual(poker([7, 5, 8, 8, 9],
                        [2, 5, 7, 9, 'valete']), 'Player_1')

    # def test_two_pair_must_win_op_and_hc(self):
    #     self.assertEqual(poker([]))

    def test_toak_must_win_one_pair(self):
        self.assertEqual(poker([4, 5, 8, 8, 8],
                        [3, 5, 10, 10, 'as']), 'Player_1')

    def test_foak_must_win_toak(self):
        self.assertEqual(poker([4, 8, 8, 8, 8],
                        ['as', 5, 'as', 10, 'as']), 'Player_1')



unittest.main()
