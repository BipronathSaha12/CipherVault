# CipherVault Documentation

Welcome to the documentation for the Secure File Encryption System (CipherVault).

## Overview
This application provides secure file and folder encryption using AES-256 with PBKDF2 key derivation.

## Architecture
- `main.py`: Entry point and UI definitions using Tkinter.
- `utils/crypto_utils.py`: Contains functions for key derivation and AES encryption/decryption.
- `utils/file_handler.py`: Robust file I/O operations with logging and exception handling.
- `utils/folder_handler.py`: Recursive directory processing for bulk encryption/decryption.
- `utils/logger.py`: Centralized logging configuration for tracking events and errors.

## Production Readiness
- **Logging**: All errors, debug statements, and info messages are logged to `logs/app.log` and standard output.
- **Exception Handling**: Application prevents silent crashes by properly catching and logging Exceptions (e.g., FileNotFoundError, PermissionError, InvalidToken).
- **Security**: Passwords are wiped from memory (UI) immediately after use.
- **Packaging**: A standalone executable can be generated using PyInstaller for zero-dependency deployment.
