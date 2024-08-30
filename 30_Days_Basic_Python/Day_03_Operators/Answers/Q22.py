'''
Write a script that prompts the user to enter number of years.
Calculate the number of seconds a person can live.
Assume a person can live hundred years
'''

years = int(input("Enter number of years: "))
life = years * 365
life = life * 86400
print(f"You have lived for {life} seconds.")