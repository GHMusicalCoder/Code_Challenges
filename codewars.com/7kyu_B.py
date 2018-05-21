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


# B06 -


# B07 -


# B08 -


# B09 -


# B10 -


# B11 -


# B12 -


# B13 -


# B14 -


# B15 -


# B16 -


# B17 -


# B18 -


# B19 -


# B20 -
