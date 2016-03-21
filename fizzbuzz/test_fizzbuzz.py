import unittest
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_one_must_return_one(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_3_must_return_fizz(self):
        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_6_must_return_fizz(self):
        self.assertEqual(fizzbuzz(6), 'fizz')

    def test_5_must_return_buzz(self):
        self.assertEqual(fizzbuzz(5), 'buzz')

    def test_divisible_by_5_must_return_buzz(self):
        self.assertEqual(fizzbuzz(20), 'buzz')

    def test_15_must_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')

unittest.main()
