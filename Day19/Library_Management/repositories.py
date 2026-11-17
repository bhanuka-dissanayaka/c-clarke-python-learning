from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

from Day19.Library_Management.models import Book, LibraryError, Member, Loan


class BookRepository(ABC):
    @abstractmethod
    def add_book(self,book: Book) -> None:
        pass
    @abstractmethod
    def update_book(self ,book: Book) -> None:
        pass
    @abstractmethod
    def get_by_id(self, book_id: str) -> Book:
        pass

    @abstractmethod
    def list_all_books(self) -> List[Book]:
        pass

class MemberRepository(ABC):
    @abstractmethod
    def add_member(self, member: Member) -> None:
        pass
    @abstractmethod
    def update_member(self, member: Member) -> None:
        pass
    @abstractmethod
    def get_by_id(self , member_id: str) -> Member:
        pass
    @abstractmethod
    def list_all_members(self) -> List[Member]:
        pass


class LoanRepository(ABC):
    @abstractmethod
    def add_load_record(self, load: Loan) -> None:
        pass
    @abstractmethod
    def update_loan_record(self, loan: Loan) -> None:
        pass
    @abstractmethod
    def get_load_by_id(self ,load_id: str) -> Loan:
        pass
    @abstractmethod
    def get_all_loans(self) -> List[Loan]:
        pass


class FileBaseBookRepository(BookRepository):
    def __init__(self, filename: str = "books.txt"):
        self.__filename = filename
        self.__books: Dict[str,Book] = {}
        self.load()

    def load(self):
        try:
            with open(self.__filename, "r") as f:
                for line in f:
                    book_details = line.strip().split(",")
                    book = Book(book_id=book_details[0], title=book_details[1], author=book_details[2],year=book_details[3])
                    self.__books[book_details[0]] = book
        except (FileNotFoundError, TypeError) as e:
            print(e)
    def save(self):
        with open(self.__filename, "w") as f:
            for book in self.__books.values():
                f.write(f"{book.book_id},{book.title},{book.author},{book.year}\n")
    def update_book(self, book: Book) -> None:
        if self.__books.get(book.book_id) is None:
            raise LibraryError("Book does not exists")
        self.__books[book.book_id] = book
        self.save()

    def add_book(self, book: Book) -> None:
        self.__books[book.book_id] = book
        self.save()

    def get_by_id(self, book_id: str) -> Book:
        return self.__books.get(book_id)

    def list_all_books(self) -> List[Book]:
        return list(self.__books.values())


class FileBaseMemberRepository(MemberRepository):
    def __init__(self, filename: str = "members.txt"):
        self.__filename = filename
        self.__members : Dict[str,Member] = {}
        self.load()

    def load(self):
        try:
            with open(self.__filename, "r") as f:
                for line in f:
                    member_details = line.strip().split(",")
                    member = Member(member_details[0], member_details[1], member_details[2])
                    self.__members[member_details[0]] = member
        except FileNotFoundError as e:
            print(e)
    def save(self):
        with open(self.__filename, "w") as f:
            for member in self.__members.values():
                f.write(f"{member.member_id},{member.name},{member.contact}\n")

    def add_member(self, member: Member) -> None:
        self.__members[member.member_id] = member
        self.save()

    def update_member(self, member: Member) -> None:
        if self.__members.get(member.member_id) is None:
            raise LibraryError("Member does not exists")
        self.__members[member.member_id] = member
        self.save()

    def get_by_id(self, member_id: str) -> Member:
        return self.__members.get(member_id)

    def list_all_members(self) -> List[Member]:
        return list(self.__members.values())


class FileBaseLoanRepository(LoanRepository):
    def __init__(self, filename: str = "loans.txt"):
        self.__filename = filename
        self.__loans: Dict[str, Loan] = {}
        self.load()

    def load(self) -> None:
        try:
            with open(self.__filename, "r") as f:
                for line in f:
                    loan_details = line.strip().split(",")
                    borrowed_at = datetime.strptime(loan_details[3], "%Y-%m-%d %H:%M:%S")
                    loan = Loan(loan_details[0], loan_details[1], loan_details[2], borrowed_at)
                    self.__loans[loan.loan_id] = loan
        except FileNotFoundError as e:
            print(e)

    def save(self) -> None:
        with open(self.__filename, "w") as f:
            for loan in self.__loans.values():
                f.write(f"{loan.loan_id},{loan.member_id},{loan.book_id},{loan.borrowed_at}\n")

    def add_load_record(self, load: Loan) -> None:
        self.__loans[load.loan_id] = load
        self.save()

    def update_loan_record(self, loan: Loan) -> None:
        if self.__loans.get(loan.loan_id) is None:
            raise LibraryError("Loan Record Not found")
        self.__loans[loan.loan_id] = loan
        self.save()

    def get_load_by_id(self ,load_id: str) -> Loan:
        return self.__loans.get(load_id)

    def get_all_loans(self) -> List[Loan]:
        return list(self.__loans.values())
