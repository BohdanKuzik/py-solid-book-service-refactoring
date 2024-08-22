from app.book.book import Book

from app.book.display import BookDisplayer, ConsoleDisplay, ReverseDisplay
from app.book.print import BookPrinter, ConsolePrint, ReversePrint
from app.book.serialize import BookSerializer, JSONSerialize, XMLSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_map = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_map = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }

    serialize_map = {
        "json": JSONSerialize(),
        "xml": XMLSerialize()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in display_map:
                raise ValueError(f"Unknown display type: {method_type}")
            BookDisplayer(display_map[method_type]).display(book)
        elif cmd == "print":
            if method_type not in print_map:
                raise ValueError(f"Unknown print type: {method_type}")
            BookPrinter(print_map[method_type]).print_book(book)
        elif cmd == "serialize":
            if method_type not in serialize_map:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return BookSerializer(serialize_map[method_type]).serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
