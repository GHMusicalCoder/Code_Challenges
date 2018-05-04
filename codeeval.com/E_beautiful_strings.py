import sys


# with open(sys.argv[1], 'r') as test_cases:
with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        letters = {}
        val = 26
        for c in test:
            if c.isalpha():
                if letters.get(c.lower()):
                    letters[c.lower()] += 1
                else:
                    letters[c.lower()] = 1

        sorted_letters = sorted(letters.items(), key=lambda v: (-v[1], v[0]))
        result = 0
        for i, v in sorted_letters:
            result += val * v
            val -= 1
        print(result)
