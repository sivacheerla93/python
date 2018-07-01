class Base1(object):
    def fun(self):
        print("fun() in Base1")


class Base2(object):
    def fun(self):
        print("fun() in Base2")


class Derived(Base1, Base2):
    pass


d = Derived()
d.fun()
