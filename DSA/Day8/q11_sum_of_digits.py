def sum_digits(n):
    if n == 0:
        return 0
    digit = n % 10
    result = digit + sum_digits(n // 10) 
print(sum_digits(1234))
