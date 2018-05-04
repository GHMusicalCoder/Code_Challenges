from math import sqrt


# coordinates uses x,y basis grid, starting at the period
coordinates = {'1': [0, 3], '2': [1, 3], '3': [2, 3],
               '4': [0, 2], '5': [1, 2], '6': [2, 2],
               '7': [0, 1], '8': [1, 1], '9': [2, 1],
               '.': [0, 0], '0': [1, 0]}


def calc_distance_between_points(f, t):
    """
    function calculates the distance between 2 points on the keypad using pythagoras' theorem
    :param f: from location coordinate
    :param t: to location coordinate
    :return: the distance between from and to, based on the pythagorean theorem a^2 + b^2 = c^2
    """
    return sqrt(((coordinates[t][1] - coordinates[f][1]) ** 2 + (coordinates[t][0] - coordinates[f][0]) ** 2))


def get_ip():
    """
    will get an IP address and return it - right now this is 'coded' - but can be changed to an input or a file read
    :return: ip address to traverse
    """
    return '219.45.143.143'


def main():
    """
    main function - will call an get function to get data (which may be changed from file read or input
    and will use said input to calculate the distance on a keypad given the keypad is 123456789.0 variety
    :return: prints the distance finger will trave4l
    """
    distance = 0
    ip = get_ip()
    start = ip[0]
    for pos in ip[1:]:
        distance += calc_distance_between_points(start, pos)
        start = pos
    print('{:.2f} cm'.format(distance))


if __name__ == '__main__':
    main()