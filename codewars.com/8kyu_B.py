# B01 Is this my tail? - https://www.codewars.com/kata/is-this-my-tail
def correct_tail(body, tail):
    return tail == body[-1]


def correct_tail_bp(body, tail):
    return body.endswith(tail)


# B02 Calculate average - https://www.codewars.com/kata/calculate-average
def find_average(array):
    return sum(array)/len(array) if (sum(array) != 0) else 0


def find_average_bp(array):
    return sum(array) / len(array) if array else 0


# B03 Jenny's secret message - https://www.codewars.com/kata/jennys-secret-message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# B04 Parse nice int from char problem - https://www.codewars.com/kata/parse-nice-int-from-char-problem
def get_age(age):
    return int(age[0])


# B05 String cleaning - https://www.codewars.com/kata/string-cleaning
def string_clean(s):
    return ''.join([c for c in s if c not in '1234567890'])


def string_clean_bp(s):
    return ''.join(x for x in s if not x.isdigit())


# B06 String repeat - https://www.codewars.com/kata/string-repeat
def repeat_str(repeat, string):
    return string * repeat


# B07 Hex to Decimal - https://www.codewars.com/kata/hex-to-decimal
def hex_to_dec(s):
    return int(s, 16)


# B08 Bin to Decimal - https://www.codewars.com/kata/bin-to-decimal
def bin_to_decimal(inp):
    return int(inp, 2)


# B09 Will you make it? -  https://www.codewars.com/kata/will-you-make-it
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if (mpg * fuel_left) >= distance_to_pump else False


def zeroFuel_bp(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


#B10 Convert boolean values to strings 'Yes' or 'No'. -
# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

