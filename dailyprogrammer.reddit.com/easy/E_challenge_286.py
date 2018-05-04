def get_input():
    data = []
    for _ in range(int(input().strip())):
        data.append(int(input().strip()))
    return data


def reverse_factorial(num):
    """
    test to see if the given number is a factorial of some other number (example - given 6, we'd return 3! since
    1 x 2 x 3 = 6, so 6 is the result of 3!
    :param num: an integer greater than 0
    :return: a string that is either #! to show the factoral, or NONE to say that it is not a factoral
    """
    # we will start at 2 and move up with each iteration
    temp = num
    fact = 2
    while temp % fact == 0:
        temp //= fact
        if temp == 1:
            return '{} = {}!'.format(num, fact)
        fact += 1
    return '{}  NONE'.format(num)


def main():
    data = get_input()
    for datum in data:
        print(reverse_factorial(datum))


if __name__ == '__main__':
    main()
