'''
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
'''

txt = "You cannot end a sentence with because because because is a conjunction"
word_to_remove = "because"

# Replace the word with an empty string (removing the word)
result = txt.replace(word_to_remove, "")

print(result)

# To get a patter output
result = "  ".join(result.split())
print(result)
