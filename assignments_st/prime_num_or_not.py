cond = True
while cond:
    num = int(input("Enter a number to check prime or not!(Enter 00 to stop) "))

    if num == 00:
        print("Thank you! See you again!!")
        break
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not a prime number!")
                print(i, "times", num // i, "is", num)
                break
        else:
            print("Prime number!")
    else:
        print("Not a prime number!")

# method 2
num = int(input("Enter number: "))
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print("Not a prime number!")
        break
else:
    print("Prime number!")
