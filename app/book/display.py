from abc import ABC, abstractmethod

from app.book.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class BookDisplayer:
    def __init__(self, displayer: Display) -> None:
        self.displayer = displayer

    def display(self, book: Book) -> None:
        return self.displayer.display(book)
