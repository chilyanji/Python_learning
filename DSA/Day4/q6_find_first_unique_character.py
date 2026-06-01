word = "leetcode"

uni = []

for ch in word:
    if ch in uni:
        continue
    else:
        uni.append(ch)
print(uni[0])