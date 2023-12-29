import tkinter as tk

root = tk.Tk()
root.state('zoomed')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.minsize(width = int(screen_width / 2), height = int(screen_height / 2))

root.title("Project Akhir Steganografi oleh Hans")
root.iconbitmap('assets/favicon.ico')
root.configure(bg='white', padx=20, pady=20)

heading = tk.Label(root, text="Selamat Datang", font = ('Arial', 20), padx = 20, pady = 10)
heading.pack()

def start_insert_mode():
  heading.config(text="Insert Text to Picture")

def start_mix_mode():
  heading.config(text="Mix Two Picture")

menu_bar = tk.Menu(root)
menu_bar.add_cascade(label="Insert Text to Picture", command=start_insert_mode)
menu_bar.add_cascade(label="Mix Two Picture", command=start_mix_mode)
menu_bar.add_cascade(label="Exit", command=root.quit)

root.config(menu=menu_bar)
root.mainloop()

# menu_bar.add_cascade(label="File", menu=file_menu)
# menu = Menu(root)
# root.config(menu=menu)
# mode_menu = Menu(menu)
# menu.add_cascade(label="Start Mode", menu=mode_menu)
# mode_menu.add_command(label="Encryption", command=start_encryption_mode)
# mode_menu.add_command(label="Decryption", command=start_decryption_mode)

# label = Label(root, text="Select an image to encrypt/decrypt:", bg='lightblue', fg='black')
# label.pack()

# entry = Entry(root, bg='white', fg='black', width=40)
# entry.pack()

# browse_button = Button(root, text="Browse", command=browse_image, bg='blue', fg='white')
# browse_button.pack()

# filename_label = Label(root, text="Enter the output filename:", bg='lightblue', fg='black')

# filename_entry = Entry(root, bg='white', fg='black', width=40)

# key_label_encrypt = Label(root, text="Enter the encryption key:", bg='lightblue', fg='black')

# key_entry = Entry(root, bg='white', fg='black', width=40)

# encrypt_button = Button(root, text="Encrypt", command=encrypt, bg='green', fg='white')

# key_label_decrypt = Label(root, text="Enter the decryption key:", bg='lightblue', fg='black')

# key_entry = Entry(root, bg='white', fg='black', width=40)

# decrypt_button = Button(root, text="Decrypt", command=decrypt, bg='red', fg='white')

# copy_key_button = Button(root, text="Copy Key", command=copy_key, bg='lightblue', fg='black')

# key_hex_label = Label(root, text="", bg='lightblue', fg='black')

# info_label = Label(root, text="", bg='lightblue', fg='black')