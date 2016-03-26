DECK = {'valete': 11, 'dama': 12, 'rei': 13, 'as': 14}
#one_pair = 15 two_pair = 16 three_of_a_kind = 17 straight = 18
#flush = 19 full_house = 20 four_of_a_kind = 21 straight_flush = 22
#royal_flush = 23

def poker(hand_1, hand_2):
    if one_pair(hand_1) > one_pair(hand_2):
        return 'Player_1'
    else:
        return 'Player_2'

def normalize_value(hand):
    final_hand = []
    for card in hand:
        if card in DECK:
            final_hand.append(DECK[card])
        else:
            final_hand.append(card)
    return final_hand

def higher_card(hand):
    return max(normalize_value(hand))

def one_pair(hand):
    count = {}
    for card in normalize_value(hand):
        # val = count[card].values()
        if card in count:
            count[card] += 1
        else:
#assim se cria uma nova chave/valor em um dicionario>
            count[card] = 1
    for checked_card in count.values():
        if checked_card == 4:
            return 21
        if checked_card == 3:
            return 17
        if checked_card == 2:
            return 15
    else:
        return higher_card(hand)
