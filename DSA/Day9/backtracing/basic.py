def subsets(nums, index, path):

    if index == len(nums):
        print(path)
        return

    # Take current number
    subsets(nums, index + 1, path + [nums[index]])

    # Skip current number
    subsets(nums, index + 1, path)

subsets([1,2], 0, [])