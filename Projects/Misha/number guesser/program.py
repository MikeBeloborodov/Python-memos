from http.cookies import CookieError
import os
import random
import msvcrt
import math

def check_for_smallest_or_biggest_number(number, guess):
    collected_data = guess[3]
    if collected_data[0] == collected_data[1]:
        print(f"Yay! It took me {guess[2]} times to guess {collected_data[0]}...")
        print("Press any key to exit the program.")
        msvcrt.getch()
        exit()
    if guess[4] == "more_than_0":
        if guess[0] == "bigger":
            collected_data[0] = number
        else:
            collected_data[1] = number
    else:
        if guess[0] == "bigger":
            collected_data[0] = number
        else:
            collected_data[1] = number
    return collected_data
          

def bigger_number(first_guess):
    min_max_list = first_guess[3]
    my_guess = random.randint(min_max_list[0] + 1, min_max_list[1] - 1)
    os.system('CLS')
    print(f"Is it {my_guess}?")
    user_input = input("Enter your answer here: ")
    if user_input.casefold() == "yes":
        print(f"Yay! It took me {first_guess[2]} times to guess {my_guess}...")
        print("Press any key to exit the program.")
        msvcrt.getch()
        exit()
    else:
        first_guess[2] += 1
        print("Is it bigger?")
        user_input = input("Enter your answer here: ")
        if user_input == "yes":
            first_guess[0] = "bigger"
            first_guess[3] = check_for_smallest_or_biggest_number(my_guess, first_guess)
            first_guess[1] = my_guess
            bigger_number(first_guess)
        else:
            first_guess[0] = "smaller"
            first_guess[3] = check_for_smallest_or_biggest_number(my_guess, first_guess)
            first_guess[1] = my_guess
            smaller_number(first_guess)

def smaller_number(first_guess):
    min_max_list = first_guess[3]
    my_guess = random.randint(min_max_list[0] + 1, min_max_list[1] - 1)
    os.system('CLS')
    print(f"Is it {my_guess}?")
    user_input = input("Enter your answer here: ")
    if user_input.casefold() == "yes":
        print(f"Yay! It took me {first_guess[2]} times to guess {my_guess}...")
        print("Press any key to exit the program.")
        msvcrt.getch()
        exit()
    else:
        first_guess[2] += 1
        print("Is it bigger?")
        user_input = input("Enter your answer here: ")
        if user_input == "yes":
            first_guess[0] = "bigger"
            first_guess[3] = check_for_smallest_or_biggest_number(my_guess, first_guess)
            first_guess[1] = my_guess
            bigger_number(first_guess)
        else:
            first_guess[0] = "smaller"
            first_guess[3] = check_for_smallest_or_biggest_number(my_guess, first_guess)
            first_guess[1] = my_guess
            smaller_number(first_guess)

def init_number_positive(first_guess):
    begger_smaller = first_guess[0]
    if begger_smaller == "bigger":
        bigger_number(first_guess)
    else:
        smaller_number(first_guess)

def init_number_negative(first_guess):
    begger_smaller = first_guess[0]
    if begger_smaller == "bigger":
        bigger_number(first_guess)
    else:
        smaller_number(first_guess)

def number_guesser(first_guess):
    my_guess = first_guess[1]
    if my_guess > 0:
        init_number_positive(first_guess)
    else:
        init_number_negative(first_guess)

def initial_guess():
    print("Is it bigger than 0?")
    user_input = input("Enter your answer here: ")
    if user_input.casefold() == "yes":
        my_guess = random.randint(1, 100)
        os.system('CLS')
        print(f"Is it {my_guess}?")
        user_input = input("Enter your answer here: ")
        if user_input.casefold() == "yes":
            print(f"Yay! {my_guess} was my first guess!")
            print("Press any key to exit the program.")
            msvcrt.getch()
        else:
            print("Is it bigger?")
            user_input = input("Enter your answer here: ")
            if user_input.casefold() == "yes":
                return ["bigger", my_guess, 1, [my_guess + 1, 100], "more_than_0"]
            else:
                return ["smaller", my_guess, 1, [1, my_guess], "more_than_0"]
    else:
        my_guess = random.randint(-100, 1)
        os.system('CLS')
        print(f"Is it {my_guess}?")
        user_input = input("Enter your answer here: ")
        if user_input.casefold() == "yes":
            print(f"Yay! {my_guess} was my first guess!")
            print("Press any key to exit the program.")
            msvcrt.getch()
        else:
            print("Is it bigger?")
            user_input = input("Enter your answer here: ")
            if user_input.casefold() == "yes":
                return ["bigger", my_guess, 1, [my_guess, -1], "less_than_0"]
            else:
                return ["smaller", my_guess, 1, [-100, my_guess], "less_than_0"]

def main_program():
    os.system('CLS')
    print("Please guess any number.")
    print("I will ask you some questions about this number.")
    print("Type yes or no.")
    first_guess = initial_guess()
    number_guesser(first_guess)

main_program()
