# ------------------------------------
# LPTHW  -- Ex18. Names, Variables, Code, Functions
# ------------------------------------

# similiar to how argv works
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# defining a functions arguments
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# takes one arguement
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing!")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First")
print_none()
