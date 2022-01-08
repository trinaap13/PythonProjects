# Calculator
from tkinter import *

# Getting a frame
kp_calculator = Tk()

# Geometry method defines window size
kp_calculator.geometry("500x400")

# Resizing window
kp_calculator.resizable(2, 2)

# Window title
kp_calculator.title("Katrina's Calculator")


def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def button_clear():
    global expression
    expression = ""
    input_text.set("")


def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

# Using Frame widget to create a frame for the input field
input_frame = Frame(kp_calculator, width=300, height=50, bd=2, highlightbackground="pink", highlightcolor="black", highlightthickness=10)
input_frame.pack(side=TOP)

# Create an input field inside the Frame; output aligned right
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#ffa54c", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
# ipady is internal padding to increase height of input field
input_field.pack(ipady=10)

# Secondary Frame below input field to include buttons
buttons_frame = Frame(kp_calculator, width=312, height=272.5, bg="pink")
buttons_frame.pack()

# First row, two buttons, 'Clear' and 'Divide'
clear = Button(buttons_frame, text="Clear", fg="black", width=38, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)

# Second row, 4 buttons, '7', '8', '9', 'Multiply'
seven = Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor = "hand2", command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor = "hand2", command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor = "hand2", command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor = "hand2", command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# Third row, 4 buttons, '4', '5', '6', 'Subtract'
four = Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

# Fourth row, 4 buttons, '1','2','3','Plus'
one = Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

# Fifth row, 3 buttons, '0','Decimal', 'Equals'
zero = Button(buttons_frame, text="0", fg="black", width=25, height=3, bd=0, bg="#fff", cursor="hand2", command = lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command = lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command = lambda: button_click('=')).grid(row=4, column=3, padx=1, pady=1)

kp_calculator.mainloop()
