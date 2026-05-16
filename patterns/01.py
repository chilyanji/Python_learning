

def pattern1(n):
    for num in range (1,n+1):
        for num2 in range(1,n+1):
            print("*", end=" ")
        print()


def pattern2(n):
    for num in range(1, n + 1):
        for num2 in range(1, num + 1):
            print("*", end=" ")
        print()
     
def pattern3(n):
    for num in range(1, n + 1):
        for num2 in range(1, num + 1):
            print(num2, end=" ")
        print()
def pattern4(n):
    for num in range(1, n + 1):
        for num2 in range(1, num + 1):
            print(num, end=" ")
        print()
def pattern5(n):
    for num in range(1, n + 1):
        for num2 in range(num, n + 1):
            print("*", end=" ")
        print()
def pattern6(n):
    for num in range(n, 0, -1):
        for num2 in range(1, num + 1):
            print(num2, end=" ")
        print()


def pattern7(n):
    for num in range(1, n + 1):
        for num2 in range(n - num):
            print(" ", end=" ")
        for k in range(2 * num - 1):
            print("*", end=" ")
        for num2 in range(n - num):
            print(" ", end=" ")
        print()
        
def pattern8(n):
    for num in range(n, 0, -1):
        for num3 in range(n - num):
            print(" ", end=" ")
        for num2 in range(2 * num - 1):
            print("*", end=" ")
        for num3 in range(n - num):
            print(" ", end=" ")
        print()


def pattern9(n):
    for num in range(1, n + 1):
        for num2 in range(n - num):
            print(" ", end=" ")
        for k in range(2 * num - 1):
            print("*", end=" ")
        for num2 in range(n - num):
            print(" ", end=" ")
        print()
    for num in range(n - 1, 0, -1):
        for num3 in range(n - num):
            print(" ", end=" ")
        for num2 in range(2 * num - 1):
            print("*", end=" ")
        for num3 in range(n - num):
            print(" ", end=" ")
        print()


def pattern10(n):
    for num in range(1, n + 1):
        for num2 in range(num):
            print("*", end=" ")
        print()
    for num in range(n - 1, 0, -1):
        for num2 in range(num):
            print("*", end=" ")
        print()

def pattern11(n):
    for num in range(1, n + 1):
        for num2 in range(num):
            if (num + num2) % 2 == 0:
                print(0, end=" ")
            else:
                print(1, end=" ")
            
        print()
def pattern12(n):
    for num in range(1, n + 1):
        for num2 in range(1, num + 1):
            print(num2, end=" ")
        for num2 in range(2 * (n - num)):
            print(" ", end=" ")
        for num2 in range(num, 0, -1):
            print(num2, end=" ")
        print()

def pattern13(n):
    count = 1
    for num in range(1, n + 1):
        for num2 in range(1, num + 1):
            print(count, end=" ")
            count = count + 1
        print()

def pattern14(n):
    for num in range(1, n + 1):
        for num2 in range(num):
            print(chr(65 + num2), end=" ")
        print()

def pattern15(n):
    for num in range(n, 0, -1):
        for num2 in range(num):
            print(chr(65 + num2), end=" ")
        print()
def pattern16(n):
    for num in range(1, n + 1):
        for num2 in range(num):
            print(chr(64 + num), end=" ")
        print()

def pattern17(n):
     for num in range(1, n + 1):
        for num2 in range(n - num):
            print(" ", end=" ")
        for num2 in range(num):
            print(chr(65 + num2), end=" ")
        for num2 in range(num  - 2, -1, -1):
            print(chr(65 + num2), end=" ")
        print()

    
def pattern18(n):
    for num in range (n, 0, -1):
        for num2 in range(n - num - 1):
            print(" ", end=" ")
        for num3 in range (num):
            print(chr(65 + num3), end=" ")
        
        print ()
    




# def pattern19(n):
# def pattern20(n):


n = int(input("Please enter the number: "))
pattern18(n)