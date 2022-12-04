class BookShelf:
    def __init__(self, *books) -> None:
        self.books = books
    
    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."

class Book(BookShelf):
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Book {self.name}"

book = Book("Harry Potter")
book2 = Book("Python 101")

shelf = BookShelf(book, book2)

print(shelf)

# # Inheritance
# class BookShelf:
#     def __init__(self, quantity) -> None:
#         self.quantity = quantity
    
#     def __str__(self) -> str:
#         return f"BookShelf with {self.quantity} books."

# shelf = BookShelf(300)

# class Book(BookShelf):
#     def __init__(self, quantity, name) -> None:
#         super().__init__(quantity)
#         self.name = name

#     def __str__(self) -> str:
#         return f"Book {self.name}"

# book = Book("Harry Potter", 120)
# print(book)