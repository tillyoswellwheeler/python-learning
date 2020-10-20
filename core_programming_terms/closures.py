# ------------------------------------
# Programming Terms -- Closures
# ------------------------------------


def outer_func():
    message = "Hi"

    def inner_func():
        print(message) # Free variable

    return inner_func # Returned (stored) but not executed


my_func = outer_func() # This is equal to the returned stored inner_func function

my_func() # By executing, adding (), we add () to the inner_func that means that we execute the inner_func functionality.
my_func() # Thereby printing or executing the stored inner_function output value at a later time.