'''
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
Join the list with a hash with space string.
'''
txt = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

result = ' '.join(txt)
print(result)
print()
result = result.replace(' ', '#')
print(result)

#or
'''
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' # '.join(libraries)
print(result)

'''