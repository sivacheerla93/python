# To be frank python doesn't support method overloading like other languages,
# but it can do like that by overriding old method
class Test:
    def fun(self, x):
        print("First fun!")

    def fun(self, y):
        print("Second fun!")

    def fun(self, z):
        print("Third fun!")


v = Test()
# only Third fun will be called, First fun and Second fun will be gone
v.fun(10)
v.fun(20)
v.fun(30)
