cases = []
primes = [2]

def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    p_max = int(n ** 0.5)   # the largest possible divisor for a prime candidate is its square root
    test = 5                # since we've already eliminated 2, 3 - so 5 is the next prime to test against
    while test <= p_max:
        if n % test == 0:
            return False
        if n % (test + 2) == 0:
            return False
        test += 6
    return True

# since our problems only deal with up to 10000 primes - we'll just build to 10001
def build_primes():
    count = 1
    candidate = 1
    while count < 10001:
        candidate += 2
        if is_prime(candidate):
            primes.append(candidate)
            count += 1


# T = int(input().strip())
# build_primes()
# for _ in range(T):
#     cases.append(int(input().strip()))
# for case in cases:
#     print(primes[case - 1])
build_primes()
print(primes[10001-1])
