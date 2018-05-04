def kaprekar_routine(num, opt=0):
    """
    daily programmer challenge 287 - take a number, and return its largest digit

    :param num: an integer
    :param opt: which option to use
    :return: varied based on option
    """
    temp = list(str(num))
    while len(temp) < 4:
        temp.append('0')

    if opt == 1:
        return ''.join(sorted(temp, reverse=True))
    elif opt == 2:
        cnt = 0
        if len(set(temp)) > 1:
            while temp != ['6', '1', '7', '4']:
                x = int(''.join(sorted(temp, reverse=True)))    # max num
                n = int(''.join(sorted(temp)))                  # min num
                temp = list(str(x - n))
                while len(temp) < 4:
                    temp.append('0')
                cnt += 1
        return cnt
    else:       # opt 0
        return max(temp)

# output testing
print('---Base Routine---')
print(kaprekar_routine(1234))
print(kaprekar_routine(3253))
print(kaprekar_routine(9800))
print(kaprekar_routine(3333))
print(kaprekar_routine(120))
print('--- Bonus 1 ---')
print(kaprekar_routine(1234, 1))
print(kaprekar_routine(3253, 1))
print(kaprekar_routine(9800, 1))
print(kaprekar_routine(3333, 1))
print(kaprekar_routine(120, 1))
print('--- Bonus 2 ---')
print(kaprekar_routine(1234, 2))
print(kaprekar_routine(3253, 2))
print(kaprekar_routine(9800, 2))
print(kaprekar_routine(3333, 2))
print(kaprekar_routine(120, 2))
print(kaprekar_routine(6589, 2))
print(kaprekar_routine(5455, 2))
print(kaprekar_routine(6174, 2))
