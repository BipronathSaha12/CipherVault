import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from utils.logger import logger

def generate_key_from_password(password: str, salt: bytes):
    """Generate a key from password using PBKDF2."""
    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),   # use SHA256 for hashing
            length=32,    
            salt=salt,          # unique salt for each encryption
            iterations=100000,  # number of iterations
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    except Exception as e:
        logger.exception("Error generating key from password")
        raise

# encrypt and decrypt functions
def encrypt_data(data, password):
    try:
        salt = os.urandom(16)
        key = generate_key_from_password(password, salt)
        fernet = Fernet(key)

        encrypted = fernet.encrypt(data)
        logger.debug("Data encrypted successfully")
        return salt + encrypted  # store salt with data
    except Exception as e:
        logger.exception("Error encrypting data")
        raise

def decrypt_data(data, password):
    try:
        salt = data[:16]
        encrypted_data = data[16:]    #extract salt and encrypted data

        key = generate_key_from_password(password, salt)
        fernet = Fernet(key)

        decrypted = fernet.decrypt(encrypted_data)
        logger.debug("Data decrypted successfully")
        return decrypted
    except Exception as e:
        logger.error(f"Error decrypting data: Invalid password or corrupted file.")
        raise