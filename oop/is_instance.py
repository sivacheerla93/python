class Employee:
    pass


class Manager:
    pass


e = Employee()
print(e)
# returns True if object e belongs to class Employee
print(isinstance(e, Employee))
# object is also super class, Employee is derived from object
print(isinstance(e, object))
print(isinstance(e, Manager))
