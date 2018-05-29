# B01 - How Green Is My Valley? - https://www.codewars.com/kata/how-green-is-my-valley
def make_valley(arr):
    arr.sort()
    left, right, middle = [], [], []
    if len(arr) % 2:
        middle.append(arr[0])
        arr = arr[1:]
    for a in arr:
        if len(left) < len(right):
            left.append(a)
        else:
            right.append(a)
    return left[::-1] + middle[:] + right[:]


def bp_make_valley(arr):
    arr = sorted(arr, reverse = True)
    return arr[::2] + arr[1::2][::-1]


# B02 - Easy Line - https://www.codewars.com/kata/easy-line
def easyline(n):
    result = x = 1
    for i in range(n):
        x = x * (n - i) // (i + 1)
        result += x ** 2
    return result


from scipy.misc import comb


def bp_easyline(n):
    return comb(2 * n, n, exact = True)


# B03 - Two to One - https://www.codewars.com/kata/two-to-one
def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))


def bp_longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


# B04 - Find the nth Digit of a Number - https://www.codewars.com/kata/find-the-nth-digit-of-a-number
def find_digit(num, nth):
    if nth < 1:
        return -1
    if abs(num) < 10 ** (nth-1):
        return 0
    return int(str(abs(num))[len(str(abs(num)))-nth])


def bp_find_digit(num, nth):
    if nth <= 0:
        return -1
    try:
        return int(str(num).lstrip('-')[-nth])
    except IndexError:
        return 0


# B05 - Thinkful - List Drills: Longest word - https://www.codewars.com/kata/thinkful-list-drills-longest-word
def longest(words):
    words.sort(key=lambda w: len(w), reverse=True)
    return len(words[0])


def bp_longest(words):
    return max(map(len, words))


# B06 - Find the next perfect square! - https://www.codewars.com/kata/find-the-next-perfect-square
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return ((sq ** 0.5) + 1) ** 2 if (sq ** 0.5).is_integer() else -1


def bp_find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


# B07 - Sort Numbers - https://www.codewars.com/kata/sort-numbers
def solution(nums):
    return [] if nums is None else sorted(nums, key=lambda i: i)


def bp_solution(nums):
    return sorted(nums) if nums else []


# B08 - ToLeetSpeak - https://www.codewars.com/kata/toleetspeak
leet = { 'A' : '@', 'B' : '8', 'C' : '(', 'D' : 'D', 'E' : '3', 'F' : 'F', 'G' : '6', 'H' : '#', 'I' : '!',
  'J' : 'J', 'K' : 'K', 'L' : '1', 'M' : 'M', 'N' : 'N', 'O' : '0', 'P' : 'P', 'Q' : 'Q', 'R' : 'R', 'S' : '$',
  'T' : '7', 'U' : 'U', 'V' : 'V', 'W' : 'W',  'X' : 'X', 'Y' : 'Y', 'Z' : '2', ' ': ' ' }


def to_leet_speak(str):
    return ''.join([leet[s] for s in str])


def bp_to_leet_speak(str):
    return str.translate(str.maketrans("ABCEGHILOSTZ", "@8(36#!10$72"))


# B09 - Minimize Sum Of Array (Array Series #1) -
# https://www.codewars.com/kata/minimize-sum-of-array-array-series-number-1
def min_sum(arr):
    return sum(x * y for x, y in zip(sorted(arr)[:int(len(arr) / 2)], list(sorted(arr)[int(len(arr) / 2)*-1:])[::-1]))


# B10 - Product Of Maximums Of Array (Array Series #2) -
# https://www.codewars.com/kata/product-of-maximums-of-array-array-series-number-2
def max_product(lst, n_largest_elements):
    return eval('*'.join(str(item) for item in sorted(lst, reverse=True)[:n_largest_elements]))


def bp_max_product(lst, n_largest_elements):
    lst = sorted(lst, reverse=True)[:n_largest_elements]
    value = 1
    for l in lst:
        value *= l
    return value


# B11 - Sum of differences between products and LCMs -
# http://www.codewars.com/kata/sum-of-differences-between-products-and-lcms
def sum_differences_between_products_and_LCMs(pairs):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b / gcd(a, b)

    result = 0
    for pair in pairs:
        value_prod = pair[0] * pair[1]
        value_lcm = lcm(pair[0], pair[1]) if pair[1] > 0 else 0
        result += value_prod - value_lcm

    return result


def bp_sum_differences_between_products_and_LCMs(pairs):
    from math import gcd
    return sum(a*b - a*b//gcd(a, b) for a, b in pairs if a and b)


# B12 - Next Prime - http://www.codewars.com/kata/next-prime/train/python
def next_prime(n):
    for poss in range(n+1, 2*n):
        for i in range(2, poss):
            if poss % i == 0:
                break
        else:
            return poss
    return 2


def bp_nextPrime(n):
    while True:
        n += 1
        if n == 2 or (n > 2 and n % 2 and all(n % i for i in range(3, int(n**0.5) + 1, 2))): return n


# B13 - Balanced Number (Special Numbers Series #1 ) -
# https://www.codewars.com/kata/balanced-number-special-numbers-series-number-1
def balanced_num(number):
    def sum_digits(digits):
        return sum([int(x) for x in digits])

    number = str(number)
    middle = len(number) // 2 if len(number) % 2 else (len(number) // 2) - 1

    if len(number) < 3:
        return "Balanced"
    else:
        return "Balanced" if sum_digits(number[:middle]) == sum_digits(number[(middle * -1):]) else "Not Balanced"


def bp_balanced_num(n):
    if n < 100: return 'Balanced'
    n = [int(i) for i in str(n)]
    return 'Balanced' if sum(n[:int(len(n)/2)-1+(len(n)%2)]) == sum(n[int(len(n)/2)+1:]) else 'Not Balanced'


# B14 -


# B15 -


# B16 -


# B17 -


# B18 -


# B19 -


# B20 -
