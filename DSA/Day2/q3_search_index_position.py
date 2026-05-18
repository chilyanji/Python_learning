numbers = [4, 7, 1, 9, 3]
target = 9

index = -1

for num in range(len(numbers)):
    if numbers[num] == target:
        index = num

print(index)