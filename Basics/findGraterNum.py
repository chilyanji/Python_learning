a = int(input("Enter Your First Number: "))
b = int(input("Enter Your Second Number: "))
c = int(input("Enter Your Third Number: "))

if (a >= b and a >= c):
    print("First number is the largest",a)
elif b >= c:
    print("Second numebr is the largest",b)
else:
    print("Third number is the largest", c)