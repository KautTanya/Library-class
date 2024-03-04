"""Library-class"""


class Book:
    """pass"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        raise TypeError("Error")

    def __ne__(self, other):
        if isinstance(other, Book):
            return self.title != other.title or self.author != other.author
        raise TypeError("Error")


class Library:
    """pass"""
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

    def __getitem__(self, item):
        return self.books[item]


b1 = Book("Title1", "Author1")
b2 = Book("Title2", "Author2")
b3 = Book("Title3", "Author3")

library = Library([b1, b2, b3])

print(len(library))
print(library[2])
