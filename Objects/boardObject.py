# Author Michelle Simoni
# creation date: 04.18.2022

from deckObject import Deck
from userObject import User


class board:

    def __init__(self,computer_user: User,user: User,deck: Deck):
        self.deck = deck
        self.computer_user = computer_user
        self.user = user
        self.discard_stack = []


