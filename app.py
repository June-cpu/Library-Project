from flask import Flask, render_template, request, redirect, url_for, flash
from library import Library, Book, Member

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize library
library = Library("my Library")

# Sample books
library.add_book(Book("Quran", "UNKNOWN"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_book(Book("The Midnight Library", "Matt Haig"))
library.add_book(Book("Where the Crawdads Sing", "Delia Owens"))
library.add_book(Book("The Alchemist", "Paulo Coelho"))
library.add_book(Book("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid"))
library.add_book(Book("A Court of Thorns and Roses", "Sarah J. Maas"))



# Sample members
library.add_member(Member("Junaid Taf", "226"))
library.add_member(Member("Ahmed Muhammad", "512"))

# Junaid borrowed a few books
library.members[0].borrow_book(library.search_book("Quran"), library)
library.members[0].borrow_book(library.search_book("1984"), library)
library.members[0].borrow_book(library.search_book("The Great Gatsby"), library)


# Ahmed borrowed a few books
library.members[1].borrow_book(library.search_book("The Midnight Library"), library)
library.members[1].borrow_book(library.search_book("Where the Crawdads Sing"), library)


@app.route("/")
def index():
    return render_template("index.html", library=library)

@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    if title and author:
        library.add_book(Book(title, author))
        flash("Book added successfully!", "success")
    else:
        flash("Invalid input!", "danger")
    return redirect(url_for("index"))

@app.route("/add_member", methods=["POST"])
def add_member():
    name = request.form.get("name")
    unique_id = request.form.get("unique_id")
    if name and unique_id:
        library.add_member(Member(name, unique_id))
        flash("Member added successfully!", "success")
    else:
        flash("Invalid input!", "danger")
    return redirect(url_for("index"))

@app.route("/borrow_book", methods=["POST"])
def borrow_book():
    member_id = request.form.get("member_id")
    book_title = request.form.get("book_title")

    # Find the member and book
    member = next((m for m in library.members if m.unique_ID == member_id), None)
    book = library.search_book(book_title)

    if not member:
        flash("Member not found.", "danger")
        return redirect(url_for("index"))
    if not book:
        flash("Book not found in the catalog.", "danger")
        return redirect(url_for("index"))

    # Attempt to borrow the book
    result = member.borrow_book(book, library)
    if result == "success":
        flash(f"'{book.title}' borrowed successfully by {member.name}.", "success")
    elif result == "already_borrowed":
        flash(f"'{book.title}' is already borrowed by {member.name}.", "warning")
    elif result == "unavailable":
        flash(f"'{book.title}' is currently unavailable.", "warning")
    elif result == "not_found":
        flash(f"'{book.title}' does not exist in the library catalog.", "danger")

    return redirect(url_for("index"))


@app.route("/return_book", methods=["POST"])
def return_book():
    member_id = request.form.get("member_id")
    book_title = request.form.get("book_title")
    member = next((m for m in library.members if m.unique_ID == member_id), None)
    book = library.search_book(book_title)

    if member and book:
        member.return_book(book)
        flash("Book returned successfully!", "success")
    else:
        flash("Invalid member ID or book title!", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
