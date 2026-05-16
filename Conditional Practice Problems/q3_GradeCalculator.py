# Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(Below 60)

marks = int(input("Please Enter Your Marks: "))
if(marks<60):
    print("Grade F")
elif(marks<70):
    print("Grade D")
elif(marks<80):
    print("Grade C")
elif(marks<90):
    print("Grade B")
elif(marks<=100):
    print("Grade A")