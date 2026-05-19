numbers = [1, 2, 3, 4, 5]
target = 6
count = 0

for num1 in range(len(numbers)):
    for num2 in range(num1 + 1, len(numbers)):
        pair_sum = numbers[num1] + numbers[num2]
        if pair_sum == target:
            count += 1

print(count)