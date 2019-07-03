import json, csv, datetime


class Library:
    id = 0

    @staticmethod
    def generate_id():
        Library.id += 1
        return Library.id

    def __init__(self):
        self.librarians = []
        self.catalog = Catalog()
        self.loan_administration = LoanAdministration()

        # TODO: load books from json on startup
        # TODO: load customers from csv on startup

    def restore_from_backup(self):
        # Todo
        print("Sorry, not done yet!")

    def create_backup(self):
        json.dump(self, open('backup.json', 'w'), default=lambda o: o.__dict__)


class Catalog:
    def __init__(self):
        self.book_items = []
        self.books = []

    # todo: load initial data or whatever from json
    def load_books(self):
        pass

    def add_book(self, title, authors):
        book = Book(
            title,
            authors
        )
        self.books.append(book)
        return book

    def add_book_item(self, book):
        book_item = BookItem(book)
        self.book_items.append(book_item)
        return book_item

    def search_books(self, title):
        available_book_items = []
        for book in self.books:
            if title in book.title:
                for item in self.book_items:
                    if library.loan_administration.check_available(item):
                        available_book_items.append(item)
        return available_book_items


class LoanAdministration:
    def __init__(self):
        self.loaned_items = []
        self.customers = []

    def add_customer(self, first_name, last_name, **kwargs):
        customer = Customer(first_name, last_name, **kwargs)
        self.customers.append(customer)
        return customer

    def load_customers(self):
        # todo: load customers from csv
        pass

    def check_available(self, book_item):
        for item in self.loaned_items:
            if item.book_item.id == book_item.id:
                return False
        return True

    def loan_book(self, customer, book_item):
        if not self.check_available(book_item):
            return False

        loan_item = LoanItem(book_item, customer)
        self.loaned_items.append(loan_item)
        return True


class Person:
    def __init__(self, first_name, last_name, **kwargs):
        self.id = Library.generate_id()
        self.first_name = first_name
        self.last_name = last_name
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Customer(Person):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)


class Librarian(Person):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)


class Author(Person):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)


class Book:
    def __init__(self, title, authors, **kwargs):
        self.id = Library.generate_id()
        self.title = title
        self.authors = authors
        for key in kwargs:
            setattr(self, key, kwargs[key])


class BookItem:
    def __init__(self, book):
        self.id = Library.generate_id()
        self.book = book


class LoanItem:
    def __init__(self, book_item, customer):
        self.id = Library.generate_id()
        self.book_item = book_item
        self.customer = customer
        self.return_date = datetime.date.today() + datetime.timedelta(weeks=3)


if __name__ == '__main__':
    library = Library()
