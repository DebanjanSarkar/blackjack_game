# Blackjack Console Game - made in Python

## Overview

Welcome to the Blackjack Console Game! This project implements a simple console-based version of the popular card game Blackjack (also known as 21). Players can engage in rounds of Blackjack against a computerized dealer and experience the thrill of making strategic decisions to beat the house.

## Game Rules

### Objective

The goal of Blackjack is to have a hand value closer to 21 than the dealer's hand without exceeding 21.

### Card Values

- Number cards (2 through 10) are worth their face value.
- Face cards (Jack, Queen, King) are each worth 10 points.
- Aces can be worth either 1 point or 11 points, depending on which value benefits the hand more.

### Gameplay

1. Players are dealt two cards, and one of the dealer's cards is initially hidden.
2. Players can choose to "hit" (take another card) or "stand" (keep their current hand).
3. The dealer must hit until their hand is worth at least 17 points and must stand once their hand is 17 or higher.
4. The round ends when the player or dealer busts (exceeds 21) or when both have completed their turns.

### Winning

- Players win if their hand is closer to 21 than the dealer's hand without going over 21.
- If a player's hand exceeds 21, they lose (bust), regardless of the dealer's hand.
- If the dealer busts, all remaining players win.

## Project Structure

### Files

- **blackjack.py:** The main file containing the game logic and user interaction.
- **cards_util_module.py:** A utility module providing functions for card-related operations.
- **README.md:** This documentation file providing an overview of the project.

### Code Structure

- **Game Initialization:**
  - The game starts with a welcome message and an option for the player to start a new round.
  - Player and computer hands are initialized with two random cards each.

- **User Interaction:**
  - Players are prompted to decide whether to draw another card or pass.
  - Input validation ensures that only 'y' (yes) or 'n' (no) is accepted.

- **Card Handling:**
  - The utility module (`cards_util_module.py`) contains functions to get a random card, determine card values, and calculate the total value of a hand.

- **Game Logic:**
  - The main file (`blackjack.py`) contains the core game logic, including determining winners, handling busts, and managing the flow of the game.

- **Outcome Display:**
  - ASCII art is used to display visual outcomes for winning, losing, or tying.

### How to Play

1. Clone the repository to your local machine.
2. Run the `blackjack.py` file using a Python interpreter.
3. Follow the on-screen instructions to play rounds of Blackjack against the computer dealer.


## Author

- **Debanjan Sarkar**

Feel free to explore, enjoy, and contribute to this Blackjack Console Game project! If you have any questions or suggestions, please don't hesitate to contact me. Happy gaming!
