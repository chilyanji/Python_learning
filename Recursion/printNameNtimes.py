# Take input n, its an integer, and then print your name n times.

def repeat(num, name):
    
    if num == 0:
        return
    else:
        print(name)
        repeat(num - 1, name)

num = int(input("Please enter the value of n: "))
name = str(input("Please enter your name: "))
repeat(num, name)
