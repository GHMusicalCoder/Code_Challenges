import sys


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        temp = list(map(float, test.strip().split(' ')))
        print(*["{:.3f}".format(item) for item in sorted(temp)], sep=' ')
