from collections import defaultdict

word = "banana"
freq = defaultdict(int)

for ch in word:
    freq[ch] += 1

print(freq)