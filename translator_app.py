#-----------------------------------------
# Python Learning -- Translator App
#-----------------------------------------

#-----------------------------------------
# Cockney Rhyming Slang Translator and American Slang translatror
#---> Use a transaltor class with two sub classes of cockney and american

#---- RULES:
#---- words  --> phrases
# look --> butcher's hook
# talk --> rabbit and pork
# car --> jam jar
# phone --> dog and bone
# on one's own --> on one's Jack Jones
# pinch --> half-inch
# lie --> porky-pie
# skint --> boracic lint
# wig --> syrup of figs
# facts --> brass-tacks
# money --> bread and honey
# feet --> plates-of-meat
# wife --> trouble-and-strife
# eyes --> mince-pies
# road --> frog-and-toad
#

# AMERICAN WORDS
# looking good --> fleek
# having a meeting --> having a pow-wow
# that's crazy --> get out of here


# mystr = 'This is a string, with words!'
# wordList = re.sub("[^\w]", " ",  mystr).split()

import re


# a = [1, 2, 3, 4, 1, 5, 3, 2, 6, 1, 1]
# dic = {1: 10, 2: 20, 3: 'foo'}
#
# print([dic.get(n, n) for n in a])


# def cockney_replace_words():
#     words_list = user_string_input()
#
#     cockney_slang = {
#         "look": "butcher's hook",
#         "talk": "rabbit and pork",
#         "car": "jam jar",
#         "phone": "dog and bone",
#         "alone": "on one's Jack Jones",
#         "pinch": "half-inch",
#         "lie": "porky-pie",
#         "skint": "boracic lint",
#         "wig": "syrup of figs",
#         "facts": "brass-tacks",
#         "money": "bread and honey",
#         "feet": "plates-of-meat",
#         "wife": "trouble-and-strife",
#         "eyes": "mince-pies",
#         "road": "frog-and-toad",
#     }

import re

class Translation():
    def __init__(self, text_for_translation, dict_for_translation):
        self.text_for_translation = text_for_translation
        self.dict_for_translation = dict_for_translation
        if dict_for_translation == "cockney rhyming slang":
            dictionary = {
                "look": "butcher's hook",
                "talk": "rabbit and pork",
                "car": "jam jar",
                "phone": "dog and bone",
                "alone": "on one's Jack Jones",
                "pinch": "half-inch",
                "lie": "porky-pie",
                "skint": "boracic lint",
                "wig": "syrup of figs",
                "facts": "brass-tacks",
                "money": "bread and honey",
                "feet": "plates-of-meat",
                "wife": "trouble-and-strife",
                "eyes": "mince-pies",
                "road": "frog-and-toad",
            }
            # print(dictionary)
            return dictionary
        elif dict_for_translation == "american slang":
            dictionary = {
                "looking good" : "fleek",
                "having a meeting" : "having a pow-wow",
                "that's crazy" : "get out of here",
            }
            # print(dictionary)
            return dictionary
        else:
            print("Invalid Entry")
            return TypeError

trans_1 = Translation("Look at the facts", "")



    def make_trans_cockney(self, dict_cockney):
        words_list = user_string_input()
        word = words_list.group()
        print(dict_cockney.get(word.lower(), word))
        return dict_cockney.get(word.lower(), word)

    # translated = re.sub(r'\w+', maketrans(right_dict), sentence)
    # print (translated)
#
#     @staticmethod
#     def user_string_input():
#         user_str = input("Enter your story for translation: ")
#         words_list = user_str.split()
#
#         print(words_list)
#         return words_list
#
#
# if __main__ is


