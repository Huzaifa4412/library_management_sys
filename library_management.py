import os
import json
import sys


# ANSI color codes
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

print(f"\n{BLUE}--------------\t Welcome to Library Management System \t --------------{RESET}")

FILE_NAME = "library_management.json"

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Handle empty or corrupted file
    return []

books = load_books()

def save_books(books):    
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    print(f"\n{GREEN}--------------\t Add Book \t --------------{RESET}\n")
    book_name = input("Enter book name: ")
    author_name = input("Enter author name: ")
    publication_year = input("Enter book publication year: ")
    book_price = input("Enter book price: ")
    book_quantity = input("Enter book quantity: ")
    book_genre = input("Enter book genre: ")
    isRead = input("Have you read this book? (yes/no) ").lower()
    
    book = {
        "title": book_name, 
        "author": author_name, 
        "publish_year": publication_year, 
        "price": book_price, 
        "qnty": book_quantity, 
        "genre": book_genre,
        "isRead": isRead
    }
    
    books.append(book)
    save_books(books)
    print(f"\n{CYAN}Book added successfully!{RESET}\n")
    menu()

def remove_book():
    print(f"\n{RED}--------------\t Delete Book \t --------------{RESET}\n")
    book_name = input("Enter the title of the book to remove: ")
    global books
    books = [book for book in books if book["title"].lower() != book_name.lower()]
    save_books(books)
    print(f"\n{GREEN}Book Deleted successfully!{RESET}\n")
    menu()

def display_book():
    print(f"\n{YELLOW}--------------\t Display Books \t --------------{RESET}\n")
    if not books:
        print(f"{RED}No books available{RESET}")   
    else:
        print(f"{BLUE}Available Books:{RESET}")
        for i, book in enumerate(books):
            print(f"{i+1}) {book['title']} - {book['author']} ({book['publish_year']})")
    menu()

def search_book():
    print(f"\n{MAGENTA}--------------\t Search Book \t --------------{RESET}\n")
    search_by = input("Search by:\n1. Title\n2. Author\nEnter choice: ")

    if search_by == "1":
        book_title = input("Enter the book title: ")
        matching_books = [book for book in books if book["title"].lower() == book_title.lower()]
        if matching_books:
            for i, match_book in enumerate(matching_books):
                print(f"{i+1}.	{match_book['title']}")
        else:
            print(f"{RED}No Book found with the title: {book_title}{RESET}")
    
    elif search_by == "2":
        book_author = input("Enter the book author: ")
        matching_books = [book for book in books if book["author"].lower() == book_author.lower()]
        if matching_books:
            for i, match_book in enumerate(matching_books):
                print(f"{i+1}.	{match_book['title']}")
        else:
            print(f"{RED}No Book found by author: {book_author}{RESET}")
    
    else:
        print(f"{RED}Invalid choice, please select 1 or 2.{RESET}")
    
    menu()

def display_statistics():
    print(f"\n{CYAN}--------------\t Display Statistics \t --------------{RESET}\n")
    total_books = len(books)
    print(f"{BLUE}Total Books: {total_books}{RESET}")
    
    read_books = [book for book in books if book["isRead"] in ["yes", "y"]]
    if total_books > 0:
        percentage = (len(read_books) / total_books) * 100
        print(f"{GREEN}Percentage of read books: {percentage:.2f}%{RESET}")
    else:
        print(f"{RED}No books available to calculate statistics.{RESET}")
    
    menu()

def menu():
    print(f"\n{YELLOW}1. Add Book{RESET}")
    print(f"{YELLOW}2. Remove Book{RESET}")
    print(f"{YELLOW}3. Search Book{RESET}")
    print(f"{YELLOW}4. Display Books{RESET}")
    print(f"{YELLOW}5. Display Statistics{RESET}")
    print(f"{RED}6. Exit{RESET}\n")
    
    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            add_book()
        elif user_choice == 2:
            remove_book()
        elif user_choice == 3:
            search_book()
        elif user_choice == 4:
            display_book()
        elif user_choice == 5:
            display_statistics()
        elif user_choice == 6:
            print(f"{RED}Exiting... Goodbye!{RESET}")
            sys.exit()
        else:
            print(f"{RED}Invalid choice! Please enter a number between 1-6.{RESET}")
            menu()
    except ValueError:
        print(f"{RED}Invalid input! Please enter a number.{RESET}")
        menu()

menu()


# Now your program will be more visually appealing with color-coded messages! Let me know if you want any adjustments. 🚀
