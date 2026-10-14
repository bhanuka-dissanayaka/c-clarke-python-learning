contacts = []
print(type((5,)))
def add_contact():
    contact = {}
    name = input("Enter Name : ")
    number = input("Enter the phone number : ")
    while True:
        if name == "" or number == "":
            print("Name and Number can not be empty.")
            name = input("Enter Name : ")
            number = input("Enter the phone number : ")
        elif len(number) != 10:
            print("Valid Number Should be Exactly 10 digits")
            number = input("Enter the phone number : ")
        else:
            break
    city = input("Enter the City : ")
    email = input("Enter the Email : ")
    contact["name"] = name
    contact["number"] = number
    contact["city"] = city
    contact["email"] = email
    contacts.append(contact)
    print("Contact added successfully")

def view_contacts():
    for contact in contacts:
        print(f"{contact["name"]:>50}  {contact["number"]}  {contact["city"]}  {contact["email"]}")

def search_contact():
    name = input("Enter name to search : ")
    for contact in contacts:
        if contact["name"] == name:
            print(f"{contact["name"]}  {contact["number"]}  {contact["city"]}  {contact["email"]}")
            return
    print("Contact Not Found")

def update_contact():
    name = input("Enter name to search : ")
    new_num = input("Enter New Number : ")
    for contact in contacts:
        if contact["name"] == name:
            contact["number"] = new_num
            print("Contact Updated Successfully")
            return
    print("Contact Not Found")

def delete_contact():
    name = input("Enter name to search : ")
    for i in range(len(contacts)):
        if contacts[i]["name"] == name:
            del contacts[i]
            print("Contact Deleted Successfully")
            return
    print("Contact Not Found")

def count_contact():
    count = len(contacts)
    print(f"You have {count} contacts")

while True:
    print("\n==============================")
    print("   CONTACT APP")
    print("==============================")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("0. Exit")
    choice = input("Enter a choice : ")
    if choice=="1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "0":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")