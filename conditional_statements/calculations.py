a = eval(input("Enter 1st number: "))
b = eval(input("Enter 2nd number: "))
c = eval(input(
    "Enter option(1. Addition, 2. Subtraction, 3. Multiplication, 4. Division): "))

if c == 1:
    print(a + b)
elif c == 2:
    print(a - b)
elif c == 3:
    print(a * b)
elif c == 4:
    print(a // b)
else:
    print("Invalid option!")
