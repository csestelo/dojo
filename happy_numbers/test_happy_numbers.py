import unittest
from happy_numbers import happy_number

class TestHappyNumbers(unittest.TestCase):
    def test_number_1_must_return_true(self):
        self.assertTrue(happy_number(1))

    def test_number_10_must_return_true(self):
        self.assertTrue(happy_number(10))

    def test_number_13_must_return_true(self):
        self.assertTrue(happy_number(13))


unittest.main()
