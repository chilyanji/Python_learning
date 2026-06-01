number = [1,2,3,4,5,6,7]
target = 8
left = 0
right = len(number) - 1

while left < right:
    current_sum = number[left] + number[right]

    if current_sum == target:
        print(number[left], number[right])

        left += 1
        right -= 1

    elif current_sum < target:
        left += 1

    else:
        right -= 1

