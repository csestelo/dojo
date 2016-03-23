import unittest
from happy_numbers import happy_number2 as happy_number

class TestHappyNumbers(unittest.TestCase):
    def test_number_1_must_return_true(self):
        self.assertTrue(happy_number(1))

    def test_number_10_must_return_true(self):
        self.assertTrue(happy_number(10))

    def test_number_13_must_return_true(self):
        self.assertTrue(happy_number(13))

    def test_number_6_must_return_false(self):
        self.assertFalse(happy_number(6))

    def test_number_0_must_return_false(self):
        self.assertFalse(happy_number(0))


unittest.main()
