from math import factorial as f
for _ in range(int(input().strip())):
    print(sum([int(d) for d in str(f(int(input().strip())))]))
