class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone_number}")

    def search_contact(self, keyword):
        return [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    address_book = AddressBook()
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            if len(phone_number) != 10:
                print("Phone number must be 10 digits long.")
                continue
            contact = Contact(name, phone_number)
            address_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == "2":
            address_book.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            found_contacts = address_book.search_contact(keyword)
            for idx, contact in enumerate(found_contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone_number}")

        elif choice == "4":
            index = int(input("Enter index of contact to update: ")) - 1
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            if len(phone_number) != 10:
                print("Phone number must be 10 digits long.")
                continue
            new_contact = Contact(name, phone_number)
            address_book.update_contact(index, new_contact)
            print("Contact updated successfully.")

        elif choice == "5":
            index = int(input("Enter index of contact to delete: ")) - 1
            address_book.delete_contact(index)
            print("Contact deleted successfully.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
