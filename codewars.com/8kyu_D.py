# D01 - Transportation on vacation - https://www.codewars.com/kata/transportation-on-vacation
def rental_car_cost(d):
    disc = 0
    if d > 6:
        disc = 50
    elif d > 2:
        disc = 20

    return d * 40 - disc


def bp_rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result


def mc_rental_car_cost(d):
    return d * 40 - (d > 2) * 20 - (d > 6) * 30


# D02 -


# D03 -


# D04 -


# D05 -


# D06 -


# D07 -


# D08 -


# D09 -


# D10 -


# D11 -


# D12 -


# D13 -


# D14 -


# D15 -


# D16 -


# D17 -


# D18 -


# D19 -


# D20 -
