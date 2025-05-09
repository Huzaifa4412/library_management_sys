import json
import os
import streamlit as st


# Checking that file exits or not
FILE_NAME = "library_management.json"


def load_books():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
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
    books_names = [book["title"] for book in books]
    return books_names


# ? Add book
def add_book():
    with st.form("add_book_form"):
        book_title = st.text_input("Book Name", placeholder="Enter the Book Name")
        book_author = st.text_input(
            "Author Name", placeholder="Enter the Book Author Name"
        )
        publication_year = st.text_input(
            "Publication Year", placeholder="Enter the Book published year"
        )
        book_price = st.number_input(
            "Book Price", min_value=0, placeholder="Enter the Book price", value=5000
        )
        book_quantity = st.number_input(
            "Book Quantity",
            min_value=1,
            placeholder="Enter the Book Quantity",
            value=10,
        )
        book_genre = st.text_input("Book Genre", placeholder="Enter the Book Genre")
        is_read = st.checkbox("Have you read this book?")
        if st.form_submit_button("Add Book"):
            newBook = {
                "title": book_title,
                "author": book_author,
                "genre": book_genre,
                "price": book_price,
                "qnty": book_quantity,
                "publish_year": publication_year,
                "isRead": is_read,
            }
            if book_title.lower() in [book["title"].lower() for book in books]:
                st.info(f"The book '{book_title}' already exits")
            else:
                if book_title != "":
                    books.append(newBook)
                    save_books(books)
                    st.toast(
                        f"Book '{book_title}' added successfully in the library 📚"
                    )
                else:
                    st.info("Please write some thing")


# ? Remove Book
def remove_book():
    st.subheader("Remove Book ❌")
    book_name = st.selectbox("Select the book that you want to delete", books_name())
    global books
    if books == []:
        st.info("There are nothing any books present")
    else:
        if st.button("Remove Book"):
            updateBook = [book for book in books if book["title"] != book_name]
            st.info("Book has been Deleted Successfully")
            save_books(updateBook)
        if len(books) > 1:
            if st.button("Delete All books"):
                # global books
                books = []
                save_books(books)
                st.info("All Books has been deleted ⚙")


# ? View All Books
def view_books():
    st.subheader("View All Books 📚")
    st.dataframe(
        books,
        column_config={
            0: "Book title",
            1: "Book Author",
            2: "Genre",
            3: "Price",
            4: "Quantity",
            5: "Publish_year",
            6: "IsRead",
        },
        use_container_width=True,
    )


# ? Search Books
def search_books():
    st.subheader("Search Books 🔍")
    search_by = st.radio("Search by", ["Title", "Author"])
    search_value = st.text_input("Enter Search Value")
    if st.button("Search"):
        if search_by == "Title":
            filtered_books = [
                book for book in books if search_value.lower() in book["title"].lower()
            ]
        else:
            filtered_books = [
                book for book in books if search_value.lower() in book["Author"].lower()
            ]

        st.dataframe(
            filtered_books,
            column_config={
                0: "Book title",
                1: "Book Author",
                2: "Genre",
                3: "Price",
                4: "Quantity",
                5: "Publish_year",
                6: "IsRead",
            },
        )


# ? Update Book
def update_book():
    st.subheader("Update Book 📝")
    book_name = st.selectbox("Select the book that you want to update", books_name())
    update_thing = st.radio(
        "Select the thing that you want to update",
        ["Title", "Author", "Genre", "Price", "Quantity", "Publish_year", "IsRead"],
    )
    if update_thing == "Title":
        new_title = st.text_input(
            "New Title", value=books[books_name().index(book_name)]["title"]
        )
        books[books_name().index(book_name)]["title"] = new_title

    if update_thing == "Author":
        new_author = st.text_input(
            "New Author", value=books[books_name().index(book_name)]["author"]
        )
        books[books_name().index(book_name)]["author"] = new_author
    if update_thing == "Genre":
        new_genre = st.text_input(
            "New Genre", value=books[books_name().index(book_name)]["genre"]
        )
        books[books_name().index(book_name)]["genre"] = new_genre
    if update_thing == "Price":
        new_price = st.number_input(
            "New Price", value=books[books_name().index(book_name)]["price"]
        )
        books[books_name().index(book_name)]["price"] = new_price
    if update_thing == "Quantity":
        new_quantity = st.number_input(
            "New Quantity", value=books[books_name().index(book_name)]["qnty"]
        )
        books[books_name().index(book_name)]["qnty"] = new_quantity
    if update_thing == "Publish_year":
        new_publish_year = st.text_input(
            "New Publish Year",
            value=books[books_name().index(book_name)]["publish_year"],
        )
        books[books_name().index(book_name)]["publish_year"] = new_publish_year
    if update_thing == "IsRead":
        new_isRead = st.checkbox(
            "Have you read this book?",
            value=books[books_name().index(book_name)]["isRead"],
        )
        books[books_name().index(book_name)]["isRead"] = new_isRead
    if st.button("Update Book"):
        save_books(books)
        st.info("Book has been Updated Successfully")


st.set_page_config(page_title="Library Management", layout="wide")

# Coding for adding background image
st.markdown(
    """
        <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1481627834876-b7833e8f5570?q=80&w=2128&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
    unsafe_allow_html=True,
)


# coding for adding transparent sidebar
def add_transparent_sidebar():
    st.markdown(
        """
    <style>
    [data-testid="stSidebar"] {
        background-color: rgba(200, 225, 255, 0.4); ; 
        backdrop-filter: blur(6px); 
    }
    
    [data-testid="stSidebar"] .element-container {
        color: black;
        font-size: 18px;
    }
    
    [data-testid="stSidebar"] {
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 10px;
    }
    
    </style>
    """,
        unsafe_allow_html=True,
    )


st.title("📚 Library Management System")
menu = ["Add Book", "Remove Book", "View Book", "Update Book", "Search Book"]

with st.sidebar:
    st.markdown(
        "<h2 style='fontSize='20px''>Library Management System</h2>",
        unsafe_allow_html=True,
    )
    st.caption(
        "This is a simple library management system that allows you to add, remove, update, and search for books."
    )
    choice = st.selectbox("Menu", menu)

add_transparent_sidebar()

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

st.caption("Made with ❤️ by Huzaifa")
