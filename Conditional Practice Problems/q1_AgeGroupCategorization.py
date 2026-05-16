# Classify a person's age group: child(<13), Teenager(13-19), Adult(20-59), Senior(60+)

age = int(input("Give me your age: "))
if(age<13):
    print("Child")
elif(13<=age<20):
    print("Teenager")
elif(20<=age<60):
    print("Adult")
else:
    print("Senior")