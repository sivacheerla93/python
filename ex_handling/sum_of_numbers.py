sum = 0
i = 1
error_count = 0
while i <= 5:
    try:
        n = int(input("Enter number: "))
        sum += n
        i += 1
    except ValueError:
        print("Invalid number!")
        error_count += 1
        if error_count == 2:
            print("2 invalid inputs given. Quitting..")
            break
else:
    avg = sum / 5
    print(avg)
print("The End!")
