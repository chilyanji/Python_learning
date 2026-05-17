import tkinter as tk

def show():
    print(entry.get())

def update_text():
    label.config(text="Updated!")

root = tk.Tk()
root.geometry("720x520")
entry = tk.Entry(root)
entry.pack()

label = tk.Label(root, text="Old Text")
label.pack()

button = tk.Button(root, text="Change", command=update_text)
button.pack()

btn = tk.Button(root, text="Submit", command=show)
btn.pack()

root.mainloop()