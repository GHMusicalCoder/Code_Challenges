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


# B10 Convert boolean values to strings 'Yes' or 'No'. -
# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


# B11 Sleigh Authentication - https://www.codewars.com/kata/sleigh-authentication
class Sleigh(object):
    def authenticate(self, name, password):
        return True if name == 'Santa Claus' and password == 'Ho Ho Ho!' else False


class Sleigh_bp(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'


# B12 Convert number to reversed array of digits
# https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits
def digitize(n):
    return [int(i) for i in str(n)[::-1]]


def digitize_bp(n):
    return map(int, str(n)[::-1])


# B13 Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence -
# https://www.codewars.com/kata/exclamation-marks-series-number-11-replace-all-vowel-to-exclamation-mark-in-the-sentence
def replace_exclamation(s):
    vowels = ['A', 'E', "I", 'O', 'U']
    result = ''
    for letter in s:
        if letter.upper() in vowels:
            result += '!'
        else:
            result += letter
    return result


def replace_exclamation_bp(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


# B14 Number of People in the Bus - https://www.codewars.com/kata/number-of-people-in-the-bus
def number(bus_stops):
    count = 0
    for stop in bus_stops:
        count += stop[0]
        count -= stop[1]
    return count


def number_bp(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


# B15 Remove String Spaces - https://www.codewars.com/kata/remove-string-spaces
def no_space(x):
    return x.replace(' ', '')


# B16 Correct the mistakes of the character recognition software -
# https://www.codewars.com/kata/correct-the-mistakes-of-the-character-recognition-software
def correct(string):
    fixes = {'0': 'O', '5': 'S', '1': 'I'}
    issue = '015'
    result = ''
    for s in string:
        if s in issue:
            result += fixes[s]
        else:
            result += s
    return result


def correct_bp(string):
    return string.translate(str.maketrans("501", "SOI"))


# B17 Remove First and Last Character - https://www.codewars.com/kata/remove-first-and-last-character
def remove_char(s):
    return s[1:-1]


# B18 Basic Mathematical Operations - https://www.codewars.com/kata/basic-mathematical-operations
def basic_op(operator, value1, value2):
    return eval('{}{}{}'.format(value1, operator, value2))


# B19 Opposite number - https://www.codewars.com/kata/opposite-number
def opposite(number):
    return number * -1


def opposite_bp(number):
    return -number


# B20 Fake Binary - https://www.codewars.com/kata/fake-binary
def fake_bin(x):
    return ''.join(['0' if int(d) < 5 else '1' for d in x])


def fake_bin_bp(x):
    return ''.join('0' if c < '5' else '1' for c in x)
