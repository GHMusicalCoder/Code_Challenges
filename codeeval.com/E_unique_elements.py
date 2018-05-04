import sys


with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        temp = list(map(int, test.strip().split(',')))
        print(*sorted(set(temp)), sep=',')
