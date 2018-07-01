# function definitions
def process():
    print("Processing... !")


def add(n1, n2):
    return n1 + n2


def line():
    for i in range(1, 25):
        print('_', end=" ")


def line2(length):
    for i in range(1, length):
        print("-", end="")


def line3(length=25):
    for i in range(1, length):
        print("_", end=" ")


def line4(length=45, char='*'):  # with two default arguments
    for i in range(1, length):
        print(char, end="")


# calling functions
process()
print(add(10, 40))
print(add("Siva ", "Cheerla"))
line()
print()
line2(50)
# line2() # which gives TypeError # refer follow syntax
# default arguments is the resolution # def line3(length=40)
print()
line3()
print()
line3(length=30)  # keyword arguments
print()
line4()
print()
line4(length=35, char='&')  # keyword arguments
