
import json
import os

def borrow_book():
    fileName = "books.json"

    if not os.path.exists(fileName):
        print("File not found..")
        return
    try:
        with open(fileName, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Error:books.json contain invalid json data")
        return
    print("======= BORROW BOOK =======")
    user_choice = input("Enter book id: ")
    book_found = False

    for book in data:
        if book["id"] == user_choice:
            book_found = True

            if book["available"]:
                book["available"] = False
                print(f"===== BOOK INFORMATION  =====")
                print(f"BOOK TITLE : {book["title"]}")
                print(f"AUTHOR NAME: {book["author"]}")
                print(f"==== BOOK BORROW SUCCESSFULL! ====")
                print("------------------------------------")

                with open(fileName, "w") as f:
                    json.dump(data, f, indent=4)
            else:
                print(f"===== BOOK INFORMATION  =====")
                print(f"BOOK TITLE : {book["title"]}")
                print(f"AUTHOR NAME: {book["author"]}")
                print("===== SORRY ! Book is already borrowed! ====")
                print("-----------------------------------------------")

            break

    if not book_found:
        print(f"BOOK ID :{user_choice} not availabe")
        print("===== Book not found ======")


if __name__ == "__main__":
    borrow_book()
