# ------------------------------------
# LPTHW  -- Ex15. Reading Files
# ------------------------------------

from sys import argv

# this means when you run the python, you need to run it with the name of the python command
# and the file you want to read in
script, filename = argv

# This opens the file and assigns it to a variable to use later
txt = open(filename)

# A string that passes through the filename given when you run the command
# This can happen because of the sys argv module
print(f"Here's your file {filename}:")
# This reads the saved txt from the txt variable above
print(txt.read())

# This print outputs a string and then asks the user for input
# If the user types in a valid txt file it saves to the variable file_again
# If you had another txt file in the same directory you could pass it through here by using its name
print("Type the filename again:")
file_again = input("> ")

# This opens the file and saves the output to the variable txt_again
txt_again = open(file_again)

# This uses the read() module to read what is in txt_again.
print(txt_again.read())

txt_again.close()
txt.close()
