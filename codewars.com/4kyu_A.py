# A01 - The observed PIN - https://www.codewars.com/kata/the-observed-pin
def get_pins(observed):
    from itertools import product
    combos = { '1': ('1', '2', '4'), '2': ('1', '2', '3', '5'),
        '3': ('2', '3', '6'), '4': ('1', '4', '5', '7'), '5': ('2', '4', '5', '6', '8'),
        '6': ('3', '5', '6', '9'), '7': ('4', '7', '8'), '8': ('5', '7', '8', '9', '0'),
        '9': ('6', '8', '9'), '0': ('8', '0') }
    table = [combos[c] for c in observed]
    result = [R for R in (r for r in product(*table))]
    return [''.join(r) for r in result]


def bp_get_pins(observed):
    from itertools import product
    ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]


# A02 - Getting along with Integer Partitions - https://www.codewars.com/kata/getting-along-with-integer-partitions
def make_partition(num):
    # borrowed from http://jeromekelleher.net/generating-integer-partitions.html
    a = [0 for i in range(num + 1)]
    k = 1
    y = num - 1
    while k != 0:
        x = a[k-1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def part(n):
    from numpy import prod, mean, median
    products = sorted(set([prod(p) for p in make_partition(n)]))
    return 'Range: {} Average: {:.2f} Median: {:.2f}'\
        .format(products[-1] - products[0], mean(products), median(products))


def prod(u):
    p = 1
    for x in u:
        p *= x
    return p


def part_aux(s, k):
    cache = {}
    k0 = min(s, k)
    if k0 < 1:
        return []
    i = (s - 1) * s / 2 + k0 - 1
    ret = cache.get(i)
    if ret:
        return ret
    res = []
    for n in range(k0, 0, -1):
        r = s - n
        if (r > 0):
            for t in part_aux(r, n):
                if type(t) is list:
                    res.append([n] + t)
                else: res.append([n, t])
        else:
            res.append([n])
    cache[i] = res
    return res


def bp_part(n):
    r = sorted(set(map(prod, part_aux(n, n))))
    lg = len(r)
    avg = reduce(lambda x, y : x + y, r, 0)  / float(lg)
    rge = r[lg - 1] -  r[0]
    md = (r[(lg - 1) // 2] + r[lg // 2]) / 2.0
    return "Range: %d Average: %.2f Median: %.2f" % (rge, avg, md)


# A03 - Strings Mix - https://www.codewars.com/kata/strings-mix
def get_letters(string):
    temp = {}
    for s in string:
        if s.isalpha() and s.islower():
            temp[s] = 1 + temp.get(s, 0)
    return {k: v for (k, v) in temp.items() if v > 1}


def get_mixed_list(d1, d2):
    temp = []
    for k, v in d1.items():
        if v > d2.get(k, 0):
            temp.append(('1:', k, v))
        elif v == d2.get(k, 0):
            temp.append(('=:', k, v))
        else:
            temp.append(('2:', k, d2.get(k)))
        d2[k] = 0
    for k, v in d2.items():
        if v > 0:
            temp.append(('2:', k, v))
    return sorted(temp, key=lambda t: (-t[2], t[0], t[1]))


def mix(s1, s2):
    s = ''
    for cp, l, c in get_mixed_list(get_letters(s1), get_letters(s2)):
        # cp is codepoint, l is letter, c is count
        if s:
            s += '/'
        s += cp+l*c
    return s


def bp_mix(s1, s2):
    from collections import Counter

    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1.keys() + c2.keys()):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))


# A04 -


# A05 -


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
