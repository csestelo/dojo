import unittest
from leap_year import leap_year


class TestLeapYear(unittest.TestCase):
    def test_1993_must_return_false(self):
        self.assertFalse(leap_year(1993))

    def test_1994_must_return_false(self):
        self.assertFalse(leap_year(1994))

    def test_92_must_return_true(self):
        self.assertTrue(leap_year(92))

    def test_100_must_return_false(self):
        self.assertFalse(leap_year(100))

    def test_800_must_return_true(self):
        self.assertTrue(leap_year(800))

unittest.main()
