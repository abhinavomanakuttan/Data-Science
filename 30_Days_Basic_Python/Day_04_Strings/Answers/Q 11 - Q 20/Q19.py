'''
Create an acronym or an abbreviation for the name 'Coding For All'.
'''

phrase = "Coding For All"
words = phrase.split()  # Split the phrase into words
acronym = ''.join(word[0].upper() for word in words)  # Take the first letter of each word and capitalize it
print(acronym)
