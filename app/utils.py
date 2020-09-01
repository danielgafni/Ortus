from cryptography.fernet import Fernet


def encrypt(text, key):
    """
    Encrypts a string with a bytes key
    """
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())

    return encrypted_text


def decrypt(encrypted_text, key):
    """
    Decrypts encrypted text with a bytes key
    """
    f = Fernet(key)
    text = f.decrypt(encrypted_text).decode()

    return text
