from player import Player
from card import Card, Deck
import itertools

class Basra:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.table = []
        self.players = [Player(player1_name), Player(player2_name)]
        self.current_player = 0  # Index of the current player

        # Deal initial cards
        self.deal_initial_cards()

    def deal_initial_cards(self):
        for player in self.players:
            player.receive_cards(self.deck.deal_hand(4))
        self.table = self.deck.deal_ground()

    def play_turn(self, card_index):
        player = self.players[self.current_player]
        card = player.play_card(card_index)

        if card:
            captured_cards = self.check_capture(card)
            if captured_cards:
                player.capture_cards(captured_cards)
                if len(self.table) == 0 and card.value != 'Jack':
                    print(f"{player.name} made a Basra!")
                    player.score += 10  # Award 10 points for a Basra
            else:
                self.table.append(card)

            self.current_player = 1 - self.current_player  # Switch turns

            if all(len(player.hand) == 0 for player in self.players):
                self.deal_new_round()
        else:
            print("Invalid move. Try again.")

    def check_capture(self, card):
        captured = []

        # Jack captures all cards on the table
        if card.value == 'Jack':
            if self.table:
                captured = self.table[:]
                self.table = []
            else:
                self.table.append(card)
                
            if captured != []:
                captured.append(card)
            return captured

        # Capture cards that match the card's value
        captured = [c for c in self.table if c.value == card.value]

        # Only perform sum capture if the card is not a face card
        if card.value not in ['Jack', 'Queen', 'King']:
            numeric_cards_on_table = [c for c in self.table if c.value not in ['Jack', 'Queen', 'King']]
            card_value = self.get_card_value(card)
            table_values = [self.get_card_value(c) for c in numeric_cards_on_table]
            valid_combinations = []

            for r in range(2, len(table_values) + 1):
                for combo in itertools.combinations(numeric_cards_on_table, r):
                    if sum(self.get_card_value(c) for c in combo) == card_value:
                        valid_combinations.append(combo)

            valid_combinations.sort(key=lambda x: len(x), reverse=True)

            used_cards = set()
            for combo in valid_combinations:
                if all(c not in used_cards for c in combo):
                    captured.extend(combo)
                    used_cards.update(combo)

        self.table = [c for c in self.table if c not in captured]
        if captured != []:
            captured.append(card)
        return captured

    def get_card_value(self, card):
        if card.value.isdigit():
            return int(card.value)
        elif card.value == 'Ace':
            return 1
        elif card.value in ['Jack', 'Queen', 'King']:
            return None
        return 0
    
    def deal_new_round(self):
        if len(self.deck.cards) >= 8:
            for player in self.players:
                player.receive_cards(self.deck.deal_hand(4))
        else:
            self.end_game()

    def end_game(self):
        last_player = self.players[1 - self.current_player]
        last_player.capture_cards(self.table)

        for player in self.players:
            player.calculate_score()

        self.display_final_scores()

    def display_final_scores(self):
        for player in self.players:
            print(f"{player.name}'s final score: {player.score}")
        winner = max(self.players, key=lambda p: p.score)
        print(f"{winner.name} wins the game!")
