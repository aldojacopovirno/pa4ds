# Assignment
# Build a standard deck with four suits and thirteen ranks in each suit. Produce
# a shuffled deck containing every original card exactly once, then display the
# shuffled order.
#
# Solution

# Import an integer generator whose two bounds are both included. We will use
# it to choose a valid position in the deck on each random draw.
from random import randint

# Describe the suits and ranks separately so we can combine every suit with
# all thirteen ranks. The same rank in a different suit is a different card.
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

# Start with no cards and build the full deck before shuffling it.
deck = []

# The outer loop picks a suit; the inner loop visits every rank for that suit.
# It starts again for each new suit, giving 4 * 13 = 52 distinct cards.
for suit in suits:
    for value in values:
        # Store one card as a (rank, suit) tuple, then append that single item.
        # The tuple keeps both parts together when a card is selected later.
        deck.append((value, suit))


# Define a function so the same process can shuffle a supplied deck. Build a
# new list in shuffled order while keeping the input deck unchanged.
def shuffle(deck):
    # Record chosen positions to recognise a repeated draw. shuffled_deck
    # holds the cards accepted so far, in the order they were first drawn.
    used_indices = []
    shuffled_deck = []

    # Keep drawing until the result contains as many cards as the original.
    # An empty input skips this loop and returns an empty list immediately.
    while len(shuffled_deck) < len(deck):
        # Python indices start at 0, and the final index is len(deck) - 1.
        # Since randint includes both bounds, every generated index is valid.
        i = randint(0, len(deck) - 1)

        # in produces a Boolean: True when we already used this position.
        if i in used_indices:
            # Skip both append operations and try another draw. continue ends
            # this iteration, then the while condition is checked again.
            continue

        # A new position contributes exactly one card. Record it before adding
        # the card so future draws of the same index will be rejected.
        used_indices.append(i)
        shuffled_deck.append(deck[i])

    # Each accepted draw adds one unused position, so reaching the target size
    # means every original position has been included exactly once.
    # Repeated draws make the total number of attempts variable, and become
    # more likely as the used-index list grows.
    # Return only after the loop so the caller receives the completed shuffle.
    return shuffled_deck

# Pass the complete deck to the function, store the returned list, and display
# it. The cards remain the same; their order is determined by the random draws.
shuffled_deck = shuffle(deck)
print(shuffled_deck)
