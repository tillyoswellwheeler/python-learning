# ------------------------------------
# HackerRank Challenge
# ------------------------------------

# ------------------------------------
# Task
# You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of is not equal to . Here,
#
# Input Format
#
# Four integers  and  each on four separate lines, respectively.
#
# Constraints
#
# Print the list in lexicographic increasing order.

# ---- For Loop (without list comprehension)
# x = int(input())
# y = int(input())
# n = int(input())
#
# ar = []
# p = 0
#
# for i in range(x + 1):
#     for j in range(y + 1):
#         if(i + j) != n:
#           ar.append([])
#           ar[p] = [i, j]
#           p += 1
#           print(ar)

# ---- For Loop (with list comprehension)
# x = int(input())
# y = int(input())
# n = int(input())
#
# ar = [[i, j] for i in range(x + 1) for j in range(y + 1) if ((i + j) != n)]
# # p = 0
#
# print(ar)

# --- ANSWER
x = int(input())
y = int(input())
z = int(input())
n = int(input())

ar = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]

print(ar)