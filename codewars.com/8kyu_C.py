# C01 Count of positives / sum of negatives - https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives
def count_positives_sum_negatives(arr):
    if not arr:
        return arr
    pos, neg = 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        else:
            neg += i
    return [pos, neg]


# C02 Determine offspring sex based on genes XX and XY chromosomes -
# https://www.codewars.com/kata/determine-offspring-sex-based-on-genes-xx-and-xy-chromosomes
def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {0}.'.format('son' if sperm[-1] == 'Y' else 'daughter')


def chromosome_check_bp(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')


# C03 Remove duplicates from list - https://www.codewars.com/kata/remove-duplicates-from-list
def distinct(seq):
    # tried list(set(seq)) but it failed as it didn't return them in the order they were in
    final = []
    for s in seq:
        if s not in final:
            final.append(s)
    return final


def distinct_bp(seq):
    return sorted(set(seq), key = seq.index)


# C04 Multiply - https://www.codewars.com/kata/multiply
def multiply(a, b):
    return a * b


# C05 Reversed sequence - https://www.codewars.com/kata/reversed-sequence
def reverse_seq(n):
    return [x for x in range(n, 0, -1)]


def reverseseq_bp(n):
    return list(range(n, 0, -1))


# C06 Sum of positive - https://www.codewars.com/kata/sum-of-positive
def positive_sum(arr):
    return sum([a for a in arr if a > 0]) if arr else 0


def positive_sum_bp(arr):
    return sum(x for x in arr if x > 0)


# C07 The Feast of Many Beasts - https://www.codewars.com/kata/the-feast-of-many-beasts
def feast(beast, dish):
    # your code here
    return beast[0] == dish[0] and beast[-1] == dish[-1]


# C08 Expressions Matter - https://www.codewars.com/kata/expressions-matter
def expression_matter(a, b, c):
    return max(a+b+c, (a+b)*c, a*(b+c), a*b*c)


# C09 - Get the mean of an array - https://www.codewars.com/kata/get-the-mean-of-an-array
def get_average(marks):
    return sum(marks) / len(marks)


# C10 - Sort and Star - https://www.codewars.com/kata/sort-and-star
def two_sort(array):
    return "***".join(l for l in sorted(array)[0])


def bp_two_sort(array):
    return '***'.join(min(array))


# C11 - altERnaTIng cAsE <=> ALTerNAtiNG CaSe -
# https://www.codewars.com/kata/alternating-case-%3C-equals-%3E-alternating-case
def to_alternating_case(string):
    temp = ''
    for s in string:
        if s.isalpha():
            if s.islower():
                temp += s.upper()
            else:
                temp += s.lower()
        else:
            temp += s
    return temp


def bp_to_alternating_case(string):
    return string.swapcase()


# C12 - Geometry Basics: Circle Circumference in 2D -
# https://www.codewars.com/kata/geometry-basics-circle-circumference-in-2d
def circle_circumference(circle):
    from math import pi
    return round(2 * pi * circle.radius, 6)


# C13 - Grasshopper - Terminal game combat function -
# https://www.codewars.com/kata/grasshopper-terminal-game-combat-function-1
def combat(health, damage):
    return health - damage if damage < health else 0


def bp_combat(health, damage):
    return max(0, health-damage)


# C14 - Training JS #18: Methods of String object--concat() split() and its good friend join() -
# https://www.codewars.com/kata/training-js-number-18-methods-of-string-object-concat-split-and-its-good-friend-join
def split_and_merge(string, sp):
    return " ".join(sp.join(word) for word in string.split())


# C15 - Thinkful - Logic Drills: Traffic light - http://www.codewars.com/kata/thinkful-logic-drills-traffic-light
def update_light(current):
    return {'green': 'yellow', 'yellow': 'red', 'red': 'green'}[current]


# C16 -


# C17 -


# C18 -


# C19 -


# C20 -
