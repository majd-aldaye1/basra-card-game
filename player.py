from card import Card, Deck

# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.captured = []
        self.score = 0

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        return None

    def capture_cards(self, cards):
        self.captured.extend(cards)

    def calculate_score(self):
        self.score += sum(1 for card in self.captured if card.value in ['Jack', 'Ace'])
        print(25, sum(1 for card in self.captured if card.value in ['Jack', 'Ace']))
        self.score += sum(2 for card in self.captured if card.suit == 'Clubs' and card.value == '2')
        print(360, sum(2 for card in self.captured if card.suit == 'Clubs' and card.value == '2'))
        self.score += sum(3 for card in self.captured if card.suit == 'Diamonds' and card.value == '10')
        print(365, sum(3 for card in self.captured if card.suit == 'Diamonds' and card.value == '10'))
        print(len(self.captured))

        if len(self.captured) >= 27:
            self.score += 3

    def __repr__(self):
        return f"{self.name}: Hand: {self.hand}, Captured: {self.captured_cards}, Score: {self.score}"
