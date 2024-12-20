import sqlite3
import logging
from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox, OptionMenu, StringVar
from datetime import datetime, timedelta

# Set up logging to a file
logging.basicConfig(filename='library_error_log.txt', level=logging.ERROR)

# Custom Exceptions
class BookNotAvailable(Exception):
    pass

class OverdueBook(Exception):
    pass

# Database setup
def initialize_database():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available INTEGER NOT NULL CHECK (available IN (0, 1)),
            due_date TEXT
        )
    ''')
    connection.commit()
    connection.close()

# Function to handle database connection failures
def connect_to_db():
    try:
        return sqlite3.connect("library.db")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Could not connect to database: {e}")
        logging.error(f"Database connection error: {e}")
        return None

# Borrow a book with custom exceptions
def borrow_book_with_nested_exception_handling():
    try:
        # Validate the book selection
        book_id = get_selected_book_id()
        if book_id is None:  # No selection made
            return

        # Outer exception handling for database connection
        connection = sqlite3.connect("library.db")  # Establish database connection
        cursor = connection.cursor()
        print("Database connection established.")

        try:
            # Inner exception handling for book not found
            cursor.execute("SELECT available, due_date FROM books WHERE id = ?", (book_id,))
            result = cursor.fetchone()
            if result is None:
                raise ValueError(f"Book with ID {book_id} not found in the database.")

            # Check availability
            if result[0] == 1:  # Book is available
                # Set a due date (for example, 7 days from now)
                due_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
                cursor.execute("UPDATE books SET available = 0, due_date = ? WHERE id = ?", (due_date, book_id))
                connection.commit()
                messagebox.showinfo("Success", f"Book borrowed successfully! Due date: {due_date}")

                # Refresh the book list
                load_books()
            else:
                raise BookNotAvailable("Book is already borrowed.")  # Raise exception if not available

        except BookNotAvailable as e:
            # Handle book not available exception
            print(f"Inner Exception: {e}")
            messagebox.showerror("Error", str(e))
            logging.error(f"BookNotAvailable: {e}")

        except ValueError as e:
            # Handle book not found
            print(f"Inner Exception: {e}")
            messagebox.showerror("Error", str(e))

        finally:
            # Ensure connection is closed
            connection.close()
            print("Database connection closed.")

    except sqlite3.Error as e:
        # Handle database connection failure
        print(f"Outer Exception: Failed to connect to the database: {e}")
        messagebox.showerror("Database Error", f"Connection failure: {e}")
        logging.error(f"Database connection error: {e}")
    finally:
        print("End of borrowing operation.")


# Return a book with overdue check
def return_book(book_id):
    connection = connect_to_db()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT available, due_date FROM books WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Error", "Book not found!")
            return

        if result[0] == 0:  # Book is borrowed
            # Check for overdue
            if result[1] and is_overdue(result[1]):
                raise OverdueBook("This book is overdue. Please pay the fine.")
            cursor.execute("UPDATE books SET available = 1, due_date = NULL WHERE id = ?", (book_id,))
            connection.commit()
            messagebox.showinfo("Success", "Book returned successfully!")

            # Refresh the book list
            load_books()
        else:
            messagebox.showerror("Error", "Book is not borrowed!")
    except OverdueBook as e:
        messagebox.showerror("Error", str(e))
        logging.error(f"OverdueBook: {e}")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Operation failed: {e}")
        logging.error(f"Database operation failed: {e}")
    finally:
        connection.close()


# Helper to check if the book is overdue
def is_overdue(due_date):
    due_date = datetime.strptime(due_date, '%Y-%m-%d')
    return due_date < datetime.now()

# Load books into the listbox with optional filtering
def load_books(search_term=None, status_filter=None):
    connection = connect_to_db()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        query = "SELECT id, title, author, available FROM books WHERE 1=1"
        params = []

        if search_term:
            query += " AND title LIKE ?"
            params.append('%' + search_term + '%')

        if status_filter and status_filter != "All":
            if status_filter == "Available":
                query += " AND available = 1"
            elif status_filter == "Borrowed":
                query += " AND available = 0"

        cursor.execute(query, tuple(params))
        books = cursor.fetchall()
        book_listbox.delete(0, END)
        for book in books:
            status = "Available" if book[3] == 1 else "Borrowed"
            book_listbox.insert(END, f"{book[0]}: {book[1]} by {book[2]} ({status})")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Could not fetch books: {e}")
        logging.error(f"Error fetching books: {e}")
    finally:
        connection.close()

# Search bar for dynamic search
def search_books(event):
    search_term = search_entry.get()
    load_books(search_term=search_term, status_filter=status_var.get())

# Dropdown menu listener
def filter_books(*args):
    load_books(search_term=search_entry.get(), status_filter=status_var.get())

# Add book to database
def add_book(title, author):
    # Input validation
    if not title.strip():
        messagebox.showerror("Input Error", "Title field cannot be empty.")
        return
    if not author.strip():
        messagebox.showerror("Input Error", "Author field cannot be empty.")
        return

    connection = connect_to_db()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO books (title, author, available) VALUES (?, ?, 1)", (title.strip(), author.strip()))
        connection.commit()
        messagebox.showinfo("Success", "Book added successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Could not add book: {e}")
        logging.error(f"Error adding book: {e}")
    finally:
        connection.close()
        load_books()

# Delete a book from database
def delete_book():
    book_id = get_selected_book_id()  # Get the ID of the selected book
    if not book_id:
        return  # If no book is selected, return early

    response = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this book?")
    if not response:
        return  # If the user cancels the deletion, return early

    connection = connect_to_db()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        connection.commit()
        messagebox.showinfo("Success", "Book deleted successfully!")
        load_books()  # Refresh the book list
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Could not delete book: {e}")
        logging.error(f"Error deleting book: {e}")
    finally:
        connection.close()

# Helper to get selected book ID
def get_selected_book_id():
    try:
        selection = book_listbox.curselection()
        if not selection:
            raise ValueError("No book selected. Please select a book from the list.")
        return book_listbox.get(selection).split(":")[0].strip()
    except ValueError as e:
        messagebox.showerror("Selection Error", str(e))
        return None

# GUI setup
app = Tk()
app.title("Library Management System")

Label(app, text="Book List:").grid(row=0, column=0, padx=5, pady=5)
book_listbox = Listbox(app, width=50, height=10)
book_listbox.grid(row=1, column=0, padx=5, pady=5)

Label(app, text="Title:").grid(row=2, column=0, sticky='w', padx=5)
title_entry = Entry(app)
title_entry.grid(row=3, column=0, padx=5, pady=5)

Label(app, text="Author:").grid(row=4, column=0, sticky='w', padx=5)
author_entry = Entry(app)
author_entry.grid(row=5, column=0, padx=5, pady=5)

Button(app, text="Add Book", command=lambda: add_book(title_entry.get(), author_entry.get()), bg="green", fg="white").grid(row=6, column=0, pady=10)
Button(app, text="Borrow Book", command=borrow_book_with_nested_exception_handling, bg="blue", fg="white").grid(row=7, column=0, pady=5)
Button(app, text="Return Book", command=lambda: return_book(get_selected_book_id())).grid(row=8, column=0, pady=5)
Button(app, text="Delete Book", command=delete_book, bg="red").grid(row=9, column=0, pady=5)


Label(app, text="Search Books:").grid(row=10, column=0, sticky='w', padx=5)
search_entry = Entry(app)
search_entry.grid(row=11, column=0, padx=5, pady=5)
search_entry.bind("<KeyRelease>", search_books)

Label(app, text="Filter by Status:").grid(row=12, column=0, sticky='w', padx=5)
status_var = StringVar(app)
status_var.set("All")
status_var.trace("w", filter_books)
status_menu = OptionMenu(app, status_var, "All", "Available", "Borrowed")
status_menu.grid(row=13, column=0, padx=5, pady=5)

initialize_database()
load_books()

app.mainloop()