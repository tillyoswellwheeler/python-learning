#------------------------------------
# HackerRank Challenges -- If Statements
#------------------------------------

# ------------------------------------
# Task

# Given an integer, n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird


def if_n_conditional(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0:
            if n >= 2 and n <= 5:
                print("Not Weird")
            elif n >= 6 and n <= 20:
                print("Weird")
            elif n > 20:
                print("Not Weird")
            else:
                # Returned nullx
    else:
        # Returned null


if_n_conditional(22)

