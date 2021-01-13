# ------------------------------------
# LPTHW  -- Ex16. Reading and Writing Files
# ------------------------------------

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do this hit CTRL-C.")
print("I you want to do this hit ENTER.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to a file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()
