# A01 - Bit Counting - https://www.codewars.com/kata/bit-counting
def countBits(n):
    return bin(n).count('1')


# A02 - Algebraic string - https://www.codewars.com/kata/algebraic-string
def sum_prod(strexpression):
    value = eval(strexpression)
    return '%.5e' % value


def bp_sum_prod(strexpression):
    return "%.5e" %(eval(strexpression))


# A03 - Number , number ... wait LETTER ! - https://www.codewars.com/kata/number-number-dot-dot-dot-wait-letter
def do_math(s) :
    mixed = s.split()
    alphanum = []
    for m in mixed:
        alphanum.append((int(''.join(d for d in m if d.isdigit())), ''.join(a for a in m if a.isalpha())))
    alphanum.sort(key=lambda x: x[1])
    result = 0
    for i in range(len(alphanum)):
        if i == 0 or i % 4 == 1:
            result += alphanum[i][0]
        elif i % 4 == 2:
            result -= alphanum[i][0]
        elif i % 4 == 3:
            result *= alphanum[i][0]
        else:       #i is divisible by 4
            result /= alphanum[i][0]
    return int('{:.0f}'.format(result))


# A04 - The Supermarket Queue - https://www.codewars.com/kata/the-supermarket-queue
def queue_time(customers, n):
    if not customers:
        return 0
    if len(customers) == 1:
        return customers[0]
    if n >= len(customers):
        return max(customers)
    if n == 1:
        return sum(customers)
    time = [0 for _ in range(n)]
    for i in customers:
        mn, idx = min((time[x], x) for x in range(n))
        time[idx] += i
    return max(time)


def bp_queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)


# A05 - Tribonacci Sequence - https://www.codewars.com/kata/tribonacci-sequence
def tribonacci(signature,n):
    if n <= 3: return signature[:n]
    else:
        a = 0
        b = 1
        c = 2
        while c < n - 1:
            signature.append(signature[a] + signature[b] + signature[c])
            a += 1
            b += 1
            c += 1
        return signature


def bp_tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res


# A06 - Format a string of names like 'Bart, Lisa & Maggie'. -
# https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie
def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    else:
        justnames = [name['name'] for name in names]
        name_list = justnames[:-2]
        name_list.append(' & '.join(justnames[-2:]))
        return ', '.join(name_list)


def bp_namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


# A07 - Stop gninnipS My sdroW! - https://www.codewars.com/kata/stop-gninnips-my-sdrow
def spin_words(sentence):
    words = sentence.split(' ')
    result = []
    for word in words:
        if len(word) > 4:
            result.append(word[::-1])
        else:
            result.append(word)

    return ' '.join(result)


def bp_spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


# A08 - Find The Duplicated Number in a Consecutive Unsorted List - Tougher Version -
# https://www.codewars.com/kata/find-the-duplicated-number-in-a-consecutive-unsorted-list-tougher-version
def find_dup(arr):
    # returns sum of array - sum of consecutive integers 1 - len(arr) - 1
    return sum(arr) - ((len(arr) - 1) * len(arr) // 2)


def bp_find_dup(arr):
    return sum(arr) - sum(range(1, max(arr)+1))


# A09 - Persistent Bugger. - https://www.codewars.com/kata/persistent-bugger
def persistence(n):
    arr = list(str(n))
    if len(arr) == 1:
        return 0
    return 1 + persistence(reduce(lambda x, y: int(x) * int(y), arr))


import operator


def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i


# A10 - Build Tower - https://www.codewars.com/kata/build-tower
def tower_builder(n_floors):
    width = 1 + (n_floors - 1) * 2
    rpt = 1
    result = []
    for _ in range(n_floors):
        result.append(('*' * rpt).center(width, ' '))
        rpt += 2
    return result


def bp_tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


# A11 - Find the odd int - https://www.codewars.com/kata/find-the-odd-int
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i


# A12 - Decode the Morse code - https://www.codewars.com/kata/decode-the-morse-code
def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    result = ''
    morseCode = morseCode.strip(' ')
    words = morseCode.split('   ')
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            result += MORSE_CODE[letter]

        result += ' '

    return result[:-1]

    # return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')


def bp_decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))


# A13 -


# A14 -


# A15 -


# A16 -


# A17 -


# A18 -


# A19 -


# A20 -
