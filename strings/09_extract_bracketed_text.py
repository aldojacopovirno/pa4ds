# Assignment
# Given a string containing square-bracket pairs, locate each opening bracket
# and its matching closing bracket, then print the text between them. Continue
# searching after each closing bracket and stop safely if no further complete
# pair exists.
#
# Solution

# Continue the next search after the closing bracket just handled.
text = "The [quick] brown [fox] jumps."
start = 0

while True:
    opening_index = text.find("[", start)
    if opening_index == -1:
        break

    closing_index = text.find("]", opening_index + 1)
    if closing_index == -1:
        break

    print(text[opening_index + 1:closing_index])
    # Continue after this closing bracket so the next search cannot reuse it.
    start = closing_index + 1
