def sieve_of_eratosthenes(n):
    array = [True for _ in range(n + 1)]
    for p in range(2, int(n ** 0.5)):
        if array[p]:
            for i in range(p * 2, n + 1, p):
                array[i] = False

    return [i for i, a in enumerate(array) if i > 1 and a]


def sum_of_digits(number):
    """
    takes the sum of the individual digits of a number
    :param number: the actual number (ex: 483)
    :return: the sum of the individual digits (4+8+3)
    """
    num = [int(n) for n in str(number)]
    return sum(num)


def product_of_digits(number):
    """
    returns the product of the digits of a number
    :param number: the actual number (483)
    :return: the product of the individual digits (4*8*3)
    """
    value = 1
    num = [int(n) for n in str(number)]
    for n in num:
        value *= n
    return value


def sum_of_consecutive_digits(n):
    """
    returns the sum of all the digits leading to a number 1 + 2 + 3 + ... n
    :param n: the number to calc
    :return: the sum of the consecutive digits
    """
    return (n * (n + 1)) // 2


def get_prime_factors(n):
    """
    returns a list of integers that are prime #s and all factors of n
    :param n: the number to prime factorize
    :return: list of the prime factors
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(sieve_of_eratosthenes(30))

print(sum_of_digits(483))

print(product_of_digits(483))

print(sum_of_consecutive_digits(10))

print(get_prime_factors(600851475143))