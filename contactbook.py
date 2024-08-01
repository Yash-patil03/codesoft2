# Define the structure of a contact
contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if results:
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("No contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Contact found. Enter new details (leave blank to keep current value):")
            contact['name'] = input(f"Name [{contact['name']}]: ") or contact['name']
            contact['phone'] = input(f"Phone [{contact['phone']}]: ") or contact['phone']
            contact['email'] = input(f"Email [{contact['email']}]: ") or contact['email']
            contact['address'] = input(f"Address [{contact['address']}]: ") or contact['address']
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    global contacts
    new_contacts = [contact for contact in contacts if contact['name'].lower() != name]

    if len(new_contacts) == len(contacts):
        print("Contact not found.")
    else:
        contacts = new_contacts
        print(f"Contact {name} deleted successfully.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
