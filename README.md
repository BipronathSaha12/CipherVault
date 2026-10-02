# 🔐 CipherVault

A **GUI-based desktop application** for encrypting and decrypting files using **AES-256 encryption**. This project demonstrates **password-based file security**, **desktop GUI development**, **robust error handling**, **logging**, and packaging Python applications into a standalone executable.

---

## 💻 Features

* GUI-based application using **Tkinter**
* **AES-256 encryption** for secure file protection with PBKDF2 derivation
* Password-based file encryption & decryption
* Folder-level recursive encryption and decryption
* **Enterprise-grade logging** and robust exception handling
* Secure memory handling (passwords are cleared from UI after usage)
* Drag & Drop support
* Standalone desktop application using **PyInstaller**

---

## 🛠 Technologies Used

* Python 3.x
* Tkinter (GUI) & tkinterdnd2 (Drag & drop)
* Cryptography (AES-256 encryption & PBKDF2)
* PyInstaller (for building `.exe`)
* Python Logging module

---

## ⚙️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/BipronathSaha12/CipherVaultt.git
cd CipherVault
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python main.py
```

4. Build standalone executable:

```bash
pyinstaller --onefile --windowed main.py
```

---

## 📂 Architecture and Logging

1. User selects a file/folder to encrypt or decrypt.
2. The application uses **PBKDF2HMAC** to derive a secure 256-bit key from the password.
3. **AES-256** (Fernet) is used for encryption/decryption.
4. All application events, errors, and debug traces are logged inside the `logs/app.log` file.
5. Errors are gracefully handled to prevent application crashes, and user-friendly messages are shown in the GUI.

---

## 🚀 Future Enhancements

* Add **Argon2 key derivation** for improved security
* Add **login system** for user authentication
* Add **file history dashboard** and file management
* Integrate with **cloud storage** (Google Drive, AWS S3)
* Convert to **Django web app** for web interface

---


## 💼 Use in Resume / Interview

> Developed an Enterprise-ready GUI-based file encryption system using Python and AES-256, enabling secure file protection and standalone desktop deployment. Implemented password-based encryption via PBKDF2, comprehensive logging, and robust error handling. Designed a user-friendly interface with drag-and-drop capabilities. 

---

## ⚖ License

This project is open-source.
