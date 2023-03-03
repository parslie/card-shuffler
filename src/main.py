#!/bin/python
from argparse import ArgumentParser

parser = ArgumentParser('card-shuffler')
parser.add_argument('card_count', type=int, help='the amount of cards to shuffle')


def init_deck(card_count) -> list[int]:
    return [x for x in range(card_count)]


def alternating_suffle(card_count):
    orig_deck = init_deck(card_count)
    curr_deck = orig_deck.copy()

    shuffle_count = 0

    while shuffle_count == 0 or curr_deck != orig_deck:
        shuffle_count += 1
        
        new_deck = []
        for i, card in enumerate(curr_deck):
            if i % 2 == 0:
                new_deck.append(card)
            else:
                new_deck.insert(0, card)
        curr_deck = new_deck
        
    print(f'{shuffle_count} cycles needed to return to original order')
    print(f'1 cycle needed to be maximally shuffled')  # Experiments showed that only 1 cycle was needed


if __name__ == '__main__':
    args = parser.parse_args()
    alternating_suffle(args.card_count)