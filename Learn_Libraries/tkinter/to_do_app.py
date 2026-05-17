import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_input.get()

    if task !="":
        task_listbox.insert(tk.END, task)
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")



def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task")


root = tk.Tk()
root.title("To-Do App")
root.geometry("400x450")

title_label = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 20)
)
title_label.pack(pady=10)


task_input = tk.Entry(
    root,
    width=30,
    font=("Arial", 16)
)
task_input.pack(pady=10)

add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task,
    width=15,
    font=("Arial", 14)
)
add_button.pack(pady=5)


task_listbox = tk.Listbox(
    root,
    width=35,
    height=12,
    font=("Arial", 14)
)
task_listbox.pack(pady=10)

delete_button = tk.Button(
    root,
    text="Delete Task",
    command=delete_task,
    width=15,
    font=("Arial", 14)
)
delete_button.pack(pady=5)

root.mainloop()



# Future work : add these items
# Save tasks in file
# Checkbox tasks
# Dark mode
# Edit task
# Deadline/date
# Scrollbar
# SQLite database storage