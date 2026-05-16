# Given a number ‘N’, find out the sum of the first N natural numbers .


def integer(num):
    if num == 0:
        return
    else:
        integer(num - 1)
        num = num + 1
        result = ((num * (num - 1))/2)
        return result

num = int(input("Enter the value of n: "))
print(integer(num))


