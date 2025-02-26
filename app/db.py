import sqlite3
import os
from cryptography.fernet import Fernet
from app.utils.cipher_vulnerable import encrypt_card_number
from app.utils.passwords import hash_password, hash_password_md5

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
    
    users = [
        ('admin', 'password123'),
        ('guest', 'guest123'),
        ('jose', 'Passwd432')
    ]
    
    # Encrypt password before storing to database
    #users = [(username, hash_password_md5(password)) for username, password in users]
    
    c.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)

def create_cards(c):
    c.execute('''DROP TABLE IF EXISTS credit_cards''')
    c.execute('''CREATE TABLE IF NOT EXISTS credit_cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                card_number TEXT,
                cardholder_name TEXT,
                expiration_date TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )'''
    )

    # Hardcoded passwords for encryption (for demonstration)
    user_passwords = {
        1: "password123",  # Admin's password
        2: "guest123",      # Guest's password
        3: "passwd432"      # Jose's password
    }

    cards = [
        (1, "0498526458274365295", "Alice", "12/25"),
        (2, "0243204358623450847", "Bob", "08/26"),
        (3, "4025874652934857642", "Jose", "05/27"),
        (2, "4025874652934857642", "Bob", "05/27")
    ]

    # Encrypt card numbers before storing to db
    cards = [
        (user_id, encrypt_card_number(card_number, user_passwords.get(user_id)), cardholder_name, expiration_date)
        for user_id, card_number, cardholder_name, expiration_date in cards
    ]

    c.executemany("INSERT INTO credit_cards (user_id, card_number, cardholder_name, expiration_date) VALUES (?, ?, ?, ?)", cards)

    
    

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    create_users(c)
    create_cards(c)
    conn.commit()
    conn.close()
    
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    return conn