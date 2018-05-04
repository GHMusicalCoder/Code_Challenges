import sys

with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        items = test.split(';')
        a = set(map(int, items[0].split(',')))
        b = set(map(int, items[1].split(',')))
        results = [x for x in a.intersection(b)]
        results.sort()
        print(*results, sep=',')
