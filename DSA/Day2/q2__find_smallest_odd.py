numbers = [8, 3, 11, 2, 5]

minimum = float('inf')

for num in numbers:
    if num % 2 != 0:
        if num < minimum:
            minimum = num
if minimum == float('inf'):
    print("No odd number")
else:
    print(minimum)
