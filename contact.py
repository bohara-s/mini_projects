contacts ={}
def menu():
    print("\n" * 2)
    print("Welcome to the Contact Management System")
    print("====================================")
    print("Contact Management System")
    print("Choose an option:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. delete Contact")
    print("4. Exit")


def delete_contact():
    print("\n" * 2)
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted.")
    else:
        print("❌ Contact not found.")

    

def add_contact(name,phone):
    print("\n" * 2)
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    if name in contacts:
        print(f"Contact {name} already exists.")
        return
    if not phone.isdigit():
        print("Invalid phone number. Please enter digits only.")
        return
    if len(phone) != 10:
        print("Invalid phone number. Please enter a 10-digit number.")
        return
    contacts[name] = phone
    print(f"Contact {name} added with phone number {phone}.")


def view_contacts():
    print("\n" * 2)
    if not contacts:
        print("No contacts available.")
        return
    print("Contacts:")
    for name,phone in contacts.items():
        print(f"Name: {name}, Phone: {phone}")


def search_contact(name):
    print("\n" * 2)
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"contact found:{name}-contacts[{name}]")
    else:
        print(f"Contact {name} not found.")


while True:
    print("\n" * 2)
    try:
        menu()
        choice = input("enter your choice: ")
        if choice == "1":
            add_contact(name="name", phone="phone")
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact(name="name")
        
        elif choice == "4":
            delete_contact()
    
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")