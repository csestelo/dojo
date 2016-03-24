import unittest
from linebreak import linebreak3 as linebreak

class Linebreak(unittest.TestCase):
    def test_empty_text_must_return_empty_string(self):
        self.assertEqual(linebreak('', 3), '')

    def test_linebreak_in_the_middle(self):
        self.assertEqual(linebreak('Green house.', 6),
                        'Green\nhouse.')

    def test_linebreak_is_a_blank_space(self):
        self.assertEqual(linebreak('A ', 1), 'A')

    def test_linebreak_in_the_middle_of_the_word(self):
        self.assertEqual(linebreak('casa brasileira de literatura', 17),
                        'casa brasileira\nde literatura')

    def test_last_line_is_smaller_than_limit(self):
        self.assertEqual(linebreak('casa brasileira', 12),
                        'casa\nbrasileira')

    def test_last_line_is_too_long(self):
        self.assertRaises(ValueError, linebreak, 'casa brasileira', 8)

unittest.main()
