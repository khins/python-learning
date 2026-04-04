# 11_notes_app.py
# 📝 Notes App
# 11_notes_app.py

import os

FILE_NAME = "notes.txt"


def get_file_path():
    return os.path.join(os.path.dirname(__file__), FILE_NAME)


def add_note():
    note = input("Enter your note: ")

    with open(get_file_path(), "a") as file:
        file.write(note + "\n")

    print("Note saved!")


def view_notes():
    try:
        with open(get_file_path(), "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes yet.")
            return

        print("\n--- Your Notes ---")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note.strip()}")

    except FileNotFoundError:
        print("No notes file found yet.")


def main():
    while True:
        print("\n--- Notes App ---")
        print("1. Add note")
        print("2. View notes")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()