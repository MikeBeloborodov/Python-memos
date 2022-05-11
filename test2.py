class Teacher:
    def __init__(self, subject, num_of_students, self_employed):
        self.subject = subject
        self.num_of_students = num_of_students
        self.self_employed = self_employed

        self.school_name = "Izhevsk Academy"
        if(self.subject == "English"):
            self.salary = 50000
        else:
            self.salary = 20000

    def teacher_info(self):
        print("---------Izhevsk Academy---------")
        print("Subject: " + self.subject)
        print("Number of students: " + str(self.num_of_students))
        print("Self-employed: " + str(self.self_employed))
        print("Salary: " + str(self.salary))
        print("---------------------------------")

    def give_promotion(self):
        if (self.num_of_students >= 20):
            print("My salary is " + str(self.salary) + "! I need more gold!")
            self.salary += 5000
            print("My salary is " + str(self.salary) + " now! Thank you, kind sir!")
        else:
            print("I need more students :(")

teacher1 = Teacher("English", 30, True)
teacher2 = Teacher("Maths", 10, False)

teacher1.teacher_info()
teacher2.teacher_info()

teacher1.give_promotion()
teacher2.give_promotion()