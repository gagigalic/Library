import sqlite3

def create_table():
    conn = sqlite3.connect("Library.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
        id TEXT PRIMARY KEY,
        title TEXT,
        author TEXT,
        status TEXT )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books_issued (
        id TEXT PRIMARY KEY,
        issuedto TEXT )
        ''')

create_table()

def fetch_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books