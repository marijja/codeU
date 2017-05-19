#Given two strings, write a method to decide if one is a permutation of the other
# Magdalena Grodzińska

import re
from collections import Counter

# helper funtions

def validate_input(input):
    pattern = '[a-zA-Z]+'

    result = re.fullmatch(pattern, input)

    if result == None:
        return False
    else:
        return True

def check_letters_match(text1, text2):
    res1 = Counter(text1)
    res2 = Counter(text2)

    return res1 == res2

# main function

def check_permutation(text1, text2):
    if validate_input(text1) and validate_input(text2):
        return check_letters_match(text1, text2)
    else:
        return False

# tests

a = "abcdef"
b = "bdcfea"
c = "abcdeg"
d = "ab"
e = "ąb"

assert check_permutation(a, b) == True
assert check_permutation(e, d) == False
assert check_permutation(a, c) == False
assert check_permutation(a, d) == False
