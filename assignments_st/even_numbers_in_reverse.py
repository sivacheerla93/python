num = int(input("Enter a number to get even numbers in reverse order: "))
for i in range(num, 1, -1):
    if i % 2 == 0:
        print(i)
