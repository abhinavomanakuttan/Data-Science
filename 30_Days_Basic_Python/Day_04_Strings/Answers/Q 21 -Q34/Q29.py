'''
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
'''
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"

print(var1.isidentifier())  # Output: False
print(var2.isidentifier())  # Output: True


'''
In Python the isidentifier() method returns True if a string is a valid identifier (i.e., a valid variable name). A valid identifier must:

Start with a letter (a-z or A-Z) or an underscore (_).
Contain only letters, digits, or underscores.
Not be a reserved keyword (like if, for, while, etc.).
'''