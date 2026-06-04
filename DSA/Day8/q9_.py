def count_chars(ch):
    if ch == "":
        return 0
    else:
        return 1 + count_chars(ch[1:])

print(count_chars("hello"))