'''
Create an acronym or an abbreviation for the name 'Python For Everyone'.
'''

# input -> Python for Everyone
# output -> PFE

phrase = "Python For Everyone"
words = phrase.split()  # Split the phrase into words
acronym = ''.join(word[0].upper() for word in words)  # Take the first letter of each word and capitalize it
print(acronym)
