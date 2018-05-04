import sys


# with open(sys.argv[1], 'r') as test_cases:
with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        print(sum(map(int, "{0:b}".format(int(test)))))
