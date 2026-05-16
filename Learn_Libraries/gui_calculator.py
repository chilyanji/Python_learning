import tkinter as tk
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    addition = num1 + num2
    output1.config(text=f"Your answer is: {addition}")
    
 
def sub():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    substraction = num1 - num2
    output2.config(text=f"Your answer is: {substraction}")

def multi():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    multiplication = num1 * num2
    output3.config(text=f"Your answer is: {multiplication}")

def div():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    division = num1 / num2
    output4.config(text=f"Your answer is: {division}")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()

btn1 = tk.Button(root, text="Add", command=add)
btn1.pack()
btn2 = tk.Button(root, text="Subtract", command=sub)
btn2.pack()
btn3 = tk.Button(root, text="Multiply", command=multi)
btn3.pack()
btn4 = tk.Button(root, text="Divide", command=div)
btn4.pack()

output1 = tk.Label(root, text="")
output1.pack()
output2 = tk.Label(root, text="")
output2.pack()
output3 = tk.Label(root, text="")
output3.pack()
output4 = tk.Label(root, text="")
output4.pack()



root.mainloop()