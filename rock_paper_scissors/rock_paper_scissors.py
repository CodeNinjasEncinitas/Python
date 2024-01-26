import time
import random

# list of possible choices for the computer
choices = ["rock", "paper", "scissors"]

while True:
    print("----------NEW GAME-----------")
    print("Type rock, paper, or scissors")
    player_choice = input("What is your choice? ").lower()
    # if player entered something that isn't rock, paper, or scissors
    if not player_choice in choices:
        print("BAD INPUT, RESETTING GAME")
        continue
    # simulate computer thinking and sleep for a little bit (in seconds)
    print("Computer is thinking...")
    time.sleep(1.5)
    # computer randomly picks one of the 3 choices
    computer_choice = choices[random.randint(0,2)]
    print("Computer choose: " + computer_choice)
    # if player chose rock
    if player_choice == "rock":
        if computer_choice == "rock":
            print("Tie!")
        elif computer_choice == "paper":
            print("You Lose!")
        elif computer_choice == "scissors":
            print("You Win!")
    # if player chose paper
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You Win!")
        elif computer_choice == "paper":
            print("Tie!")
        elif computer_choice == "scissors":
            print("You Lose!")
    # if player chose scissors
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("You Lose!")
        elif computer_choice == "paper":
            print("You Win!")
        elif computer_choice == "scissors":
            print("Tie!")
    
