#----------------------------------------------
# HackerRank Challenges -- Division
#----------------------------------------------

# ------------------------------------
# Task

# Read two integers and print two lines. The first line should contain integer division,  a//b .
# The second line should contain float division, a/b .
#
# You don't need to perform any rounding or formatting operations.

# INPUT TYPE
#--- The first line contains the first integer, a . The second line contains the second integer, b .

def calc_division(a, b):
    integer_div = a // b
    float_div = a / b
    print(integer_div)
    print(float_div)
    return integer_div, float_div

calc_division(a,b)