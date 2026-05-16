# Compute the factorial of a number using a while loop

num = int(input("Enter the Number: "))

total = 1

while(num > 0):
    total *= num
    num -= 1


print(f"Factorial value is: {total}")