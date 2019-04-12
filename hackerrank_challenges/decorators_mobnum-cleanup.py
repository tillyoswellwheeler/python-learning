# ------------------------------------
# HackerRank Challenge
# ------------------------------------

# ------------------------------------
# Task
# You are given  mobile numbers. Sort them in ascending order then print them in the standard format shown below:
# +91 xxxxx xxxxx
#
# The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number.
# Alternatively, there may not be any prefix at all.
#
# ---- Input Format
# The first line of input contains an integer N, the number of mobile phone numbers.
# N lines follow each containing a mobile number.
#
# ---- Output Format
# Print N mobile numbers on separate lines in the required format.

def standard_mobnumber(mobilenumber):
    number = mobilenumber

    def clean_up():
        # check if there is a 0 at index 0
            # if there is remove
            # return indices 1-the end of the range
        # check