class Book:
    def __init__(self, title, author, status=True):
        self.title = title
        self.author = author
        self.status = status

    def borrow(self):
        self.status = False

    def return_book(self):
        self.status = True

    def display_book(self):
        print(f'Book: {self.title}, Author: {self.author}, Available: {"Yes" if self.status else "No"}')


class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class BookCatalog:
    def __init__(self):
        self.root = None

    def insert(self, book):
        def _insert(root, book):
            if root is None:
                return BSTNode(book)
            if book.title < root.book.title:
                root.left = _insert(root.left, book)
            elif book.title > root.book.title:
                root.right = _insert(root.right, book)
            else:
                print("Book with this title already exists.")
            return root

        self.root = _insert(self.root, book)

    def search(self, title):
        def _search(root, title):
            if root is None or root.book.title == title:
                return root
            if title < root.book.title:
                return _search(root.left, title)
            return _search(root.right, title)

        node = _search(self.root, title)
        return node.book if node else None

    def remove(self, title):
        def _remove(root, title):
            if root is None:
                return root
            if title < root.book.title:
                root.left = _remove(root.left, title)
            elif title > root.book.title:
                root.right = _remove(root.right, title)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                temp = self._min_value_node(root.right)
                root.book = temp.book
                root.right = _remove(root.right, temp.book.title)

            return root

        self.root = _remove(self.root, title)

    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def get_all_books(self):
        """Retrieve all books in alphabetical order as a list."""
        books = []

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                books.append(node.book)
                inorder_traversal(node.right)

        inorder_traversal(self.root)
        return books


class Member:
    def __init__(self, name, unique_ID, borrowed_books=None):
        if borrowed_books is None:
            borrowed_books = []
        self.name = name
        self.unique_ID = unique_ID
        self.borrowed_books = borrowed_books

    def borrow_book(self, book, library):
        if book.title in self.borrowed_books or not book.status or library.book_catalog.search(book.title) is None:
            print("Book is already borrowed or does not exist in the catalog.")
            return
        self.borrowed_books.append(book.title)
        book.borrow()

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
        else:
            print("Book is not borrowed.")

    def display_member(self):
        print(f'Member: {self.name}, Unique ID: {self.unique_ID}, Borrowed books: {", ".join(self.borrowed_books) or "None"}')


class Library:
    def __init__(self, name):
        self.name = name
        self.book_catalog = BookCatalog()
        self.members = []

    def add_book(self, book):
        self.book_catalog.insert(book)

    def remove_book(self, title):
        self.book_catalog.remove(title)

    def search_book(self, title):
        return self.book_catalog.search(title)

    def display_books(self):
        print(f"Books in {self.name}:")
        for book in self.book_catalog.get_all_books():
            book.display_book()

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
        else:
            print("Member already exists.")

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print("Member removed.")
        else:
            print("Member not found.")

    def display_members(self):
        print(f"Members of {self.name}:")
        for member in self.members:
            member.display_member()
