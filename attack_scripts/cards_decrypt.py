import base64
import hashlib
from cryptography.fernet import Fernet

def generate_key(password: str) -> bytes:
    """Generate an encryption key from the user's password"""
    hashed_password = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hashed_password[:32])  # Fernet requires a 32-byte key

def decrypt_card_number(encrypted_card: str, password: str) -> str:
    """Decrypts the card number using the user's password"""
    try:
        key = generate_key(password)
        cipher = Fernet(key)
        decrypted_card = cipher.decrypt(encrypted_card.encode())
        return decrypted_card.decode()
    except Exception:
        return "DECRYPTION FAILED - Wrong password or corrupted data"

if __name__ == "__main__":
    # Simulating an attack where the hacker has access to both encrypted data and the user's password
    encrypted_card = input("Enter the encrypted card number: ")
    user_password = input("Enter the stolen user password: ")

    decrypted_card = decrypt_card_number(encrypted_card, user_password)
    print("\n🔓 Decrypted Card Number:", decrypted_card)
