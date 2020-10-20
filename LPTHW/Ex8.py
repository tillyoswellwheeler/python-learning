# ------------------------------------
# LPTHW  -- Ex8. Printing, Printing
# ------------------------------------

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try you",
    "Own text in here.",
    "Maybe a poem",
    "or a song?"
))
