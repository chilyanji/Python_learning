def reverse(word):

    if word == "":
        return

    reverse(word[1:])

    print(word[0])
word = "CAT"
reverse(word)