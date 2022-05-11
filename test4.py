class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

def add_new_employee(employee, employee_list):
    employee_list.append(employee)
    print("You have added a new employee.")

def create_new_employee():
    name = input("Enter name: ")
    age = input("Enter age: ")
    position = input("Enter position: ")
    new_employee = Employee(name, age, position)
    return new_employee


def print_employee_list(employee_list):
    for item in employee_list:
        print("Name: " + item.name)
        print("Age: " + str(item.age))
        print("Position: " + item.position)

def main_menu():
    print("1 - add new employee")
    print("2 - print the database")
    print("3 - exit the program")
    user_choice = input("Please, enter one of the numbers: ")
    return user_choice

def main_program():
    employee_list = []

    while True:
        user_choice = main_menu()
        if user_choice == "1":
            print("Employee database.  Please, enter new employee: ")
            new_employee = create_new_employee()
            add_new_employee(new_employee, employee_list)
        elif user_choice == "2":
            print_employee_list(employee_list)
        elif user_choice == "3":
            print("Bye!")
            break
        else:
            print("Error. Try again.")
            continue

main_program()
