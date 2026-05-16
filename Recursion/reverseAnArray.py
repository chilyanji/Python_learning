# You are given an array. The task is to reverse the array and print it.
def arr(n):
    arr_list = []
    for i in range(1, n+1):
        arr1 = int(input(f"Enter the {i}th value of array: "))
        arr_list.append(arr1)
    return arr_list[:: - 1]
        
n = int(input("Enter the size of your array: "))
print(arr(n))
    