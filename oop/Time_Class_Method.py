# whenever we use class method, the first param should be class itself! i.e., cls
class MyTime:
    name = "Siva Cheerla"

    @classmethod
    def create(cls):
        print("Class method is calling!")
        print(cls.name)


MyTime.create()


# example2
class MyTime2:
    @classmethod  # takes no parameters except cls
    def create(cls):
        return cls(10, 20, 30)

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)


t = MyTime2.create()
print(t)
