words = ["banana", "apple", "cat"]
words.sort()
print(words)
words.sort(reverse=True)
print(words)
words.sort(key= lambda x: len(x))
print(words)