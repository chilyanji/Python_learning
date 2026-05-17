numbers = [1, 2, 3, 4, 5]
revese = []
for num in range(len(numbers), 0, -1):
    revese.append(numbers[num])
print(revese)

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])