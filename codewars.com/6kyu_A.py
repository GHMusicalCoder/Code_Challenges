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


# A06 -


# A07 -


# A08 -


# A09 -


# A10 -


# A11 -


# A12 -


# A13 -


# A14 -


# A15 -


# A16 -


# A17 -


# A18 -


# A19 -


# A20 -
