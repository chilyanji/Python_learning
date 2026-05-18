import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("520x720")

# Global expression
expression = ""

# Display function
def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

# Clear screen
def clear():
    global expression

    expression = ""

    equation.set("")

# Calculate result
def equal():
    global expression

    try:
        result = str(eval(expression))

        equation.set(result)

        expression = result

    except:
        equation.set("Error")

        expression = ""

# String variable
equation = tk.StringVar()

# Display entry
entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 20),
    bd=10,
    relief="ridge",
    justify="right"
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    ipadx=8,
    ipady=25,
    pady=10
)

# Buttons
buttons = [
    ('7', 1, 0),
    ('8', 1, 1),
    ('9', 1, 2),
    ('/', 1, 3),

    ('4', 2, 0),
    ('5', 2, 1),
    ('6', 2, 2),
    ('*', 2, 3),

    ('1', 3, 0),
    ('2', 3, 1),
    ('3', 3, 2),
    ('-', 3, 3),

    ('0', 4, 0),
    ('C', 4, 1),
    ('=', 4, 2),
    ('+', 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:

    if text == "=":
        action = equal

    elif text == "C":
        action = clear

    else:
        action = lambda x=text: press(x)

    tk.Button(
        root,
        text=text,
        padx=20,
        pady=20,
        font=("Arial", 16),
        command=action
    ).grid(
        row=row,
        column=col,
        sticky="nsew"
    )

# Make grid responsive
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run app
root.mainloop()