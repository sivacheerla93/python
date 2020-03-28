time = int(input("Please enter the time: "))

if 0 <= time <= 100:
    print("Missile is in Stage 1 flight")
elif 101 <= time <= 170:
    print("Missile is in Stage 2 flight")
elif 171 <= time <= 260:
    print("Missile is in Stage 3 flight")
else:
    print("Free flight (unpowered)")


# Input - Please enter the time: 50
# Output - Missile is in Stage 1 flight


# Input - Please enter the time: 150
# Output - Missile is in Stage 2 flight


# Input - Please enter the time: 250
# Output - Missile is in Stage 3 flight


# Input - Please enter the time: 350
# Output - Free flight (unpowered)