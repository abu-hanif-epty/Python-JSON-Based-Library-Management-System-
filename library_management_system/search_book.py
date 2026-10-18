import json
import os


def search_book():
    fileName = "books.json"

    if not os.path.exists(fileName):
        print("This file does not exist.")
        return
    try:
        with open(fileName, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Error: books.json contain invalid json")

    print("========== SEARCH BOOK ===========")
    user_choice = input("Enter book ID: ")

    book_found = False

    for book in data:
        if user_choice == book["id"]:
            print("==== BOOK FOUND =====")
            print(f"Book ID: {book['id']}")
            print(f"Book Title: {book['title']}")
            print(f"Book Author: {book['author']}")
            print(f"Available: {book['available']}")

            print("------------------------------")


            book_found = True
            break

    if not book_found:
        print("====================")
        print(f" BOOK ID : {user_choice} - NOT AVILABLE ! ")

        print("=====Book not found! =====")

if __name__ == "__main__":
    search_book()

