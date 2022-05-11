text1 = "OldLittleGarden1"# 16 letters
text2 = "MyOwnLittleFarm" # 15 letters
text3 = "Dog" # 3 letters

def print_four_letters(text):
    buffer = ""
    counter = 1

    for letter in text:
        if (counter % 4 != 0):
            buffer = buffer + letter
            if (counter == len(text)):
                print(buffer)
        else:
            buffer = buffer + letter
            print(buffer)
            buffer = ""
        counter = counter + 1

print_four_letters(text1)
print_four_letters(text2)
print_four_letters(text3)

def get_sum1(num1, num2):
    return num1 + num2

def get_sum2(num1, num2):
    sum1 = num1 + num2
    return sum1

print(get_sum1(2, 4))
print(get_sum2(2, 4))

total_sum = get_sum1(10, 20)

print(total_sum)

def dummy_func():
    sum1 = 1 + 1

dummy_func()