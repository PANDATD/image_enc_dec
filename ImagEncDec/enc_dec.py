import tkinter as tk					
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Encryption & Decryption")
window.geometry("450x350")
message= """Image Encryption Decryption project is built using Tkinter.
Devloped by Mr.Tejas Dixit and Datta kale 
Blog:- https://medium.com/coddersclub
Contact us:- coddersclub@gmil.com
Feedback or Feature request :- github.com/coddersclub, github.com/pandatd
"""
def browse_files():
	window.path = filedialog.askopenfilename(initialdir='/',title = "Select a File",filetypes = (("jpg format","*.jpg*"),("jpeg format","*.jpeg*"),("png format","*.png*"),("all files","*.*")))
	
def encrypet():
	try:
		path = window.path
		key = key_entry1.get()
		
		key = len(key) + 128
		
		 	  
		fobj = open(path,'rb')
		image = fobj.read()
		fobj.close()

		image = bytearray(image)
		for index, values in enumerate(image):
			image[index] = values ^ key
		fobj = open(path,'wb')
		fobj.write(image)

		fobj.close()
		tk.messagebox.showinfo(title="msg",message="IMAGE ENCRYPTION DONE")
	except Exception:
    		print('Error caught : ', Exception.__name__)

def decrypet():
	try:
		path = window.path
		key = key_entry1.get()
		
		key = len(key) + 128
		
		 	  
		fobj = open(path,'rb')
		image = fobj.read()
		fobj.close()

		image = bytearray(image)
		for index, values in enumerate(image):
			image[index] = values ^ key
		fobj = open(path,'wb')
		fobj.write(image)

		fobj.close()
		tk.messagebox.showinfo(title="msg",message="IMAGE DECRYPTION DONE")
	except Exception:
    		print('Error caught : ', Exception.__name__)
    		

tabControl = ttk.Notebook(window)
ttk.Style().configure("TNotebook", bg="red", foreground='green');

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='encrypt')
tabControl.add(tab2, text ='decrypt')
tabControl.add(tab3, text ='About Us')
tabControl.pack(expand = 1, fill ="both")
label_1 =ttk.Label(tab1,text='Encryption Decryption for Image', font=("Times New Roman",25),)


button_exp = ttk.Button(tab1, text='browse_file',command=browse_files)

key_label1 = ttk.Label(tab1, text='Encryption-Key!',  font=("Arial",10),)
key_entry1 = ttk.Entry(tab1, text="Enter Your Encryption or Decryption key",show="*")
button_enc = ttk.Button(tab1, text='Encryption', command=encrypet )
label_1.pack(pady=10)
button_exp.pack()
key_label1.pack(pady=10)
key_entry1.pack(pady=10)

button_enc.pack(pady=10)

label_2 =ttk.Label(tab2,text='Encryption Decryption for Image', font=("Times New Roman",25),)


button_exp = ttk.Button(tab2, text='browse_file', command=browse_files)

key_label2 = ttk.Label(tab2, text='Encryption-Key!',  font=("Arial",10),)
key_entry2 = ttk.Entry(tab2, text="Enter Your Encryption or Decryption key",show="*")
button_enc1 = ttk.Button(tab2, text='Decryption', command=decrypet)
label_2.pack(pady=10)
button_exp.pack()
key_label2.pack(pady=10)
key_entry2.pack(pady=10)

button_enc1.pack(pady=10)
key_label3 = ttk.Label(tab3, text='CodderscluB',  font=("Times New Roman",14),)
key_label3.pack()
key_label4 = ttk.Label(tab3, text=message)
key_label4.pack()
window.mainloop()
