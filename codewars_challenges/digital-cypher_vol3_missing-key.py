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

# -----------------------------------------
# Stage 1 -- Create dic for digital cypher
# --->

import numpy as np

# import re

digital_cypher = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
    "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
    "z": 26
}


def user_string_to_list():  # Change the user string to a list so that you can use the list to search the dict
    user_string = input("What word do you want to encrypt? ").lower()
    string_list = list(user_string)
    return string_list


def check_list_against_dict():  # create a list of letters passed through the dictionary
    string_list = user_string_to_list()
    out = [digital_cypher[letter] for letter in string_list]
    return out  # The output is the code


def difference_code_dict():
    out = list(check_list_against_dict())  # New variable with words code
    int_list = user_input_code()  # New variable with the user input code
    arrays = []  # Adding the two lists to an array
    arrays.append(out)
    arrays.append(int_list)
    array_mat = np.array(arrays)  # Convert the list of lists to an array
    difference = np.subtract(array_mat[0], array_mat[1])
    positive_result = abs(difference)  # Converting to positive ints
    return positive_result


def pattern_identify():
    sequence = difference_code_dict()
    # create empty list
    # store sequence[0] as a variable
    # use a for loop to run through the list
    # while index != sequence[0] variable
    # add index value to empty list
    # if index == sequence[0] variable
    # check next index == empty list [1]
    # if next index == empty list [1] then return empty list
    result = []
    first_num = sequence[0]
    second_num = sequence[1]
    for index in sequence:
        while index != first_num:
            result.append(index)
            print(result)
            if index == first_num:
                if index == second_num:


#    print(first_num)
#    print(result)


def user_input_code():
    input_code = input("What code do you want to use to encrypt it? **hint** separate with space: ")
    str_list = input_code.split()  # This turns the str into a list
    ints_code_list = [int(i) for i in str_list]  # This loops through the list and changes each item to an int.
    return ints_code_list


# difference_code_dict()
pattern_identify()
#
# print(check_list_against_dict())


# # using ''.join makes the new list a single string
# print(''.join(out))