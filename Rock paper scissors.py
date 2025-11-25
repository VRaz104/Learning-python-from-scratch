#Rock, paper and scissors game!

import random
quit=False
computer_score=0
player_score=0
while quit==False:
    player_choice=str(input("Choose either rock, paper scissors, or you can quit by typing 'quit':"))
    if player_choice not in ["rock", "paper", "scissors", "quit"]:
        print("there was an error.")
        break
    computer_choice=random.choice(["rock", "paper", "scissors"])
    if computer_choice=="rock" and player_choice=="rock":
        print("There was a draw!")
    elif computer_choice=="rock" and player_choice=="paper":
        print("You won!")
        player_score+=1
    elif computer_choice=="rock" and player_choice=="scissors":
        print("You lost!")
        computer_score+=1
    elif computer_choice=="paper" and player_choice=="rock":
        print("You lost!")
        computer_score+=1
    elif computer_choice=="paper" and player_choice=="paper":
        print("There was a draw!")
    elif computer_choice=="paper" and player_choice=="scissors":
        print("You won!")
        player_score+=1
    elif computer_choice=="scissors" and player_choice=="rock":
        print("You won!")
        player_score+=1
    elif computer_choice=="scissors" and player_choice=="paper":
        print("You lost!")
        computer_score+=1
    elif computer_choice=="scissors" and player_choice=="scissors":
        print("There was a draw!")
    elif player_choice=="quit":
        quit=True
        break
    print(f"The score is {player_score} to {computer_score}!")
print("You decided to quit!")