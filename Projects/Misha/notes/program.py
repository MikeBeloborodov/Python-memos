import os
import json
import msvcrt

class Note:
    def __init__(self, title, text, note_id):
        self.title = title
        self.text = text
        self.note_id = note_id

def add_note(notes):
    os.system('CLS')
    note_title = input("Enter the title: ")
    note_text = input("Enter the text: ")
    if notes:
        note_id = int(notes[len(notes) - 1].note_id) + 1
    else:
        note_id = 1
    
    new_note = Note(note_title, note_text, note_id)
    notes.append(new_note)
    return notes

def update_note(notes):
    os.system('CLS')
    for note in notes:
        print(f"{note.note_id} - {note.title}")
    user_choice = input("Enter the number of the note you want to update: ")
    if int(user_choice) < 0 or int(user_choice) > len(notes):
        os.system('CLS')
        print("Error. There is no such note. Press any key to return")
        msvcrt.getch()
        return notes
    else:
        print(f"Old title - {notes[int(user_choice) - 1].title}")
        notes[int(user_choice) - 1].title = input("Enter new title: ")
        print(f"Old text - {notes[int(user_choice) - 1].text}")
        notes[int(user_choice) - 1].text = input("Enter new text: ")
        print("Note updated!")
        print("Press any key to continue.")
        msvcrt.getch()
        return notes

def view_notes(notes):
    if notes:
        os.system('CLS')
        for note in notes:
            print(f"{note.note_id} note: ")
            print(f"Title: {note.title}")
            print(f"Text: {note.text}")
            print("----------------------")
        print("Press any key to return.")
        msvcrt.getch()
        return notes
    else:
        os.system('CLS')
        print("You don't have any notes!")
        print("Press any key to return.")
        msvcrt.getch()
        return notes

def delete_note(notes):
    os.system('CLS')
    for note in notes:
        print(f"{note.note_id} - {note.title}")
    user_choice = input("Enter the number of the note you want to delete: ")
    if int(user_choice) < 0 or int(user_choice) > len(notes):
        os.system('CLS')
        print("Error. There is no such note. Press any key to return")
        msvcrt.getch()
        return notes
    else:
        notes.pop(int(user_choice) - 1)
        counter = 1
        for note in notes:
            note.note_id = counter
            counter += 1
    return notes

def load_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt") as file:
            content = file.read()
            if content:
                notes_dict = json.loads(content)
                notes_list = []
                for note in notes_dict:
                    note_id = int(note[5:])
                    note_title = notes_dict[note].get("note_title")
                    note_text = notes_dict[note].get("note_text")
                    new_note = Note(note_title, note_text, note_id)
                    notes_list.append(new_note)
                return notes_list
            else:
                return []
    else:
        with open("notes.txt", "w") as file:
            return []

def save_notes(notes):
    notes_dict = {}
    for note in notes:
        notes_dict.update({f"note_{note.note_id}" : {"note_title" : note.title, "note_text" : note.text}})
    with open("notes.txt", "w") as file:
        file.write(json.dumps(notes_dict))

def print_main_menu():
    os.system('CLS')
    print("1 - View notes")
    print("2 - Add a note")
    print("3 - Change a note")
    print("4 - Delete a note")
    print("5 - Exit program\n")

def get_user_choice():
    print_main_menu()
    user_choice = input("Enter the number here: ")
    while user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4" and user_choice != "5":
        print_main_menu()
        print("Error. Try again.\n")
        user_choice = input("Enter the number here: ")
    return user_choice

def apply_user_choice(user_choice, notes):
    if user_choice == "1":
        return view_notes(notes)
    elif user_choice == "2":
        return add_note(notes)
    elif user_choice == "3":
        return update_note(notes)
    elif user_choice == "4":
        return delete_note(notes)
    elif user_choice == "5":
        save_notes(notes)
        exit()

def main_program():
    notes = load_notes()

    while True:
        user_choice = get_user_choice()
        notes = apply_user_choice(user_choice, notes)

main_program()
