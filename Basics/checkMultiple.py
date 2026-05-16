print("Jis number ka aapko multiple print krna hai")
x = int(input("Please Enter Your Number: "))
num = int(input("Enter your number: "))

if(num%x==0):
    print("Your Entered number is",num,"\nThis number is a multiple of:",x)

else:
    print("Your Entered number is",num,"\nThis number is not a multiple of:",x)