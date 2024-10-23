'''tkinter is the standard Python library for creating graphical user interfaces (GUIs).
We use it to create the calculator window and buttons.'''
import tkinter as tk
import math

# Function to evaluate the expression entered by the user
def evaluate_expression():
    try:
        '''eval(): A Python function that interprets and evaluates a string as code.
        For example, if the user inputs "3+5", eval() returns 8'''
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("Error")

# Function to update the expression as the user clicks buttons
def update_expression(value):
    current_expression = expression.get()
    expression.set(current_expression + str(value))

# Function to clear the input field
def clear_expression():
    expression.set("")

# Function to clear only the last entry (CE functionality)
def clear_last_entry():
    current_expression = expression.get()
    expression.set(current_expression[:-1])

# Function to calculate square root
def calculate_square_root():
    try:
        result = str(math.sqrt(float(expression.get())))
        expression.set(result)
    except:
        expression.set("Error")

# Function to calculate percentage
def calculate_percentage():
    try:
        current_expression = expression.get()
        result = str(eval(current_expression) / 100)
        expression.set(result)
    except:
        expression.set("Not Defined")

# Create the main application window
root = tk.Tk()
root.title("Calculator :Ash")

# Set the size of the window and apply a theme/color
root.geometry("640x480")
root.configure(bg="#808080")  # Grey background because it looks cool

# Function to create a button with custom styling
def create_button(parent, text, row, column, command, bg_color, fg_color, width=5, height=2):
    button = tk.Button(parent, text=text, command=command, font=('Arial', 16),
                       width=width, height=height, bg=bg_color, fg=fg_color,
                       activebackground="#388E3C", relief="raised")
    button.grid(row=row, column=column, sticky='nsew', padx=5, pady=5)
    return button

# Expression variable (holds the text to display)
# This is where the expression variable is defined
#tk.StringVar() is a special tkinter variable that can store and update string values in a GUI.
expression = tk.StringVar()

# Entry field for the calculator
entry = tk.Entry(root, textvariable=expression, justify='right', font=('Arial', 24),
                 bg="white", relief="groove", borderwidth=2)
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipady=10)
#tk.Entry(): Creates an input field
#textvariable=expression:Links the entry field to the expression variable, changes in expression will be reflected in the display.

# Button layout with custom styling
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3), ('=', 4, 2),
]

# Create and place buttons on the grid
for (text, row, col) in buttons:
    if text == '=':
        create_button(root, text, row, col, evaluate_expression, "#f77b72", "white")
    else:
        create_button(root, text, row, col, lambda t=text: update_expression(t), "#5f997f", "white")

# Additional functionality buttons (square root, percentage, CE, backspace)
create_button(root, '√', 5, 0, calculate_square_root, "orange", "white")
create_button(root, '%', 5, 1, calculate_percentage, "orange", "white")
create_button(root, '←', 5, 2, clear_last_entry, "white", "black")
create_button(root, 'AC', 5, 3, clear_expression, "white", "black")
root.bind('<Return>', lambda event: evaluate_expression()) #added for keyboard support to Enter key.

# Configure the grid to expand with window size
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the main application loop
if __name__ =="__main__":
    root.mainloop()