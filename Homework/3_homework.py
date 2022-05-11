# Можно писать код под каждым заданием

# 1) при помощи for вывести на экран числа от -100 до 100 (включительно)
for x in range(-100, 101):
    print(x)

# 2) при помощи while вывести на экран числа от -25 до 120 (включительно)
counter = -25
while counter <= 120:
    print(counter)
    counter += 1

# 3) при помощи for вывести на экран
# только четные числа от 2 до 20 (включительно), использовать continue
for x in range(2, 21):
    if x % 2 == 0:
        print(x)
    else:
        continue

# 4) при помощи while вывести на экран
# только нечетные числа от 3 до 30 (включительно), использовать continue
counter = 3
while counter <= 30:
    if counter % 2 != 0:
        print(counter)
        counter += 1
    else:
        counter += 1
        continue


# 5) создать лист с пятью именами, при помощи for пройтись
# по списку и сделать break на имени Ivan (сделать так, чтобы это имя было не в конце)
name_list = ["Masha", "Tolya", "Ivan", "Kostya", "Anatoly"]
for name in name_list:
    if name == "Ivan":
        break
    else:
        print(name)

# 6) при помощи while бесконечно просить пользователя вводить числа
# и выйти из цикла при помощи break только если пользователь ввёл 13
while True:
    number = input("Please enter a number: ")
    if int(number) == 13:
        break
    else:
        continue

# 7) использая двойной for и 2 листа adjectives, nouns (добавить по 4 штуки в каждый)
# вывести на экран каждое существительное со всеми прилагательными

adjectives = ["beautiful", "colorful", "wonderfull", "magnificent"]
nouns = ["bird", "car", "house", "room"]

for noun in nouns:
    for adjective in adjectives:
        print(adjective + " " + noun)