from math import factorial as fact
mod = 10**9 + 7
for _ in range(int(input().strip())):
    N, M = map(int, input().strip().split())
    n = M + N
    r = M
    print(int(fact(n)//(fact(r)*fact(n-r))))
