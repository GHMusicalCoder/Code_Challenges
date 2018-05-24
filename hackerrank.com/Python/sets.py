# Introduction to Sets - https://www.hackerrank.com/challenges/py-introduction-to-sets
N, heights = int(input().strip()), set(map(int, input().strip().split(' ')))
print(sum(heights) / len(heights))

# Symmetric Difference - https://www.hackerrank.com/challenges/symmetric-difference
x = int(input().strip())
M = set(map(int, input().strip().split(' ')))
x = int(input().strip())
N = set(map(int, input().strip().split(' ')))
result_set = set(M.difference(N))
result_set.update(N.difference(M))
print(*sorted(result_set), sep='\n')


# No Idea! - https://www.hackerrank.com/challenges/no-idea
happiness = 0
n, m = map(int, input().strip().split(' '))
array_of_happiness = (map(int, input().strip().split(' ')))
A = set(map(int, input().strip().split(' ')))
B = set(map(int, input().strip().split(' ')))
for el in array_of_happiness:
    if el in A:
        happiness += 1
    if el in B:
        happiness -= 1
print(happiness)


# Set .add() - https://www.hackerrank.com/challenges/py-set-add
loop = int(input().strip())
stamps = set()
for _ in range(loop):
    stamps.add(input().strip())
print(len(stamps))


# Set .discard(), .remove() & .pop() - https://www.hackerrank.com/challenges/py-set-discard-remove-pop
x = int(input())
s = set(map(int, input().split()))
x = int(input())
commands = []
for _ in range(x):
    command = input().strip().split(' ')
    if len(command) > 1:
        commands.append([command[0], int(command[1])])
    else:
        commands.append(command)
for command in commands:
    if len(command) > 1:
        # either discard or remove
        eval('s.{}({})'.format(command[0], command[1]))
    else:
        s.pop()
print(sum(s))


# Set .union() Operation - https://www.hackerrank.com/challenges/py-set-union
n = int(input().strip())
english = set(map(int, input().strip().split(' ')))
n = int(input().strip())
french = set(map(int, input().strip().split(' ')))
print(len(english | french))


# Set .intersection() Operation - https://www.hackerrank.com/challenges/py-set-intersection-operation
n = int(input().strip())
english = set(map(int, input().strip().split(' ')))
n = int(input().strip())
french = set(map(int, input().strip().split(' ')))
print(len(english & french))


# Set .difference() Operation - https://www.hackerrank.com/challenges/py-set-difference-operation
n = int(input().strip())
english = set(map(int, input().strip().split(' ')))
n = int(input().strip())
french = set(map(int, input().strip().split(' ')))
print(len(english - french))


# Set .symmetric_difference() Operation - https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation
n = int(input().strip())
english = set(map(int, input().strip().split(' ')))
n = int(input().strip())
french = set(map(int, input().strip().split(' ')))
print(len(english ^ french))


# Set Mutations - https://www.hackerrank.com/challenges/py-set-mutations
n = int(input().strip())
A = set(map(int, input().strip().split(' ')))
n = int(input().strip())
commands = []
for _ in range(n):
    cmd, x = input().strip().split(' ')
    a_set = set(map(int, input().strip().split(' ')))
    commands.append((cmd, a_set))
for command, the_set in commands:
    eval('A.{}({})'.format(command, the_set))
print(sum(A))


# Check Subset - https://www.hackerrank.com/challenges/py-check-subset
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    print(len(A-B) == 0)


# Check Strict Superset - https://www.hackerrank.com/challenges/py-check-strict-superset
A = set(input().split(' '))
output = True
for _ in range(int(input())):
    other = set(input().split(' '))
    if len(other-A) > 0:
        output = False
        break
print(output)


# The Captain's Room - https://www.hackerrank.com/challenges/py-the-captains-room
family_count, room_array = int(input()), list(map(int, input().split()))
unique_set = set(room_array)    # distinct room # set
# every room but the capt room is in the array family_count # of times
# so if we take the set of the array (the distinct #s) and multiply it by our count
# then subtract from that sum of the array, the different will be family_count-1 X the single room #
print((sum(unique_set) * family_count - (sum(room_array))) // (family_count - 1))
