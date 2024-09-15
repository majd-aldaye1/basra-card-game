# Basra Card Game

Basra is a popular card game in the Middle East, particularly in Egypt and Turkey. This project is a digital version of the Basra card game implemented using Python and Pygame, allowing two players to play against each other.


## About the Project

The Basra card game is a traditional two-player game where the goal is to capture cards from the table that match the value of a card played from your hand. This project allows you to play Basra on your computer with a simple graphical interface built using Pygame.

## Gameplay

### Game Rules

1. **Objective**: The objective of Basra is to capture cards from the table and accumulate the highest score.
2. **Setup**: The game is played with a standard 52-card deck. At the start, four cards are dealt to each player, and four cards are placed face-up on the table.
3. **Playing a Card**: On their turn, a player plays a card from their hand. The card can capture:
   - **Matching Cards**: Any card on the table that matches the value of the played card.
   - **Sum Combinations**: A combination of cards on the table that add up to the value of the played card.
   - **Jacks**: The Jack card captures all cards currently on the table.
4. **Scoring**: Points are awarded based on captured cards:
   - 1 point per Jack or Ace.
   - 2 points for the 2 of Clubs.
   - 3 points for the 10 of Diamonds.
   - 3 bonus points if a player captures 27 or more cards.
   - 10 points for a Basra (clearing the table with a non-Jack card).
5. **Game End**: The game ends when all cards have been played, and the player with the highest score wins.

## Screenshot of the Basra game interface

![Basra Card Game](https://github.com/majd-aldaye1/basra-card-game/blob/main/game_interface.png) 

## Built With

This project was built using the following technologies:

- **Python** - The main programming language.
- **Pygame** - A set of Python modules designed for writing video games.
