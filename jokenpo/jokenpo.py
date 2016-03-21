PAPER = 3
ROCK = 2
SCISSORS = 1

def jokenpo(player1, player2):
    if player1 == player2:
        return None
    elif {PAPER, SCISSORS} == {player1, player2}:
        return player1 < player2
    return player1 > player2


def jokenpo2(p1, p2):
    rank = [PAPER, ROCK, SCISSORS]
    if p1 == p2:
        return None
    elif {PAPER, SCISSORS} == {p1, p2}:
        return rank.index(p1) > rank.index(p2)
    else:
        return rank.index(p1) < rank.index(p2)
