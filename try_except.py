#------------------------------------
# Python Learning -- Try Except
#------------------------------------

#------------------------------------
# Initial Code

# number = int(input("Enter a number: "))
# print(number)

#------------------------------------
# Code with Basic Try and Except added

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid Input")

#------------------------------------
# Code with further Try and Except added

try:
    value = 10 / 0 # Comment and uncomment to have the first exception to be activated
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid Input")
