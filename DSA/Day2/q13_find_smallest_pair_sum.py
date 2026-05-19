numbers = [4, 1, 7, 2]

smallest_sum = float('inf')
smallest_pair = ()

for num1 in range(len(numbers)):
    for num2 in range(num1 + 1, len(numbers)):
        pair_sum = (numbers[num1] + numbers[num2])
        if pair_sum < smallest_sum:
            smallest_sum = pair_sum
            smallest_pair = (numbers[num1], numbers[num2])
print(smallest_pair)