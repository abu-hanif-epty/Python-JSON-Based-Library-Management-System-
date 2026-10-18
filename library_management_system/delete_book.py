import json
import os


def delete_books():
    fileName = "books.json"

    if not os.path.exists(fileName):
        print("File does not exist.")
        return
    try:
        with open(fileName, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Error:Book.json contain invalid json..")
        return

    print("============ DELETE BOOK =============")

    user_choice = input("Enter book ID: ")

    book_found = False

    for book in data:
        if user_choice == book["id"]:
            data.remove(book)
            book_found = True
            break

    if book_found:
        with open(fileName, "w") as f:
            json.dump(data, f, indent=4)

        print("---------------------------------")
        print("==== Book deleted successfully! =====")
        print(f"BOOK TITLE : {book["title"]}")
        print(f"AUTHOR NAME : {book["author"]}")
        print("---------------------------------")
    else:
        print("Book not found!")


if __name__ == "__main__":
    delete_books()