'''
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
'''

# in simple form

result = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(result)

# By using the join() method

words = ['Coding', 'For', 'ALl']
result = ' '.join(words)
print(result)