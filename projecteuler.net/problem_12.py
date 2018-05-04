def sieve_of_eratosthenes(num):
    numbers = [i for i in range(0, num)]
    for prime in numbers:
        if prime < 2:
            continue
        if prime > num ** 0.5:
            break
        for i in range(prime ** 2, num, prime):
            numbers[i] = 0
    return [x for x in numbers if x > 1]


primes = sieve_of_eratosthenes(1001)
def get_result(target):
    n = 3
    Dn = 2
    cnt = 0
    while cnt < target:
        n += 1
        n1 = n
        if n1 % 2 == 0:
            n1 //= 2
        Dn1 = 1
        for i in range(len(primes)):
            if primes[i] * primes[i] > n1:
                Dn1 *= 2
                break
            exp = 1
            while n1 % primes[i] == 0:
                exp += 1
                n1 //= primes[i]
            if exp > 1:
                Dn1 *= exp
            if n1 == 1:
                break
        cnt = Dn * Dn1
        Dn = Dn1
    return n * (n-1) // 2


for _ in range(int(input().strip())):
    x = int(input().strip())
    if x == 1:
        print(3)
    else:
        print(get_result(x+1))
