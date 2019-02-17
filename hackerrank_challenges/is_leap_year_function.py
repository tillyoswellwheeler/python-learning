# ------------------------------------
# HackerRank Challenge
# ------------------------------------

# ------------------------------------
# Task
# You are given the year, and you have to write a function to check if the year is leap or not.
#
# Note that you have to complete the function and remaining code is given as template.

# NOTES
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.


def is_leap(year):
    leap = False
    isleap = True


    if year // 4:
        if year is not // 100:
        return isleap
    # Write your logic here

    return leap