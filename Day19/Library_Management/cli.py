from Day19.Library_Management.models import LibraryError
from Day19.Library_Management.repositories import BookRepository, MemberRepository, LoanRepository, \
    FileBaseBookRepository, FileBaseMemberRepository, FileBaseLoanRepository
from Day19.Library_Management.services import LibraryService


def print_menu():
    print("\n===== Library Management System =====")
    print("1. List all books")
    print("2. Add a book")
    print("3. Register a member")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. List active loans")
    print("7. List members")
    print("0. Exit")

def show_books(service: LibraryService):
    books = service.get_all_books()
    if not books:
        print("No Books Found")
    for book in books:
        if book.is_available():
            status = "Available"
        else:
            status = f"Borrowed by {book.book_lend_member_id}"
        print(f"{book.book_id} | {book.title} | {book.author} | {book.year} | {status}")

def add_book(service):
    pass
def register_member(service):
    pass
def borrow_book(service):
    pass
def return_book(service):
    pass
def show_active_loans(service):
    pass
def show_members(service):
    pass



def main():
    service = LibraryService(FileBaseMemberRepository(), FileBaseBookRepository(), FileBaseLoanRepository())

    actions = {
        "1": show_books,
        "2": add_book,
        "3": register_member,
        "4": borrow_book,
        "5": return_book,
        "6": show_active_loans,
        "7": show_members,
    }

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Thank you!")
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid option. Try again.")
            continue

        try:
            action(service)
        except LibraryError as error:
            print("Error:", error)
        except OSError as error:
            print("File error:", error)


if __name__ == "__main__":
    main()