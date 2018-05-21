# A01 - Primes in numbers - https://www.codewars.com/kata/primes-in-numbers
def factor(n):
    f, factors, prime_gaps = 1, [], [2, 4, 2, 4, 6, 2, 6, 4]
    if n < 1:
        return []
    while True:
        for gap in ([1, 1, 2, 2, 4] if f < 11 else prime_gaps):
            f += gap
            if f * f > n:  # If f > sqrt(n)
                if n == 1:
                    return factors
                else:
                    return factors + [(n, 1)]
            if not n % f:
                e = 1
                n //= f
                while not n % f:
                    n //= f
                    e += 1
                factors.append((f, e))


def primeFactors(n):
    factors = factor(n)
    result = ""
    for a, b in factors:
        if b == 1:
            result += "({})".format(a)
        else:
            result += "({}**{})".format(a, b)
    return result


def bp_primeFactors(n):
    ret = ''
    for i in range(2, n + 1):
        num = 0
        while not n % i:
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret


# A02 - Product of consecutive Fib numbers - https://www.codewars.com/kata/product-of-consecutive-fib-numbers
def productFib(prod):
    fib = [0, 1]
    while fib[-2] * fib[-1] < prod:
        fib.append(fib[-1] + fib[-2])
    return [fib[-2], fib[-1], fib[-2]*fib[-1] == prod]


def bp_productFib(prod):
    a, b = 0, 1
    while prod > a * b:
    a, b = b, a + b
    return [a, b, prod == a * b]


# A03 - Number of trailing zeros of N! - https://www.codewars.com/kata/number-of-trailing-zeros-of-n
def zeros(n):
    factor = 5
    total = 0
    while factor < n:
        total += n // factor
        factor *= 5
    return total


def bp_zeros(n):
  x = n/5
  return x+zeros(x) if x else 0


# A04 -


# A05 -


# A06 -


# A07 -


# A08 -


# A09 -


# A10 -


# A11 -


# A12 -


# A13 -


# A14 -


# A15 -


# A16 -


# A17 -


# A18 -


# A19 -


# A20 -
