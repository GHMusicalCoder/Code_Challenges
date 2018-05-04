cases = []


def determine_largest_palindrome(a, b, curr, limit):
    if a * b <= curr or a * b >= limit or a * b != int(str(a*b)[::-1]):
        return curr

    return a * b


def get_result(N):
    lp = 0
    for a in range(999, 100, -1):
        if a % 11 == 0:
            for b in range(999, a - 1, -1):
                lp = determine_largest_palindrome(a, b, lp, N)
        else:
            for b in range(990, a - 1, -11):
                lp = determine_largest_palindrome(a, b, lp, N)
    return lp


# T = int(input().strip())
# for _ in range(T):
#     cases.append(int(input().strip()))
# for case in cases:
#     print(calc_even_fib(case))

print(get_result(800000))
