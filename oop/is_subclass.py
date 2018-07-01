class Employee(object):
    pass


class Manager(Employee):
    pass


print(issubclass(Manager, Employee))
print(issubclass(Manager, object))
print(issubclass(Employee, object))
print(issubclass(Employee, Manager))
