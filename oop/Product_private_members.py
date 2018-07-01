# class
class Product_private_members:
    # initializer or special method or can be call it as constructor
    def __init__(self, name, price=None):
        # instance variables
        # if we assigin __ before instance var then it'll become private!
        # if _ then it'll become protected
        # if no _ then it is public
        self.__name = name
        self.__price = price

    # normal function
    def print(self):
        print("Name: ", self.__name)
        print("Price: ", self.__price)


# object
p1 = Product_private_members("Iphone 6", 600000)
# prints details of p1 object
p1.print()
print()
# it may give TypeError!
# p2 = Product()
p2 = Product_private_members("Ipad Air 2")
p2.print()
print()
# prints members and attributes of p1 object
print(dir(p1))
print()

p1.price = 100000
# it doesn't print price 100000 as it is private member,
# it prints only 60000 and we can't assigin 100000 from outside. we can do it if it is public
p1.print()
print()
# if we want to get that value then we can use getattr()
print(getattr(p1, 'price'))
# the following will give an error
# print(getattr(p2, 'price'))
p2.__Product_private_members__price = 70000
print()
p2.print()
