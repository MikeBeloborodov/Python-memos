my_favorite_animal = "cat"
the_worst_animal = "dog"

test_str = "The best animal is the Dog of course!"

while True:
    user_input = input("Enter text: ")
    user_input = user_input.casefold()
    the_worst_animal_start = user_input.find(the_worst_animal) # coordinates (int)
    the_worst_animal_end = the_worst_animal_start + len(the_worst_animal)
    if the_worst_animal_start != -1: 
        print(user_input[:the_worst_animal_start] + my_favorite_animal + user_input[the_worst_animal_end:])