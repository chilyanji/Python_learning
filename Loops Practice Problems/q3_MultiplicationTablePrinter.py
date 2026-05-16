# Print the multiplication table for a given number upto 10, but skip the fifth iteration.

# num = int(input("Enter Your number: "))
# for i in range (1, 11):
#     if i == 5:
#         continue
#     print(num, 'x', i, '=', num * i)



# Table from 1 to n -->
num = int(input("Enter Your number: "))
for i in range (1, num+1):
    for j in range (1, 11):
        print(i, 'x', j, '=', i * j)
    print("\t")