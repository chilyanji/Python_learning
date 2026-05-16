# Revserse a string

str1 = str(input("Enter Your String: "))
str2 = ""

for ch in reversed(str1):
    str2 += ch

print("Your reverse string is: ",str2)