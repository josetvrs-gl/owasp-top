import re
import hashlib
import bcrypt

def is_valid_password(password):
    """Check if password meets security criteria: at least 8 chars, 1 uppercase, 1 symbol."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, ""

def hash_password_md5(password):
    # Usar MD5 para hashear la contraseña (¡Inseguro!)
    return hashlib.md5(password.encode()).hexdigest()


def hash_password(password):
    # Usar bcrypt para hashear contraseñas (con sal)
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())