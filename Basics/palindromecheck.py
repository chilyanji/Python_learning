# Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.
s = "MALAYALAM"

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1

else:
    print("Palindrome")