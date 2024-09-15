import random

# Card Class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

# Deck Class
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        return None

    def deal_hand(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

    def deal_ground(self):
        ground_cards = [self.cards.pop() for _ in range(4)]
        for card in ground_cards:
            if card.value == 'Jack':
                self.cards.insert(0, card)
                ground_cards.append(self.cards.pop())
        return ground_cards