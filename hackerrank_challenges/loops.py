#----------------------------------------------
# HackerRank Challenges -- Division
#----------------------------------------------

#------------------------------------
# Task

# Read an integer N . For all non-negative integers i < N , print i sqaured . See the sample for details.

# INPUT TYPE
#--- The first and only line contains the integer, N .

def square_by(n):
    i_squared = 0
    for i in range(n):
        i_squared = i * i
        print(i_squared)
    return i_squared

square_by(5)

