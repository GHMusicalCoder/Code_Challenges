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
