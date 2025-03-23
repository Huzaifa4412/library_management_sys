
import json
import os
import streamlit as st


# Checking that file exits or not
FILE_NAME = "library_management.json"

def load_books():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                print("Books loaded successfully!")
                return json.load(file)
        except:
            return []
    else:
        return []

books = load_books()

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

def books_name():
    books_names = []
    for book in books:
        books_names.append(book["title"])
    return books_names
        

# ? Add book
def add_book():
    with st.form("add_book_form"):
        book_title = st.text_input("Book Name", placeholder="Enter the Book Name")
        book_author = st.text_input("Author Name", placeholder="Enter the Book Author Name")
        publication_year = st.text_input("Publication Year",placeholder="Enter the Book published year")
        book_price = st.number_input("Book Price", min_value=0,placeholder="Enter the Book price", value=5000)
        book_quantity = st.number_input("Book Quantity", min_value=1,placeholder="Enter the Book Quantity", value=10)
        book_genre = st.text_input("Book Genre", placeholder="Enter the Book Genre")
        is_read = st.checkbox("Have you read this book?")
        newBook = {
                "title":book_title,
                "author":book_author,
                "genre":book_genre,
                "price":book_price,
                "qnty":book_quantity,
                "publish_year":publication_year,
                "isRead":is_read
        }
        if st.form_submit_button("Add Book"):
            books.append(newBook)
            save_books(books)


# ? Remove Book
def remove_book():
    st.subheader("Remove Book ❌")
    book_name = st.selectbox("Select the book that you want to delete", books_name())
    if st.button("Remove Book"):
            updateBook = [book for book in books if book["title"] != book_name]
            st.info("Book has been Deleted Successfully")
            save_books(updateBook)

# ? View All Books
def view_books():
    st.subheader("View All Books 📚")
    st.dataframe(books, column_config={
        0:"Book title",
        1:"Book Author",
        2:"Genre",
        3:"Price",
        4:"Quantity",
        5:"Publish_year",
        6:"IsRead"
    })


# ? Search Books
def search_books():
    st.subheader("Search Books 🔍")
    search_by = st.radio("Search by", ["Title", "Author"])
    search_value = st.text_input("Enter Search Value")
    if st.button("Search"):
        if search_by == "Title":
            filtered_books = [book for book in books if search_value.lower() in book["title"].lower()]
        else:
            filtered_books = [book for book in books if search_value.lower() in book["Author"].lower()]

        st.dataframe(filtered_books, column_config={
            0:"Book title",
            1:"Book Author",
            2:"Genre",
            3:"Price",
            4:"Quantity",
            5:"Publish_year",
            6:"IsRead"
        })


# ? Update Book
def update_book():
    st.subheader("Update Book 📝")
    book_name = st.selectbox("Select the book that you want to update", books_name())
    update_thing = st.radio("Select the thing that you want to update", ["Title", "Author", "Genre", "Price", "Quantity", "Publish_year", "IsRead"])
    if update_thing == "Title":
        new_title = st.text_input("New Title", value=books[books_name().index(book_name)]["title"])
        books[books_name().index(book_name)]["title"] = new_title
    if update_thing == "Author":
        new_author = st.text_input("New Author", value=books[books_name().index(book_name)]["author"])
        books[books_name().index(books_name)]["author"] = new_author
    

st.set_page_config(page_title="Library Management", layout="wide")
st.title("📚 Library Management System")

menu = ["Add Book", "Remove Book", "View Book", "Update Book", "Search Book"]

choice = st.sidebar.selectbox("Menu",menu)

if choice == "Add Book":
    add_book()
elif choice == "Remove Book":
    remove_book()
elif choice == "View Book":
    view_books()
elif choice == "Search Book":
    search_books()
elif choice == "Update Book":
    update_book()
