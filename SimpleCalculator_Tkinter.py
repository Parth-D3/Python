from tkinter import *
from tkinter import ttk

# Globals to hold numbers and operation
num1 = None
op = None
num = 0

# Root window
root = Tk()
root.title("Simple Calculator")

# Frame
frm = ttk.Frame(root, padding=10)
frm.grid()

# Display
display_var = StringVar(value="0")
display = ttk.Entry(frm, textvariable=display_var, justify="right", font=("Arial", 16))
display.grid(column=0, row=0, columnspan=4, pady=10)

# Functions
def create_num(x):
    """Build number from button presses"""
    global num
    num = num * 10 + x
    display_var.set(str(num))

def get_op(x):
    """Store operator and first number"""
    global num1, num, op
    num1 = num
    op = x
    num = 0
    display_var.set(str(num1) + " " + op)

def calculate():
    """Perform calculation when = pressed"""
    global num1, num, op
    num2 = num
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Error"
    display_var.set(str(result))
    # reset for next calculation
    num1 = None
    op = None
    num = 0

def clear():
    """Clear the calculator"""
    global num1, num, op
    num1 = None
    op = None
    num = 0
    display_var.set("0")

# Buttons
buttons = [
    ("7", lambda: create_num(7)), ("8", lambda: create_num(8)), ("9", lambda: create_num(9)), ("/", lambda: get_op("/")),
    ("4", lambda: create_num(4)), ("5", lambda: create_num(5)), ("6", lambda: create_num(6)), ("*", lambda: get_op("*")),
    ("1", lambda: create_num(1)), ("2", lambda: create_num(2)), ("3", lambda: create_num(3)), ("+", lambda: get_op("+")),
    ("C", clear),                ("0", lambda: create_num(0)), ("=", calculate),               ("-", lambda: get_op("-")),
]

# Place buttons in grid
row = 1
col = 0
for (text, cmd) in buttons:
    ttk.Button(frm, text=text, command=cmd, width=5).grid(column=col, row=row, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
