# -*- coding: utf-8 -*-

# -----------------------------------------------
# CodeWars -- Digital cypher vol 3 - missing key
# -----------------------------------------------

# Task
# Write a function that accepts a message string and an array of integers code. As the result, return the key that was used to encrypt the message. The key has to be shortest of all possible keys that can be used to code the message: i.e. when the possible keys are 12 , 1212, 121212, your solution should return 12.
#
# Input / Output:
# The message is a string containing only lowercase letters.
# The code is an array of positive integers.
# The key output is a positive integer.

import string
import numpy as np
import itertools as itr

alpha = list(string.ascii_lowercase)
values = list(range(1, 27))
dictionary = dict(zip(alpha, values))


def find_the_key(message, code):
    message = list(string.ascii_lowercase)
    code = list(range(1, 27))
    dictionary = dict(zip(code, message))
    for size in range(1, len(code) +1): # Starting from 1, using the range of the length of the code +1 because of how range in python is calculated
        key = dictionary[:size] # Assigning a variable which use the diffs key and goes from the start index to the end index
        if (key * len(code))[:len(code)] == dictionary: # as it loops through it save the first key then times that by the length tp see andthen goes to the end of the code and if that equals the diff it returns the variable and if not it carries on.
            return int(key)


# def find_the_key(message, code):
#     diffs = "".join( str(c - ord(m) + 96) for c, m in zip(code, message) ) # This creates the difference between the string assigned and the code given
#     for size in range(1, len(code) +1): # Starting from 1, using the range of the length of the code +1 because of how range in python is calculated
#         key = diffs[:size] # Assigning a variable which use the diffs key and goes from the start index to the end index
#         if (key * len(code))[:len(code)] == diffs: # as it loops through it save the first key then times that by the length tp see andthen goes to the end of the code and if that equals the diff it returns the variable and if not it carries on.
#             return int(key)

find_the_key("scout", [20, 12, 18, 30, 21])
find_the_key("masterpiece", [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])
find_the_key("nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20])