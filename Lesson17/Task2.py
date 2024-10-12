class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"{self.name} ({self.country})"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={repr(self.author)})"

    def __str__(self):
        return f"'{self.name}' by {self.author.name} ({self.year})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={len(self.books)} books, authors={len(self.authors)} authors)"

    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books and {len(self.authors)} authors"


# Create authors
author1 = Author("J.K. Rowling", "UK", "1965-07-31")
author2 = Author("George Orwell", "UK", "1903-06-25")

# Create a library
library = Library("City Library")

# Add books to the library
book1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
book2 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)
book3 = library.new_book("1984", 1949, author2)

# Print library, books, and authors
print(library)
print(book1)
print(author1)

# Group books by author and years
print(library.group_by_author(
    author1))  # [Book(name='Harry Potter and the Philosopher's Stone', year=1997, author=Author(name='J.K. Rowling', country='UK', birthday='1965-07-31')), Book(name='Harry Potter and the Chamber of Secrets', year=1998, author=Author(name='J.K. Rowling', country='UK', birthday='1965-07-31'))]
print(library.group_by_year(
    1997))  # [Book(name='Harry Potter and the Philosopher's Stone', year=1997, author=Author(name='J.K. Rowling', country='UK', birthday='1965-07-31'))]

print(f"Total books in the library: {Book.total_books}")  # Total books in the library: 3
