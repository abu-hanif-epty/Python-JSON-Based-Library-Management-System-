
import json
import os

def view_books():
    fileName = "books.json"

    if not os.path.exists(fileName):
        print("This file does not exist.")
        return

    try:
        with open(fileName, "r") as f:
            data = json.load(f)

    except json.JSONDecodeError:
        print("Error: books.json contains invalid JSON.")
        return

    if not data:
        print("No books available.")
        return

    print("========== ALL BOOKS ===========")

    for book in data:
        print("-----------------")
        print(f"Book ID: {book['id']}")
        print(f"Book title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Available: {book['available']}")
        print("-----------------------")
    print("========== END ==========")

if __name__ == "__main__":
    view_books()
