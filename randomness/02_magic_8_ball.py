# Assignment
# Create a list of possible Magic 8-Ball responses. Ask the user a question,
# choose one response at random, and print it. The random choice must always be
# a valid item from the response list.
#
# Solution

# Import randint() so we can randomly choose an integer to use as a list index.
from random import randint

# Store the possible replies in a nonempty list so there is always a response
# to choose. Each reply has an index, starting at 0 for the first one.
answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy; try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

# Ask a question for the game interaction. input() keeps it as text; the reply
# is selected independently of the question's content.
question = input("Ask the magic 8-ball a question: ")

# len(answers) counts the replies, so the final valid index is one less than
# this count. This limit adjusts if replies are added or removed, as long as
# the list still contains at least one reply.
# randint() includes both endpoints, so it selects an index from 0 through
# len(answers) - 1. The brackets retrieve that reply, then print() displays it.
print(answers[randint(0, len(answers) - 1)])
