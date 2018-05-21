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
