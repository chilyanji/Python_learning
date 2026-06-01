from collections import defaultdict
words = ["cat", "car", "dog", "duck"]
freq = defaultdict(list)

for ch in words:
    freq[ch[0]].append(ch)

print(freq)