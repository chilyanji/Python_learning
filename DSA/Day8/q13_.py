def product_digits(n):
    if n <= 1:
        return 1
    else:
        digit = n % 10
        result = digit * product_digits(n // 10)
        return result
    
print(product_digits(234))