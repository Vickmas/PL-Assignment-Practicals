import sqlite3
from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox

# Database setup
def initialize_database():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available INTEGER NOT NULL CHECK (available IN (0, 1))
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
        return None

# Borrow a book
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
            cursor.execute("SELECT available FROM books WHERE id = ?", (book_id,))
            result = cursor.fetchone()
            if result is None:
                raise ValueError(f"Book with ID {book_id} not found in the database.")

            # Check availability
            if result[0] == 1:  # Book is available
                cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
                connection.commit()
                messagebox.showinfo("Success", "Book borrowed successfully!")
            else:
                messagebox.showerror("Error", "Book is already borrowed.")

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
    finally:
        print("End of borrowing operation.")


# Return a book
def return_book(book_id):
    connection = connect_to_db()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT available FROM books WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Error", "Book not found!")
            return

        if result[0] == 0:
            cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
            messagebox.showinfo("Success", "Book returned successfully!")
        else:
            messagebox.showerror("Error", "Book is not borrowed!")
        connection.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Operation failed: {e}")
    finally:
        connection.close()

# Load books into the listbox
def load_books():
    connection = connect_to_db()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, title, author, available FROM books")
        books = cursor.fetchall()
        book_listbox.delete(0, END)
        for book in books:
            status = "Available" if book[3] == 1 else "Borrowed"
            book_listbox.insert(END, f"{book[0]}: {book[1]} by {book[2]} ({status})")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Could not fetch books: {e}")
    finally:
        connection.close()

# Add book to database
def add_book(title, author):
    connection = connect_to_db()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO books (title, author, available) VALUES (?, ?, 1)", (title, author))
        connection.commit()
        messagebox.showinfo("Success", "Book added successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Could not add book: {e}")
    finally:
        connection.close()
        load_books()

# GUI setup
app = Tk()
app.title("Library Management System")

Label(app, text="Book List:").grid(row=0, column=0, padx=5, pady=5)
book_listbox = Listbox(app, width=50, height=15)
book_listbox.grid(row=1, column=0, padx=5, pady=5)

Label(app, text="Title:").grid(row=2, column=0, sticky='w', padx=5)
title_entry = Entry(app)
title_entry.grid(row=3, column=0, padx=5, pady=5)

Label(app, text="Author:").grid(row=4, column=0, sticky='w', padx=5)
author_entry = Entry(app)
author_entry.grid(row=5, column=0, padx=5, pady=5)

Button(app, text="Add Book", command=lambda: add_book(title_entry.get(), author_entry.get())).grid(row=6, column=0, pady=10)
Button(app, text="Borrow Book", command=borrow_book_with_nested_exception_handling).grid(row=7, column=0, pady=5)
Button(app, text="Return Book", command=lambda: return_book(get_selected_book_id())).grid(row=8, column=0, pady=5)

# Helper to get selected book ID
def get_selected_book_id():
    try:
        selection = book_listbox.curselection()  # Get the selected item index
        if not selection:
            raise ValueError("No book selected. Please select a book from the list.")
        return book_listbox.get(selection)  # Return the selected book ID
    except ValueError as e:
        messagebox.showerror("Selection Error", str(e))
        return None  # Return None if no book is selected

# Initialize and load books
initialize_database()
load_books()

app.mainloop()
