# Write your blackjack game here.
import random
# Outline my classes
SUITS = ['♥️', '♣️', '♦️','♠️']
RANK_VALUES = {
    'K': 10,
    'Q': 10,
    'J': 10,
    'A': (11, 1),
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9, 
    10: 10,
}


class Game:
    # make a new deck of cards, which calls __init__() method
    def __init__(self):
        self.deck = Deck('Bicycle')
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()

    def deal(self):
        pass

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# example of building one card
queen_of_hearts = Card('♥️', 'Q', 10)
# print(f'{queen_of_hearts} is worth {queen_of_hearts.value}')
# build a whole deck


class Deck:
    def __init__(self, brand):
        self.cards = []
        self.brand = brand
        self.used = False
        for suit in SUITS:
            for rank_value in RANK_VALUES.items():
                new_card = Card(suit, rank_value[0], rank_value[1])
                self.cards.append(new_card)

    def __str__(self):
        return f'{self.brand} deck of {len(self.cards)} cards'

    def shuffle(self):
        random.shuffle(self.cards)



class Player:
    def __init__(self):
        self.hand = []


class Dealer:
    def __init__(self):
        self.hand = []