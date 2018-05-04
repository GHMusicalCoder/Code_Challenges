cases = []


def sum_consecutive_digits(num):
    return num * (num + 1) // 2


def get_result(num):
    num -= 1
    three = sum_consecutive_digits(num // 3) * 3
    five = sum_consecutive_digits(num // 5) * 5
    fifteen = sum_consecutive_digits(num // 15) * 15
    return three + five - fifteen


# T = int(input().strip())
# for _ in range(T):
#     cases.append(int(input().strip()))
# for case in cases:
#     print(calc_even_fib(case))

print(get_result(1000))
