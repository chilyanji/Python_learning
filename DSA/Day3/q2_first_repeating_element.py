numbers = [4, 7, 1, 7, 9, 4]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
        print(num)
        break
    else:
        freq[num] = 1
        