numbers = [1, 2, 3, 4]

pair_sum = 5

for num1 in range(len(numbers)):
    for num2 in range(num1 + 1,len(numbers)):
        pairs = (numbers[num1], numbers[num2])
        if pair_sum == numbers[num1] + numbers[num2]:
            print(pairs)