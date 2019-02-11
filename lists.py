#------------------------------------
# Python Learning -- Lists
#------------------------------------

#------------------------------------
# Creating a list

countries = ["France", "England", "Norway", "Italy", "Scotland"]

#------------------------------------
# Indexing a list

print(countries[2])

#------------------------------------
# Modifying a list

countries[2] = "Norge"

print(countries[2])

#-----------------------------------------#
# List Functions
#-----------------------------------------#

#--- print()
#--- extend("pass in new list to add")
#--- append()
#--- insert(first_param_insert_index, second_param_what_to_add)
#--- remove("thing_to_remove")
#--- clear() clears all of the list items
#--- pop() Removes the last element
#--- index("find an item in a list")
#--- count("see how many times the item appears in the list")
#--- sort() Sort the list A-Z or numbers in asc order
#--- reverse() Reverse the list order
#--- copy() Takes a copy of a pre-created list

#------------------------------------
# Appending a list

countries.append("Wales")
print(countries[5])

#------------------------------------
# Sorting a list

countries.sort()
print(countries[2])
