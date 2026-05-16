print("Aaj ham apna ek Calculator Bna rhe hai")
print("For addition press : 1")
print("For subtraction press : 2")
print("For Multiplication press : 3")
print("For Division press : 4")
option = int(input("Enter Your Option: "))


num1 = int(input("Enter Your first number: "))
num2 = int(input("Enter Your first number: "))

sum    = num1 + num2
sub    = num1 - num2
multi  = num1 * num2
div    = num1 / num2



match option:
    case 1:
            print("Your Result is :", sum)
    case 2 :
            print("Your Result is :", sub)
    case 3 :
            print("Your Result is :", multi)
    case 4 :
            print("Your Result is :", div)
    case _:
            print("Invalid choice")


print("kaisa lga apko mera calculator")
feed = str(input("jarur batana : "))
print("Thank You 🙏 for your Valueble Feedback: ", feed)

