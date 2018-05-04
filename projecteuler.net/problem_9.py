from math import ceil, gcd
#from fractions import gcd
for _ in range(int(input().strip())):
    max_value = -1
    N = int(input().strip())
    s = N / 2
    m_max = ceil(s ** 0.5)
    for m in range(2, m_max):
        sm = s // m
        while sm % 2 == 0:
            sm //= 2    #reduce sm to lowest value
        if m % 2 == 1:
            k = m + 2
        else:
            k = m + 1
        while k < 2 * m and k <= sm:
            if sm % k == 0 and gcd(k, m) == 1:
                d = s // (k * m)
                n = k - m
                a = d * (m ** 2 - n ** 2)
                b = 2 * d * m * n
                c = d * (m ** 2 + n ** 2)
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == N:
                    if (a * b * c) > max_value:
                        max_value = int(a * b * c)
            k += 2
    print(max_value)
