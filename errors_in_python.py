# NameError
c = Python  # Python isn't string, it is var, so var should've defined

# TypeError
a = "Python"
a + 10  # can't assign int to str!

# IndentationError
if 10 > 20:
    print("False")  # print should be right sided by three spaces

# SyntaxError
if 10 % 10 == 0:  # If there's no colon, that is syntax error
    print("Even number!")
print("Odd number!")  # else is expected

# IndexError
# print("{0} since {1}".format(name))
