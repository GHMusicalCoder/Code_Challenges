cases = []


def sum_consecutive_digits(num):
    return num * (num + 1) // 2


def sum_consecutive_squares(num):
    return num * (num + 1) * (2 * num + 1) // 6

def get_result(N):
    return abs(sum_consecutive_squares(N) - (sum_consecutive_digits(N) ** 2))


# T = int(input().strip())
# for _ in range(T):
#     cases.append(int(input().strip()))
# for case in cases:
#     print(get_result(case))
print(get_result(100))
