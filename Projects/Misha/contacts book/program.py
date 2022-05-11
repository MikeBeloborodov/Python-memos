from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import json

class Contact:
    def __init__(self, name: str, last_name: str, phone_number: str, about: str, affiliation: str, contact_id: int):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.about = about
        self.affiliation = affiliation
        self.contact_id = contact_id

def list_box_item_selected(name_label: StringVar, last_name_label: StringVar, phone_label: StringVar, affiliation_label: StringVar, about_label: StringVar, contacts_list: list, currently_selected):
    contact_index = int(str(currently_selected)[1])
    selected_contact = contacts_list[contact_index]

    name_label.set(selected_contact.name)
    last_name_label.set(selected_contact.last_name)
    phone_label.set(selected_contact.phone_number)
    affiliation_label.set(selected_contact.affiliation)
    about_label.set(selected_contact.about)

def change_contact_button_pressed(name_label: StringVar, last_name_label: StringVar, phone_label: StringVar, affiliation_label: StringVar, about_label: StringVar, contacts_list: list, currently_selected, change_contact_window):
    contact_index = int(str(currently_selected)[1])

    contacts_list[contact_index].name = name_label.get()
    contacts_list[contact_index].last_name = last_name_label.get()
    contacts_list[contact_index].phone_number = phone_label.get()
    contacts_list[contact_index].affiliation = affiliation_label.get()
    contacts_list[contact_index].about = about_label.get()

    save_all_contacts(contacts_list)

    messagebox.showinfo(message="Contact is changed!")

    change_contact_window.destroy()
    
def delete_button_pressed(currently_selected, contacts_list: list, delete_contact_window):
    contact_index = int(str(currently_selected)[1])
    contacts_list.pop(contact_index)

    save_all_contacts(contacts_list)

    messagebox.showinfo(message="Contact deleted.")

    delete_contact_window.destroy()

def add_contact_pressed(name: StringVar, last_name: StringVar, phone_number: StringVar, about: Text, affiliation: StringVar, add_contact_window):
    last_contact_id = get_last_contact_id()
    new_contact = Contact(name.get(), last_name.get(), phone_number.get(), about.get("1.0", END).strip(), affiliation.get(), last_contact_id)
    save_contact(new_contact)

    # remove everything from the entry forms
    name.set("")
    last_name.set("")
    phone_number.set("")
    about.delete("1.0", END)
    affiliation.set("")

    messagebox.showinfo(message="Contact successfully added!")

    add_contact_window.destroy()

def save_all_contacts(contacts_list: list):
    contact_dict = {}

    for contact in contacts_list:
        contact_dict.update({f"contact_{contact.contact_id}" : 
        {"name" : contact.name,
         "last_name" : contact.last_name,
         "phone_number" : contact.phone_number,
         "about" : contact.about,
         "affiliation" : contact.affiliation,
         "contact_id" : contact.contact_id}})

    with open("contacts_database.txt", "w") as file:
        file.write(json.dumps(contact_dict))        

def get_last_contact_id():
    contacts_list = load_contacts()
    if contacts_list:
        last_contact_id = contacts_list[len(contacts_list) - 1].contact_id + 1
        return last_contact_id
    else:
        return 1

def from_dict_to_list_of_contacts(contacts_dict: dict):
    contacts_list = []
    for contact in contacts_dict:
        name = contacts_dict[contact].get("name")
        last_name = contacts_dict[contact].get("last_name")
        phone_number = contacts_dict[contact].get("phone_number")
        about = contacts_dict[contact].get("about")
        affiliation = contacts_dict[contact].get("affiliation")
        contact_id = int(contacts_dict[contact].get("contact_id"))
        new_contact = Contact(name, last_name, phone_number, about, affiliation, contact_id)
        contacts_list.append(new_contact)
    return contacts_list

def load_contacts():
    if os.path.exists("contacts_database.txt"):
        with open("contacts_database.txt") as file:
            content = file.read()
            if content:
                contacts_dict = json.loads(content)
                contacts_list = from_dict_to_list_of_contacts(contacts_dict)
                return contacts_list
            else:
                return []
    else:
        with open("contacts_database.txt", "w") as file:
            return []

def save_contact(contact: Contact):
    contacts_list = load_contacts()
    contacts_list.append(contact)
    contact_dict = {}

    for contact in contacts_list:
        contact_dict.update({f"contact_{contact.contact_id}" : 
        {"name" : contact.name,
         "last_name" : contact.last_name,
         "phone_number" : contact.phone_number,
         "about" : contact.about,
         "affiliation" : contact.affiliation,
         "contact_id" : contact.contact_id}})

    with open("contacts_database.txt", "w") as file:
        file.write(json.dumps(contact_dict))        

def open_contacts():
    contacts_window = Toplevel(root)
    contacts_window.title("Contacts")
    # focus_set and grab_set prevents users from interacting with parent window
    contacts_window.focus_set()
    contacts_window.grab_set()
    # 300x200 is the size, -500 and + 40 are the coordinates of the location
    contacts_window.geometry('470x330-850+400')
    contacts_window.resizable(False, False)

    contacts_window_frame = ttk.Frame(contacts_window, padding="50 12 12 12")
    contacts_window_frame.grid(column=0, row=0, sticky=(N, W, E, S))

    ttk.Label(contacts_window_frame, text="All contacts:").grid(column=1, row=1)

    # loading contacts names and placing them in the listbox
    contacts_list = load_contacts()
    choices_list = [contact.name for contact in contacts_list]
    choicesvar = StringVar(value=choices_list)
    
    info_frame = ttk.Frame(contacts_window_frame, width=300, height=300)
    info_frame.grid(column=2, row=2, sticky='N')

    ttk.Label(info_frame, text="Name: ").grid(column=1, row=1, sticky='E')
    ttk.Label(info_frame, text="Last name: ").grid(column=1, row=2, sticky='E')
    ttk.Label(info_frame, text="Phone number: ").grid(column=1, row=3, sticky='E')
    ttk.Label(info_frame, text="Contact group: ").grid(column=1, row=4, sticky='E')
    ttk.Label(info_frame, text="About: ").grid(column=1, row=5, sticky='E')

    name_label = StringVar()
    ttk.Label(info_frame, textvariable=name_label).grid(column=2, row=1, sticky=W)
    last_name_label = StringVar()
    ttk.Label(info_frame, textvariable=last_name_label).grid(column=2, row=2, sticky=W)
    phone_number_label = StringVar()
    ttk.Label(info_frame, textvariable=phone_number_label).grid(column=2, row=3, sticky=W)
    affiliation_label = StringVar()
    ttk.Label(info_frame, textvariable=affiliation_label).grid(column=2, row=4, sticky=W)
    about_label = StringVar()
    ttk.Label(info_frame, textvariable=about_label).grid(column=2, row=5, sticky=W)

    ttk.Button(contacts_window_frame, text="Back", command=lambda : contacts_window.destroy()).grid(column=1, row=3)

    # activestyle none removes underline
    list_box = Listbox(contacts_window_frame, height=14, listvariable=choicesvar, activestyle='none')
    list_box.grid(column=1, row=2)
    list_box.bind("<<ListboxSelect>>", lambda g, a=name_label, b=last_name_label, c=phone_number_label, d=affiliation_label, e=about_label: list_box_item_selected(a, b, c, d, e, contacts_list, list_box.curselection()))

    for child in info_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    for child in contacts_window_frame.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

def open_add_contact():
    add_contact_window = Toplevel(root)
    add_contact_window.title("Add contact")
    # focus_set and grab_set prevents users from interacting with parent window
    add_contact_window.focus_set()
    add_contact_window.grab_set()
    # 300x200 is the size, -500 and + 40 are the coordinates of the location
    add_contact_window.geometry('320x300-850+400')
    add_contact_window.resizable(False, False)

    add_contact_window_frame = ttk.Frame(add_contact_window, padding="12 12 12 12")
    add_contact_window_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    
    # name
    ttk.Label(add_contact_window_frame, text="Name").grid(column=1, row=1)
    contact_name = StringVar()
    ttk.Entry(add_contact_window_frame, width=25, textvariable=contact_name).grid(column=2, row=1)
    
    # last name
    ttk.Label(add_contact_window_frame, text="Last name").grid(column=1, row=2)
    contact_last_name = StringVar()
    ttk.Entry(add_contact_window_frame, width=25, textvariable=contact_last_name).grid(column=2, row=2)
    
    # phone_number
    ttk.Label(add_contact_window_frame, text="Phone number").grid(column=1, row=3)
    contact_phone_number = StringVar()
    ttk.Entry(add_contact_window_frame, width=25, textvariable=contact_phone_number).grid(column=2, row=3)
    
    # about
    ttk.Label(add_contact_window_frame, text="About").grid(column=1, row=4)
    about_contact = StringVar()
    about_text = Text(add_contact_window_frame, width=19, height=5)
    about_text.grid(column=2, row=4)

    # affiliation
    affiliation = StringVar()
    family = ttk.Radiobutton(add_contact_window_frame, text='Family', variable=affiliation, value='family')
    family.grid(column=1, row=5)
    friend = ttk.Radiobutton(add_contact_window_frame, text='Friend', variable=affiliation, value='friend')
    friend.grid(column=2, row=5, sticky=W)
    colleague = ttk.Radiobutton(add_contact_window_frame, text='Colleague', variable=affiliation, value='colleague')
    colleague.grid(column=2,row=5, sticky=E)

    # button add
    ttk.Button(add_contact_window_frame, text="Add contact",
     command=lambda a=contact_name, b=contact_last_name, c=contact_phone_number, d=about_text, e=affiliation: add_contact_pressed(a, b, c, d, e, add_contact_window)
     ).grid(column=2, row=7, sticky=W)

    for child in add_contact_window_frame.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

def open_change_contact():
    change_contact_window = Toplevel(root)
    change_contact_window.title("Change contact")
    # focus_set and grab_set prevents users from interacting with parent window
    change_contact_window.focus_set()
    change_contact_window.grab_set()
    # 300x200 is the size, -500 and + 40 are the coordinates of the location
    change_contact_window.geometry('470x380-850+400')
    change_contact_window.resizable(False, False)

    change_contact_window_frame = ttk.Frame(change_contact_window, padding="50 12 12 12")
    change_contact_window_frame.grid(column=0, row=0, sticky=(N, W, E, S))

    ttk.Label(change_contact_window_frame, text="All contacts:").grid(column=1, row=1)

    # loading contacts names and placing them in the listbox
    contacts_list = load_contacts()
    choices_list = [contact.name for contact in contacts_list]
    choicesvar = StringVar(value=choices_list)

    info_frame = ttk.Frame(change_contact_window_frame, width=300, height=300)
    info_frame.grid(column=2, row=2, sticky='N')

    ttk.Label(info_frame, text="Name: ").grid(column=1, row=1, sticky='E')
    ttk.Label(info_frame, text="Last name: ").grid(column=1, row=2, sticky='E')
    ttk.Label(info_frame, text="Phone number: ").grid(column=1, row=3, sticky='E')
    ttk.Label(info_frame, text="Contact group: ").grid(column=1, row=4, sticky='E')
    ttk.Label(info_frame, text="About: ").grid(column=1, row=5, sticky='E')

    name_label = StringVar()
    ttk.Entry(info_frame, width=25, textvariable=name_label).grid(column=2, row=1, sticky=W)
    last_name_label = StringVar()
    ttk.Entry(info_frame, width=25, textvariable=last_name_label).grid(column=2, row=2, sticky=W)
    phone_number_label = StringVar()
    ttk.Entry(info_frame, width=25, textvariable=phone_number_label).grid(column=2, row=3, sticky=W)
    affiliation_label = StringVar()
    ttk.Entry(info_frame, width=25, textvariable=affiliation_label).grid(column=2, row=4, sticky=W)
    about_label = StringVar()
    ttk.Entry(info_frame, width=25, textvariable=about_label).grid(column=2, row=5, sticky=W)

    ttk.Button(change_contact_window_frame, text="Back", command=lambda : change_contact_window.destroy()).grid(column=1, row=3)
    ttk.Button(change_contact_window_frame, text="Change", command=lambda a=name_label, b=last_name_label, c=phone_number_label, d=affiliation_label, e=about_label, f=change_contact_window: change_contact_button_pressed(a, b, c, d, e, contacts_list, list_box.curselection(), f)).grid(column=1, row=4)

    # activestyle none removes underline
    # exportselection false makes sure that selected item stays selected
    list_box = Listbox(change_contact_window_frame, exportselection=False, height=14, listvariable=choicesvar, activestyle='none')
    list_box.grid(column=1, row=2)
    list_box.bind("<<ListboxSelect>>", lambda g, a=name_label, b=last_name_label, c=phone_number_label, d=affiliation_label, e=about_label: list_box_item_selected(a, b, c, d, e, contacts_list, list_box.curselection()))
    
    for child in info_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    for child in change_contact_window_frame.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

def open_delete_contact():
    delete_contact_window = Toplevel(root)
    delete_contact_window.title("Delete contact")
    # focus_set and grab_set prevents users from interacting with parent window
    delete_contact_window.focus_set()
    delete_contact_window.grab_set()
    # 300x200 is the size, -500 and + 40 are the coordinates of the location
    delete_contact_window.geometry('470x380-850+400')
    delete_contact_window.resizable(False, False)

    delete_window_frame = ttk.Frame(delete_contact_window, padding="50 12 12 12")
    delete_window_frame.grid(column=0, row=0, sticky=(N, W, E, S))

    ttk.Label(delete_window_frame, text="All contacts:").grid(column=1, row=1)

    # loading contacts names and placing them in the listbox
    contacts_list = load_contacts()
    choices_list = [contact.name for contact in contacts_list]
    choicesvar = StringVar(value=choices_list)

    info_frame = ttk.Frame(delete_window_frame, width=300, height=300)
    info_frame.grid(column=2, row=2, sticky='N')

    ttk.Label(info_frame, text="Name: ").grid(column=1, row=1, sticky='E')
    ttk.Label(info_frame, text="Last name: ").grid(column=1, row=2, sticky='E')
    ttk.Label(info_frame, text="Phone number: ").grid(column=1, row=3, sticky='E')
    ttk.Label(info_frame, text="Contact group: ").grid(column=1, row=4, sticky='E')
    ttk.Label(info_frame, text="About: ").grid(column=1, row=5, sticky='E')

    name_label = StringVar()
    ttk.Label(info_frame, textvariable=name_label).grid(column=2, row=1, sticky=W)
    last_name_label = StringVar()
    ttk.Label(info_frame, textvariable=last_name_label).grid(column=2, row=2, sticky=W)
    phone_number_label = StringVar()
    ttk.Label(info_frame, textvariable=phone_number_label).grid(column=2, row=3, sticky=W)
    affiliation_label = StringVar()
    ttk.Label(info_frame, textvariable=affiliation_label).grid(column=2, row=4, sticky=W)
    about_label = StringVar()
    ttk.Label(info_frame, textvariable=about_label).grid(column=2, row=5, sticky=W)

    ttk.Button(delete_window_frame, text="Back", command=lambda : delete_contact_window.destroy()).grid(column=1, row=3)
    ttk.Button(delete_window_frame, text="Delete", command=lambda : delete_button_pressed(list_box.curselection(), contacts_list, delete_contact_window)).grid(column=1, row=4)

    # activestyle none removes underline
    list_box = Listbox(delete_window_frame, height=14, listvariable=choicesvar, activestyle='none')
    list_box.grid(column=1, row=2)
    list_box.bind("<<ListboxSelect>>", lambda g, a=name_label, b=last_name_label, c=phone_number_label, d=affiliation_label, e=about_label: list_box_item_selected(a, b, c, d, e, contacts_list, list_box.curselection()))

    for child in info_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    for child in delete_window_frame.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

root = Tk()
root.title("Contacts book")
root.resizable(False, False)
# places window in the center
root.eval('tk::PlaceWindow . center')

mainframe = ttk.Frame(root, padding="30 30 30 30")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Button(mainframe, text="View contacts", command=open_contacts).grid(column=2, row=1)
ttk.Button(mainframe, text="Add contact", command=open_add_contact).grid(column=2, row=2)
ttk.Button(mainframe, text="Change contact", command=open_change_contact).grid(column=2, row=3)
ttk.Button(mainframe, text="Delete contact", command=open_delete_contact).grid(column=2, row=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=50, pady=10)

root.mainloop()