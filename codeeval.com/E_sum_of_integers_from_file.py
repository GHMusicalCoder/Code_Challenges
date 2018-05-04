import sys

total = 0
with open(sys.argv[1], 'r') as test_cases:
    # with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        if test:
            total += int(test.strip())
print(total)
