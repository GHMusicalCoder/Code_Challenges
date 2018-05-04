grid = []
for _ in range(20):
    grid.append(list(map(int, input().strip().split())))
max_product = 0
# cells are from 0 to 19
# left and right are the same thing - so we'll focus on right
# up & down are the same thing - so we'll focus on down
# diag up-right and down-left are the same - so we'll focus on down left
# diag up-left and down-right are the same - so we'll focus on down right
# cells 17-19 are useless for right & down-right
# cells 0-2 are useless for down-left
# rows 17-19 are useless for down & down-left & down-right
for R in range(20):
    for C in range(20):
        if C < 17:  # we can do the next for right
            if grid[R][C] * grid[R][C + 1] * grid[R][C + 2] * grid[R][C + 3] > max_product:
                max_product = grid[R][C] * grid[R][C + 1] * grid[R][C + 2] * grid[R][C + 3]
        if R < 17:  # we can do down
            if grid[R][C] * grid[R + 1][C] * grid[R + 2][C] * grid[R + 3][C] > max_product:
                max_product = grid[R][C] * grid[R + 1][C] * grid[R + 2][C] * grid[R + 3][C]
        if C < 17 and R < 17:  # we can do down-right
            if grid[R][C] * grid[R + 1][C + 1] * grid[R + 2][C + 2] * grid[R + 3][C + 3] > max_product:
                max_product = grid[R][C] * grid[R + 1][C + 1] * grid[R + 2][C + 2] * grid[R + 3][C + 3]
        if C > 2 and R < 17:  # we can do down-left
            if grid[R][C] * grid[R + 1][C - 1] * grid[R + 2][C - 2] * grid[R + 3][C - 3] > max_product:
                max_product = grid[R][C] * grid[R + 1][C - 1] * grid[R + 2][C - 2] * grid[R + 3][C - 3]
print(max_product)
