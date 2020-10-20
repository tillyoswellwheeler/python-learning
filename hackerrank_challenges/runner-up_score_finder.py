# ------------------------------------
# HackerRank Challenge
# ------------------------------------

# ------------------------------------
# Task
#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# --- Input Format

# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# Pseudocode
# First stage order the list highest to lowest
# Second stage select and print index 1


if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    # print(arr) # checking

    scores_no_duplicates = list(arr)
    scores_no_duplicates.sort(reverse=True)
    # print(scores_no_duplicates)
    runnerup_score = scores_no_duplicates[1]

    print(runnerup_score) # checking