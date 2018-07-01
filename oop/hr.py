class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

    def __str__(self):
        return "%s %d" % (self._name, self._salary)


class Manager(Employee):
    def __init__(self, name, salary, hra):
        super().__init__(name, salary)
        self._hra = hra

    # overriding get_salary() of super class
    def get_salary(self):
        return super().get_salary() + self._hra

    # overriding __str__() of super class
    def __str__(self):
        return super().__str__() + " %d" % self._hra


class ME(Employee):
    def __init__(self, name, salary, ta):
        super().__init__(name, salary)
        self._ta = ta

    # overriding get_salary() of super class
    def get_salary(self):
        return super().get_salary() + self._ta

    # overriding __str__() of super class
    def __str__(self):
        return super().__str__() + " %d" % self._ta


class Sr_Manager(Manager):
    def __init__(self, name, salary, hra, da):
        super().__init__(name, salary, hra)
        self._da = da

    # overriding get_salary() of manager class
    def get_salary(self):
        return super().get_salary() + self._da

    # overriding __str__() of manager class
    def __str__(self):
        return super().__str__() + " %d" % self._da


e = Employee("Mr. Bean", 50000)
print(e.get_salary())
print(e)
print()

m = Manager("Mr. Bill", 100000, 20000)
print(m.get_salary())
print(m)
print()

me = ME("Mr. Tom", 55000, 15000)
print(me.get_salary())
print(me)
print()

sm = Sr_Manager("Mr. Allison", 100000, 20000, 15000)
print(sm.get_salary())
print(sm)
