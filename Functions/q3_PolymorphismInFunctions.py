# Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a,b):
    return a * b

a = int(input("Enter the first Input: "))
b = int(input("Enter the second Input: "))
print(multiply(5,4))
print(multiply("a",5))
print(multiply(5,"b"))
print(multiply(a,b))