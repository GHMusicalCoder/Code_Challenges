cases = []


def calc_even_fib(N):
    even = []
    fib = [0, 1, 1]
    next_fib = fib[-2] + fib[-1]
    while next_fib < N:
        fib.append(next_fib)
        if next_fib % 2 == 0:
            even.append(next_fib)
        next_fib = fib[-2] + fib[-1]
    return sum(even)


# T = int(input().strip())
# for _ in range(T):
#     cases.append(int(input().strip()))
# for case in cases:
#     print(calc_even_fib(case))

print(calc_even_fib(4000000))
