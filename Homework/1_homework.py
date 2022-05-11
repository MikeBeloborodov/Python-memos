# Создать 3 класса:
# Salad, Main_dish, Drink

# в этих классах создать поля name(строка), price(инт), dish_of_the_day(булеан)

# так же в этих классах создать функцию show_price, которая будет 
# выводить на экран стоимость блюда в рублях. 
# При этом, если блюдо является блюдом дня, то из стоимости вычесть 50 рублей

# создать по 3 объекта каждого из классов с разным блюдом и добавить в лист menu

# написать функцию print_menu, с аргументом нашего листа меню - menu,
# используя for пройтись по всему листу и вывести на экран меню для клиента
# (название каждого блюда и стоимость)

# вывод на экран оформить по усмотрению, но так, чтобы пользователю было понятно

class Salad:
    def __init__(self, name, price, dish_of_the_day):
        self.name = name
        self.price = price
        self.dish_of_the_day = dish_of_the_day

    def show_price(self):
        if self.dish_of_the_day == True:
            self.price -= 50
        
        print("Цена: " + str(self.price) + "р.")

class Main_dish:
    def __init__(self, name, price, dish_of_the_day):
        self.name = name
        self.price = price
        self.dish_of_the_day = dish_of_the_day

    def show_price(self):
        if self.dish_of_the_day == True:
            self.price -= 50

        print("Цена: " + str(self.price) + "р.")

class Drink:
    def __init__(self, name, price, dish_of_the_day):
        self.name = name
        self.price = price
        self.dish_of_the_day = dish_of_the_day
    
    def show_price(self):
        if self.dish_of_the_day == True:
            self.price -= 50

        print("Цена: " + str(self.price) + "р.")

def print_menu(menu_list):
    print("----Меню на день----")
    for item in menu_list:
        print(item.name)
        item.show_price()
        print()


salad_1 = Salad("Оливье", 250, False)
salad_2 = Salad("Парус", 350, True)
salad_3 = Salad("Морковь по-корейски", 150, False)

main_dish_1 = Main_dish("Пюре с тефтелями", 300, True)
main_dish_2 = Main_dish("Плов", 290, False)
main_dish_3 = Main_dish("Макароны с сосисками", 310, False)

drink_1 = Drink("Чай с сахаром", 20, False)
drink_2 = Drink("Апельсиновый сок", 50, False)
drink_3 = Drink("Кофе", 40, False)

menu = [salad_1, salad_2, salad_3, main_dish_1, main_dish_2, main_dish_3, drink_1, drink_2, drink_3]

print_menu(menu)

input("Press any button")
