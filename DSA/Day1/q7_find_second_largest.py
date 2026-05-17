numbers = [3, 8, 2, 10, 5]

maximum = numbers[0]
secondMaximum = numbers[0]

for num in numbers:
    if num > maximum:
        secondMaximum = maximum
        maximum = num
    elif num > secondMaximum and num != maximum:
        secondMaximum = num
        
print(secondMaximum)