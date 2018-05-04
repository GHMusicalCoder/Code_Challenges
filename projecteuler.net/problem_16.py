def sum_of_digits(n):
    result = 0
    while n:
        result, n = result + n % 10, n // 10
    return result

print(sum_of_digits(2**1000))