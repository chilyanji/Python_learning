# Problem Description: Given an integer N, write a program to print numbers from N to 1.
def revInteger(num):
    if num == 0:
        return
    else:
        print(num)
        revInteger(num - 1)

num = int(input("Enter the value of N: "))
revInteger(num)