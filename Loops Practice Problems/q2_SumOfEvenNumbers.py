# Calclulate the sum of even numbers upto a given number n.
num = int(input("Enter the value of a number: "))
sumEven = 0
for i in range(1,num+1):
    if i%2 == 0:
        sumEven += i
print("Sum of even numbers is ", sumEven)