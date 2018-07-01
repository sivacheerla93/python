# String can be either in single quotes or double quotes
print('Hello')
print("Hello")

# It is dynamically typed language!
# Even we get type of var, if we don't assign datatype
a = 10
print(a)
print(type(a))
a = "Python"
print(type(a))
# We get TypeError for below statement, must be str! not int as it is str!!
# a + 10

b = 10
print(b + 10)

# We get NameError for below statement, It should've defined!
# c = Python

# we can give multiple params to a print() method
print(10, 20, sep='-', end='*')
