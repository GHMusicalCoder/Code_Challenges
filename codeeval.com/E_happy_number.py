import sys


tested = []

def is_happy(num):
    if num == 1:
        return 1
    if num in tested:
        return 0
    tested.append(num)
    s_num = str(num)
    return is_happy(sum(int(i)**2 for i in s_num))


# with open(sys.argv[1], 'r') as test_cases:
with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        tested = []
        print(is_happy(int(test)))
