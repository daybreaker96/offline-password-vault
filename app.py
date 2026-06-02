import tkinter as tk
from tkinter import messagebox

passwords = []

def save_password():
  website = website_entry.get()
  username = username_entry.get()
  password = password_entry.get()

  if not website or not username or not password:
    messagebox.showerror("Error", "Please fill in the fields.")
    return

  passwords.append({
    "website": website,
    "username": username,
    "password": password
  })

  update_list()

  website_entry.delete(0, tk.END)
  username_entry.delete(0, tk.END)
  password_entry.delete(0, tk.END)

def update_list():
  password_list.delete(0, tk.END)

  for item in passwords:
    password_list.insert(
      tk.END,
      f"{item['website']} | {item['username']}"
    )

root = tk.Tk()
root.title("Offline Password Vault")
root.geometry("500x400")

tk.Label(root, text="Website").pack()
website_entry = tk.Entry(root, width=40)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack()

tk.Button(
  root,
  text="Save Password",
  command=save_password
).pack(pady=10)

password_list = tk.Listbox(root, width=60)
password_list.pack(pady=10)

root.mainloop()
