#------------------------------------
# Python Learning -- If Statements
#------------------------------------

#------------------------------------
# Creating a BASIC If Statement

#--- Changing the boolean below affects the if statement output
is_male = False

if is_male:
    print("You are a male")
else:
    print("You are a female")

#------------------------------------
# Creating an OR If Statement

is_tall = True
is_male = False

if is_male or is_tall:
    print("You are a tall male or you are just a male or tall")
else:
    print("You are a female")

# ------------------------------------
# Creating an AND If Statement

    is_tall = True
    is_male = False

    if is_male or is_tall:
        print("You are a tall male or you are just a male or tall")
    else:
        print("You are a female")

# ------------------------------------
# Creating an IS If Statement

    is_tall = True
    is_male = False

    if is_male or is_tall:
        print("You are a tall male or you are just a male or tall")
    else:
        print("You are a female")

# ------------------------------------
# Using comparison operators -- INT

def min_number(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3


print(min_number(300, 60, 20))

# ------------------------------------
# Using comparison operators -- STR

def check_strings():
    string1 = input("Put in your word to check: ")
    string2 = input("Put in your word to check: ")
    if string1 == string2:
        print("Your words are the same")
        return True
    else:
        print("Your words are not the same!")
        return False

check_strings()


