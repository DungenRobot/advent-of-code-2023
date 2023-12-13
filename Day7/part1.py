
card_values = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10,
    '9' : 9, 
    '8' : 8,
    '7' : 7, 
    '6' : 6, 
    '5' : 5, 
    '4' : 4, 
    '3' : 3, 
    '2' : 2, 
}

def raw_score(hand: str):
    """
    Takes in a hand string. Returns the raw hand score.
    """
    score = 0

    for i, card in enumerate(hand):
        base = 13
        power = 4 - i

        value = card_values[card] - 2

        score += pow(base, power) * value

    return score


def type_score(hand_array: list):
    """
    Takes in a sorted hand array of [quantity, card].
    Returns the score of the type of hand that it is
    """
    match hand_array[0][0]:
        #five of a kind
        case 5: return 6
        #four of a kind
        case 4: return 5
        case 3:
            #full house
            if hand_array[1][0] == 2: return 4
            #three of a kind
            else: return 3
        case 2:
            #two pair
            if hand_array[1][0] == 2: return 2
            #one pair
            else: return 1
        #high card
        case _: return 0


def score_hand(hand: str):

    hand_dict = {}

    for card in hand:
        hand_dict[card] = 1 + hand_dict.get(card, 0)


    #creates a list where every element is a list containing [amount_in_hand, card]
    hand_array = [[hand_dict[card], card] for card in hand_dict]

    hand_array.sort(reverse=True)

    score = raw_score(hand) + (type_score(hand_array) * 1_000_000)

    return score


def main():

    all_hands = []

    with open('input.txt') as f:
        for line in f.readlines():
            line.strip()

            hand, bid = line.split(' ')
            bid = int(bid)

            score = score_hand(hand)

            all_hands.append([score, bid])
    
    all_hands.sort()

    total = 0

    for i in range(len(all_hands)):
        bid = all_hands[i][1]
        place = i + 1

        total += bid * place
    
    print(total)


if __name__ == "__main__":
    main()
