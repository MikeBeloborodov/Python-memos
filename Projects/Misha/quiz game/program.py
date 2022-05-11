import os
import msvcrt
import json

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Player:
    def __init__(self, name, score, password):
        self.name = name
        self.score = score
        self.password = password

def clear_console():
    os.system('CLS')

def load_questions():
    questions_txt = open(os.path.abspath("questions.txt"))
    questions = questions_txt.read()
    questions_txt.close()
    questions_dict = json.loads(questions)
    return questions_dict

def load_scoreboard():
    scoreboard_txt = open("scoreboard.txt")
    scoreboard_dict = json.loads(scoreboard_txt.read())
    scoreboard_txt.close()
    return scoreboard_dict

def draw_scoreboard():
    scoreboard = load_scoreboard()
    counter = 1
    clear_console()
    print("------     Quiz game    ------")
    for item in scoreboard:
        print(f"{counter} - " + scoreboard[item].get("player_name") + "\t\t" + scoreboard[item].get("player_score") + " points")
        counter += 1
    print("------------------------------")
    print("Press any key to exit back.")
    msvcrt.getch()


def save_scoreboard(player):
    scoreboard = load_scoreboard()
    check = False
    for item in scoreboard:
        if scoreboard[item].get("player_name") == player.name:
            scoreboard[item].update({"player_score" : str(player.score)})
            check = True
    if check == False:
        scoreboard.update({f"player_{len(scoreboard) + 1}" : {"player_name" : player.name, "player_score" : str(player.score)}})

    scoreboard_txt = open("scoreboard.txt", "w")
    scoreboard_json = json.dumps(scoreboard)
    scoreboard_txt.write(scoreboard_json)
    scoreboard_txt.close()

def make_new_question():
    text = input("Enter your question: ")
    answer = input("Enter the answer: ")
    new_question = Question(text, answer)
    return new_question

def save_new_question(questions_database, new_question):
    counter = 1
    last_id = 0
    for item in questions_database:
        if len(questions_database) == counter:
            last_id = int(item[9:]) + 1
        else:
            counter += 1

    questions_database.update({f"question_{str(last_id)}" : {"text" :
        f"{new_question.text}", "answer" : f"{new_question.answer}"
    }})

    questions_json = json.dumps(questions_database)
    database_txt = open("questions.txt", "w")
    database_txt.write(questions_json)
    database_txt.close()

def exit_game():
    clear_console()
    print("Thank you for playing! Press any key to exit.")
    msvcrt.getch()
    return False

def draw_main_menu():
    clear_console()
    print("------     Quiz game    ------")
    print("|                            |")
    print("| 1 - New game               |")
    print("| 2 - Make new questions     |")
    print("| 3 - Scoreboard             |")
    print("| 4 - Exit game              |")
    print("|                            |")
    print("------------------------------")

def get_user_main_menu_input():
    
    user_input = input("Please, enter your choice - ")

    if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4":
        while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4":
            print("Error. Please try again.")
            user_input = input("Please, enter your choice - ")

    return user_input

def draw_new_game_menu():
    clear_console()
    print("------     Quiz game    ------")
    print("|                            |")
    print("| 1 - New player             |")
    print("| 2 - Load player            |")
    print("| 3 - Exit back              |")
    print("|                            |")
    print("------------------------------")

def load_player(player_name, player_password):
    players_txt = open("players.txt")
    players_json = json.loads(players_txt.read())
    players_txt.close()
    check = False
    loaded_player_name = ""
    loaded_player_score = 0
    for item in players_json:
        if players_json[item].get("player_name") == player_name and players_json[item].get("player_password") == player_password:
            loaded_player_name = players_json[item].get("player_name")
            loaded_player_score = players_json[item].get("player_score")
            check = True
            print(f"Loading is complete! Welcome back, {loaded_player_name}!")
            print(f"You have {loaded_player_score} points.")
            player = Player(loaded_player_name, int(loaded_player_score), player_password)
            print("Press any key to continue.")
            msvcrt.getch()
            return player
    if check == False:
        print("Player name or password is incorrect.")
        print("Press any key to continue.")
        msvcrt.getch()
        return None
        
def create_new_player():
    clear_console()
    player_name = input("Enter your name: ")
    player_password = input("Enter your password: ")
    new_player = Player(player_name, 0, player_password)
    return new_player

def draw_game_screen(player, question):
    clear_console()
    print("------     Quiz game    ------")
    print(f"Player name - {player.name}")
    print(f"Score: {player.score}")
    print("")
    print("Question:")
    print(question["text"])
    print("------------------------------")

def get_player_answer():
    answer = input("Enter your answer here: ")
    return answer

def check_correct_answer(answer, question, player):
    if question["answer"].casefold() == answer.casefold():
        player.score += 10
        print("That's correct! +10 points!")
        print("Press any key to continue.")
        msvcrt.getch()
    else:
        print("It's not a correct answer :(")
        print("The answer was - " + question["answer"])
        print("-10 points to the player!")
        player.score -= 10
        print("Press any key to continue.")
        msvcrt.getch()

def draw_endgame_screen(player):
    clear_console()
    print("------     Quiz game    ------")
    print(f"Congratulations, {player.name}! You have earned {player.score} points!")
    print("You can check your score on the scoreboard.")
    print("")
    print("------------------------------")

def save_player(player):
    players_txt = open("players.txt")
    players_json = json.loads(players_txt.read())
    players_txt.close()
    check = False
    for item in players_json:
        if players_json[item].get("player_name") == player.name:
            players_json[item].update({f"player_score" : str(player.score)})
            check = True
        
    if check == False:
        players_json.update({f"player_{len(players_json) + 1}" : {"player_name" : player.name, "player_score" : str(player.score), "player_password" : player.password}})

    players_txt = open("players.txt", "w")
    players_txt.write(json.dumps(players_json))
    players_txt.close()

    print("Your profile is saved now.")
    print("Press any key to continue.")
    msvcrt.getch()

def start_the_game(player, questions):
    for question in questions:
        draw_game_screen(player, questions[question])
        answer = get_player_answer()
        check_correct_answer(answer, questions[question], player)
    draw_endgame_screen(player)
    save_scoreboard(player)
    save_player(player)

def new_player_mode():
    player = create_new_player()
    questions = load_questions()
    start_the_game(player, questions)

def apply_new_game_choice(user_input):
    if user_input == "1":
        new_player_mode()
    elif user_input == "2":
        clear_console()
        player_name = input("Please enter your name: ")
        player_password = input("Please enter your password: ")
        player = load_player(player_name, player_password)
        if player == None:
            return
        questions = load_questions()
        start_the_game(player, questions)
    else:
        return

def get_user_new_game_menu_input():
    user_input = input("Please, enter your choice - ")

    if user_input != "1" and user_input != "2" and user_input != "3":
        while user_input != "1" and user_input != "2" and user_input != "3":
            print("Error. Please try again.")
            user_input = input("Please, enter your choice - ")

    return user_input

def new_game():
    draw_new_game_menu()
    user_input = get_user_new_game_menu_input()
    apply_new_game_choice(user_input)

def apply_main_menu_choice(user_input, questions_database):
    if user_input == "1":
        new_game()
        return True
    elif user_input == "2":
        new_question = make_new_question()
        save_new_question(questions_database, new_question)
        return True
    elif user_input == "3":
        draw_scoreboard()
        return True
    else:
        return exit_game()

def main_menu():
    no_exit = True
    while no_exit:
        questions_database = load_questions()
        draw_main_menu()
        user_choice = get_user_main_menu_input()
        no_exit = apply_main_menu_choice(user_choice, questions_database)

main_menu()


