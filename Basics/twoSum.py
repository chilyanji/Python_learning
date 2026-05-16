# Given a sorted array and a target, find if two numbers add up to target.

# arr = [1, 2, 4, 7, 11, 15]
# target = 15

arr = [1, 3, 5, 6, 8, 10]
target = 13

left = 0
right = len(arr) - 1

while left < right:
    currentSum = arr[left] + arr[right]

    if currentSum == target:
        print(left, right)
        break
    
    if currentSum < target:
        left += 1
    else:
        right -= 1