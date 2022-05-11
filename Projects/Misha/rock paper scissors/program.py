import os
import random
import msvcrt

def game(user_choice, items_list, score):
    computer_choice = items_list[random.randint(0, 2)]
    if user_choice == computer_choice:
        print(f"Computer chooses {user_choice}, it's a draw!")
        print(f"Score: Computer - {score[0]}\tPlayer - {score[1]}")
    elif user_choice == "rock" and computer_choice == "paper":
        print(f"Computer chooses {computer_choice}, computer wins!")
        score[0] += 1
        print(f"Score: Computer - {score[0]}\tPlayer - {score[1]}")
    elif user_choice == "rock" and computer_choice == "scissors":
        print(f"Computer chooses {computer_choice}, player wins!")
        score[1] += 1
        print(f"Score: Computer - {score[0]}\tPlayer - {score[1]}")
    elif user_choice == "paper" and computer_choice == "scissors":
        print(f"Computer chooses {computer_choice}, computer wins!")
        score[0] += 1
        print(f"Score: Computer - {score[0]}\tPlayer - {score[1]}")
    elif user_choice == "paper" and computer_choice == "rock":
        print(f"Computer chooses {computer_choice}, player wins!")
        score[1] += 1
        print(f"Score: Computer - {score[0]}\tPlayer - {score[1]}")
    elif user_choice == "scissors" and computer_choice == "paper":
        print(f"Computer chooses {computer_choice}, computer wins!")
        score[0] += 1
        print(f"Score: Computer - {score[0]}\tPlayer - {score[1]}")
    elif user_choice == "scissors" and computer_choice == "paper":
        print(f"Computer chooses {computer_choice}, player wins!")
        score[1] += 1
        print(f"Score: Computer - {score[0]}\tPlayer - {score[1]}")
    print("Press any button to continue.")
    msvcrt.getch()

def main_program():
    items_list = ["rock", "paper", "scissors"]
    score = [0, 0]
    while True:
        os.system('CLS')
        print("Welcome to rock, paper, scissors game!")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("4 - Exit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            user_choice = "rock"
            game(user_choice, items_list, score)
        elif user_choice == "2":
            user_choice = "paper"
            game(user_choice, items_list, score)
        elif user_choice == "3":
            user_choice = "scissors"
            game(user_choice, items_list, score)
        elif user_choice == "4":
            os.system('CLS')
            print(f"Filal score: Player - {score[1]}\tComputer - {score[0]}")
            print("Goodbye!")
            msvcrt.getch()
            exit()
        else:
            print("Error. Try again")

main_program()
