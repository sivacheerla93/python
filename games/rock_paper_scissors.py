from random import randint

t = ["Rock", "Paper", "Scissors"]  # list of play options

computer = t[randint(0, 2)]  # assigning a random play to the computer

player = False  # set player to false

while player == False:
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie! Both are same!!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play, Check your spelling!")

    player = False  # loop continues...
    computer = t[randint(0, 2)]
