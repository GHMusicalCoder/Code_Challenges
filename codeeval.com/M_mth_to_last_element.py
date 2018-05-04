import sys


with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        if test:
            items = list(test.strip().split())
            mth = int(items.pop())
            if mth <= len(items):
                print(items[len(items)-mth])
