for _ in range(int(input())):
    a_list = []
    perm = list('abcdefghijklm')
    result = []
    num = int(input().strip()) - 1
    if num == 0:
        print(*perm, sep='')
    else:
        d = 1
        while num > 0:
            q, r = divmod(num, d)
            a_list.append(r)
            num = q
            d += 1
        while len(a_list) < 13:
            a_list.append(0)
        for a in a_list[::-1]:
            result.append(perm[a])
            del perm[a]
        print(*result, sep='')