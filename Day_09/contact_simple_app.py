contact_list = {
    "Amal":["5556","4565"],
    "Bhanuka":["5578"]
}
def add_contact(phone_book,name,phone_no):
    if name in phone_book:
        if phone_no in phone_book[name]:
            print("Phone number exist")
            return
        phone_book[name].append(phone_no)
        print("Contact added successfully")
    else:
        phone_book[name] = [phone_no]
        print("Contact added successfully")

def search_contact(phone_book,name):
    if name in phone_book:
        print(f"The Phone Numbers You searched for : {phone_book[name]}")
    else:
        print("contact not found")

def remove_contact(phone_book,name):
    if name in phone_book:
        del phone_book[name]
        print("Contact removed successfully")
    else:
        print("contact not found")

def update_contact(phone_book,name,phone_no,new_phone_no):
    if name in phone_book:
        if phone_no in phone_book[name]:
            index = phone_book[name].index(phone_no)
            phone_book[name][index] = new_phone_no
            print("Contact updated successfully")
        else:
            print("The number does not exist")
    else:
        print("Person not found")

while True:
    print("\n==============================")
    print("   CONTACT APP")
    print("==============================")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Remove Contact")
    print("4. Update Contact")
    print("0. Exit")
    choice = int(input("Enter a choice : "))

    if choice=="1":
        input_name = input("Enter the name : ")
        input_phone_no = input("Enter the Number : ")
        add_contact(phone_book=contact_list,name=input_name , phone_no=input_phone_no)
        print(contact_list)

    elif choice == "2":
        input_name = input("Enter the name to search: ")
        search_contact(phone_book=contact_list, name=input_name, )

    elif choice == "3":
        input_name = input("Enter the name to remove: ")
        remove_contact(phone_book=contact_list,name=input_name)
        print(contact_list)

    elif choice == "4":
        input_name = input("Enter the name : ")
        existing_number = input("Enter the number you want to update : ")
        new_number = input("Enter the new number : ")
        update_contact(phone_book=contact_list,name=input_name,phone_no=existing_number,new_phone_no=new_number)
        print(contact_list)

    elif choice == "0":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")


