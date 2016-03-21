import unittest
from holeintheletters import hole_numbers


class TestHoleLetters(unittest.TestCase):
    def test_letter_a_must_return_1(self):
        self.assertEqual(hole_numbers('a'), 1)

    def test_word_ae_must_return_2(self):
        self.assertEqual(hole_numbers('ae'), 2)

    def test_word_house_must_return_2(self):
        self.assertEqual(hole_numbers('house'), 2)


unittest.main()
