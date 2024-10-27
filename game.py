from random import shuffle

# Suit and rank definitions for card creation
SUITES = 'Hearts Diamonds Spades Clubs'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """Represents a deck of 52 playing cards."""

    def __init__(self):
        self.all_cards = [(s, r) for s in SUITES for r in RANKS]
        print("New deck created in order.")

    def shuffle(self):
        shuffle(self.all_cards)
        print("Deck shuffled.")

    def split_in_half(self):
        return self.all_cards[:26], self.all_cards[26:]

class Hand:
    """Represents a player's hand of cards."""

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"Hand contains {len(self.cards)} cards."

    def add(self, new_cards):
        """Adds new cards to the hand."""
        self.cards.extend(new_cards)

    def remove_card(self):
        """Removes and returns the top card from the hand."""
        return self.cards.pop() if self.cards else None

class Player:
    """Represents a player with a hand of cards."""

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        """Plays the top card from the player's hand."""
        drawn_card = self.hand.remove_card()
        if drawn_card:
            print(f"{self.name} plays: {drawn_card}")
        return drawn_card

    def remove_war_cards(self):
        """Removes three cards from the player's hand for 'war'."""
        return [self.hand.remove_card() for _ in range(3) if self.hand.cards]

    def has_cards_left(self):
        """Checks if the player still has cards."""
        return len(self.hand.cards) > 0

def compare_cards(card1, card2):
    """Compares the ranks of two cards."""
    return RANKS.index(card1[1]) - RANKS.index(card2[1])

def main():
    print("Welcome to War! Let's start the game...")

    # Create and shuffle deck, then split in half
    deck = Deck()
    deck.shuffle()
    half1, half2 = deck.split_in_half()

    # Create players
    computer = Player("Computer", Hand(half1))
    player_name = input("Enter your name: ")
    user = Player(player_name, Hand(half2))

    # Game statistics
    round_count = 0
    war_count = 0

    # Main game loop
    while user.has_cards_left() and computer.has_cards_left():
        round_count += 1
        print(f"Round {round_count} begins!")
        print(f"{user.name}: {len(user.hand.cards)} cards | {computer.name}: {len(computer.hand.cards)} cards")

        # Cards played this round
        table_cards = []
        user_card = user.play_card()
        comp_card = computer.play_card()

        # Add played cards to the table
        table_cards.extend([user_card, comp_card])

        # Check if 'war' is required
        if user_card[1] == comp_card[1]:
            war_count += 1
            print("War declared! Each player places 3 cards face down and 1 face up.")

            # Collect war cards from each player
            table_cards.extend(user.remove_war_cards())
            table_cards.extend(computer.remove_war_cards())

            # Draw war deciding cards
            user_card = user.play_card()
            comp_card = computer.play_card()

            # Add the deciding cards to the table
            table_cards.extend([user_card, comp_card])

        # Determine who wins the round
        if compare_cards(comp_card, user_card) > 0:
            print(f"{computer.name} wins the round.")
            computer.hand.add(table_cards)
        else:
            print(f"{user.name} wins the round.")
            user.hand.add(table_cards)

    # End of game summary
    winner = user if user.has_cards_left() else computer
    print(f"Game Over! {winner.name} wins after {round_count} rounds.")
    print(f"Wars occurred {war_count} times.")

if __name__ == "__main__":
    main()
