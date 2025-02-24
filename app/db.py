import sqlite3
import os
from cryptography.fernet import Fernet

DATABASE = os.path.join(os.path.dirname(__file__), 'database', 'sqlite.db')
SECRET_KEY = Fernet.generate_key()
cipher = Fernet(SECRET_KEY)
# Create a SQLite database and a sample table

def create_users(c):
    c.execute('''DROP TABLE IF EXISTS users''')

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
    
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    c.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest123')")
    c.execute("INSERT INTO users (username, password) VALUES ('jose', 'passwd432')")

def create_cards(c):
    c.execute('''DROP TABLE IF EXISTS credit_cards''')
    c.execute('''CREATE TABLE IF NOT EXISTS credit_cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                card_number TEXT, -- Se almacena cifrada automáticamente
                cardholder_name TEXT,
                expiration_date TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )'''
    )
    cards = [
        (1, cipher.encrypt(b"4111111111111111").decode(), "Alice", "12/25"),
        (2, cipher.encrypt(b"5500000000000004").decode(), "Bob", "08/26"),
        (3, cipher.encrypt(b"340000000000009").decode(), "Jose", "05/27")
    ]
    c.executemany("INSERT INTO credit_cards (user_id, card_number, cardholder_name, expiration_date) VALUES (?, ?, ?, ?)", cards)
    
    

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    create_users(c)
    conn.commit()
    create_cards(c)
    conn.commit()
    conn.close()
    
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    return conn