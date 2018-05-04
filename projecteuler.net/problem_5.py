from math import sqrt, log, floor


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
cases = []


def get_result(N):
    exp = [1 for _ in range(N)]  # exponents of prime factors
    i = 0                           # index for primes and exponents
    result = 1
    while primes[i] <= N:
        if primes[i] <= sqrt(N):
            exp[i] = floor(log(N)/log(primes[i]))
        result *= primes[i] ** exp[i]
        i += 1
    return result


# T = int(input().strip())
# for _ in range(T):
#     cases.append(int(input().strip()))
# for case in cases:
#     print(calc_even_fib(case))

print(get_result(20))
