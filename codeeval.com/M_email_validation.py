import sys
import re


with open(sys.argv[1], 'r') as test_cases:
# with open('data.txt', 'r') as test_cases:
    for test in test_cases:
        if test:
            print(str(bool(re.search("^[\w.\-+,!#$%^&*]+@[\w.\-+,!#$%^&*]*\.[\w,-]+$", test.strip()))).lower())
