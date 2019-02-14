#-----------------------------------------
# Python Learning -- Loops
#-----------------------------------------

#-----------------------------------------
# While Loops

# i = 1 # you have to initiate the variable value before the loop
#
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with loop")

#-----------------------------------------
# For Loops

#--- Looping through letters
# for letter in "How to Loop through a string":
#     print(letter)

#--- Looping through a list

# bt_cohort = ["Amanda", "Rachel", "Katie", "Seraphine", "Pam", "Mandy", "Loren"]
#
# for cohort in bt_cohort:
#     print(cohort)

#--- Looping through numbers/index in a range. It will not include the final number in the range.
# for index in range(10):
#     print(index)

#--- Looping through range with two arguments. Includes first number in print.
# for number in range(3, 10):
#     print(number)

#--- Looping through array using range and len()
# bt_cohort = ["Amanda", "Rachel", "Katie", "Seraphine", "Pam", "Mandy", "Loren"]
#
# for index in range(len(bt_cohort)): #The len() creates an index for each list item.
#     print(bt_cohort[index])

#--- CONDITIONALS AND LOOPS

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")