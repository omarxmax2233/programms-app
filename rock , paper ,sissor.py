import random

txt = "WELCOME TO ROCK, PAPER, SCISSORS!"
print(txt.center(100))

choose = ["rock", "paper", "scissor"]

player = True

while player:


    # choice of computer
    computer = random.choice(choose)
    # choice of player
    player_choice = input("Enter your choice > :  ")

    print(computer)

    # player == computer

    if player_choice == computer:
        print("Tie")

    # paper == rock
    elif player_choice == "paper" and computer == "rock":
        print("you win")
        # paper == scissor
    elif player_choice == "paper" and computer == "scissor":
        print("you lost")

        # rock == paper
    elif player_choice == "rock" and computer == "paper":
        print("you lost")
        # rock == scissor
    elif player_choice == "rock" and computer == "scissor":

        print("you win")

        # scissor == rock
    elif player_choice == "scissor" and computer == "rock":

        print("you lost")

        # scissor == paper

    elif player_choice == "scissor" and computer == "paper":

        print("you win")
