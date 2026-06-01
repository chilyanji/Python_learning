word = list("datascience")

left = 0
right = len(word) - 1

while left < right:
    word[left], word[right] = word[right], word[left]

    left += 1
    right -= 1

print("".join(word))