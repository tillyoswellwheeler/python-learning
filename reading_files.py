#------------------------------------
# Python Learning -- Reading Files
#------------------------------------

#------------------------------------
# Read functionality

employee_file = open("test_file.txt", "r")

# Using r ==> read
# Using w ==> write
# Using a ==> append that means adding things onto the end of the file
# Using r+ ==> Read and Write

# print(employee_file.readable()) # Returns a boolean value to say if it can be read
# print(employee_file.read()) # Reads the files in its entirity
# print(employee_file.readline()) # Reads the first line and moves a cursor onto next line
# print(employee_file.readlines()) # Reads the lines and adds them to an array
# print(employee_file.readlines()[2]) # You can index into the readlines array list to get a specific line

#------------------------------------
# Using a For Loop with the read function

for line in employee_file.readlines():
    print(line)

employee_file.close()