# ------------------------------------
# LPTHW  -- Ex5. More Variables and Printing
# ------------------------------------

my_name = 'TOW'
my_age = 300
my_height = 250
my_weight = 180
my_eyes = 'blue'
my_teeth = 'Yellow'
my_hair = 'Purple'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the meal.")

# this line is tricky try to get it completely right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")

# inches to cm
my_height_cm = my_height * 2.54
print(f"My height in cm is {my_height_cm}cm.")

my_weight_kg = round((my_weight * 0.45359237), 4)
print(f"My weight in kilograms is {my_weight_kg}kg.")
