collatz = {1: 1}
the99pct = [3732423, 3542887, 3064033, 2298025, 1723519, 1564063, 1501353, 1126015, 1117065, 837799,
            626331, 511935, 410011, 230631, 216367, 156159, 142587, 106239, 77031, 52527,
            35655, 35497, 34239, 26623, 23529, 17673, 17647, 13255, 10971, 6171,
            3711, 2919, 2463, 2323, 2322, 2223, 1161, 871, 703, 667,
            655, 654, 649, 327, 313, 235, 231, 171, 129, 97]

def get_collatz(number):
    if number not in collatz:
        collatz[number] = 1 + get_collatz(number // 2 if not number % 2 else number * 3 + 1)[0]

    return collatz[number], number


for _ in range(int(input().strip())):
    case = int(input().strip())
    if case >= the99pct[-1]:
        # case's max number is in the top 35
        for pct in the99pct:
            if case >= pct:
                print(pct)
                break
    else:
        print(max([get_collatz(i) for i in range(1, case)])[1])
