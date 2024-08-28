'''Write a script that prompts the user to enter base and height of the triangle
and calculate an area of this triangle (area = 0.5 x b x h).
'''

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * (base * height) ** 2
print(f"The area of the triangle is {area}")
