import tkinter as tk
from tkinter import filedialog, messagebox, ttk
# pyrefly: ignore [missing-import]
from tkinterdnd2 import DND_FILES, TkinterDnD
import traceback

from utils.crypto_utils import encrypt_data, decrypt_data
from utils.file_handler import read_file, write_file
from utils.folder_handler import encrypt_folder, decrypt_folder
from utils.logger import logger


def update_progress(value):
    progress['value'] = value
    root.update_idletasks()

# file encryption and decryption functions
def encrypt_file(path):
    password = password_entry.get()  # get password from entry
    if not password:
        messagebox.showerror("Error", "Enter password!")
        return

    logger.info(f"Encrypting file: {path}")
    data = read_file(path)
    if data is None:           # if file read fails, stop process
        logger.error(f"Failed to read file: {path}")
        messagebox.showerror("Error", f"Failed to read file: {path}")
        return

    try:
        update_progress(30)
        encrypted = encrypt_data(data, password)   # encrypt data
        update_progress(70)

        write_file(path + ".enc", encrypted)
        update_progress(100)

        logger.info(f"File encrypted successfully: {path}")
        messagebox.showinfo("Success", "File Encrypted!")
    except Exception as e:
        logger.exception("Encryption failed")
        messagebox.showerror("Error", f"Encryption failed: {str(e)}")
    finally:
        password_entry.delete(0, tk.END)
        update_progress(0)

def decrypt_file(path):
    password = password_entry.get()
    if not password:                    # if no password entered, show error and stop process
        messagebox.showerror("Error", "Enter password!")
        return

    logger.info(f"Decrypting file: {path}")
    data = read_file(path)
    if data is None:
        logger.error(f"Failed to read file: {path}")
        messagebox.showerror("Error", f"Failed to read file: {path}")
        return

    try:
        update_progress(30)
        decrypted = decrypt_data(data, password)
        update_progress(70)

        write_file(path.replace(".enc", "_dec.txt"), decrypted)
        update_progress(100)

        logger.info(f"File decrypted successfully: {path}")
        messagebox.showinfo("Success", "File Decrypted!")
    except Exception as e:
        logger.exception("Decryption failed")
        messagebox.showerror("Error", "Wrong password or corrupted file!")
    finally:
        password_entry.delete(0, tk.END)
        update_progress(0)

# folder encryption and decryption functions
def select_file_encrypt():
    path = filedialog.askopenfilename()
    if path:
        encrypt_file(path)

# select_file_decrypt function
def select_file_decrypt():
    path = filedialog.askopenfilename()   # open file dialog to select .enc file for decryption
    if path:
        decrypt_file(path)

# folder encryption and decryption functions
def select_folder_encrypt():
    path = filedialog.askdirectory()
    if path:
        password = password_entry.get()
        if not password:
            messagebox.showerror("Error", "Enter password!")
            return
        
        logger.info(f"Encrypting folder: {path}")
        encrypt_folder(path, password)
        logger.info("Folder encrypted successfully")
        messagebox.showinfo("Done", "Folder Encrypted!")
        password_entry.delete(0, tk.END)

# select_folder_decrypt function
def select_folder_decrypt():
    path = filedialog.askdirectory()
    if path:
        password = password_entry.get()
        if not password:
            messagebox.showerror("Error", "Enter password!")
            return
            
        logger.info(f"Decrypting folder: {path}")
        success = decrypt_folder(path, password)
        if success:
            messagebox.showinfo("Done", "Folder Decrypted successfully!")
        else:
            messagebox.showwarning("Warning", "Folder Decrypted with some errors. Check log.")
        password_entry.delete(0, tk.END)

# drag and drop function
def drop(event):
    path = event.data.strip("{}")   # get file path from drop event, strip {} added by tkinterdnd2
    if path.endswith(".enc"):       # if dropped file is .enc, decrypt it
        decrypt_file(path)
    else:
        encrypt_file(path)


# GUI setup
root = TkinterDnD.Tk()
root.title("CipherVault")
root.geometry("450x350")

tk.Label(root, text="🔐 CipherVault", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Encrypt File", command=select_file_encrypt).pack(pady=5)
tk.Button(root, text="Decrypt File", command=select_file_decrypt).pack(pady=5)

tk.Button(root, text="Encrypt Folder", command=select_folder_encrypt).pack(pady=5)
tk.Button(root, text="Decrypt Folder", command=select_folder_decrypt).pack(pady=5)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=15)

drop_label = tk.Label(root, text="Drag & Drop File Here", bg="lightgray", width=40, height=3)
drop_label.pack(pady=10)

drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', drop)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()