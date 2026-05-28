word = "python"
reverse = ""
for alpha in range(len(word)-1,-1, -1):
    reverse += word[alpha]

print(reverse)