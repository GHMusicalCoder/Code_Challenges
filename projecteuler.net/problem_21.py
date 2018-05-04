# credit http://www.ams.org/journals/mcom/1967-21-098/S0025-5718-1967-0222006-7/S0025-5718-1967-0222006-7.pdf
# for giving me the 13 amicable pairs under 100000
ami_pairs = [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595),
             (17296, 18416), (63020, 76084), (66928, 66992), (67095, 71145), (69615, 87633), (79750, 88730)]


def sum_ami_pairs(N):
    sums = 0
    for p1, p2 in ami_pairs:
        if N >= p1:
            sums += p1
            if N >= p2:
                sums += p2
        else:
            break
    return sums


for _ in range(int(input().strip())):
    print(sum_ami_pairs(int(input().strip())))
