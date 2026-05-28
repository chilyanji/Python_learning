numbers = [1, 2, 1, 3, 2, 1]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for key, value in freq.items():
    print(f"{key} -> {value}")