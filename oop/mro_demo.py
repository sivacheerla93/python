class Base1():
    def __init__(self):
        print("__init__ of Base1")

    def fun(self):
        print("Fun() in Base1")


class Base2():
    def fun(self):
        print("Fun() in Base2")


class Derived(Base1, Base2):
    def fun(self):
        Base1.fun(self)
        Base2.fun(self)
        print("Fun() in derived")


d = Derived()
d.fun()
