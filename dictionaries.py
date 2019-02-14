#-----------------------------------------
# Python Learning -- Dictionaries
#-----------------------------------------

#-----------------------------------------
# Creating Dictionary

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

#--- Printing the whole dict
print(monthConversions)

#--- Print a specific value
print(monthConversions["Nov"])

#--- Print using get() via key searching
print(monthConversions.get("Dec"))

#--- Print using get() via key searching AND add a message to replace None output
print(monthConversions.get("December", "Not a valid key"))


