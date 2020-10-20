#-----------------------------------------
# Python Learning -- 2D & Nested Loops
#-----------------------------------------

#-----------------------------------------
# Creating a 2D array

number_grid = [
    [1, 3, 4],
    [3, 4, 5],
    [3, 6, 7],
    [2]
]

#-----------------------------------------
# Accessing rows and cols

print(number_grid[0][1])

#-----------------------------------------
# Accessing rows using a For Loop

for row in number_grid:
    print(row)

#-----------------------------------------
# Accessing cols using a NESTED For Loop

for row in number_grid:
    for col in row:
        print(col)