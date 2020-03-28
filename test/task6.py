import random

number1 = random.randint(1, 6)
number2 = random.randint(1, 6)

if number1 == number2:
    print("You rolled a pair of " + str(number1) + "s!")
else:
    print("You rolled a " + str(number1) + " and a " + str(number2))


# Output - You rolled a pair of 3s!

# Output - You rolled a 1 and a 3