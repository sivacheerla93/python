def sum(*nums):
    total = 0
    for n in nums:
        total += n
    return total


def wish(*names, message="Hi"):
    for n in names:
        print(message, n)


def wish2(*names, message="Hi", footer):
    for n in names:
        print(message, n)
    print(footer)


# kwargs(**something) prints in the form of keys and values, i.e.,dict
def print_values(**details):
    print(details)
    print(type(details))


print(sum(10, 20, 30))
print(sum(10, 20, 30, 50, 90))
wish("Siva", "Raju", "Ramesh")
wish("Siva Cheerla!", message="Hello")
wish2("Siva", "Raju", message="Welcome", footer="Bye all!")
print_values(n1=10, n=20, n3=30, name="Siva")
print_values(n1=10, n2=[20, 30, 40, 50])
