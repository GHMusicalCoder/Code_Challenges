import sys

with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        if test:
            result = test.strip().split(' ')
            print(' '.join(result[::-1]))
