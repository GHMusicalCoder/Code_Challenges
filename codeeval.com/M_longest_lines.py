import sys


line = 0
lines = []
with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        if test:
            if line == 0:
                length = int(test)
            else:
                lines.append((test.strip(), len(test.strip())))
        line = 1
    lines.sort(key=lambda x: x[1], reverse=True)
    for i in range(length):
        print(lines[i][0])
