import json
import os

def add_books():
    filename = "books.json"

    # 1. Load existing books
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                books_list = json.load(file)

                if not isinstance(books_list, list):
                    books_list = []

            except json.JSONDecodeError:
                books_list = []
    else:
        books_list = []

    print("========== ADD BOOK ===========")

    # 2. Ask for a unique book ID
    while True:

        while True:
            book_id = input("Enter book ID: ")
            if not book_id:
                print("Book id can't be empty.")
            else:
                break

        book_found = False

        for book in books_list:
            if book.get("id") == book_id:
                book_found = True
                break

        if book_found:
            print("Error: This book ID already exists!")
            print("Please enter another book ID.\n")
        else:
            break

    # 3. Get the remaining book information
    while True:
        title = input("Enter book title: ").strip()
        if not title:
            print("Book title can't be empty !")
        else:
            break

    while True:
        author = input("Author name : ")
        if not author:
            print("Author can't be empty!")
        else:
            break
    
    # 4. Create the new book dictionary
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    # 5. Add the new book to the list
    books_list.append(new_book)

    # 6. Save all books to the JSON file
    with open(filename, "w") as file:
        json.dump(books_list, file, indent=4)

    print("Book added successfully!")
if __name__ == "__main__":
    add_books()