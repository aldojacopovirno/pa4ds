# Assignment
# In the sentence provided in the program, the substring `woot` is used where
# `wood` is intended. Use the string method `replace` to correct every
# occurrence, then print the corrected sentence.
#
# Solution

# replace returns a new string with every matching occurrence corrected.
text = 'How much woot would a wootchuck chuck if a wootchuck could chuck the woot'

text = text.replace('woot', 'wood')
print(text)
