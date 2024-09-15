import pygame
import sys
from basra import Basra
from card import Card, Deck

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARD_WIDTH = 60
CARD_HEIGHT = 90
MARGIN = 20

# Colors
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basra Card Game")

# Load card images
def load_card_images():
    images = {}
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    for suit in suits:
        for value in values:
            card_name = f"{value}_of_{suit}.png"
            images[f"{value} of {suit}"] = pygame.transform.scale(
                pygame.image.load(f"cards_png/{card_name.lower()}"), (CARD_WIDTH, CARD_HEIGHT)
            )
    return images

card_images = load_card_images()

def draw_hand(player, y_position):
    for i, card in enumerate(player.hand):
        card_rect = pygame.Rect(MARGIN + i * (CARD_WIDTH + MARGIN), y_position, CARD_WIDTH, CARD_HEIGHT)
        card_name = f"{card.value} of {card.suit}"
        screen.blit(card_images[card_name], card_rect)

        # Detect card click
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if card_rect.collidepoint(mouse_pos):
                return i  # Return the index of the clicked card
    return None

def draw_table(table_cards):
    for i, card in enumerate(table_cards):
        card_rect = pygame.Rect((SCREEN_WIDTH // 2) - (CARD_WIDTH // 2) + i * (CARD_WIDTH + MARGIN // 2), SCREEN_HEIGHT // 2 - CARD_HEIGHT // 2, CARD_WIDTH, CARD_HEIGHT)
        card_name = f"{card.value} of {card.suit}"
        screen.blit(card_images[card_name], card_rect)

def main():
    game = Basra("Player 1", "Player 2")

    running = True
    while running:
        screen.fill((0, 128, 0))  # Green background for the table

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw Player 1's hand at the bottom
        p1_card_index = draw_hand(game.players[0], SCREEN_HEIGHT - CARD_HEIGHT - MARGIN)

        # Draw Player 2's hand at the top
        p2_card_index = draw_hand(game.players[1], MARGIN)

        # Draw table cards in the center
        draw_table(game.table)

        if game.current_player == 0 and p1_card_index is not None:
            game.play_turn(p1_card_index)

        elif game.current_player == 1 and p2_card_index is not None:
            game.play_turn(p2_card_index)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()