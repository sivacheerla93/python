# varible scopes: LEGB i.e., Local Enclosing Global Built-in
a = 10  # Global var


def f1():
    b = 20  # Enclosing var

    def f2():
        c = 30  # Local var
        print(a, b, c)

    f2()


f1()
