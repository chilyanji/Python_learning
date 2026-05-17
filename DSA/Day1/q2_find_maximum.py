numbers = [3, 8, 2, 10, 5]
print(max(numbers))


maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum number is:", maximum)