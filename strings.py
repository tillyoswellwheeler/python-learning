#------------------------------------
# Python Learning -- Strings
#------------------------------------

#------------------------------------
# Using the print() function

print("Hello World")

#------------------------------------
# Using the print() with variable

name = "George"
time = "3:00"
age = 50

print("The long walk\n") # this EOL special character makes a new para
print("The long walk")
print("at " + time + " with " + name) # You can concatenate strings but not ints however you need to add spaces
print(name, "was older than he once was, being a grand old age of", age, ".")

#------------------------------------
# Working with strings

# Special characters with strings
print("Hello\nWorld") # Newline character. It works differently when within a string rather than EOL.
print("My name\" is Tilly") # Using a \ before a character means it will print

# Functions
name = "Tilly"

print(name.lower()) # lower() makes is all lowercase
print(name.lower().islower()) # You can stack functions on top of eachother
print(name.upper()) # upper() makes it all uppercase
print(name.islower()) # islower() isupper() asks for a True or False (Boolean) answer from the computer.
print(name.upper().isupper())
print(name.replace("Tilly", "Matilda")) # Replaces the string with a new string


# Indexing into a string
print(len(name)) # Gets the length of the string, how many characters there are.
print(name[0]) # Indexing into a string
# print(name.index("t")) # Here I tru searching for t but it cant find it however it returns an error
# lowercase_name = name.lower() # Instead I must convert the string to all lower, store it in a new variable
# print(lowercase_name.index("t")) # Here I run index on the new variable
print(name.lower().index("t")) # This works too