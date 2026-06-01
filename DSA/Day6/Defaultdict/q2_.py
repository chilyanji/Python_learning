from collections import defaultdict
number = [1,2,3,4,5]

freq = defaultdict(list)

for num in number:
    if num % 2 == 0:
        freq['even'].append(num)
    if num % 2 != 0:
        freq['Odd'].append(num)

print(freq)