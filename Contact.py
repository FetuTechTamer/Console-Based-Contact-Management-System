import json

def load_contacts(filename):
    """Load contacts from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(filename, contacts):
    """Save contacts to a JSON file."""
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact to the contacts dictionary."""
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return
    phone = input("Enter contact phone: ").strip()
    email = input("Enter contact email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    """View all contacts."""
    if contacts:
        print("\nContacts:")
        for name in sorted(contacts.keys()):
            info = contacts[name]
            print(f"- {name}: {info['phone']}, {info['email']}")
    else:
        print("No contacts found.")

def delete_contact(contacts):
    """Delete a contact from the contacts dictionary."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(contacts):
    """Update an existing contact's details."""
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone (or press Enter to skip): ").strip()
        email = input("Enter new email (or press Enter to skip): ").strip()
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")
  
def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter the name of the contact to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"Found contact - {name}: {info['phone']}, {info['email']}")
    else:
        print(f"Contact '{name}' not found.")

def main():
    filename = "contacts.json"
    contacts = load_contacts(filename)

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Search Contact")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            search_contact(contacts)
        elif choice == "6":
            save_contacts(filename, contacts)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
