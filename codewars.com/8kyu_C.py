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


