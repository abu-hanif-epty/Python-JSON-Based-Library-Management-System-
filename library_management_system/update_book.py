import json
import os

def update_book():
    if not os.path.exists("books.json"):
        print("Book file not found!")
        return
    
    try:
        with open("books.json", "r") as f:
            data = json.load(f)
            
    except json.JSONDecodeError:
        print("Error: Books.json file contain invalid json data.. ")
        return

    print("========= UPDATE BOOK =========")
    user_choice = input("Enter book ID to update: ")
    book_found = False

    for book in data:
        if book["id"] == user_choice:
            print("===== PREVIOUS INFO =======")
            print(f"PREVIOUS TITLE :{book["title"]}!")
            print(f"PREVIOUS AUTHOR : {book["author"]}")
            print("----------------------------------")
            print("====== ADD NEW INFO =====")

            while True:
                new_title = input("Enter new title: ")
                if not new_title:
                    print("Title cant be empty..")
                else:
                    break
            while True:
                new_author = input("Enter new author: ")
                if not new_title:
                    print("Author name cant be empty..")
                else:
                    break

            book["title"] = new_title
            book["author"] = new_author

            book_found = True
            break

    if book_found:
        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

        print("==== Book updated successfully! ====")
        print()
    else:
        print(f" BOOK ID : {user_choice} NOT AVILABLE !")
        print("==== Book not found! ======")

if __name__ == "__main__":
    update_book()