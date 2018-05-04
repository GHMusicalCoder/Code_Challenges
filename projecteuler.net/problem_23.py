def d(n):
    s = 1
    t = n ** 0.5
    for i in range(2, int(t) + 1):
        if n % i == 0: s += i + n // i
    if t == int(t):
        s -= t  # correct s if t is a perfect square
    return s


def build_abundant(L):
    abn = set()
    for n in range(12, L):
        if d(n) > n:
            abn.add(n)
    return abn

limit = 28123
abundant = build_abundant(limit)

for _ in range(int(input().strip())):
    num = int(input().strip())
    if num < 24:
        print('NO')
    elif num > 46 and num % 2 == 0:
        print('YES')
    elif num > limit:
        print('YES')
    elif any((num - a in abundant) for a in abundant):
        print('YES')
    else:
        print('NO')
