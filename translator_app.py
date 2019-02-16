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
# mystr = 'This is a string, with words!'
# wordList = re.sub("[^\w]", " ",  mystr).split()

import re


# a = [1, 2, 3, 4, 1, 5, 3, 2, 6, 1, 1]
# dic = {1: 10, 2: 20, 3: 'foo'}
#
# print([dic.get(n, n) for n in a])

def convert_weather(self, description):
    """
    Using a dictionary to create a switch statement alternative
    """
    conditions = {
        'clear sky': 'clear',
        'few clouds': 'clouds with some sunshine',
        'scattered clouds': 'cloudy',
        'broken clouds': 'cloudy',
        'shower rain': 'showers',
        'thunderstorm': 'thunder and lightning',
        'mist': 'fog'
    }

    if description in conditions:
        return conditions.get(description, "Look out of the window.")
    else:
        return description

def cockney_replace_words():
    words_list = user_string_input()

    cockney_slang = {
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

    if words_list in cockney_slang:
        return cockney_slang.get(words_list, )
    else:
        return words_list

def user_string_input():
    user_str = input("Enter your story for translation: ")
    words_list = user_str.split()

    print(words_list)
    return words_list



