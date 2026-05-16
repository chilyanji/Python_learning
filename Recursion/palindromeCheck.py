# Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.

def palindrome(inputString, left, right):

    if left >= right:
        return True

    if inputString[left] != inputString[right]:
        return False
    return palindrome(inputString, left + 1, right - 1)

inputString = str(input("Please Enter your String: "))
result = palindrome(inputString, 0, len(inputString) - 1)
print(result)


