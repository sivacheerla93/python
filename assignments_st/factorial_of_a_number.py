num = int(input("Enter a number to get factorial! "))
fact = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial for 0 is: 0")
else:
    for i in range(1, num + 1):
        fact *= i
    print("Factorial for ", num, "is: ", fact)

# method 2
num2 = int(input("Enter number for method 2: "))
facts2 = []
for i in range(1, num2 + 1):
    fact2 = 1
    for n in range(2, i + 1):
        fact2 *= n
    facts2.append(fact2)
for idx, f in enumerate(facts2, 1):
    print(idx, f)
