from poker_const import RANKS, DECK

def poker(hand_1, hand_2):
    if royal_flush(hand_1):
        hand_1 = RANKS.ROYAL_FLUSH
    elif same_suits(hand_1):
        hand_1 = RANKS.FLUSH
    else:
        hand_1 = wich_hand(card_value(hand_1))

    if royal_flush(hand_2):
        hand_2 = RANKS.ROYAL_FLUSH
    elif same_suits(hand_2):
        hand_2 = RANKS.FLUSH
    else:
        hand_2 = wich_hand(card_value(hand_2))
        
    if hand_1 > hand_2:
        return 'Player_1'
    else:
        return 'Player_2'

def same_suits(hand):
    return len(set(suits(hand))) == 1

def card_value(hand):
    return [card[0] for card in hand]

def suits(hand):
    return [card[1] for card in hand]

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

def royal_flush(hand):
    sorted_hand = sorted(normalize_value(card_value(hand)))
    check = range(sorted_hand[0], sorted_hand[0] + 5)
    return sorted_hand == check and same_suits(hand) and check[4] == 14

def straight(hand):
    sorted_hand = sorted(normalize_value(hand))
    check = range(sorted_hand[0], sorted_hand[0] + 5)
    return sorted_hand == check

def wich_hand(hand):
    count = {}
    for card in normalize_value(hand):
        if card in count:
            count[card] += 1
            #assim se cria uma nova chave/valor em um dicionario>
        else:
            count[card] = 1
    for checked_card in count.values():
        if checked_card == 4:
            return RANKS.FOUR_OF_A_KIND
        if straight(hand):
            return RANKS.STRAIGHT
        if checked_card == 3 or checked_card == 2:
            full_house = []
            for recheck in count.values():
                if recheck == 2 or recheck == 3:
                    full_house.append(recheck)
            if full_house == [3, 2] or full_house == [2, 3]:
                return RANKS.FULL_HOUSE
        if checked_card == 3:
            return RANKS.THREE_OF_A_KIND
        if checked_card == 2:
            two_pair = []
            for checked_card in count.values():
                if checked_card == 2:
                    two_pair.append(checked_card)
            if len(two_pair) == 2:
                return RANKS.TWO_PAIR
            else:
                return RANKS.ONE_PAIR
    else:
        return higher_card(hand)
