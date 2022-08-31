import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, publisher text)")
    conn.commit()
    conn.close()

def insert(title, author, year, publisher):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, publisher))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", publisher=""):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR publisher=?", (title, author, year, publisher))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, publisher):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, publisher=? WHERE id=?", (title, author, year, publisher, id))
    conn.commit()
    conn.close()


# connect()
# insert("The earth", "Jhon Smith", 1918, "sokoro")
# delete(1)
# update(4, "The Moon",  "Jhon Smooth", 1917, "dachi")
# print(view())
# print(search(author="Jhon Smith"))