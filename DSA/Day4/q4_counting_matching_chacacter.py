word = "racecar"

left = 0
right = len(word) - 1


count = 0
while left <= right:

    if word[left] == word[right]:
        count += 1

    left += 1
    right -= 1

print(count)