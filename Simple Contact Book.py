contacts = {}

def add_contact(name, phone_number):
    contacts[name] = phone_number
    print("Contact added successfully")

def search_contact(name):
    if name in contacts:
        print(f"Phone Number: {contacts[name]}")
    else:
        print("Contact not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("Contact not found")

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        add_contact(name, phone_number)
    elif choice == "2":
        name = input("Enter name: ")
        search_contact(name)
    elif choice == "3":
        name = input("Enter name: ")
        delete_contact(name)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
