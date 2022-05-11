# Создать класс Student с полями degree (str), year (int), university_name (str)

# Создать в этом классе функцию show_info(), котрая будет выводить в
# консоль информацию о студенте в понятном пользователю виде

# Далее при помощи нескольких функций (на своё усмотрение) и понятной логики
# создать бесконечный цикл while,
# который будет предлагать пользователю  1- ввести нового студента,
# 2 - посмотреть о всех студентах инфо, 3 - выйти из программы

# студентов сохранять в листе student_list и выводить на экран используя for
# и внутреннюю функцию show_info() 

# постараться сделать так, чтобы всё было разложено по функциям и программа
# запускалась лишь при помощи 1 функции main_program()
import os

class Student:
    def __init__(self, degree, year, university_name):
        self.degree = degree
        self.year = year
        self.university_name = university_name

    def show_info(self):
        print("Degree: " + self.degree)
        print("Year: " + str(self.year))
        print("University: " + self.university_name)

def main_menu():
    print("--- Main menu ---")
    print("1 - add new student")
    print("2 - show students info")
    print("3 - exit program")
    print("-----------------")
    user_choice = input("Enter the number: ")
    return user_choice

def create_new_student():
    degree = input("Enter degree: ")
    year = input("Enter student year: ")
    university_name = input("Enter university name: ")
    new_student = Student(degree, int(year), university_name)
    return new_student

def add_new_student(student, student_list):
    student_list.append(student)
    print("You have succesfully added a new student!")

def print_student_info(student_list):
    print("  Students info")
    for student in student_list:
        print("------------------")
        student.show_info()
    
    print("------------------")

def main_program():
    student_list = []

    while True:
        user_choice = main_menu()

        if user_choice == "1":
            os.system('CLS')
            new_student = create_new_student()
            add_new_student(new_student, student_list)
        elif user_choice == "2":
            os.system('CLS')
            print_student_info(student_list)
        elif user_choice == "3":
            print("Bye!")
            break
        else:
            print("Error, try again.")

main_program()
