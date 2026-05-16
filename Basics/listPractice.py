# list = []
# movie1 = str(input("Please Enter Your 1st Movie:"))
# list.append(movie1)
# movie2 = str(input("Please Enter Your 2nd Movie:"))
# list.append(movie2)
# movie3 = str(input("Please Enter Your 3rd Movie:"))
# list.append(movie3)

# print("Your Favorite Movies is: ", list)


list = [1,2,3,2,1]
list1 = list.copy()
list1.reverse()
if(list==list1):
    print("Yes, this is Palindrome")
else:
    print("This is not a Palindrome")