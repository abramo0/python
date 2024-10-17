# Program that simulates an address book
# You can view the data, add or remove contacts from the address book.
# Data is saved in a json file named address_book.json

import json
import os

def load_address_book(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_address_book(add_book, filename):
    with open(filename, 'w') as file:
        json.dump(add_book, file)

def view_address_book(add_book):
    if not add_book:
        print("address_book is empty")
    else:
        print("address_book:")
        for name, number in add_book.items():
            print(f"{name}: {number}")

def insert_contact(add_book):
    name = input("Write name and surname: ")
    number = input("Write the phone number: ")
    add_book[name] = number
    print(f"Contact {name} added.")
    view_address_book(add_book)

def delete_contact(add_book):
    name = input("Enter the name of the contact to delete: ")
    if name in add_book:
        del add_book[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} is not present.")
    view_address_book(add_book)

def inizialize():
    filename = "address_book.json"
    add_book = load_address_book(filename)

    while True:
        option = int(input("Enter the number that indicates what you want to do:\n1. View address book\n2. Add a contact\n3. Delete a contact\n4. Save and Exit\n"))
        
        if option == 1:
            view_address_book(add_book)
        elif option == 2:
            insert_contact(add_book)
        elif option == 3:
            delete_contact(add_book)
        elif option == 4:
            save_address_book(add_book, filename)
            print("Exiting and saving the address book.")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    inizialize()

if __name__ == "__main__":
    main()
