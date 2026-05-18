numbers = [1, 2, 3]

for num1 in range(len(numbers)):
    for num2 in range(num1,len(numbers)):
        print(numbers[num1], numbers[num2])