from itertools import *


# itertools.product() - https://www.hackerrank.com/challenges/itertools-product
A = list(map(int, input().strip().split(' ')))
B = list(map(int, input().strip().split(' ')))
A.sort()
B.sort()
print(*product(A,B))


# itertools.permutations() - https://www.hackerrank.com/challenges/itertools-permutations
S, k = input().split(' ')
print(*[''.join(item) for item in permutations(sorted(S), int(k))], sep='\n')


# itertools.combinations() - https://www.hackerrank.com/challenges/itertools-combinations
S, k = input().split(' ')
for i in range(int(k)):
    print(*[''.join(item) for item in combinations(sorted(S), i+1)], sep='\n')


# itertools.combinations_with_replacement() -
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
S, k = input().split(' ')
print(*[''.join(item) for item in combinations_with_replacement(sorted(S), int(k))], sep='\n')


# Compress the String! - https://www.hackerrank.com/challenges/compress-the-string
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


# Iterables and Iterators - https://www.hackerrank.com/challenges/iterables-and-iterators
idx = input()   # not really used
letters = input().split()
idx = int(input())
combos = list(combinations(letters, idx))
valid_combos = list(filter(lambda c: 'a' in c, combos))
print('{:.3f}'.format(len(valid_combos)/len(combos)))


# Maximize It! - https://www.hackerrank.com/challenges/maximize-it
k, m = map(int, input().split())
lists = [[x**2 for x in [int(y) for y in input().split()[1:]]] for _ in range(k)]
sum_lists = [sum(x) % m for x in product(*lists)]
print(max(sum_lists))