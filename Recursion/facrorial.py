# Given a number X,  print its factorial.
# To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.
# Note: X  is always a positive number. 

def fact(num):
    
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
num = int(input("Please enter your number: "))
print(fact(num))
