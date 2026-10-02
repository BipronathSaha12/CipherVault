import os
from cryptography.fernet import InvalidToken
from utils.crypto_utils import encrypt_data, decrypt_data
from utils.file_handler import read_file, write_file
from utils.logger import logger

# folder encryption and decryption functions
def encrypt_folder(folder_path, password):
    logger.info(f"Starting encryption for folder: {folder_path}")
    for root, _, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(root, file) # encrypt each file in folder
            if path.endswith(".enc"):
                continue # Skip already encrypted files
            try:
                data = read_file(path)
                if data:
                    encrypted = encrypt_data(data, password) # encrypt data
                    write_file(path + ".enc", encrypted)
                    logger.debug(f"Encrypted file: {path}")
            except Exception as e:
                logger.error(f"Failed to encrypt file {path}: {e}")

def decrypt_folder(folder_path, password):
    logger.info(f"Starting decryption for folder: {folder_path}")
    success_count = 0
    fail_count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".enc"):
                path = os.path.join(root, file) # decrypt each .enc file in folder
                try:
                    data = read_file(path)
                    if data:
                        decrypted = decrypt_data(data, password) # decrypt data
                        new_path = path.replace(".enc", "_dec.txt") # consistent with main.py
                        write_file(new_path, decrypted)
                        logger.debug(f"Decrypted file: {path}")
                        success_count += 1
                except InvalidToken:
                    logger.warning(f"Invalid password or corrupted data for file: {path}")
                    fail_count += 1
                except Exception as e:
                    logger.error(f"Failed to decrypt file {path}: {e}")
                    fail_count += 1
    
    if fail_count > 0:
        logger.warning(f"Decryption finished with {fail_count} failures and {success_count} successes.")
    else:
        logger.info(f"Decryption finished successfully for {success_count} files.")
    return fail_count == 0