from dataclasses import dataclass
from datetime import datetime
from typing import List

from Day19.Library_Management.models import LibraryError, Book, Member, Loan
from Day19.Library_Management.repositories import MemberRepository, BookRepository, LoanRepository


@dataclass
class LibraryService:
    member_repository : MemberRepository
    book_repository : BookRepository
    loan_repository : LoanRepository

    def add_book(self ,book_id: str, title: str, author: str, year: str) -> Book:
        if self.book_repository.get_by_id(book_id) is not None:
            raise LibraryError("The book id is already exist")
        book = Book(book_id=book_id, title=title, author=author, year=year)
        self.book_repository.add_book(book)
        return book

    def get_all_books(self) -> List[Book]:
        if len(self.book_repository.list_all_books()) == 0:
            return []
        return self.book_repository.list_all_books()

    def add_member(self, member_id: str, name: str, contact: str) -> Member:
        if self.member_repository.get_by_id(member_id) is not None:
            raise LibraryError("Member already exist")
        member = Member(member_id,name,contact)
        self.member_repository.add_member(member)
        return member

    def borrow_book(self,loan_id:str, book_id: str, member_id: str) -> None:
        if self.member_repository.get_by_id(member_id) is None:
            raise LibraryError("Member does not exist")
        if self.book_repository.get_by_id(book_id) is None:
            raise LibraryError("The book does not exist")
        loan_date = datetime.now()
        loan_record = Loan(loan_id, member_id, book_id, loan_date)
        self.loan_repository.add_load_record(loan_record)

    def return_book(self,  loan_id: str):
        if self.loan_repository.get_load_by_id(loan_id):
            raise LibraryError("Borrow Record Not Found")
        loan_record = self.loan_repository.get_load_by_id(loan_id)
        returned_date = datetime.now()
        updated_loan_record = Loan(loan_record.loan_id, loan_record.member_id, loan_record.book_id, loan_record.borrowed_at , returned_date)
        self.loan_repository.update_loan_record(updated_loan_record)

    def list_active_loans(self):
        return [loan for loan in self.loan_repository.get_all_loans() if loan.is_active()]


@dataclass
class MemberService:
    member_repository : MemberRepository

    def add_member(self, member_id: str, name: str, contact: str):
        if self.member_repository.get_by_id(member_id) is not None:
            raise LibraryError("Member already exist")
        member = Member(member_id, name, contact)
        self.member_repository.add_member(member)

    def get_all_members(self):
        return self.member_repository.list_all_members()

