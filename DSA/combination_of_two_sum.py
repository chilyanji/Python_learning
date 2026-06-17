def backtrack(index, target, path):

    if target == 0:
        print(path)
        return

    if index == len(nums):
        return

    if target < 0:
        return

    # Take current number
    backtrack(index,
              target - nums[index],
              path + [nums[index]])

    # Skip current number
    backtrack(index + 1,
              target,
              path)
nums = [2,3]
target = 6
backtrack(0, target, [])