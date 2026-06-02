from itertools import permutations, combinations

nums = [1,2,3]

result1 = list(permutations(nums,2))
result2 = list(combinations(nums,2))
print(result1)
print(len(result1))
print(result2)
print(len(result2))

print("Now Permutation")

for item in result1:
    print(item)

print("Now Combinations")
for item in result2:
    print(item)