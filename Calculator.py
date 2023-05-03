import tkinter as tk
from tkinter import *

# Functions
def button_Click(button_input):
    """
    Updates the global expression with the input from a button click and sets the display value.
    
    Parameters:
    button_input (str): The input from the button click.
    """
    global current_expression

    current_expression=current_expression + str(button_input)
    display_value.set(current_expression)
    

def calculate_Result():
    """
    Calculates the result of the expression stored in the global variable `current_expression`.
    The result is stored in the global variable `display_value`.
    """
    global current_expression
    
    try:
        result=str(eval(current_expression))
        current_expression=result  # Update current_expression with the result
        display_value.set(result)
    except ZeroDivisionError:
        result="Cannot divide by zero"
    except ValueError:
        result="Invalid expression"
        

def all_clear_Entry():
    """
    Clears the global expression and sets the display value to an empty string.
    """
    global current_expression

    current_expression=""
    display_value.set(current_expression)
    
    
def clear_Entry():
    """
    Clears the last character from the global expression and sets the display value to the updated expression.
    """
    global current_expression, display_value

    clearedisplay_value=display_value.get()[:-1]

    current_expression=clearedisplay_value
    display_value.set(current_expression)


def CreateWidgets():
    """
    Creates the widgets for the calculator.
    """
    CalcDisplay=Entry(root, bd=10, justify="right", font=("Arial", 20, "bold"), 
    textvariable=display_value, bg="sienna3")
    CalcDisplay.grid(row=0, column=0, columnspan=5) 

    button_properties = [
        {"text": "AC", "row": 1, "column": 0, "command": all_clear_Entry},
        {"text": "C", "row": 1, "column": 1, "command": clear_Entry},
        {"text": "%", "row": 1, "column": 2, "command": lambda: button_Click('%')},
        {"text": "/", "row": 1, "column": 3, "command": lambda: button_Click('/')},
        {"text": "7", "row": 2, "column": 0, "command": lambda: button_Click(7)},
        {"text": "8", "row": 2, "column": 1, "command": lambda: button_Click(8)},
        {"text": "9", "row": 2, "column": 2, "command": lambda: button_Click(9)},
        {"text": "*", "row": 2, "column": 3, "command": lambda: button_Click('*')},
        {"text": "4", "row": 3, "column": 0, "command": lambda: button_Click(4)},
        {"text": "5", "row": 3, "column": 1, "command": lambda: button_Click(5)},
        {"text": "6", "row": 3, "column": 2, "command": lambda: button_Click(6)},
        {"text": "-", "row": 3, "column": 3, "command": lambda: button_Click('-')},
        {"text": "1", "row": 4, "column": 0, "command": lambda: button_Click(1)},
        {"text": "2", "row": 4, "column": 1, "command": lambda: button_Click(2)},
        {"text": "3", "row": 4, "column": 2, "command": lambda: button_Click(3)},
        {"text": "+", "row": 4, "column": 3, "command": lambda: button_Click('+')},
        {"text": "0", "row": 5, "column": 0, "columnspan": 2, "command": lambda: button_Click(0)},
        {"text": ".", "row": 5, "column": 2, "command": lambda: button_Click('.')},
        {"text": "=", "row": 5, "column": 3, "command": lambda: calculate_Result()}]

    for button in button_properties:
        B = Button(root, text=button["text"], bd=5, font=("Arial", 20, "bold"), width=4, height=2, command=button["command"])
        B.grid(row=button["row"], column=button["column"], padx=5, pady=5, columnspan=button.get("columnspan", 1))
        

# Main
root=tk.Tk()
root.title('GUI Calculator')
root.resizable(False, False)
root.configure(background='sienna4')

display_value=StringVar()
current_expression=""

CreateWidgets()

root.mainloop()
