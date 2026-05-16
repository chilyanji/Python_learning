# Create a lambda function to compute the cube of a number.

num = int(input("Please enter the number: "))
cube = lambda x: x ** 3
print(cube(num))