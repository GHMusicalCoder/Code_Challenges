def number_jewels(J, S):
    return sum([S.count(jewel) for jewel in J])


print(number_jewels("aA","aAAbbbb"))