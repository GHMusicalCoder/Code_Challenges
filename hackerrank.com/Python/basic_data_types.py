# Lists - https://www.hackerrank.com/challenges/python-lists
loop = int(input())
l = []
for _ in range(loop):
    temp = input().strip().split(' ')
    c = temp[0]
    args = temp[1:]
    if c == 'print':
        print(l)
    else:
        a = ', '.join(args)
        eval('l.{}({})'.format(c, a))


# Tuples - https://www.hackerrank.com/challenges/python-tuples
no_need = input()
print(hash(tuple(map(int, input().strip().split(' ')))))


# List Comprehensions - https://www.hackerrank.com/challenges/list-comprehensions
X = int(input())
Y = int(input())
Z = int(input())
bad = int(input())
print([[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != bad])


# Find the Runner-Up Score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
who_cares = input()
the_list = [int(x) for x in input().split(' ')]
mv = max(the_list)
the_list[:] = (x for x in the_list if x != mv)
print(max(the_list))


# Nested Lists - https://www.hackerrank.com/challenges/nested-list
counter = int(input())
students = []
for x in range(counter):
    name = input().strip()
    grade = float(input().strip())
    students.append([name, grade])

lowest_grade = min(students, key=lambda k: k[1])[1]
filtered_students = [x for x in students if x[1] != lowest_grade]
second_lowest_grade = min(filtered_students, key=lambda k: k[1])[1]
bad_students_names = [x[0] for x in filtered_students if x[1] == second_lowest_grade]
bad_students_names = sorted(bad_students_names)
print(*bad_students_names, sep='\n')


# Finding the percentage - https://www.hackerrank.com/challenges/finding-the-percentage
counter = int(input().strip())
students = []
for i in range(counter):
    line = input().strip()
    temp = line.split(' ')
    students.append({'Name': temp[0], 'Maths': float(temp[1]), 'Physics': float(temp[2]), 'Chemistry': float(temp[3])})
get_name = input().strip()
s = [student for student in students if student['Name'] == get_name]
s = s[0]
avg_score = (s.get('Maths') + s.get('Physics') + s.get('Chemistry')) / 3
print('{:.2f}'.format(avg_score))


