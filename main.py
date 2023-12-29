import tkinter as tk
import pathlib
import os

from tkinter import filedialog
from PIL import Image
from datetime import datetime

root = tk.Tk()
root.state('zoomed')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.minsize(width = int(screen_width / 2), height = int(screen_height / 2))

root.title("Project Akhir Steganografi oleh Hans")
root.iconbitmap('assets/favicon.ico')
root.configure(bg = 'white', padx = 20, pady = 20)

heading = tk.Label(root, text = "Selamat Datang", font = ('Arial', 16), padx = 8, pady = 4)
heading.pack()

def is_image(file_path):
  image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
  return any(file_path.lower().endswith(ext) for ext in image_extensions)

def write_image(file_path, folder_path):
  now = datetime.now()
  ext = pathlib.Path(file_path).suffix
  filename = now.strftime("%m-%d-%Y-%H-%M-%S" + ext)

  original_folder, original_filename = os.path.split(filename)
  decryption_folder = os.path.join(original_folder, folder_path)
  os.makedirs(decryption_folder, exist_ok=True)

  decrypted_file_path = os.path.join(decryption_folder, original_filename)
  os.rename(filename, decrypted_file_path)

def start_encode_mode():
  heading.config(text = "Encode Text to Picture")
  browse_image_button.pack(side = tk.TOP)
  browse_image_entry.pack(side = tk.TOP)
  string_entry_label.pack(side = tk.TOP)
  string_entry.pack(side = tk.TOP)
  encode_button.pack(side = tk.TOP)

def start_decode_mode():
  heading.config(text = "Decode Text from Picture")

def start_mix_mode():
  heading.config(text = "Mix Two Picture")

def encode():
  input_image = browse_image_entry.get()

  if input_image == "":
    heading.config(text = "Please select an image", fg = "red")
    return
  
  if is_image(input_image) == False:
    heading.config(text = "This file is not an image", fg = "red")
    return

  image = Image.open(input_image, 'r')
  data = string_entry.get()

  if (len(data) == 0):
    heading.config(text = "Please write something", fg = "red")
    return
  
  res = []
  res.append(len(data))

  for index, x in enumerate(data):
    res.append(ord(data[index]))

  new_image = []
  image_d = image.getdata()

  for index, x in enumerate(image_d):
    if (index) <= res[0]:
      temp = (image_d[index][0], image_d[index][1], res[index])
      new_image.append(temp)
    else:
      new_image.append(image_d[index])

  image.putdata(new_image)
  now = datetime.now()
  ext = pathlib.Path(input_image).suffix
  filename = now.strftime("%m-%d-%Y-%H-%M-%S" + ext)

  image.save("output/" + "encode/" + filename)
  heading.config(text = "Encode Success", fg = "green")

def browse_image():
  file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
  browse_image_entry.delete(0, tk.END)
  browse_image_entry.insert(0, file_path)

menu_bar = tk.Menu(root)
menu_bar.add_cascade(label = "Encode Text to Picture", command = start_encode_mode)
menu_bar.add_cascade(label = "Decode Text from Picture", command = start_decode_mode)
menu_bar.add_cascade(label = "Mix Two Picture", command = start_mix_mode)
menu_bar.add_cascade(label = "Exit", command = root.quit)

browse_image_button = tk.Button(root, text = "Browse Image", command = browse_image, font = ('Arial', 8), padx = 8, pady = 4)
browse_image_entry = tk.Entry(root)
string_entry = tk.Entry(root, text = "Write here", bg = 'white', fg = 'black', width = 40)
string_entry_label = tk.Label(root, text = "Enter string to encode")
encode_button = tk.Button(root, text = "Encode", command = encode, font = ('Arial', 8), padx = 8, pady = 4, bg = "green", fg = "white")

root.config(menu = menu_bar)
root.mainloop()