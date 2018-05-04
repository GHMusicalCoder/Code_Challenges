# from datetime import date


def zeller_calculation(yr, mo):
    """
    don't need day as all days will be on first of month
    :param yr: year in question
    :param mo: month in question
    :return: returns 1 if 1st was on Sunday otherwise 0
    """
    if mo < 3:
        mo += 12
        yr -= 1
    m = 13 * (mo + 1)
    m_calc = m // 5
    K = yr % 100
    K_calc = K + (K // 4)
    J = yr // 100
    J_calc = (J // 4) + (5*J)

    return 1 if (1 + m_calc + K_calc + J_calc) % 7 == 1 else 0


def accum_month(yr, mo):
    mo += 1
    if mo > 12:
        mo = 1
        yr += 1
    return mo, yr


# normal calendar
# for _ in range(int(input().strip())):
#     sy, sm, sd = map(int, input().strip().split())
#     ey, em, ed = map(int, input().strip().split())
#     if sd > 1:
#         sm, sy = accum_month(sy, sm)
#
#     sundays = 0
#     while True:
#         test = date(sy, sm, 1)
#         if test.weekday() == 6:
#             sundays += 1
#         sm, sy = accum_month(sy, sm)
#         if sy > ey or (sm > em and sy == ey):
#             break
#     print(sundays)


# zeller
for _ in range(int(input().strip())):
    sy, sm, sd = map(int, input().strip().split())
    ey, em, ed = map(int, input().strip().split())
    if sd > 1:
        sm, sy = accum_month(sy, sm)

    sundays = 0
    while True:
        sundays += zeller_calculation(sy, sm)
        sm, sy = accum_month(sy, sm)
        if sy > ey or (sm > em and sy == ey):
            break
    print(sundays)
