# This program uses deck class to deal a 5 card Poker hand,
# lets the user choose which cards to replace,
# draws new cards from the deck, and displays final hand.

import random

# card class
class Card:

    # initializing card
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # converting card to text
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# deck class
class Deck:

    # creating deck
    def __init__(self):
        self.cards = []
        self.build_deck()

    # building full deck
    def build_deck(self):
        RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8",
                 "9", "10", "Jack", "Queen", "King"]

        SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]

        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))

    # shuffling deck
    def shuffle(self):
        random.shuffle(self.cards)

    # dealing a card
    def deal_card(self):
        return self.cards.pop()


# dealing 5 card hand
def deal_hand(deck):
    hand = []

    for _ in range(5):
        hand.append(deck.deal_card())

    return hand


# printing hand
def print_hand(hand):
    print("\nYour current hand:")

    for index, card in enumerate(hand, start=1):
        print(f"{index}: {card}")


# drawing new cards
def draw_new_cards(hand, deck):

    # asking user which cards to replace
    user_input = input(
        "\nEnter the card numbers to replace (example: 1, 3, 5) "
        "or press Enter to keep all cards: "
    )

    # user keeps all cards
    if user_input.strip() == "":
        return hand

    # turning input into positions
    positions = [int(num.strip()) for num in user_input.split(",")]

    # replacing selected cards
    for pos in positions:
        hand[pos - 1] = deck.deal_card()

    return hand


# main function
def main():

    # creating and shuffling deck
    deck = Deck()
    deck.shuffle()

    # dealing initial hand
    hand = deal_hand(deck)

    # showing starting hand
    print_hand(hand)

    # drawing new cards
    hand = draw_new_cards(hand, deck)

    # showing final hand
    print("\nYour final hand:")
    print_hand(hand)


# calling main
main()
