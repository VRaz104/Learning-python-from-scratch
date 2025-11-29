#Dice rolling code
import random
total=0
choice=input("How many times would you like to roll the dice? ")
if not choice.isdigit():
    print("Please enter a valid number!")
    quit()
choice=int(choice)
if choice <= 0:
    print("You must roll the dice at least 1 time!")
    quit()   
for i in range(choice):
    roll=random.randint(1,6)
    print(f"Dice {i+1}: {roll}")
    total=total+roll
print(f"Your total is:{total}")