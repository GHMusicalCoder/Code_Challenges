import sys

with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        if test:
            n, p1, p2 = map(int, test.strip().split(','))
            temp = '{0:#b}'.format(n)
            temp = temp[::-1]
            if temp[p1-1] == temp[p2-1]:
                print('true')
            else:
                print('false')
