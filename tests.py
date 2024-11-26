from library import Library, Book, Member, BookCatalog

def test_book():
    print("Testing Book Class...")
    book = Book("Test Book", "Test Author")
    assert book.status is True, "Book should be available upon creation"
    book.borrow()
    assert book.status is False, "Book should not be available after borrowing"
    book.return_book()
    assert book.status is True, "Book should be available after returning"
    print("Book Class tests passed!")

def test_member():
    print("Testing Member Class...")
    book = Book("Test Book", "Test Author")
    library = Library("Test Library")
    library.add_book(book)
    member = Member("Test Member", "123")
    library.add_member(member)

    member.borrow_book(book, library)
    assert book.title in member.borrowed_books, "Book should be in member's borrowed books"
    assert book.status is False, "Book should not be available after borrowing"

    member.return_book(book)
    assert book.title not in member.borrowed_books, "Book should not be in member's borrowed books after returning"
    assert book.status is True, "Book should be available after returning"
    print("Member Class tests passed!")

def test_library():
    print("Testing Library Class...")
    library = Library("Test Library")

    # Add books
    book1 = Book("Book 1", "Author 1")
    book2 = Book("Book 2", "Author 2")
    library.add_book(book1)
    library.add_book(book2)

    assert library.search_book("Book 1") == book1, "Book 1 should be found in library"
    assert library.search_book("Nonexistent Book") is None, "Nonexistent book should not be found"

    library.remove_book("Book 1")
    assert library.search_book("Book 1") is None, "Book 1 should be removed from library"

    # Add members
    member = Member("Test Member", "123")
    library.add_member(member)
    assert member in library.members, "Member should be added to library"

    library.remove_member(member)
    assert member not in library.members, "Member should be removed from library"
    print("Library Class tests passed!")

def test_bst_capabilities():
    print("Testing BST Capabilities...")
    catalog = BookCatalog()

    books = [
        Book("D", "Author D"),
        Book("B", "Author B"),
        Book("A", "Author A"),
        Book("C", "Author C"),
        Book("E", "Author E")
    ]

    # Insert books
    for book in books:
        catalog.insert(book)

    # Check order with in-order traversal
    def inorder_titles(root):
        if root is None:
            return []
        return inorder_titles(root.left) + [root.book.title] + inorder_titles(root.right)

    sorted_titles = inorder_titles(catalog.root)
    assert sorted_titles == ["A", "B", "C", "D", "E"], "Books should be sorted alphabetically"

    # Search for books
    assert catalog.search("A").title == "A", "Search for 'A' should return the correct book"
    assert catalog.search("E").title == "E", "Search for 'E' should return the correct book"
    assert catalog.search("Z") is None, "Search for nonexistent book should return None"

    # Remove a book and check order
    catalog.remove("C")
    sorted_titles_after_removal = inorder_titles(catalog.root)
    assert sorted_titles_after_removal == ["A", "B", "D", "E"], "Books should remain sorted after removal"
    print("BST Capabilities tests passed!")

if __name__ == "__main__":
    print("Running Comprehensive Tests...")
    test_book()
    test_member()
    test_library()
    test_bst_capabilities()
    print("All Tests Passed!")
