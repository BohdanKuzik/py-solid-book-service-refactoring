from abc import abstractmethod, ABC

from app.book.book import Book


class Print(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Print):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class BookPrinter:
    def __init__(self, printer: Print) -> None:
        self.printer = printer

    def print_book(self, book: Book) -> None:
        return self.printer.print_book(book)
