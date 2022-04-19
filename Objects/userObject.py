# Author Michelle Simoni
# creation date: 04.18.2022

from deckObject import Deck


class User:

    def __init__(self, hand_limit=10):
        self.hand_limit = hand_limit
        self.hand = []
        self.score = 0

    def fill_hand(self, deck: Deck):
        if len(self.hand) == self.hand_limit:
            return
        else:
            while len(self.hand) != self.hand_limit:
                self.hand.append(deck.pull_card())
        return
