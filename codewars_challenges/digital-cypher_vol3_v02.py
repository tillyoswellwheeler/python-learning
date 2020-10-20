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

# ----------------------------------------------------
# Stage 1 -- Imports and Create dic for digital cypher
# --->

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:20:38 2019

@author: matildaoswell-wheeler
"""

import string
import numpy as np
import itertools as itr

alpha = list(string.ascii_lowercase)
values = list(range(1, 27))
dictionary = dict(zip(alpha, values))


def find_the_key(word, key):
    letter_values = [dictionary[letter] for letter in word]
    key_value = np.array(key)
    letter_np = np.array(letter_values)
    list_key = (key_value - letter_np).tolist()
    #    str_key = ''.join(map(str, list_key))
    itr_str_key = iter(list_key)
    print(dir(itr_str_key))
    first_num = list_key[0]
    print(first_num)
    second_num = list_key[1]
    print(second_num)
    check_dict = []
    not_valid = []
    for ch in itr_str_key:
        if ch in check_dict:
            if ch == first_num:
                if next(ch) is second_num:
                    print(ch)
                    print(ch[:+1])
                    not_valid.append(ch)
                    return str(check_dict)
                elif ch[:+1] == None:
                    not_valid.append(ch)
                else:
                    continue
            elif ch == first_num and ch[:+1] != second_num:
                check_dict.append(ch)
            elif ch[:-1] != list_key[1] or ch[:-1] is None:
                not_valid.append(ch)
            else:
                check_dict.append(ch)
        else:
            check_dict.append(ch)
    return str(check_dict)


find_the_key("scout", [20, 12, 18, 30, 21])
find_the_key("masterpiece", [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])
find_the_key("nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20])
