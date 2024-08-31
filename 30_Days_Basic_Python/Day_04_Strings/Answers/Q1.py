'''
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
'''

# in simple form

result = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(result)

# By using the join() method

words = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(words)
print(result)

