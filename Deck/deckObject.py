# Author Michelle Simoni
# creation date: 04.18.2022
import random

# Globals
DECK_POINT_DICT = {
    'A': 30,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 1,
    '9': 1,
    '8': 1,
    '7': 1,
    '6': 1,
    '5': 1,
    '4': 1,
    '3': 1,
    '2': 1,
}

SUITE_LIST = [
    'heart',
    'diamond',
    'clubs',
    'spades'
]


class Deck:

    def __init__(self):
        self.deck = self.shuffle_deck(self.create_shuffled_deck())

    def create_shuffled_deck(self):
        sorted_deck = []
        suite_position = 0
        for suite in SUITE_LIST:
            for key in DECK_POINT_DICT:
                card = (suite, key)
                sorted_deck.append(card)
        return sorted_deck

    def shuffle_deck(self, deck):
        shuffled_deck = []
        for i in range(52):
            inLoop = True
            while (inLoop):
                loc = random.randint(0, 52)
                card = deck[loc]
                if card == 0:
                    loc = random.randint(0, 52)
                else:
                    shuffled_deck.append(card)
                    deck[loc] = 0
                    inLoop = False
        return shuffled_deck

    def pull_card(self):
        card = self.deck
        return card

    def put_card_back(self,card):
        self.deck.append(card)