from itertools import permutations, combinations


def gen_permuation(idx, num):
    perms = list(permutations([x for x in range(num)]))
    print(*perms[idx-1], sep=' ')


def gen_combination(idx, cnt, num):
    combos = list(combinations(range(num), cnt))
    print(*combos[idx-1], sep=' ')


if __name__ == '__main__':
    gen_permuation(240, 6)
    gen_permuation(3240, 7)
    gen_combination(24, 3, 8)
    gen_combination(112, 4, 9)
