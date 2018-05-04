"""
Project Euler functions
"""
def sumcd(num):
  """
  sum of consecutive digits function returns the sum of all numbers through num
  ex: 5 would be 15 (1 + 2 + 3 + 4 + 5)
  param: num: integer that we will return the sum of
  return: sum of the consecutive digits
  """
  return num * (num + 1) // 2


def sumpf(num):
    """
    sum of the positive factors
    :param num: an integer greater than 1
    :return: sum of all the positive factors of num (excluding num itself)
    """
    results = set()
    results.add(1)
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            results.add(i)
            results.add(num//i)
    return sum(results)

  
def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]
