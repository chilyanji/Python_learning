def count_up(n):
    if n == 0:
        return
    if n > 0:
        count_up(n - 1)
        print(n)
    

count_up(5)