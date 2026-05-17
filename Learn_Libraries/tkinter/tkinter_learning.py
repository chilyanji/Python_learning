import tkinter as tk

def greet():
    output.config(text="Namaskar")


root = tk.Tk()
root.geometry("720x520")

root.title("My First GUI")
label = tk.Label(root, text="Hello World")
label.pack()
frame = tk.Frame(root, width=400, height=300, bg="green")
frame.pack()
text = tk.Text(root, bg="blue")
text.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Submit", command=greet)
button.pack()
output = tk.Label(root, text="")
output.pack()

root.mainloop()