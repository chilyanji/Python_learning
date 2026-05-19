numbers = [1, 2, 3, 2, 5, 1]


for num1 in range(len(numbers)):
    for num2 in range(num1 + 1, len(numbers)):
        if numbers[num1] == numbers[num2]:
            print(numbers[num1])