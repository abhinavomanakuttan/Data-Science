'''
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
'''

txt = "You cannot end a sentence with because because because is a conjunction"
position = txt.rindex("because")
print(position)
'''
The rindex() method returns the highest index (position) of the substring "because" in the given string, starting the search from the right.
In this case, the last occurrence of "because" starts at index 47.
'''