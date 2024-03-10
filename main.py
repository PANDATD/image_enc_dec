#!/usr/bin/env python3.12
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import hashlib
from PIL import Image, ImageTk
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from ttkthemes import ThemedStyle

window = tk.Tk()
window.title("Encryption & Decryption")
window.geometry("450x350")

message = """Image Encryption Decryption project is built using Tkinter.
Developed by Mr.Tejas Dixit and Datta Kale 
Blog: https://medium.com/coddersclub
Contact us: coddersclub@gmail.com
Feedback or Feature request: github.com/coddersclub, github.com/pandatd"""

style = ThemedStyle(window)
style.set_theme("arc")  # Apply a theme from ttkthemes library
tabControl = ttk.Notebook(window)


# Function to browse and select an image file
def browse_files():
    window.filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("Image Files", ("*.jpg", "*.jpeg", "*.png")), ("All Files", "*.*")),
    )

# Function to perform XOR-based encryption and decryption
def xor_encrypt_decrypt():
    try:
        path = window.filename
        key = key_entry1.get()
        key = len(key) + 128

        image = Image.open(path)
        encrypted_image = image.point(lambda p: p ^ key)
        encrypted_image.save(path)
        messagebox.showinfo(
            title="XOR Encryption/Decryption", message="Image encryption/decryption done successfully."
        )
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))

# Function to perform RES-based encryption and decryption
def res_encrypt_decrypt():
    try:
        path = window.filename
        key = key_entry2.get()
        key = len(key) + 128

        image = Image.open(path)
        encrypted_image = image.convert("RGB").resize((image.width // 2, image.height // 2))
        decrypted_image = encrypted_image.resize(image.size)
        decrypted_image.save(path)
        messagebox.showinfo(
            title="RES Encryption/Decryption", message="Image encryption/decryption done successfully."
        )
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))

# Function to calculate SHA256 and MD5 hash of an image
def hash_image():
    try:
        path = window.filename

        image = Image.open(path)
        image_bytes = image.tobytes()

        sha256_hash = hashlib.sha256(image_bytes).hexdigest()
        md5_hash = hashlib.md5(image_bytes).hexdigest()

        hash_message = f"SHA256 Hash: {sha256_hash}\nMD5 Hash: {md5_hash}"
        messagebox.showinfo(title="Image Hashing", message=hash_message)
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))

# Function to perform text embedding in an image using steganography
def steganography():
    try:
        path = window.filename
        text = text_entry.get()

        image = Image.open(path).convert("RGB")
        image_bytes = bytearray(image.tobytes())

        text_bytes = text.encode()

        text_length = len(text_bytes)

        if text_length > len(image_bytes) - 4:
            raise ValueError("Text too large to fit in the image.")

        for i in range(4):
            image_bytes[i] = (image_bytes[i] & 0xFC) | ((text_length >> (i * 2)) & 0x03)

        for i in range(text_length):
            image_bytes[i + 4] = (image_bytes[i + 4] & 0xFC) | ((text_bytes[i] >> 6) & 0x03)
            image_bytes[i + 4 + text_length] = (image_bytes[i + 4 + text_length] & 0xFC) | (
                text_bytes[i] & 0x03
            )

        image.frombytes(bytes(image_bytes))
        image.save(path)

        messagebox.showinfo(title="Steganography", message="Text embedded successfully.")
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))

# Function to retrieve hidden text from an image using steganography
def retrieve_text():
    try:
        path = window.filename

        image = Image.open(path).convert("RGB")
        image_bytes = bytearray(image.tobytes())

        text_length = 0

        for i in range(4):
            text_length |= (image_bytes[i] & 0x03) << (i * 2)

        text_bytes = bytearray()

        for i in range(text_length):
            text_byte = (image_bytes[i + 4] & 0x03) << 6
            text_byte |= image_bytes[i + 4 + text_length] & 0x03
            text_bytes.append(text_byte)

        text = text_bytes.decode()

        messagebox.showinfo(title="Text Retrieval", message=f"Retrieved Text:\n{text}")
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))

# XOR-encrypt tab
tab1 = ttk.Frame(window)
tabControl.add(tab1, text="XOR-encrypt")
tabControl.pack(expand=1, fill="both")

label_1 = ttk.Label(tab1, text="XOR-based Encryption and Decryption", font=("Times New Roman", 25))
button_exp1 = ttk.Button(tab1, text="Browse File", command=browse_files)
key_label1 = ttk.Label(tab1, text="Encryption Key:", font=("Arial", 10))
key_entry1 = ttk.Entry(tab1,show="*")
key_entry1.insert(0, "Enter Your Encryption or Decryption key")
button_enc1 = ttk.Button(tab1, text="Encrypt/Decrypt", command=xor_encrypt_decrypt)

label_1.pack(pady=10)
button_exp1.pack()
key_label1.pack(pady=10)
key_entry1.pack(pady=10)
button_enc1.pack(pady=10)

# RES-Encryption tab
tab2 = ttk.Frame(window)
tabControl.add(tab2, text="RES-Encryption")

label_2 = ttk.Label(tab2, text="RES-based Encryption and Decryption", font=("Times New Roman", 25))
button_exp2 = ttk.Button(tab2, text="Browse File", command=browse_files)
key_label2 = ttk.Label(tab2, text="Encryption Key:", font=("Arial", 10))
key_entry2 = ttk.Entry(tab2,show="*")
key_entry2.insert(0, "Enter Your Encryption or Decryption key")
button_enc2 = ttk.Button(tab2, text="Encrypt/Decrypt", command=res_encrypt_decrypt)

label_2.pack(pady=10)
button_exp2.pack()
key_label2.pack(pady=10)
key_entry2.pack(pady=10)
button_enc2.pack(pady=10)

# Hashing tab
tab3 = ttk.Frame(window)
tabControl.add(tab3, text="Hashing")

label_3 = ttk.Label(tab3, text="Hashing", font=("Times New Roman", 25))
button_exp3 = ttk.Button(tab3, text="Browse File", command=browse_files)
button_hash = ttk.Button(tab3, text="Hash Image", command=hash_image)

label_3.pack(pady=10)
button_exp3.pack()
button_hash.pack(pady=10)

# Steganography tab
tab4 = ttk.Frame(window)
tabControl.add(tab4, text="Steganography")

label_4 = ttk.Label(tab4, text="Text Embedding and Retrieval", font=("Times New Roman", 25))
button_exp4 = ttk.Button(tab4, text="Browse File", command=browse_files)
text_entry = ttk.Entry(tab4,show="*")
text_entry.insert(0, "Enter the text to embed")
button_embed = ttk.Button(tab4, text="Embed Text", command=steganography)
button_retrieve = ttk.Button(tab4, text="Retrieve Text", command=retrieve_text)

label_4.pack(pady=10)
button_exp4.pack()
text_entry.pack(pady=10)
button_embed.pack(pady=10)
button_retrieve.pack(pady=10)

# About tab
tab5 = ttk.Frame(window)
tabControl.add(tab5, text="About")

label_5 = ttk.Label(tab5, text=message, font=("Times New Roman", 12), wraplength=400, justify="left")
label_5.pack(pady=30)

window.mainloop()
