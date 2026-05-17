import tkinter as tk
from tkinter import messagebox

def login():
    user = username.get()
    paswrd = password.get()

    if user == "ayush" and paswrd == "123456":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

root = tk.Tk()
root.title("Login Page")
root.geometry("350x250")

titleLabel = tk.Label(root, text="Login Form", font=("Times New roman", 16))
titleLabel.pack(pady=10)

usernameLable = tk.Label(root, text="Username", font=("Times New roman", 16))
usernameLable.pack()
username = tk.Entry(root, font=("Times New roman", 16))
username.pack(pady=5)

passwordLable = tk.Label(root, text="Password", font=("Times New roman", 16))
passwordLable.pack()
password = tk.Entry(root, font=("Times New roman", 16), show="*")
password.pack(pady=5)

loginbtn = tk.Button(root, text="Login", command=login, font=("Times New roman", 16))
loginbtn.pack()
root.mainloop()