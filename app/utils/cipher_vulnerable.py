import base64
import hashlib
from cryptography.fernet import Fernet

def generate_key(password: str) -> bytes:
    """Generate an encryption key from the user's password"""
    hashed_password = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed_password[:32])  # Fernet keys must be 32 bytes

def encrypt_card_number(card_number: str, password: str) -> str:
    """Encrypts the card number using the user's password"""
    key = generate_key(password)
    cipher = Fernet(key)
    encrypted_card = cipher.encrypt(card_number.encode())
    return encrypted_card.decode()  # Store as string in DB

def decrypt_card_number(encrypted_card: str, password: str) -> str:
    """Decrypts the card number using the user's password"""
    try:
        key = generate_key(password)
        cipher = Fernet(key)
        decrypted_card = cipher.decrypt(encrypted_card.encode())
        return decrypted_card.decode()
    except Exception:
        return "DECRYPTION FAILED"  # Demonstrating cryptographic failure
