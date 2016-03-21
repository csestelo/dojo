import unittest
from stats import min_value, max_value, lenght, mean


class TestStats(unittest.TestCase):
    def test_min_value_must_return_negative_18(self):
        sample = [6, 3, 9, -3, 15, 23, -18, 28]
        self.assertEqual(min_value(sample), -18)

    def test_min_of_empty_list_must_return_None(self):
        self.assertIsNone(min_value([]))

    def test_max_value_must_return_28(self):
        sample = [6, 3, 9, -3, 15, 23, -18, 28]
        self.assertEqual(max_value(sample), 28)

    def test_max_of_empty_list_must_return_None(self):
        self.assertIsNone(max_value([]))

    def test_mean_must_return_20(self):
        sample = [15, 20, 15, 30]
        self.assertEqual(mean(sample), 20)

    def test_mean_must_return_17_5(self):
        sample = [15, 20]
        self.assertEqual(mean(sample), 17.5)

    def test_lenght_must_return_7(self):
        sample = [2, 6, 38, 34, 84, 33, 92]
        self.assertEqual(lenght(sample), 7)


unittest.main()
