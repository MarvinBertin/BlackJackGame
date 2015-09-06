import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.hand)
