a = int(input("Enter Your First Number: "))
b = int(input("Enter Your Second Number: "))
c = int(input("Enter Your Third Number: "))

if a >= b and a >= c:
    if b >= c:
        print("The order is:", a, b, c)
    else:
        print("The order is:", a, c, b)
elif b >= a and b >= c:
    if a >= c:
        print("The order is:", b, a, c)
    else:
        print("The order is:", b, c, a)
else:
    if a >= b:
        print("The order is:", c, a, b)
    else:
        print("The order is:", c, b, a)