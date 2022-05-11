class Employee:
    def __init__(self, name, age, smoker, working_hours):
            self.name = name
            self.age = age
            self.smoker = smoker
            self.working_hours = working_hours
            self.company_name = "Google"

    def print_salary(self):
        print(self.working_hours * 6)
    
    def say_hello(self):
        print(self.name + ": Hello sir!")

employee1 = Employee("John", 35, True, 10)
employee2 = Employee("Maria", 25, False, 20)

print(employee1.name)
print(employee1.age)
print(employee1.smoker)

print(employee2.name)
print(employee2.age)
print(employee2.smoker)

print(employee1.company_name)
print(employee2.company_name)

employee1.print_salary()
employee2.print_salary()

employee1.say_hello()
employee2.say_hello()