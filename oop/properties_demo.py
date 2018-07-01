class Person:
    def __init__(self, fname, lname):
        self.__first = fname
        self.__last = lname

    @property  # Getter, to get something!
    def name(self):
        return self.__first + " " + self.__last

    @name.setter
    def name(self, value):
        self.__first, self.__last = value.split(" ")


p = Person("Siva", "Cheerla")
print(p.name)
p.name = "Srikanth Pragada"
print(p.name)
