from  add_book import add_books
from view_books import view_books
from search_book import search_book
from delete_book import delete_books
from update_book import update_book
from borrow_book import borrow_book
from return_book import return_book



def main():
    while True:
        print("---Welcome To Our Library---")
        print("1.Add books")
        print("2.view all books")
        print("3.Search book buy book id ")
        print("4.Delete books")
        print("5.Update book information..")
        print("6.Borrow book")
        print("7.Return book")
        print("8.Exit..")
        print("--------------------------")

        user_choice =  input("ENTER YOUR CHOICE(1-8):")
   
        if user_choice =="1":
            add_books()

        elif user_choice == "2":
            view_books()

        elif user_choice =="3":
            search_book()
        elif user_choice =="4":
            delete_books()

        elif user_choice == "5":
            update_book()
        elif user_choice == "6":
            borrow_book()

        elif user_choice == "7":
            return_book()
        
        elif user_choice == "8":
            print("-----------------------------")
            print("==== THANK YOU VERY MUCH ====")
            print("------------------------------")
            break
        else:
            print("==== !! NOTICE !! ====")
            print("YOUR CHOICE MUST (1-8).")
            print("==== INVALID CHOICE!! TRY AGAIN  ====")

if __name__ == "__main__":
    main()
