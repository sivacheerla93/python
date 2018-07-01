a = eval(input("Enter 1st number! "))
b = eval(input("Enter 2nd number! "))

print("Numbers you've entered before swap! are: ", a, b)

c = a
a = b
b = c

print("After swapping: ", a, b)
print("After swapping: {} {}".format(a, b))  # Different way of printing

a, b = 25, 30
a, b = b, a
print(a, b)
