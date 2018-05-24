# sWAP cASE - https://www.hackerrank.com/challenges/swap-case
print(input().strip().swapcase())


# String Split and Join - https://www.hackerrank.com/challenges/python-string-split-and-join
print('-'.join(input().strip().split(' ')))


# What's Your Name? - https://www.hackerrank.com/challenges/whats-your-name
firstname = input().strip()
lastname = input().strip()
print('Hello {} {}! You just delved into python.'.format(firstname, lastname))


# Mutations - https://www.hackerrank.com/challenges/python-mutations
s = input().strip()
a = input().strip().split(' ')
a[0] = int(a[0])
print('{}{}{}'.format(s[:a[0]], a[1], s[a[0]+1:]))


# Find a string - https://www.hackerrank.com/challenges/find-a-string
s = input().strip()
ss = input().strip()
counter = 0
for i in range(len(s)):
    if s[i:i+len(ss)] == ss:
        counter += 1

print(counter)


# String Validators - https://www.hackerrank.com/challenges/string-validators
results = [False, False, False, False, False]
S = input().strip()
for c in S:
    if c.isalnum():
        results[0] = True
    if c.isalpha():
        results[1] = True
    if c.isdigit():
        results[2] = True
    if c.islower():
        results[3] = True
    if c.isupper():
        results[4] = True
print(*results, sep='\n')


# Text Alignment - https://www.hackerrank.com/challenges/text-alignment
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# Text Wrap - https://www.hackerrank.com/challenges/text-wrap
import textwrap
S, w = (input().strip(), int(input().strip()))
print(textwrap.fill(S, w))


# Designer Door Mat - https://www.hackerrank.com/challenges/designer-door-mat
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print(('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2,-1,-2):
    print(('.|.' * i).center(M, '-'))


# String Formatting - https://www.hackerrank.com/challenges/python-string-formatting
N = int(input().strip())
w = len('{:b}'.format(N))
for n in range(N):
     print('{0:>{1}} {0:>{1}o} {0:>{1}X} {0:>{1}b}'.ljust(w, ' ').format(n+1, w))


# Alphabet Rangoli - https://www.hackerrank.com/challenges/alphabet-rangoli
N = int(input().strip())
letters = 'abcdefghijklmnopqrstuvwxyz'
w = ((N + N - 1) * 2) - 1


def make_rangoli(x):
    lset = letters[N-x:N]
    lset = lset[::-1]
    lset += letters[N-x-1:N]
    print('-'.join(list(lset)).center(w, '-'))


for x in range(N):
    make_rangoli(x)

for x in range(N-2, -1, -1):
    make_rangoli(x)


# Capitalize! - https://www.hackerrank.com/challenges/capitalize
words = input().strip().split(' ')
print(' '.join([word.capitalize() for word in words]))


# The Minion Game - https://www.hackerrank.com/challenges/the-minion-game
vowels = 'AEIOU'
word = input().strip()

kevin, stuart = 0, 0
for i, l in enumerate(word):
    if l in vowels:
        kevin += len(word) - i
    else:
        stuart += len(word) - i

if kevin > stuart:
    print('Kevin {}'.format(kevin))
elif stuart > kevin:
    print('Stuart {}'.format(stuart))
else:
    print('Draw')


# Merge the Tools! - https://www.hackerrank.com/challenges/merge-the-tools
S, K = input().strip(), int(input().strip())
T = [S[c:c+K] for c in range(0, len(S), K)]
result = []
for t in T:
    result.append(''.join([ch for i, ch in enumerate(t) if ch not in t[:i]]))
print(*result, sep='\n')


