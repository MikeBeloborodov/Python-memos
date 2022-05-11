import tkinter as tk
from tkinter import StringVar, Toplevel, ttk
import json
import os
from tkinter import messagebox

class User:
    def __init__(self, login: str, password: str, email: str):
        self.login = login
        self.password = password
        self.email = email

class Program:
    def __init__(self):
        # load login information
        self.users_info = self.load_users()

        # root settings
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Employee manager")
        self.root.resizable(False, False)

        # styles
        s = ttk.Style()
        s.configure('.', font=('Segoe Ui', 12))    

        # root mainframe settings
        self.mainframe = ttk.Frame(self.root, padding="12 12 12 12")
        self.mainframe.grid(column=0, row=0, sticky='N, W, E, S')
        self.mainframe.columnconfigure(1, minsize=280)
        self.mainframe.columnconfigure(4, minsize=100)
        self.mainframe.rowconfigure(1, minsize=150)
        self.mainframe.rowconfigure(4, minsize=30)
        self.mainframe.rowconfigure(8, minsize=100)

        # enter login and password interface
        user_login = tk.StringVar()
        user_password = tk.StringVar()
        ttk.Label(self.mainframe, text="Login").grid(column=2, row=2)
        ttk.Label(self.mainframe, text="Password").grid(column=2, row=3)
        ttk.Entry(self.mainframe, textvariable=user_login, width=20).grid(column=3, row=2)
        ttk.Entry(self.mainframe, textvariable=user_password, width=20, show="*").grid(column=3, row=3)
        ttk.Button(self.mainframe, text='Login', command=lambda : self.check_login_credentials(user_login, user_password)).grid(column=2, row=5, columnspan=2)
        ttk.Button(self.mainframe, text='Register', command=lambda : self.register_new_user_window()).grid(column=2, row=6, columnspan=2)
        ttk.Button(self.mainframe, text="Exit", command=lambda : self.root.destroy()).grid(column=2, row=7, columnspan=2)

        self.root.bind('<Return>', lambda g : self.check_login_credentials(user_login, user_password))

        # add some padding for mainframe windgets
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def open_employee_manager(self):
        self.employee_manager_window = Toplevel(self.root)
        self.employee_manager_window.title("Employee manager")
        self.employee_manager_window.geometry("800x500")
        self.employee_manager_window.protocol("WM_DELETE_WINDOW", lambda : self.employee_manager_window_closed())
        self.employee_manager_window.resizable(False, False)

    def employee_manager_window_closed(self):
        self.employee_manager_window.destroy()
        self.root.deiconify()

    def check_login_credentials(self, user_login: StringVar, user_password: StringVar):
        for user in self.users_info:
            if user_login.get() == user.login and user_password.get() == user.password:
                messagebox.showinfo(message=f"Welcome back, {user.login}!")
                self.root.withdraw()    
                self.open_employee_manager()
                return
        messagebox.showerror(message="Wrong login or password. Try again.")

    def register_new_user_window(self):
        # register window settings
        self.register_window = Toplevel(self.root)
        self.register_window.title("New user registration")
        self.register_window.geometry("500x300")
        self.register_window.focus_set()
        self.register_window.grab_set()
        self.register_window.resizable(False, False)

        # register window frame settings
        register_window_frame = ttk.Frame(self.register_window, padding="12 12 12 12")
        register_window_frame.grid(column=0, row=0, sticky="N W E S")
        register_window_frame.columnconfigure(1, minsize=130)
        register_window_frame.rowconfigure(1, minsize=40)
        register_window_frame.rowconfigure(6, minsize=20)

        # user information labels and entries
        ttk.Label(register_window_frame, text="Enter the information below:").grid(column=2, row=2, columnspan=2, sticky='W')
        ttk.Label(register_window_frame, text="Login").grid(column=2, row=3, sticky='W')
        ttk.Label(register_window_frame, text="Password").grid(column=2, row=4, sticky='W')
        ttk.Label(register_window_frame, text="Email").grid(column=2, row=5, sticky='W')
        
        user_login = StringVar()
        ttk.Entry(register_window_frame, textvariable=user_login, width=20).grid(column=3, row=3)
        user_password = StringVar()
        ttk.Entry(register_window_frame, textvariable=user_password, width=20).grid(column=3, row=4)
        user_email = StringVar()
        ttk.Entry(register_window_frame, textvariable=user_email, width=20).grid(column=3, row=5)

        ttk.Button(register_window_frame, text="Register", command=lambda : self.add_new_user(user_login, user_password, user_email)).grid(column=2, row=7, columnspan=2)

        # add some padding for every element
        for child in register_window_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def save_users_info(self):
        users_dict = dict()
        for user in self.users_info:
            users_dict.update({user.login : {
                "user_password" : user.password,
                "user_email" : user.email}})
        with open("users_info.txt", "w") as file:
            file.write(json.dumps(dict(users_dict)))
        messagebox.showinfo(message="You have successfully registered! Use your login and password to enter the program.")
        self.register_window.destroy()

    def add_new_user(self, user_login: StringVar, user_password: StringVar, user_email: StringVar):
        for user in self.users_info:
            if user.login == user_login.get():
                messagebox.showerror(message="This login already exists. Please try again.")
                return
        new_user = User(user_login.get(), user_password.get(), user_email.get())
        self.users_info.append(new_user)
        self.save_users_info()

    def load_users(self) -> list[User]:
        if os.path.exists("users_info.txt"):
            with open("users_info.txt", "r") as file:
                content = file.read()
                if content:
                    users_dict = json.loads(content)
                    users_list = []
                    for user in users_dict:
                        login = str(user)
                        password = users_dict[user].get("user_password")
                        email = users_dict[user].get("user_email")
                        new_user = User(login, password, email)
                        users_list.append(new_user)
                    return users_list
                else:
                    return []
        else:
            with open("users_info.txt", "w"):
                return []

    def start_program(self):
        self.root.mainloop()

def main():
    program = Program()
    program.start_program()

if __name__ == "__main__":
    main()