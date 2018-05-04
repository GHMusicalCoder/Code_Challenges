# A01 Grasshopper - Combine strings - https://www.codewars.com/kata/grasshopper-combine-strings
def combine_names(first, last):
    return '{} {}'.format(first, last)


# A02 Return Two Highest Values in List - https://www.codewars.com/kata/return-two-highest-values-in-list
def two_highest(a_list):
    if not a_list:
        return a_list
    if isinstance(a_list, str):
        return False
    temp = list(set(a_list))
    temp.sort(reverse=True)
    return temp[:2]


def two_highest_bp(ls):
    result = sorted(list(set(ls)), reverse=True)[:2]
    return result if isinstance(ls, (list)) else False


# A03 Powers of 2 - https://www.codewars.com/kata/powers-of-2
def powers_of_two(n):
    return [2 ** i for i in range(n+1)]


# A04 Is there a vowel in there? - https://www.codewars.com/kata/is-there-a-vowel-in-there
def is_vow(inp):
    for i, v in enumerate(inp):
        if chr(v) in 'aeiou':
            inp[i] = chr(v)
    return inp


def is_vow_bp(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]


# A05 Squash the bugs - https://www.codewars.com/kata/squash-the-bugs
def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    for s in spl:
        if len(s) > longest:
            longest = len(s)
    return longest


def find_longest_bp(strng):
    return max(len(a) for a in strng.split())


# A06 Get number from string - https://www.codewars.com/kata/get-number-from-string
def get_number_from_string(string):
    return int("".join([s for s in string if s.isdigit()]))


# A07 Fix the Bugs (Syntax) - My First Kata - https://www.codewars.com/kata/fix-the-bugs-syntax-my-first-kata
def my_first_kata(a,b):
    from numbers import Number
    if not isinstance(a, Number) or not isinstance(b, Number)\
        or type(a) == type(True) or type(b) == type(True):
        # need extra step as True and False are int types in python - and thus pass
        # this is instance
        return False
    else:
        return a % b + b % a


def my_first_kata_bp(a,b):
    if type(a) == int and type(b) == int:
        return a % b + b % a
    else:
        return False


# A08 Find the position! - https://www.codewars.com/kata/find-the-position
def position(alphabet):
    return 'Position of alphabet: {}'.format(' abcdefghijklmnopqrstuvwxyz'.index(alphabet))


def position_bp(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)


# A09 Find Maximum and Minimum Values of a List - https://www.codewars.com/kata/find-maximum-and-minimum-values-of-a-list
# this one sort of defeated the purpose as min and max already do what this was supposed to do
def minimum(arr):
    return sorted(arr)[0]


def maximum(arr):
    return sorted(arr)[-1]


# A10 Sum without highest and lowest number - https://www.codewars.com/kata/sum-without-highest-and-lowest-number
def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0

    arr.sort()
    return sum(arr[1:-1])


def sum_array_bp(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


# A11 Volume of a Cuboid - https://www.codewars.com/kata/volume-of-a-cuboid
def getVolumeOfCubiod(length, width, height):
    return length * width * height


# A12 Keep Hydrated! - https://www.codewars.com/kata/keep-hydrated-1
def litres(time):
    from math import floor
    return floor(time * 0.5)


def litres_bp(time):
    return time // 2


# A13 Duck Duck Goose - https://www.codewars.com/kata/duck-duck-goose
def duck_duck_goose(players, goose):
    while goose >= len(players):
        goose -= len(players)
    return players[goose-1].name


def duck_duck_goose_bp(players, goose):
    return players[(goose % len(players)) - 1].name


# A14 Parse float - https://www.codewars.com/kata/parse-float
def parse_float(string):
    if not isinstance(string, str):
        return None
    try:
        return float(string)
    except ValueError:
        return None


def parse_float_bp(string):
    try:
        return float(string)
    except:
        return None


# A15 I love you, a little , a lot, passionately ... not at all -
# https://www.codewars.com/kata/i-love-you-a-little-a-lot-passionately-dot-dot-dot-not-at-all
def how_much_i_love_you(nb_petals):
    return ["not at all", "I love you", "a little", "a lot", "passionately", "madly"][nb_petals % 6]


def how_much_i_love_you_bp(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]


# A16 N-th Power - https://www.codewars.com/kata/n-th-power
def index(array, n):
    return array[n] ** n if n >= 0 and n < len(array) else -1


def index_bp(array, n):
    try:
        return array[n]**n
    except:
        return -1


# A17 The Wide-Mouthed frog! - https://www.codewars.com/kata/the-wide-mouthed-frog
def mouth_size(animal):
    return 'small' if animal == 'alligator' else 'wide'


def mouth_size_bp(animal):
    return 'small' if animal.lower() == 'alligator' else 'wide'


# A18 Well of Ideas - Easy Version - https://www.codewars.com/kata/well-of-ideas-easy-version
def well(x):
    if all(idea == 'bad' for idea in x):
        return 'Fail!'
    return 'I smell a series!' if x.count('good') > 2 else 'Publish!'


def well_bp(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


# A19 Classy Extentions - https://www.codewars.com/kata/classy-extentions
class Cat(Animal):
    def speak(self):
        return '{} meows.'.format(self.name)


# A20 My head is at the wrong end! - https://www.codewars.com/kata/my-head-is-at-the-wrong-end
def fix_the_meerkat(arr):
    return arr[::-1]


