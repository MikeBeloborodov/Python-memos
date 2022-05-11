import json
import curses
import os
from curses import wrapper

from numpy import std

ARROW_DOWN = "KEY_DOWN"
ARROW_UP = "KEY_UP"
ESC_KEY = "q"
ENTER_KEY = "\n"
DEL_KEY = "KEY_DC"

TOP_ZERO_POS = 10
LEFT_ZERO_POS = 40

class Student:
    def __init__(self, name, lessons_per_week, lessons, course):
        self.name = name
        self.lessons_per_week = lessons_per_week
        self.lessons = lessons
        self.course = course

class Lesson:
    def __init__(self, date, course):
        self.date = date
        self.course = course
        if course == "Junior" or course == "Junior+" or course == "Kids":
            self.length = 30
        else:
            self.length = 50

def convert_dict_to_student_class(students_list):
    student_object_list = []
    for student in students_list:
        name = students_list[student].get("student_name")
        lessons_per_week = students_list[student].get("lessons_per_week")
        course = students_list[student].get("course")
        lessons = students_list[student].get("lessons_list")
        new_student = Student(name, lessons_per_week, lessons, course)
        student_object_list.append(new_student)
    return student_object_list

def student_lesson_date_input(stdscr, lesson_counter, lessons_per_week):
    user_input = []
    counter = 0
    while True:
        user_key = stdscr.getkey()
        if user_key != ENTER_KEY:
            if user_key == DEL_KEY:
                if len(user_input) >= 1:
                    user_input.pop(counter - 1)
                    stdscr.clear()
                    stdscr.refresh()
                    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 3, "+--- Информация о уроках ---+")
                    stdscr.addstr(TOP_ZERO_POS + lessons_per_week + 6, LEFT_ZERO_POS, "Используйте стрелки для управления ")
                    stdscr.addstr(TOP_ZERO_POS + lessons_per_week + 7, LEFT_ZERO_POS, "Q - Выйти из программы ")

                    stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, f"Дата {lesson_counter} урока:\t " + "".join(str(char) for char in user_input))
                    counter -= 1
            else:
                user_input.append(user_key)
                stdscr.addstr(user_input[counter])
                counter += 1
        else:
            input_to_string = "".join(str(char) for char in user_input)
            return input_to_string.strip()

def student_lesson_per_week_input(stdscr):
    user_input = []
    counter = 0
    while True:
        user_key = stdscr.getkey()
        if user_key != ENTER_KEY:
            if user_key == DEL_KEY:
                if len(user_input) >= 1:
                    user_input.pop(counter - 1)
                    stdscr.clear()
                    stdscr.refresh()
                    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 5, "+--- Новый ученик ---+")
                    stdscr.addstr(TOP_ZERO_POS + 6, LEFT_ZERO_POS, "Используйте стрелки для управления ")
                    stdscr.addstr(TOP_ZERO_POS + 7, LEFT_ZERO_POS, "Q - Выйти из программы ")

                    stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, "Кол-во уроков в неделю:\t " + "".join(str(char) for char in user_input))
                    counter -= 1
            else:
                user_input.append(user_key)
                stdscr.addstr(user_input[counter])
                counter += 1
        else:
            input_to_string = "".join(str(char) for char in user_input)
            return input_to_string.strip()

def student_course_input(stdscr):
    user_input = []
    counter = 0
    while True:
        user_key = stdscr.getkey()
        if user_key != ENTER_KEY:
            if user_key == DEL_KEY:
                if len(user_input) >= 1:
                    user_input.pop(counter - 1)
                    stdscr.clear()
                    stdscr.refresh()
                    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 5, "+--- Новый ученик ---+")
                    stdscr.addstr(TOP_ZERO_POS + 6, LEFT_ZERO_POS, "Используйте стрелки для управления ")
                    stdscr.addstr(TOP_ZERO_POS + 7, LEFT_ZERO_POS, "Q - Выйти из программы ")

                    stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, "Курс:\t " + "".join(str(char) for char in user_input))
                    counter -= 1
            else:
                user_input.append(user_key)
                stdscr.addstr(user_input[counter])
                counter += 1
        else:
            input_to_string = "".join(str(char) for char in user_input)
            return input_to_string.strip()

def student_name_input(stdscr):
    user_input = []
    counter = 0
    while True:
        user_key = stdscr.getkey()
        if user_key != ENTER_KEY:
            if user_key == DEL_KEY:
                if len(user_input) >= 1:
                    user_input.pop(counter - 1)
                    stdscr.clear()
                    stdscr.refresh()
                    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 5, "+--- Новый ученик ---+")
                    stdscr.addstr(TOP_ZERO_POS + 6, LEFT_ZERO_POS, "Используйте стрелки для управления ")
                    stdscr.addstr(TOP_ZERO_POS + 7, LEFT_ZERO_POS, "Q - Выйти из программы ")

                    stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, "Имя:\t " + "".join(str(char) for char in user_input))
                    counter -= 1
            else:
                user_input.append(user_key)
                stdscr.addstr(user_input[counter])
                counter += 1
        else:
            input_to_string = "".join(str(char) for char in user_input)
            return input_to_string.strip()

def get_user_input(stdscr, type_of_input, lesson_counter=1, lessons_per_week=1):
    if type_of_input == "name":
        return student_name_input(stdscr)
    elif type_of_input == "course":
        return student_course_input(stdscr)
    elif type_of_input == "lessons_per_week":
        return student_lesson_per_week_input(stdscr)
    elif type_of_input == "lesson_date":
        return student_lesson_date_input(stdscr, lesson_counter, lessons_per_week)

def add_new_student(stdscr, students_list):
    stdscr.clear()
    stdscr.refresh()

    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 5, "+--- Новый ученик ---+")
    stdscr.addstr(TOP_ZERO_POS + 6, LEFT_ZERO_POS, "Используйте стрелки для управления ")
    stdscr.addstr(TOP_ZERO_POS + 7, LEFT_ZERO_POS, "Q - Выйти из программы ")

    type_of_input = "name"
    stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, "Имя:\t ")
    name = get_user_input(stdscr, type_of_input)
        
    type_of_input = "course"
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 5, "+--- Новый ученик ---+")
    stdscr.addstr(TOP_ZERO_POS + 6, LEFT_ZERO_POS, "Используйте стрелки для управления ")
    stdscr.addstr(TOP_ZERO_POS + 7, LEFT_ZERO_POS, "Q - Выйти из программы ")
    stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, "Курс:\t ")
    course = get_user_input(stdscr, type_of_input)

    stdscr.clear()
    stdscr.refresh()
    type_of_input = "lessons_per_week"
    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 5, "+--- Новый ученик ---+")
    stdscr.addstr(TOP_ZERO_POS + 6, LEFT_ZERO_POS, "Используйте стрелки для управления ")
    stdscr.addstr(TOP_ZERO_POS + 7, LEFT_ZERO_POS, "Q - Выйти из программы ")
    stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, "Кол-во уроков в неделю:\t")
    lessons_per_week = get_user_input(stdscr, type_of_input)

    stdscr.clear()
    stdscr.refresh()
    type_of_input = "lesson_date"
    lessons_list = []
    counter = 1
    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 3, "+--- Информация о уроках ---+")
    stdscr.addstr(TOP_ZERO_POS + int(lessons_per_week) + 6, LEFT_ZERO_POS, "Используйте стрелки для управления ")
    stdscr.addstr(TOP_ZERO_POS + int(lessons_per_week) + 7, LEFT_ZERO_POS, "Q - Выйти из программы ")
    for lesson in range(1, int(lessons_per_week) + 1):
        stdscr.addstr(TOP_ZERO_POS + counter + 2, LEFT_ZERO_POS + 6, f"Дата {counter} урока:\t ")
        lesson_date = get_user_input(stdscr, type_of_input, counter, int(lessons_per_week))
        lesson = Lesson(lesson_date, course)
        lessons_list.append(lesson)
        
        counter += 1

    student = Student(name, lessons_per_week, lessons_list, course)

    if students_list.__len__() == 0:
        students_list.update({"student_1" : {"student_name" : student.name, "lessons_per_week" : student.lessons_per_week, "course" : student.course, "lessons_list" : {}}})
        
        lessons_dict = {"lessons_list" : {}}
        counter = 1
        for item in lessons_list:
            lessons_dict["lessons_list"].update({f"lesson_{counter}" : {"lesson_date" : item.date, "lesson_length" : item.length}})
            counter += 1

        students_list["student_1"].update(lessons_dict)
    else:
        counter = 1
        keys_list = students_list.keys()
        for key in keys_list:
            if counter == len(keys_list):
                number = int(key[8:])
            else:
                counter += 1
        students_list.update({f"student_{number + 1}" : {"student_name" : student.name, "lessons_per_week" : student.lessons_per_week, "course" : student.course, "lessons_list" : {}}})
        
        lessons_dict = {"lessons_list" : {}}
        counter = 1
        for item in lessons_list:
            lessons_dict["lessons_list"].update({f"lesson_{counter}" : {"lesson_date" : item.date, "lesson_length" : item.length}})
            counter += 1

        students_list[f"student_{number + 1}"].update(lessons_dict)
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 5, "+--- Новый ученик ---+")
    stdscr.addstr(TOP_ZERO_POS + 4, LEFT_ZERO_POS, "Новый ученик добавлен! ")
    stdscr.addstr(TOP_ZERO_POS + 5, LEFT_ZERO_POS, "Нажмите любую кнопку для возвращения.")
    stdscr.getkey()

def students_list_user_choice(stdscr, students_list):
    position = 1
    normal_students_list = convert_dict_to_student_class(students_list)
    students_length = len(normal_students_list)
    while True:
        print_students_list(stdscr, students_list, position)
        user_choice = stdscr.getkey()
        if user_choice == "\n":
            return position
        if user_choice == ARROW_UP and position != 1:
            position -= 1
            print_students_list(stdscr, students_list, position)
        elif user_choice == ARROW_DOWN and position != students_length:
            position += 1
            print_students_list(stdscr, students_list, position)
        elif user_choice == ESC_KEY:
            return 0
        else:
            print_students_list(stdscr, students_list, position)

def print_students_list(stdscr, students_list, pos):
    stdscr.clear()
    stdscr.refresh()
    normal_student_list = convert_dict_to_student_class(students_list)
   
    student_counter = 4
    stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 8, "+--- Список учеников ---+")
    stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS, "Имя\t\tКурс\t\tУроков в нед. ")
    stdscr.addstr(TOP_ZERO_POS + student_counter + 6, LEFT_ZERO_POS + 3, "Используйте стрелки для управления ")
    stdscr.addstr(TOP_ZERO_POS + student_counter + 7, LEFT_ZERO_POS + 3, "Q - В главное меню ")
    position_counter = 1
    for student in normal_student_list:
        if position_counter == pos:
            stdscr.addstr(TOP_ZERO_POS + student_counter, LEFT_ZERO_POS, f"{student.name}\t\t{student.course}\t\t{student.lessons_per_week}", curses.A_REVERSE)
            student_counter += 1
            position_counter += 1
        else:
            stdscr.addstr(TOP_ZERO_POS + student_counter, LEFT_ZERO_POS, f"{student.name}\t\t{student.course}\t\t{student.lessons_per_week}")
            student_counter += 1
            position_counter += 1

def change_menu_pos(stdscr, pos):
    if pos == 1:
        stdscr.clear()
        stdscr.refresh()

        stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS, "+--- Информация о учениках ---+")
        stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, "Список учеников ", curses.A_REVERSE)
        stdscr.addstr(TOP_ZERO_POS + 3, LEFT_ZERO_POS + 6, "Добавить ученика ")
        stdscr.addstr(TOP_ZERO_POS + 5, LEFT_ZERO_POS, "Используйте стрелки для управления ")
        stdscr.addstr(TOP_ZERO_POS + 6, LEFT_ZERO_POS, "Q - Выйти из программы ")
    else:
        stdscr.clear()
        stdscr.refresh()

        stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS, "+--- Информация о учениках ---+")
        stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 6, "Список учеников ")
        stdscr.addstr(TOP_ZERO_POS + 3, LEFT_ZERO_POS + 6, "Добавить ученика ", curses.A_REVERSE)
        stdscr.addstr(TOP_ZERO_POS + 5, LEFT_ZERO_POS, "Используйте стрелки для управления ")
        stdscr.addstr(TOP_ZERO_POS + 6, LEFT_ZERO_POS, "Q - Выйти из программы ")

def save_students_list(students_list):
    with open("students_list.txt", "w") as file:
        file.write(json.dumps(students_list))

def get_user_choice(stdscr, students_list):
    initial_choice = 1
    change_menu_pos(stdscr, initial_choice)
    while True:
        user_choice = stdscr.getkey()
        if user_choice == "\n":
            return initial_choice
        if user_choice == ARROW_UP and initial_choice == 2:
            initial_choice = 1
            change_menu_pos(stdscr, initial_choice)
        elif user_choice == ARROW_DOWN and initial_choice == 1:
            initial_choice = 2
            change_menu_pos(stdscr, initial_choice)
        elif user_choice == ESC_KEY:
            save_students_list(students_list)
            exit()
        else:
            change_menu_pos(stdscr, initial_choice)

def user_choice_in_student_info(stdscr, students_list, num_of_student):
    normal_students_list = convert_dict_to_student_class(students_list)
    while True:
        counter = 1
        for student in normal_students_list:
            if counter == num_of_student:
                stdscr.clear()
                stdscr.refresh()

                stdscr.addstr(TOP_ZERO_POS, LEFT_ZERO_POS + 5, "+--- Информация о ученике ---+")
                stdscr.addstr(TOP_ZERO_POS + 2, LEFT_ZERO_POS + 4, f"Имя ученика:\t\t{student.name}")
                stdscr.addstr(TOP_ZERO_POS + 3, LEFT_ZERO_POS + 4, f"Курс:\t\t\t{student.course}")
                stdscr.addstr(TOP_ZERO_POS + 4, LEFT_ZERO_POS + 4, f"Кол-во занятий в неделю:\t{student.lessons_per_week}")
                stdscr.addstr(TOP_ZERO_POS + 7, LEFT_ZERO_POS+ 5, "Del - удалить ученика ")
                stdscr.addstr(TOP_ZERO_POS + 8, LEFT_ZERO_POS+ 5, "Q - выйти в меню ")
                user_choice = stdscr.getkey()
                if user_choice == 'q':
                    return
                elif user_choice == DEL_KEY:
                    delete_counter = 1
                    for to_delete_student in students_list:
                        if delete_counter == num_of_student:
                            students_list.pop(to_delete_student)
                            return
                        delete_counter += 1
                else:
                    continue
            counter += 1

def apply_user_choice(user_choice, stdscr, students_list):
    if user_choice == 1:
        num_of_student = students_list_user_choice(stdscr, students_list)
        if num_of_student == 0:
            return
        else:
            user_choice_in_student_info(stdscr, students_list, num_of_student)
    else:
        add_new_student(stdscr, students_list)

def load_students_list():
    students_list = {}
    if os.path.exists("students_list.txt"):
        with open("students_list.txt", "r") as file:
            students_list = json.loads(file.read())
    else:
        with open("students_list.txt", "w") as file:
            pass
    return students_list

def main(stdscr):
    students_list = load_students_list()
    while True:
        stdscr.clear()  
        user_choice = get_user_choice(stdscr, students_list)
        apply_user_choice(user_choice, stdscr, students_list)

wrapper(main)
