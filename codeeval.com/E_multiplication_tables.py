table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in range(12):
    temp = list(str(t * (i+1)).rjust(4, ' ') for t in table)
    print(''.join(temp).strip())
