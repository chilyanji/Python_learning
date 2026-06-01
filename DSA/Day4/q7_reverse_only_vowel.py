word = list("hello")

left = 0
right = len(word) - 1
vowels =  "aeiouAEIOU"

while left < right:
    while left < right and word[left] not in vowels:
        left += 1

    while left < right and word[right] not in vowels:
        right -= 1

    word[left], word[right] = word[right], word[left]
    left += 1
    right -= 1
      
print("".join(word))