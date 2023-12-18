#This module makes a card object and also a deck of cards

#Creating a card object that has traits like suit, and rank
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


#Creating a deck class, which instantiates a bunch of Cards
#Will have class functions to draw and shuffle a card
class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    #Creates a deck of cards
    def __init__(self):
        self.cards = [Card(r, s) for r in self.ranks for s in self.suits]

    #Shuffles the cards (unnecessary since deal randomly gives cards)
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, number):
        import random

        selected = [Card] * number

        for i in range(number):
            selected[i] = self.cards.pop(random.randint(0,len(self.cards)-1))

        return selected

    def reset(self):
        self.cards = [Card(r, s) for r in self.ranks for s in self.suits]