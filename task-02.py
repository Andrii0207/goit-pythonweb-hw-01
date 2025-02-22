from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"title: {self.title}, author: {self.author}, year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        raise NotImplementedError()

    @abstractmethod
    def remove_book(self, title):
        raise NotImplementedError()

    @abstractmethod
    def show_books(self):
        raise NotImplementedError()


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        logging.info(f"Book {book} successfully added")

    def remove_book(self, title):
        if not self.books:
            logging.info("Library is empty")
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logging.info(f"Book {book.title} was successfully deleted")
                break

    def show_books(self):
        if not self.books:
            logging.info("Library is empty")
        else:
            for book in self.books:
                logging.info(
                    f"Title: {book.title}, Author: {book.author}, Year: {book.author}"
                )


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def run(self):
        while True:
            command = input("Enter command (add, remove, show, exit): ").strip().lower()

            match command:
                case "add":
                    title = input("Enter book title: ").strip()
                    author = input("Enter book author: ").strip()
                    year = input("Enter book year: ").strip()
                    self.library.add_book(Book(title, author, year))
                case "remove":
                    title = input("Enter book title to remove: ").strip()
                    self.library.remove_book(title)
                case "show":
                    self.library.show_books()
                case "exit":
                    break
                case _:
                    print("Invalid command. Please try again.")


if __name__ == "__main__":
    library = Library()
    manager = LibraryManager(library)
    manager.run()
