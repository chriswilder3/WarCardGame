# War Card Game in Python

A console-based Python implementation of the classic card game **War**. This project allows you to play against the computer with a shuffled deck, engaging in rounds to draw higher-ranking cards and win all 52 cards in the deck. "Wars" are declared when both players draw a card of the same rank, adding extra tension to the gameplay.

## Features

- **Deck and Card Mechanics**:
  - Create, shuffle, and split a standard deck of 52 playing cards using a `Deck` class.
  - Manage each player's hand of cards using a `Hand` class.
  - Execute player actions, including drawing cards and handling "war" scenarios, with a `Player` class.

- **Gameplay**:
  - Players draw cards each round; the player with the higher card wins and collects the cards.
  - When both players draw a card of the same rank, a "war" is triggered, where each player places three cards face down and draws a fourth to decide the round.
  - Game continues until one player has won all 52 cards.

- **Statistics**:
  - Tracks the total rounds played and the number of "wars" encountered throughout the game.

## Getting Started

### Prerequisites

- Python 3.x

No additional libraries are required; the game runs in a standard Python environment.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/war-card-game.git
   cd war-card-game
