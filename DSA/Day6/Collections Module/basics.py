from collections import Counter
word = "banana"
freq = Counter(word)
print(freq)
print(freq.most_common(1))
print(freq.most_common(2))
print(freq.most_common(3))