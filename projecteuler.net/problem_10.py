import time
from bisect import bisect_left
start = time.time()


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


primes = sieve_of_eratosthenes(10**6+4)
sums = []
accum = 0
for p in primes:
    accum += p
    sums.append(accum)

for _ in range(int(input().strip())):
    case = int(input().strip())
    idx = bisect_left(primes, case)
    if primes[idx] > case:
        print(sums[idx-1])
    else:
        print(sums[idx])




print('{:.3f} seconds to process'.format(time.time() - start))