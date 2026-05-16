# Given an integer N. Print the Fibonacci series up to the Nth term.

def fibonacci(num):
    # base condition
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    return fibonacci(num - 1) + fibonacci(num - 2)
num = int(input("Enter the value of N: "))
print(fibonacci(num))