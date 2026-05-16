# Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.

def palindrome(inputString):

    left = 0
    right = len(inputString) - 1

    while left < right:
        if inputString[left] != inputString[right]:
            print("Not Palindrome")
            break

        left += 1
        right -= 1

    else:
        print("Palindrome")


inputString = str(input("Please Enter your String: "))
palindrome(inputString)


