import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password based on complexity level
def generate_password(length, complexity):
    if complexity == "Weak":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation.replace("'", "")  # Removing ' character for medium
    elif complexity == "Strong":
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(characters, k=length))
    return password

# Function to handle Generate button click
def generate_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return

        complexity = complexity_var.get()
        password = generate_password(length, complexity)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

# Main application window
root = tk.Tk()
root.title("Password Generator")

# Colors
bg_color = "#f0f0f0"  # Light gray background
button_color = "#4CAF50"  # Green button color
text_color = "#333333"  # Dark gray text color

# Configure background color
root.configure(bg=bg_color)

# GUI Elements
title_label = tk.Label(root, text="Password Generator", bg=bg_color, fg=text_color, font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

info_label = tk.Label(root, text="Specify password length and complexity:", bg=bg_color, fg=text_color)
info_label.pack()

input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(pady=10)

length_label = tk.Label(input_frame, text="Password Length:", bg=bg_color, fg=text_color)
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

length_entry = tk.Entry(input_frame, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=5)

complexity_label = tk.Label(input_frame, text="Complexity:", bg=bg_color, fg=text_color)
complexity_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

complexity_var = tk.StringVar(root)
complexity_var.set("Strong")  # Default complexity level

complexity_option_menu = tk.OptionMenu(input_frame, complexity_var, "Weak", "Medium", "Strong")
complexity_option_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Generate Password button
generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked, bg=button_color, fg="white")
generate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", bg=bg_color, fg=text_color, font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
