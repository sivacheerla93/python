import random

input = int(input("Please enter your guess: "))
number = random.randint(1, 10)

if number == input:
    print("Well done - you guessed it!")
else:
    print("Too bad - better luck next time!")


# Input - Please enter your guess: 3
# Output - Well done - you guessed it!


# Input - Please enter your guess: 4
# Output - Too bad - better luck next time!