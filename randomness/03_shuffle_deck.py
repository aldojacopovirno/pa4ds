# Assignment
# Build a standard deck with four suits and thirteen ranks in each suit. Produce
# a shuffled deck containing every original card exactly once, then display the
# shuffled order.
#
# Solution

from random import randint

# The used-index list prevents a card from being selected twice.
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:
    for value in values:
        deck.append((value, suit))


def shuffle(deck):
    used_indices = []
    shuffled_deck = []
    while len(shuffled_deck) < len(deck):
        i = randint(0, len(deck) - 1)
        if i in used_indices:
            continue
        used_indices.append(i)
        shuffled_deck.append(deck[i])

    return shuffled_deck

shuffled_deck = shuffle(deck)
print(shuffled_deck)
