# given a contacts.csv file with columns: Name, Phone, Email. 
# Write a program that can: 
contacts = []
def load_contacts(): 
      
    try:
        with open("contacts.csv", "r") as f:
            header = f.readline()           
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                if len(parts) == 3:
                    name, phone, email = parts
                    contacts.append({"Name": name, "Phone": phone, "Email": email})
    except FileNotFoundError:
        print("Error: The file 'contacts.csv' was not found.") 
    except IOError as e:
        print(f"Error reading file: {e}")
    return contacts

# (1) search by name and return their contact info
def search_contact(name):
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
            return
    print(f"Contact '{name}' not found.")

# (2) add a new contact
def add_contact(name, phone, email):
    contacts.append({"Name": name, "Phone": phone, "Email": email})
    with open("contacts.csv", "a") as f:
        f.write(f"{name},{phone},{email}\n")

# (3) delete a contact by name, and update the CSV file
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact["Name"] != name]
    with open("contacts.csv", "w") as f:
        f.write("Name,Phone,Email\n")
        for contact in contacts:
            f.write(f"{contact['Name']},{contact['Phone']},{contact['Email']}\n")

# (4) display all contacts neatly formatted.
def display_contacts():
        print("===== CONTACTS =====")
        for contact in contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

def main():
    contacts = load_contacts()
    while True:
        search_name = None
        print("\n  Contact Manager  Menu ")
        print("=" * 40)
        print(" 1. Display all contacts ")
        print(" 2. Add a new contact ") 
        print(" 3. Delete a contact ")
        print(" 4. Search for a contact ")
        print(" 5. Quit              ")
        print("=" * 40)


        # Input validation: while loop rejects choices outside 1–5
        choice = ""
        while choice not in ("1", "2", "3", "4", "5"):
            choice = input("  Enter choice (1-5): ").strip()
            if choice not in ("1", "2", "3", "4", "5"):
                print("  Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        if   choice == "1": display_contacts()
        elif choice == "2": 
            name = input("  Enter name: ").strip()
            phone = input("  Enter phone: ").strip()
            email = input("  Enter email: ").strip()
            add_contact(name, phone, email)
        elif choice == "3": 
            name = input("  Enter name to delete: ").strip()
            delete_contact(name)    
        elif choice == "4":
            name = input("  Enter name to search: ").strip()
            search_contact(name)
        elif choice == "5":
            print("\n  Goodbye!\n")
            break

main()