#----------------------------------------------
# HackerRank Challenges -- Arithmetic Operators
#----------------------------------------------

# ------------------------------------
# Task

# Read two integers from STDIN and print three lines where:
#--- The first line contains the sum of the two numbers.
#--- The second line contains the difference of the two numbers (first - second).
#--- The third line contains the product of the two numbers.
#
# INPUT TYPE
#--- The first line contains the first integer, a . The second line contains the second integer, b .

def sum_numbers(a, b):
    result = a + b
    return result

def subtract_numbers(a, b):
    result = a - b
    return result

def multiply_numbers(a, b):
    result = a * b
    return result

print(sum_numbers(2, 4))
print(subtract_numbers(3, 4))
print(multiply_numbers(2, 3))