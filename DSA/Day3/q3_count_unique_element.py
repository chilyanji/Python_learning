numbers = [1, 2, 2, 3, 4, 4]

count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
print(len(count))