values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
    '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


def calc_base_value(base, value):
    result = 0
    temp = value[::-1]
    work = list(temp)
    for i, v in enumerate(work):
        result += values[v] * (base ** i)

    return result


def get_values():
    #this function can be changed to read from file or pull input
    #but for test cases, we will return a tuple of values
    return '0', '1', '21', 'ab3', 'ff'


def main():
    numbers = get_values()
    print('Main Answer:')
    for num in numbers:
        indy = list(num)
        base = values[max(indy)] + 1
        num_val = calc_base_value(base, num)
        print('base {} => {}'.format(base, num_val))
    print()
    print('Bonus Answers: ')
    for num in numbers:
        indy = list(num)
        base = values[max(indy)] + 1
        print()
        print('For the value {} in all bases (from minimum to base16):'.format(num))
        for bonus in range(base, 17):
            num_val = calc_base_value(bonus, num)
            print('base {} => {}'.format(bonus, num_val))


if __name__ == '__main__':
    main()
