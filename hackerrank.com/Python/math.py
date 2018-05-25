# Polar Coordinates - https://www.hackerrank.com/challenges/polar-coordinates
import cmath
print(*cmath.polar(complex(input())), sep='\n')


# Find Angle MBC - https://www.hackerrank.com/challenges/find-angle
import math
AB = int(input())
BC = int(input())
print("{}°".format(round(math.degrees(math.atan2(AB,BC)))))


# Triangle Quest 2 - https://www.hackerrank.com/challenges/triangle-quest-2
for i in range(1, int(input())+1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10 ** i - 1)//9) ** 2)


# Mod Divmod - https://www.hackerrank.com/challenges/python-mod-divmod
a, b = int(input()), int(input())
t = divmod(a, b)
print(t[0])
print(t[1])
print(t)


# Power - Mod Power - https://www.hackerrank.com/challenges/python-power-mod-power
a, b, m = int(input()), int(input()), int(input())
print(pow(a, b))
print(pow(a, b, m))


# Integers Come In All Sizes - https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print("{}".format(a**b + c**d))


# Triangle Quest - https://www.hackerrank.com/challenges/python-quest-1
for i in range(1,int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print((i*(10**i -1)//9))