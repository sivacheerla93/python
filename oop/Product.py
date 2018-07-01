# class
class Product:
    # initializer or special method or can be call it as constructor
    def __init__(self, name, price=None):
        # instance variables
        self.name = name
        self.price = price

    # normal function
    def print(self):
        print("Name: ", self.name)
        print("Price: ", self.price)

    # Getter
    @property
    def net_price(self):
        return self.price * 1.12

    # special method to return as string
    def __str__(self):
        return "{0} {1}".format(self.name, self.price)

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.price > other.price


# object
p1 = Product("Iphone 6", 60000)
# prints details of p1 object
p1.print()
# it may give TypeError!
# p2 = Product()
p2 = Product("Iphone 5", 60000)
p2.print()
print()
#  it'll return memory location if we dont declare as function, not value! we've to declare a function __str__()
print(str(p1), "\n")
# it'll return false bcoz it compares addresses, might be different! we can create __eq__ function to et TRue!
# calls __eq__ method and negates!
print(p1 == p2, "\n")
# calls __gt__() method
print(p1.price > p2.price, "\n")
print(p1.net_price)
