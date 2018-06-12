def LongestWord(sen):
    # code goes here
    import re
    array = re.split('[^a-zA-Z]', sen)
    return sorted(array, key=len, reverse=True)[0]


# keep this function call here
print(LongestWord("Argument goes here"))    # should return Argument
print(LongestWord("Fun&!! time"))   # should return time
print(LongestWord("I love dogs"))   # should return love
