# ------------------------------------
# LPTHW  -- Ex21. Functions can return something
# ------------------------------------

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a +b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math just with functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# a puzzle for extra credit
print("Here is a puzzle:")
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

# iq = 50/2 = 25
# weight = 180 * 25 = 4500
# height = 74 - 4500 = -4426
# age = 35 + -4426 = -4391
print("That becomes: ", what, "Can you do it by hand?")
