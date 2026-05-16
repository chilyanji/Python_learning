# Given a String, find the first non-repeated character.

str1 = str(input("Enter Your String: "))

for i in str1:
    # print(i)
    if str1.count(i) == 1:
        print("Char is: ", i)
        # break
        