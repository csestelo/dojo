from collections import defaultdict


HOLE_LETTERS = {'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
                'a': 1, 'b': 1, 'd': 1, 'e': 1, 'g': 1, 'o': 1, 'p': 1,
                'q': 1,}

HOLE_LETTERS_DEFAULT = defaultdict(lambda: 0, {
    'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
    'a': 1, 'b': 1, 'd': 1, 'e': 1, 'g': 1, 'o': 1, 'p': 1, 'q': 1,})

def hole_numbers(letters):
    total_hole_numbers = 0
    for letter in letters:
        if letter in hole_letters:
            total_hole_numbers = HOLE_LETTERS[letter] + total_hole_numbers
    return total_hole_numbers


def hole_numbers2(letters):
    total_hole_numbers = 0
    for letter in letters:
        if letter in hole_letters:
            total_hole_numbers += HOLE_LETTERS[letter]
    return total_hole_numbers

def hole_numbers3(letters):
    total_hole_numbers = 0
    for letter in letters:
        total_hole_numbers += HOLE_LETTERS.get(letter, 0)
    return total_hole_numbers

def hole_numbers4(letters):
    total_hole_numbers = 0
        for letter in letters:
            total_hole_numbers += HOLE_LETTERS_DEFAULT[letter]
    return total_hole_numbers


def hole_numbers5(letters):
    return sum(map(lambda letter: HOLE_LETTERS.get(letter, 0),
                   letters))


def hole_numbers6(letters):
    return sum([HOLE_LETTERS.get(letter, 0) for letter in letters])
