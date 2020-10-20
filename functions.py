#------------------------------------
# Python Learning -- Functions
#------------------------------------

#------------------------------------
# Creating a function

def say_hi(name, age): # define the function name and what parameters it requires
    print("Hello {}, you are {}".format(name, age)) # What the function is displaying to the user

say_hi("Mike", 35) #Calling the function

#------------------------------------
# Output and RETURN

def cube(num):
    cube_num = num * num * num
    return cube_num # Return breaks us out of the function

print(cube(3))