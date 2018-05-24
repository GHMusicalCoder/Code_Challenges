# Say "Hello, World!" With Python - https://www.hackerrank.com/challenges/py-hello-world
# Write your code on the next line.
print('Hello, World!')


# Python If-Else - https://www.hackerrank.com/challenges/py-if-else
N = int(input().strip())

if N % 2 == 1 or (N > 5 and N < 21):
    print('Weird')
else:
    print('Not Weird')


# Arithmetic Operators - https://www.hackerrank.com/challenges/python-arithmetic-operators
a = int(input().strip())
b = int(input().strip())
print(a + b)
print(a - b)
print(a * b)


# Python: Division - https://www.hackerrank.com/challenges/python-division
a = int(input().strip())
b = int(input().strip())
print(a // b)
print(a / b)


# Loops - https://www.hackerrank.com/challenges/python-loops
n = int(input().strip())
for x in range(n):
    print(x**2)


# Write a function - https://www.hackerrank.com/challenges/write-a-function
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True

    return leap


# Print Function - https://www.hackerrank.com/challenges/python-print
print(*[x+1 for x in range(int(input()))], sep='', end='\n')
