from itertools import chain

from twenty_twenty_one.day_four.call_numbers import call_numbers

puzzle_input = open('input.txt', 'r')
bingo_cards = []
card = []

def _check_win(bingo_card: list):
    # check horizontal
    for line in bingo_card:
        if all(v == '100' for v in line):
            # print(f'WINNER: {bingo_card}')
            return True

    # check vertical
    for a, b, c, d, e in zip(*bingo_card):
        if all(v == '99' for v in [a, b, c, d, e]):
            # print(f'WINNER: {bingo_card}')
            return True

    return False

for line in puzzle_input.readlines():
    if line == '\n':
        bingo_cards.append(card)
        card = []
    else:
        card.append(line.strip().split())
# print(len(bingo_cards))

for number in call_numbers:
    for card_index, bingo_card in enumerate(bingo_cards):
        for line in bingo_card:
            for i, num in enumerate(line):
                if int(num) == number:
                    line[i] = '100'
        if _check_win(bingo_card):
            unmarked_numbers = [[x for x in value if x != '100'] for value in bingo_card]
            unmarked_numbers_total = 0
            for group in unmarked_numbers:
                unmarked_numbers_total += sum(int(x) for x in group)

            del bingo_cards[card_index]
            print(f'UNMARKED_NUMBERS_TOTAL: {unmarked_numbers_total}')
            print(f'WINNING_NUMBER: {number}')
            print(unmarked_numbers_total * number)

# print(len(bingo_cards))


# from itertools import chain
# import sys
#
# numbers, *data = open('input.txt', 'r').read().strip().split("\n\n")
#
# boards = []
# for board in data:
#     # fmt:off
#     rows = [
#         [int(x) for x in row.split()]
#         for row in board.split("\n")
#     ]
#     # fmt:on
#     boards.append([set(line) for line in chain(rows, zip(*rows))])
#
# drawn, remaining = set(), set(range(len(boards)))
#
# for number in map(int, numbers.split(",")):
#     drawn.add(number)
#
#     for i in set(remaining):
#         if any(line <= drawn for line in boards[i]):
#             remaining.remove(i)
#
#             if len(remaining) == len(boards) - 1 or not remaining:
#                 print(number * sum(set.union(*boards[i]) - drawn))