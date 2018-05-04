import sys

with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        if test:
            X, Y, N = map(int, test.split(' '))
            result = []
            for i in range(1, N+1):
                if not i % X and not i % Y:
                    result.append('FB')
                elif not i % Y:
                    result.append('B')
                elif not i % X:
                    result.append('F')
                else:
                    result.append(str(i))
            print(*result, sep=' ')
