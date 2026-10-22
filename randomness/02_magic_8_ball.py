# Assignment
# Create a list of possible Magic 8-Ball responses. Ask the user a question,
# choose one response at random, and print it. The random choice must always be
# a valid item from the response list.
#
# Solution

from random import randint

# The selected index is always between zero and the final valid list position.
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

question = input("Ask the magic 8-ball a question: ")
print(answers[randint(0, len(answers) - 1)])
