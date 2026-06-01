def searching(arr, target):
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



arr = [1,2,2,2,3,4]
target = 2
print(searching(arr, target))


