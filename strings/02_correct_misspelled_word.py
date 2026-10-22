# Assignment
# In the sentence provided in the program, the substring `woot` is used where
# `wood` is intended. Use the string method `replace` to correct every
# occurrence, then print the corrected sentence.
#
# Solution

# Start with the sentence that contains the same spelling mistake several times.
text = 'How much woot would a wootchuck chuck if a wootchuck could chuck the woot'

# Strings are immutable: their characters cannot be changed in place. replace
# returns a new string with every occurrence of 'woot' replaced by 'wood'.
# It also matches inside longer words, so each 'wootchuck' becomes 'woodchuck'.
# Assign the result back to text so the variable now refers to the corrected text.
text = text.replace('woot', 'wood')

# Print the new value stored in text to display the complete corrected sentence.
print(text)
