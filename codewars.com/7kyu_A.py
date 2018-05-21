# A01 - Money, Money, Money - https://www.codewars.com/kata/money-money-money
def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += (principal * interest) * (1 - tax)
        years += 1

    return years


# A02 - You are a Cube! - https://www.codewars.com/kata/you-are-a-cube
def you_are_a_cube(cube):
    test = int(round(cube ** (1/3)))
    if test ** 3 == cube:
        return True
    return False


def you_are_a_cube_bp(cube):
    return round(cube ** (1/3)) ** 3 == cube


# A03 - Numbers to Objects - https://www.codewars.com/kata/numbers-to-objects
def num_obj(s):
    return [{ str(i): chr(i) } for i in s]


# A04 - Duck Shoot - Easy Version - https://www.codewars.com/kata/duck-shoot-easy-version
def duck_shoot(ammo, aim, ducks):
    success = int(ammo * aim)
    shooting = ''
    for d in ducks:
        if d == '2':
            if success:
                shooting += 'X'
                success -= 1
            else:
                shooting += d
        else:
            shooting += d
    return shooting


def duck_shoot_bp(ammo, aim, ducks):
    return ducks.replace('2', 'X', int(ammo * aim))


# A05 - Factorial - https://www.codewars.com/kata/factorial-1
def factorial(n):
    from math import factorial as fact
    return fact(n)
    # why write a function when there is already a function that does it
    # but if there wasn't...
    # if n < 2:
    #     return 1
    # return n * factorial(n-1)


# best practice for factorial:
from math import factorial


# A06 - Sentence to words - https://www.codewars.com/kata/sentence-to-words
def splitSentence(s):
    return s.split()


# A07 - Reverse list - https://www.codewars.com/kata/reverse-list
def reverse_list(lst):
    return lst[::-1]


# A08 - Keep the Order - https://www.codewars.com/kata/keep-the-order
def keep_order(ary, val):
    for i, value in enumerate(ary):
        if value >= val:
            return i
    return len(ary)


# best practice for A08
from bisect import bisect_left as keep_order


# A09 - Naming Files - https://www.codewars.com/kata/naming-files
def name_file(fmt, nbr, start):
    return [fmt.replace("<index_no>", str(i+start)) for i in range(nbr)] if nbr > 0 and int(nbr) == nbr and int(start) == start else []


# A10 - Jaden Casing Strings - https://www.codewars.com/kata/jaden-casing-strings
def toJadenCase(string):
    return ' '.join(map(lambda x: x.capitalize(), string.split()))


def toJadenCase_bp(string):
    return " ".join(w.capitalize() for w in string.split())


# A11 - Histogram - H1 - https://www.codewars.com/kata/histogram-h1
def histogram(results):
    results = results[::-1]
    string = ""
    for i, v in enumerate(results):
        string += str(6 - i) + "|"
        if v > 0:
            string += "#" * v
            string += " " + str(v)
        string += "\n"

    return string


def histogram_bp(results):
    return ''.join([str(j) + '|' + i * '#' + (' ' + str(i)) * (i > 0) + '\n' for i, j in zip(results[::-1], range(6, 0, -1))])


# A12 - Number climber - https://www.codewars.com/kata/number-climber
def climb(n):
    my_list = [n]
    while n > 0:
        if n % 2 == 0:
            my_list.append(n // 2)
            n //= 2
        elif n > 1:
            n -= 1
        else:
            n = 0
    return sorted(my_list)


def climb_bp(n):
    return [1] if n == 1 else climb(int(n/2)) + [n]


# A13 - Is this a triangle? - https://www.codewars.com/kata/is-this-a-triangle
def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b:
        return True

    return False


def is_triangle_bp(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)


# A14 - Credit Card Mask - https://www.codewars.com/kata/credit-card-mask
# return masked string
def maskify(cc):
    length = len(cc)
    if length < 5:
        return cc
    else:
        return '#' * (length - 4) + cc[-4:]


def maskify_bp(cc):
    return "#"*(len(cc)-4) + cc[-4:]


# A15 - Exes and Ohs - https://www.codewars.com/kata/exes-and-ohs
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


# A16 -


# A17 -


# A18 -


# A19 -


# A20 -
