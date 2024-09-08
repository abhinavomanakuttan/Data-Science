'''
Cut(slice) out the first word of Coding For All string.
'''

string = "Coding For All"
# Split the string into a list of words
words = string.split()
print(words) # it wil print string in the list form
# Join the words back together, excluding the first word
result = ' '.join(words[1:])

print(result)
