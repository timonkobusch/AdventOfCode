from functools import cmp_to_key
from collections import Counter


def p1(lines):
    def get_rank(card):
        count = sorted(Counter(card).values())
        rank = 1
        if count[-1] == 5: rank = 7
        elif count[-1] == 4: rank = 6
        elif count[-1] == 3 and count[-2] == 2: rank = 5
        elif count[-1] == 3: rank = 4
        elif count[-1] == 2 and count[-2] == 2: rank = 3
        elif count[-1] == 2: rank = 2
        return rank

    def compare(a, b):
        symbols = '23456789TJQKA'
        type_a = get_rank(a[0])
        type_b = get_rank(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (symbols.index(card_a) > symbols.index(card_b))
            return 1 if a_wins else -1



    cards = []
    for line in lines:
        card, bid = line.split()
        cards.append([card, bid])
    cards.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(cards, start=1):
        total += rank * int(bid)
    return total


def p2(lines):


    def get_rank(card):
        jokers = card.count("J")
        card = card.replace('J', '')
        counts = sorted(Counter(card).values(), reverse=True)
        if not counts:
            counts = [0]
        if counts[0] + jokers == 5:
            return 6
        if counts[0] + jokers == 4:
            return 5
        if counts[0] + jokers == 3 and counts[1] == 2:
            return 4
        if counts[0] + jokers == 3:
            return 3
        if counts[0] == 2 and (jokers or counts[1] == 2):
            return 2
        if counts[0] == 2 or jokers:
            return 1
        return 0

    def compare(a, b):
        symbols = '23456789TJQKA'
        type_a = get_rank(a[0])
        type_b = get_rank(b[0])
        if type_a > type_b:
            return 1
        if type_a < type_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (symbols.index(card_a) > symbols.index(card_b))
            return 1 if a_wins else -1

    cards = []
    for line in lines:
        card, bid = line.split()
        cards.append([card, bid])
    cards.sort(key=cmp_to_key(compare))
    total = 0
    for rank, (_, bid) in enumerate(cards, start=1):
        total += rank * int(bid)
    return total