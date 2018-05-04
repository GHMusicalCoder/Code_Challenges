"""
Project Euler Version:
"""
# def calc_name(name):
#     return sum([ord(l) - 64 for l in name])
#
# names = []
# with open('./data/p022_names.txt', 'r') as fin:
#     for entry in fin.readlines():
#         names.extend(map(lambda x: x.strip('"'), entry.strip().split(',')))
#
# names.sort()
# score = 0
# for i, name in enumerate(names):
#     score += (i+1) * calc_name(name)
#
# print(score)
"""
HackerRank Version
"""


def calc_name(name):
    return sum([ord(l) - 64 for l in name])


names = []
# get 1st integer and the corresponding set of names
for _ in range(int(input().strip())):
    names.append(input().strip())
names.sort()
for _ in range(int(input().strip())):
    name = input().strip()
    i = names.index(name)
    print((i+1) * calc_name(name))
