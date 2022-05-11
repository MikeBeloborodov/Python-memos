class Warrior:
    def __init__(self, attack, health_points):
        self.attack = attack
        self.health_points = health_points
        self.class_name = "Warrior"
    
class Rouge:
    def __init__(self, attack, health_points):
        self.attack = attack
        self.health_points = health_points
        self.class_name = "Rouge"


# this function takes 2 player classes as arguments
def combat(player1, player2):
    
    # player1 attacks first
    print(player1.class_name + " is attaking " + player2.class_name + "!")
    player2.health_points -= player1.attack
    print(player2.class_name + " loses " + str(player1.attack) + " health points!")

    # check if player2 is still alive
    if (player2.health_points > 0):
        print(player2.class_name + " is still alive!")
    else:
        print(player2.class_name + " is dead!")

    # if alive, another player attacks back 
    if (player2.health_points > 0):
        print(player2.class_name + " is attaking " + player1.class_name + "!")
        player1.health_points -= player2.attack
        print(player1.class_name + " loses " + str(player2.attack) + " health points!")
    
    # check if player1 is still alive
    if (player1.health_points > 0):
        print(player1.class_name + " is still alive!")
    else:
        print(player1.class_name + " is dead!")

    # player with more HP wins the game
    if (player1.health_points > player2.health_points):
        print(player1.class_name + " won the battle! Congratulations!")
    else:
        print(player2.class_name + " won the battle! Congratulations!")


# initializing 2 players
test_warrior = Warrior(10, 20) # 10 attack, 20 HP
test_rouge = Rouge(15, 100) # 15 attack, 10 HP

# start of the program
combat(test_rouge, test_warrior) # Rouge vs Warrior
