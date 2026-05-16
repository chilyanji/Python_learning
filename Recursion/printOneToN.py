# Given an integer N, write a program to print numbers from 1 to N.

def integer(num):
    if num == 0:
        return
    else:
        integer(num - 1)
        print(num)

num = int(input("Enter the value of n: "))
integer(num)