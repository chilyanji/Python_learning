numbers = [4, 7, 1, 9, 3]
target = 20

found = False

for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("Found")    
else:
    print("Not Found")
