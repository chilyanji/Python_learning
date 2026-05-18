numbers = [1, 7, 2, 9]

maximum = 0

for num1 in range(len(numbers)):
    for num2 in range(num1 + 1,len(numbers)):
        pairs = (numbers[num1], numbers[num2])
        pair_sum = numbers[num1] + numbers[num2]
        if maximum < pair_sum:
            maximum = pair_sum
print(maximum)