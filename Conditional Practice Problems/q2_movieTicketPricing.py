# Movie tickets are priced based on age: $12 for adults(18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter Your Age: "))
day = str(input("Today's Day: "))
if(age<18):
    if (day=="Wednesday"):
        print("Your Fair is: $6")
    else:
        print("Your Fair is: $8")
else:
    if (day=="Wednesday"):
        print("Your Fair is: $10")
    else:
        print("Your Fair is: $12")