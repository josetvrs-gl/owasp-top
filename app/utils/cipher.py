from cryptography.fernet import Fernet
from hashlib import pbkdf2_hmac
import base64
import os

# Key derivation using PBKDF2 (More secure)
def derive_key(user_password, salt):
    key = pbkdf2_hmac('sha256', user_password.encode(), salt, 100000)
    return base64.urlsafe_b64encode(key[:32])  # Fernet needs a 32-byte key

def encrypt_card_number(card_number, user_password):
    salt = os.urandom(16)  # Generate a random salt per card
    key = derive_key(user_password, salt)
    cipher = Fernet(key)
    encrypted_card = cipher.encrypt(card_number.encode())
    return base64.b64encode(salt + encrypted_card).decode()  # Store salt + encrypted data

def decrypt_card_number(encrypted_card, user_password):
    data = base64.b64decode(encrypted_card)
    salt, encrypted_data = data[:16], data[16:]
    key = derive_key(user_password, salt)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data).decode()
