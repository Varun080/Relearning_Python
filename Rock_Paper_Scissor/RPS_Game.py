import random

def computerschoise(user_choice,option):
    if user_choice == "rock":
        computer_pick = option[1]
    elif user_choice == "paper":
        computer_pick = option[2]
    elif user_choice == "scissors":
        computer_pick = option[0]
    return computer_pick

user_wins = 0
computer_wins = 0
option = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q" :
        print("LOOSER!!")
        break

    if user_input not in option:
        print("You can't even do this right. \n YOU DUMB PICE OF SHIT!!!")
        continue

    # random_Number = random.randint(0,2)

    # rock : 0, paper : 1, scissors : 2

    computer_pick = computerschoise(user_input,option)
    print("Computer picked",computer_pick+".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won! SUCKKER!!")
        user_wins +=1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won! SUCKKER!!")
        user_wins +=1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won! SUCKKER!!")
        user_wins +=1
    else:
        print("You lost! LOOSER!!")
        computer_wins +=1

    
print("I won", computer_wins ,"times!")
print("You won",user_wins,"times!")
print("FUCK YOU!")