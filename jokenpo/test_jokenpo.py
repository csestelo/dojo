import unittest
from jokenpo import jokenpo, jokenpo2, PAPER, ROCK, SCISSORS

class BaseJokenpo(object):
    def test_paper_beats_rock(self):
        self.assertEqual(self.jokenpo(PAPER, ROCK), True)
        self.assertEqual(self.jokenpo(ROCK, PAPER), False)

    def test_scissors_beats_paper(self):
        self.assertEqual(self.jokenpo(SCISSORS, PAPER), True)
        self.assertEqual(self.jokenpo(PAPER, SCISSORS), False)

    def test_rock_beats_scissors(self):
        self.assertEqual(self.jokenpo(ROCK, SCISSORS), True)
        self.assertEqual(self.jokenpo(SCISSORS, ROCK), False)

    def test_draw(self):
        self.assertEqual(self.jokenpo(ROCK, ROCK), None)
        self.assertEqual(self.jokenpo(PAPER, PAPER), None)
        self.assertEqual(self.jokenpo(SCISSORS, SCISSORS), None)


class TestJokenpo1(BaseJokenpo, unittest.TestCase):
    jokenpo = staticmethod(jokenpo)


class TestJokenpo2(BaseJokenpo, unittest.TestCase):
    jokenpo = staticmethod(jokenpo2)


unittest.main()
