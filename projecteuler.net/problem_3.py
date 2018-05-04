def smallest_2(n):
    if n == 1:
        return 2
    elif n % 2 == 1:
        return n
    else:
        return smallest_2(n // 2)


def get_largest_prime_factor(N):
    N = smallest_2(N)
    if N > 2:
        for test in range(3, int(1 + (N ** 0.5)), 2):
            while N % test == 0 and N != test:
                N //= test
        if N > 2:
            return N
        else:
            return test
    else:
        return 2


# HackerRank inputs
# T = int(input().strip())
# cases = []
# for _ in range(T):
#     cases.append(int(input().strip()))
# for case in cases:
#     print(get_largest_prime_factor(case))
print(get_largest_prime_factor(600851475143))
