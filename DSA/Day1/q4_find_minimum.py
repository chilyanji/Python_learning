numbers = [8, 3, 12, 1, 9]

minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(minimum)