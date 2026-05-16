# create a recursive function to calculate the factorial of a number.

# normal function calculaions

# def factorial(num):
#     fact = 1
#     for i in range(1,num + 1):
#         fact *= i
#     return fact

# num = int(input("Please enter the number: "))

# print(factorial(num))



# Recursion 

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input("Please enter the number: "))

print(factorial(num))