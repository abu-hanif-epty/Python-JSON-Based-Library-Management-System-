
import json
import os

def return_book():
    fileName = "books.json"

    if not os.path.exists(fileName):
        print("File not found!")
        return
    try:
        with open(fileName, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Error:Books.json contain invalid json data")
        return

    print("===== RETURN BOOK =====")
    
    user_choice = input("Enter book ID: ")
    book_found = False

    for book in data:
        if book["id"] == user_choice:
            book_found = True

            if book["available"] == False:
                book["available"] = True
                # print(f"Book title: {book['title']}\nReturned successfully!")
                print(f"====BOOK INFORMATION =====")
                print(f"BOOK TITLE : {book["title"]}.")
                print(f"AUTHOR NAME : {book["author"]}.")
                print(f"==== BOOK RETURNED SUCCESSFULLY! ====")
                print("------------------------------------------")
                with open(fileName, "w") as f:
                    json.dump(data, f, indent=4)
            else:
                print(f"====BOOK INFORMATION =====")
                print(f"BOOK TITLE : {book["title"]}.")
                print(f"AUTHOR NAME : {book["author"]}.")
                print("==== Book is already available! =====")
                print("----------------------------------------")

            break

    if not book_found:
        print("=== !NOTICE! =====")
        print(f"BOOK ID : {user_choice} IS NOT AVALIABLE!")
        print("==== Book not found! =====")


if __name__ == "__main__":
    return_book()
