import os

class ContactBook:
    def __init__(self, file_name='contacts.txt'):
        """Initialize the contact book and load contacts from a file."""
        self.file_name = file_name
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from a file."""
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                for line in file:
                    name, phone, email = line.strip().split(',')
                    self.contacts[name] = {'phone': phone, 'email': email}

    def save_contacts(self):
        """Save contacts to a file."""
        with open(self.file_name, 'w') as file:
            for name, info in self.contacts.items():
                file.write(f"{name},{info['phone']},{info['email']}\n")

    def add_contact(self, name, phone, email):
        """Add a new contact."""
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email}
            self.save_contacts()
            print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        """Delete a contact by name."""
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def menu():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book.add_contact(name, phone, email)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter the name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            print("Exiting the contact book.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()
