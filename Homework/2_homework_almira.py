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

class Student:
    def __init__(self, degree, year, university_name):
        self.degree = degree
        self.year = year
        self.university_name = university_name
    
def create_new_student():
    degree = input("Enter degree: ")
    year = input("Enter year: ")
    university_name = input("Enter university name: ")
    new_student = Student(degree, year, university_name)
    return new_student

def add_new_student(student, student_list):
    student_list.append(student)
    print("You have added a new student")

def show_info(student_list):
    for student in student_list:
        print("Degree: " + student.degree)
        print("Year: " + str(student.year))
        print("University name: " + student.university_name)

def main_menu():
    print("1 - add new student")
    print("2 - show student profiles")
    print("3 - exit the program")
    user_choice = input("Please, enter one of the numbers: ")
    return user_choice

def main_program():
    student_list = []

    while True:
        user_choice = main_menu()
        if user_choice == "1":
            print("Student database.  Please, create a new student profile: ")
            new_student = create_new_student()
            add_new_student(new_student, student_list)
        elif user_choice == "2":
            show_info(student_list)
        elif user_choice == "3":
            print("Have a nice day!")
            break
        else:
            print("Error. Try again.")
            continue

main_program()