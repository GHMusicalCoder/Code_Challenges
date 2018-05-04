import sys


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print("0" if int(test) % 2 else "1")
