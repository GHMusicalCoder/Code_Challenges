def two_sum(nums, target):
    count = len(nums)
    for i, v in enumerate(nums):
        for x in range(i + 1, count):
            if v + nums[x] == target:
                return [i, x]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([0, 4, 3, 0], 0))
print(two_sum([-1, -2, -3, -4, -5], -8))
