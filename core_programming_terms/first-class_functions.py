# ------------------------------------------
# Programming Terms -- First-class Functions
# ------------------------------------------


def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, array_list): # The func is a placeholder for any function you could input. By inputting that function you can utilise its functionality.
    result = [func(i) for i in array_list]
    return result

# def my_map(func, array_list):
#     result = []
#     for i in array_list:
#         result.append(func(i))
#     return result

squares = my_map(square, [1, 2, 3, 4, 5])
cube = my_map(cube, [1, 2, 3, 4, 5])

print(squares)
print(cube)
