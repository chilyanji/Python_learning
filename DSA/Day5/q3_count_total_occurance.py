def searching1(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1  
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid    
            right = mid -1 
            # left = mid + 1 
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return result
def searching2(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1  
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid    
            # right = mid -1 
            left = mid + 1 
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return result

def count_occurrences(arr, target):

    first = searching1(arr, target)

    if first == -1:
        return 0

    last = searching2(arr, target)

    return last - first + 1
arr = [1,2,2,2,2,3,4]
target = 2
print(count_occurrences(arr, target))
