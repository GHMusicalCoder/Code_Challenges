import sys

with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        if test:
            x, n = map(int, test.strip().split(','))
            val = n
            while val < x:
                val += n
            print(val)
