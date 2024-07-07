import tkinter as tk
from tkinter import messagebox

# Function to update the display
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screen.get())
            screen_var.set(value)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            screen_var.set("")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Setting up the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg='#2E2E2E')

# Setting up the screen
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Helvetica 20 bold", borderwidth=5, relief=tk.RIDGE, bg='#EEE', fg='#333')
screen.pack(fill=tk.BOTH, ipadx=8, ipady=8, pady=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button configuration
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Colors
bg_color = '#4E4E4E'
fg_color = '#FFF'
hover_color = '#1E1E1E'

# Creating and placing buttons
for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(fill=tk.BOTH, expand=True)
    for button_text in row:
        button = tk.Button(row_frame, text=button_text, font="Helvetica 15 bold", borderwidth=1, relief=tk.RAISED, bg=bg_color, fg=fg_color)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        button.bind("<Button-1>", click)
        button.bind("<Enter>", lambda e, b=button: b.configure(bg=hover_color))
        button.bind("<Leave>", lambda e, b=button: b.configure(bg=bg_color))

root.mainloop()
