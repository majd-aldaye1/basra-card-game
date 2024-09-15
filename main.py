from basra import Basra

def play_game():
    game = Basra("Player 1", "Player 2")

    while True:
        current_player = game.players[game.current_player]
        print(f"\n{current_player.name}'s turn")
        print("Your hand:", current_player.hand)
        print("Table:", game.table)

        # Ask the player to choose a card to play
        card_index = int(input(f"Choose a card to play (0-{len(current_player.hand) - 1}): "))

        game.play_turn(card_index)

        # Check if the game has ended
        if len(game.deck.cards) == 0 and all(len(player.hand) == 0 for player in game.players):
            break

if __name__ == "__main__":
    play_game()
